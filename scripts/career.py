#!/usr/bin/env python3
"""File-first career knowledge tools. Python 3.9+, standard library only.

This program retrieves and assembles evidence; the agent does semantic analysis
and writing. It never calls a model, invents bullets, or treats token overlap as
proof of a qualification. See docs/workflows.md.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import date
import hashlib
import json
import math
from pathlib import Path
import re
import shutil
import sys
import tempfile
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ELIGIBLE = {"confirmed", "reported"}
SLUG = r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*"
STOP = set("a an and are as at be by for from has have in into is it of on or our the their this to using with you your we will must experience required preferred qualifications responsibilities years degree ability strong knowledge skills engineer engineering software build work development including such that looking need".split())


class Invalid(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise Invalid(message)


def read(path):
    with Path(path).open(encoding="utf-8") as stream:
        # Duplicate keys must not silently discard facts or registry entries.
        def unique(pairs):
            result = {}
            for key, value in pairs:
                require(key not in result, f"{path}: duplicate JSON key {key}")
                result[key] = value
            return result
        return json.load(stream, object_pairs_hook=unique)


def encoded(value):
    return json.dumps(value, indent=2, ensure_ascii=False) + "\n"


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write(path, content):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as stream:
        stream.write(content)
        temporary = Path(stream.name)
    temporary.replace(path)


def within(root, relative):
    require(isinstance(relative, str) and relative and not Path(relative).is_absolute(), f"Expected relative path: {relative}")
    path = (root / relative).resolve()
    require(path.is_relative_to(root.resolve()), f"Path escapes root: {relative}")
    return path


def schema_check(value, schema, label="value"):
    """Validate the JSON Schema subset used by this repository's schemas.

    Supported: type, enum, const, required, properties, additionalProperties,
    items, minItems, uniqueItems, minLength, pattern, minimum. No dependencies.
    """
    kinds = {"object": dict, "array": list, "string": str, "integer": int,
             "number": (int, float), "boolean": bool, "null": type(None)}
    if "type" in schema:
        types = schema["type"] if isinstance(schema["type"], list) else [schema["type"]]
        require(any(isinstance(value, kinds[t]) and not (t in ("integer", "number") and isinstance(value, bool)) for t in types), f"{label}: expected {types}")
    if "enum" in schema:
        require(value in schema["enum"], f"{label}: not in {schema['enum']}")
    if "const" in schema:
        require(value == schema["const"], f"{label}: expected {schema['const']}")
    if isinstance(value, dict):
        require(set(schema.get("required", [])).issubset(value), f"{label}: missing {set(schema.get('required', [])) - value.keys()}")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            require(set(value).issubset(properties), f"{label}: unknown fields {value.keys() - properties.keys()}")
        for key, child in value.items():
            if key in properties:
                schema_check(child, properties[key], f"{label}.{key}")
    if isinstance(value, list):
        require(len(value) >= schema.get("minItems", 0), f"{label}: too few items")
        if schema.get("uniqueItems"):
            require(len({json.dumps(x, sort_keys=True) for x in value}) == len(value), f"{label}: duplicate items")
        for i, child in enumerate(value):
            if "items" in schema:
                schema_check(child, schema["items"], f"{label}[{i}]")
    if isinstance(value, str):
        require(len(value.strip()) >= schema.get("minLength", 0), f"{label}: empty text")
        if "pattern" in schema:
            require(re.search(schema["pattern"], value) is not None, f"{label}: invalid format")
    if isinstance(value, (int, float)) and "minimum" in schema:
        require(value >= schema["minimum"], f"{label}: below minimum")


def validate_as(root, value, name):
    schema_check(value, read(root / "schemas" / f"{name}.schema.json"), name)


def valid_date(value, partial=True):
    if value is None:
        return
    pattern = r"\d{4}(?:-\d{2}(?:-\d{2})?)?" if partial else r"\d{4}-\d{2}-\d{2}"
    require(re.fullmatch(pattern, value), f"Invalid date {value}")
    date.fromisoformat(value + ("-01-01" if len(value) == 4 else "-01" if len(value) == 7 else ""))


def check_locator(root, source, locator):
    path = within(root, source["path"])
    match = re.fullmatch(r"L(\d+)(?:-L?(\d+))?", locator)
    if path.suffix.lower() in {".md", ".txt", ".json", ".yaml", ".yml", ".csv", ".tsv"}:
        require(match, f"{source['id']}: use Lx-Ly locator, got {locator}")
        start, end = int(match[1]), int(match[2] or match[1])
        require(1 <= start <= end <= len(path.read_text(encoding="utf-8").splitlines()), f"{source['id']}: out-of-range {locator}")
    else:
        # Binary evidence must have a human-reviewed, specific page/visual/section locator.
        require(bool(re.fullmatch(r"p\d+(?:-p?\d+)?|visual|section:.+", locator)), f"{source['id']}: invalid binary locator {locator}")


def load_db(root=ROOT):
    root = root.resolve()
    registry = read(root / "sources/registry.json")
    validate_as(root, registry, "sources")
    sources = {}
    for source in registry["sources"]:
        require(source["id"] not in sources, f"Duplicate source {source['id']}")
        path = within(root, source["path"])
        require(path.is_file(), f"Missing source {path}; restore evidence before proceeding")
        require(digest(path) == source["sha256"], f"Source changed: {source['path']}; preserve original and ingest a new revision")
        valid_date(source["added"], False)
        sources[source["id"]] = source
    for source in sources.values():
        for parent in source.get("derived_from", []) + source.get("supersedes", []):
            require(parent in sources and parent != source["id"], f"Invalid source relationship {source['id']} -> {parent}")
    visited, visiting = set(), set()
    def visit(source_id):
        require(source_id not in visiting, f"Cyclic source provenance at {source_id}")
        if source_id in visited:
            return
        visiting.add(source_id)
        for parent in sources[source_id]["derived_from"] + sources[source_id]["supersedes"]:
            visit(parent)
        visiting.remove(source_id)
        visited.add(source_id)
    for source_id in sources:
        visit(source_id)
    records, paths = {}, {}
    folders = {"experience": "experience", "project": "projects", "accomplishment": "accomplishments", "skill": "skills", "education": "education", "leadership": "leadership", "additional": "additional", "profile": "profile"}
    for path in sorted((root / "knowledge").rglob("*.json")):
        require(path.resolve().is_relative_to(root), f"Record path escapes repository: {path}")
        record = read(path)
        validate_as(root, record, "record")
        rid = record["id"]
        require(rid == path.stem and rid not in records, f"Duplicate ID or filename mismatch: {path}")
        require(path.parent == root / "knowledge" / folders[record["type"]], f"Wrong record directory: {path}")
        dates = record["dates"]
        for field in ["start", "end", "as_of"]:
            valid_date(dates[field], partial=field != "as_of")
        require(not (dates["ongoing"] and dates["end"]), f"{rid}: ongoing with end date")
        if dates["start"] and dates["end"]:
            require(dates["start"] <= dates["end"] + "-99-99", f"{rid}: end before start")
        fact_ids = set()
        for fact in record["facts"]:
            require(fact["id"] not in fact_ids, f"{rid}: duplicate fact {fact['id']}")
            fact_ids.add(fact["id"])
            require(not re.search(r"\[TODO|\[Describe|REPLACE_ME", fact["text"], re.I), f"{rid}: unfilled template")
            for evidence in fact["evidence"]:
                require(evidence["source_id"] in sources, f"{rid}: unknown source {evidence['source_id']}")
                check_locator(root, sources[evidence["source_id"]], evidence["locator"])
        records[rid], paths[rid] = record, path
    require(records, "Knowledge base is empty")
    for record in records.values():
        require(set(record["related"]).issubset(records), f"{record['id']}: unknown related IDs {set(record['related']) - records.keys()}")
        require(record["id"] not in record["related"], f"{record['id']}: self relation")
    return records, sources, paths


def get_fact(records, ref, public=False):
    parts = ref.split("#")
    require(len(parts) == 2 and parts[0] in records, f"Invalid fact reference: {ref}")
    record = records[parts[0]]
    facts = [f for f in record["facts"] if f["id"] == parts[1]]
    require(len(facts) == 1, f"Unknown fact: {ref}")
    fact = facts[0]
    if public:
        require(fact["status"] in ELIGIBLE and fact["visibility"] == "public", f"Not eligible for application copy: {ref}")
    return record, fact


def eligible(record, private=False):
    return [f for f in record["facts"] if f["status"] in ELIGIBLE and (private or f["visibility"] == "public")]


def tokens(text, root=ROOT):
    text = text.lower()
    aliases = read(root / "config/aliases.json")
    for alias, canonical in sorted(aliases.items(), key=lambda x: -len(x[0])):
        text = re.sub(r"(?<![\w])" + re.escape(alias) + r"(?![\w])", canonical, text)
    return [x for x in re.findall(r"[a-z0-9]+(?:\.[a-z0-9]+)*", text) if x not in STOP and len(x) > 1]


def search(records, query, limit=10, private=False, root=ROOT, as_of=None):
    terms = set(tokens(query, root))
    documents = []
    for record in records.values():
        facts = eligible(record, private)
        if facts:
            # Only eligible fact text enters retrieval. Metadata and private notes
            # cannot accidentally become evidence for a job requirement.
            words = Counter(tokens(" ".join(f["text"] for f in facts), root))
            documents.append((record, facts, words))
    df = Counter(t for _, _, words in documents for t in words)
    today = date.fromisoformat(as_of) if as_of else date.today()
    results = []
    for record, facts, words in documents:
        matched = terms & words.keys()
        if not matched:
            continue
        relevance = sum((1 + math.log(1 + words[t])) * math.log(1 + len(documents) / (1 + df[t])) for t in matched)
        relevant_facts = [f for f in facts if set(tokens(f["text"], root)) & matched]
        evidence = sum(1 if f["status"] == "confirmed" else .65 for f in relevant_facts) / len(relevant_facts)
        # Indicators prioritize candidates only; they are never asserted as
        # measured impact, seniority, or semantic qualification coverage.
        fact_text = " ".join(f["text"] for f in relevant_facts).lower()
        impact = float(bool(re.search(r"\b(award|passing|passed|restoration|licensing|adopted|reduced|customers)\b", fact_text)))
        ownership = float(bool(re.search(r"\b(designed|created|led|sole|owned|implemented|developed|built)\b", fact_text)))
        last = record["dates"]["as_of"] if record["dates"]["ongoing"] else record["dates"]["end"] or record["dates"]["start"]
        recency = max(0, 1 - max(0, today.year - int(last[:4])) / 15) if last else 0
        score = relevance * (1 + .15 * evidence + .05 * impact + .05 * ownership + .05 * recency)
        results.append({"id": record["id"], "title": record["title"], "score": round(score, 4), "matched_terms": sorted(matched), "signals": {"lexical": round(relevance, 4), "evidence": round(evidence, 3), "impact_indicator": impact, "ownership_indicator": ownership, "recency": round(recency, 3), "recency_date": last}, "facts": [{"ref": record["id"] + "#" + f["id"], "text": f["text"], "status": f["status"]} for f in relevant_facts]})
    return sorted(results, key=lambda x: (-x["score"], x["id"]))[:limit]


def load_job(root, directory):
    job = read(directory / "job.json")
    validate_as(root, job, "job")
    require("REPLACE_ME" not in json.dumps(job), "Job template still contains placeholders")
    valid_date(job["captured"], False)
    source = within(directory, job["source"])
    reserved = {"job.json", "selection.json", "resume.md", "claims.json", "match-analysis.md", "build-manifest.json"}
    require(source not in {(directory / name).resolve() for name in reserved}, "Job source collides with an application input/output filename")
    require(source.is_file(), f"Missing job description: {source}")
    require(digest(source) == job["source_sha256"], "Job description changed; review requirements and update job.json deliberately")
    ids = [r["id"] for r in job["requirements"]]
    require(len(set(ids)) == len(ids), "Duplicate job requirement IDs")
    for requirement in job["requirements"]:
        check_locator(directory, {"id": requirement["id"], "path": job["source"]}, requirement["locator"])
    return job


def match_job(root, directory, limit=5):
    root = root.resolve()
    records, _, _ = load_db(root)
    job = load_job(root, directory)
    return {"notice": "Retrieval candidates only. An agent must assess semantic coverage, seniority and limitations; scores are not hiring probabilities or ATS scores.", "company": job["company"], "role": job["role"], "requirements": [{**r, "candidates": search(records, " ".join(r["terms"]), limit, root=root, as_of=job["captured"])} for r in job["requirements"]]}


def render(root, directory):
    root = root.resolve()
    records, sources, paths = load_db(root)
    job = load_job(root, directory)
    plan = read(directory / "selection.json")
    validate_as(root, plan, "selection")
    require("REPLACE_ME" not in json.dumps(plan), "Selection template still contains placeholders")
    valid_date(plan["prepared_date"], False)
    require(plan["company"] == job["company"] and plan["role"] == job["role"], "Selection target does not match job")
    require(plan["example"] == job["example"], "Example flag differs from job")
    req_ids = {r["id"] for r in job["requirements"]}
    require(len(plan["matches"]) == len(req_ids) and {m["requirement_id"] for m in plan["matches"]} == req_ids, "Every job requirement needs exactly one coverage decision")
    claims, used_records, used_sources = [], set(), set()

    def resolve(refs):
        expanded = []
        for ref in refs:
            record, fact = get_fact(records, ref, public=True)
            used_records.add(record["id"])
            evidence = []
            for item in fact["evidence"]:
                source = sources[item["source_id"]]
                used_sources.add(source["id"])
                evidence.append({**item, "path": source["path"], "sha256": source["sha256"], "kind": source["kind"]})
            expanded.append({"ref": ref, "text": fact["text"], "status": fact["status"], "evidence": evidence})
        return expanded

    lines = []
    if plan["example"]:
        lines.extend(["<!-- EXAMPLE APPLICATION: fictional job opening; career claims use documented real records. -->", ""])

    def emit(item, prefix=""):
        require("\n" not in item["text"] and "\r" not in item["text"], "Claim must occupy one Markdown source line")
        require(not re.search(r"[<>]", item["text"]), "Application text cannot contain raw HTML")
        facts = resolve(item["refs"])
        if item["verbatim"]:
            require(len(facts) == 1 and item["text"] == facts[0]["text"], "Verbatim item must exactly match one cited fact")
        lines.append(prefix + item["text"])
        claims.append({"line": len(lines), "text": item["text"], "verbatim": item["verbatim"], "facts": facts})

    for i, item in enumerate(plan["identity"]):
        emit(item, "# " if i == 0 else "")
        lines.append("")
    for section in plan["sections"]:
        lines.extend(["## " + section["heading"], ""])
        for item in section["entries"]:
            if item["kind"] == "subheading" and lines[-1] != "":
                lines.append("")
            emit(item, {"bullet": "- ", "paragraph": "", "subheading": "### "}[item["kind"]])
            if item["kind"] != "bullet":
                lines.append("")
        if lines[-1] != "":
            lines.append("")
    resume = "\n".join(lines).rstrip() + "\n"
    analysis = [f"# Job match: {job['company']} — {job['role']}", "", "Example: fictional job opening." if job["example"] else "Job source: " + job["source"], "", "## Positioning", "", plan["positioning"], "", "## Requirement coverage", ""]
    for requirement in job["requirements"]:
        match = next(m for m in plan["matches"] if m["requirement_id"] == requirement["id"])
        if match["coverage"] == "gap":
            require(not match["refs"], "A gap cannot claim supporting evidence; use partial if some exists")
        else:
            require(match["refs"], "Strong/partial coverage needs evidence")
        resolve(match["refs"])
        analysis.extend([f"- **{requirement['id']} · {requirement['importance']} · {match['coverage']}** — {requirement['text']}", f"  {match['reason']}", f"  Evidence: {', '.join(match['refs']) or 'No documented support.'}"])
    analysis.extend(["", "## Content decisions", ""] + ["- " + x for x in plan["decisions"]])
    analysis.extend(["", "## Information worth collecting", ""] + ["- " + x for x in plan["follow_up"]])
    analysis.extend(["", "## Review limits", "", "Trace validation checks references, eligibility, source hashes and output identity. It does not prove that paraphrases follow from their sources, assess actual hiring odds, or test a particular ATS. Semantic and confidentiality review remains part of the agent workflow.", "", "Factual review: " + plan["review_notes"], ""])
    inputs = {"sources/registry.json", "scripts/career.py", "config/aliases.json"}
    inputs.update(str(p.relative_to(root)) for p in (root / "schemas").glob("*.json"))
    inputs.update(str(paths[r].relative_to(root)) for r in used_records)
    inputs.update(sources[s]["path"] for s in used_sources)
    input_hashes = {p: digest(within(root, p)) for p in sorted(inputs)}
    local_hashes = {p: digest(directory / p) for p in ["job.json", "selection.json", job["source"]]}
    outputs = {"resume.md": resume, "match-analysis.md": "\n".join(analysis), "claims.json": encoded({"schema_version": 1, "claims": claims})}
    manifest = {"schema_version": 1, "prepared_date": plan["prepared_date"], "repository_inputs": input_hashes, "application_inputs": local_hashes, "outputs": {p: hashlib.sha256(text.encode()).hexdigest() for p, text in outputs.items()}, "review_limits": "Reference integrity is mechanical; paraphrase entailment and confidentiality require review."}
    outputs["build-manifest.json"] = encoded(manifest)
    return outputs


def build(root, directory, replace=False):
    outputs = render(root, directory)
    for name in outputs:
        require(replace or not (directory / name).exists(), f"{name} exists; save a new application revision or pass --replace after reviewing changes")
    for name, content in outputs.items():
        write(directory / name, content)
    return {"application": str(directory), "outputs": list(outputs)}


def audit(root, directory):
    outputs = render(root, directory)
    for name, content in outputs.items():
        require((directory / name).is_file() and (directory / name).read_text(encoding="utf-8") == content, f"Application drift: {name}; review input/output changes before rebuilding")
    return {"application": str(directory), "status": "PASS", "claims": len(json.loads(outputs["claims.json"])["claims"])}


def ingest(root, source_path, source_id, title, kind, added, private=False, supersedes=None, derived_from=None):
    root = root.resolve()
    lock = within(root, "sources/.ingest-lock")
    try:
        lock.mkdir()
    except FileExistsError:
        raise Invalid("Another ingestion holds sources/.ingest-lock; retry after it finishes. If a process crashed, inspect before removing the stale lock.")
    try:
        return _ingest(root, source_path, source_id, title, kind, added, private, supersedes, derived_from)
    finally:
        lock.rmdir()


def _ingest(root, source_path, source_id, title, kind, added, private=False, supersedes=None, derived_from=None):
    load_db(root)
    require(re.fullmatch(SLUG, source_id), "Invalid source ID")
    valid_date(added, False)
    validate_as(root, {"schema_version": 1, "sources": []}, "sources")
    registry_path = within(root, "sources/registry.json")
    registry = read(registry_path)
    require(source_path.is_file() and not source_path.is_symlink(), "Input must be a regular non-symlink file")
    fingerprint = digest(source_path)
    duplicates = [s for s in registry["sources"] if s["sha256"] == fingerprint]
    if duplicates:
        return {"status": "duplicate", "existing_source_ids": [s["id"] for s in duplicates], "message": "Original already registered; retrieve related records before normalizing."}
    require(source_id not in {s["id"] for s in registry["sources"]}, "Source ID already exists; use a new revision ID")
    supersedes = supersedes or []
    derived_from = derived_from or []
    require(set(supersedes).issubset({s["id"] for s in registry["sources"]}), "Unknown superseded source")
    require(set(derived_from).issubset({s["id"] for s in registry["sources"]}), "Unknown extraction parent source")
    destination_dir = within(root, "sources/" + ("private/" if private else "originals/") + source_id)
    require(not destination_dir.exists(), "Destination already exists")
    destination = destination_dir / source_path.name
    entry = {"id": source_id, "path": str(destination.relative_to(root)), "sha256": fingerprint, "title": title, "kind": kind, "visibility": "private", "added": added, "derived_from": derived_from, "supersedes": supersedes, "notes": "Preserved byte-for-byte. Normalization requires source review; no career claims inferred automatically."}
    registry["sources"].append(entry)
    validate_as(root, registry, "sources")
    destination_dir.mkdir(parents=True)
    try:
        shutil.copyfile(source_path, destination)
        require(digest(destination) == fingerprint, "Copy hash mismatch")
        write(registry_path, encoded(registry))
    except BaseException:
        shutil.rmtree(destination_dir)
        raise
    return {"status": "ingested", "source": entry, "next": "Extract/read the source, search for overlap, then normalize facts using templates/record.json."}


def extract(path):
    if path.suffix.lower() == ".docx":
        with zipfile.ZipFile(path) as archive:
            parts = [x for x in archive.namelist() if re.fullmatch(r"word/(document|header\d+|footer\d+)\.xml", x)]
            output = []
            for part in sorted(parts):
                output.append("## " + part)
                tree = ET.fromstring(archive.read(part))
                ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
                for p in tree.findall(".//w:p", ns):
                    output.append("".join(t.text or "" for t in p.findall(".//w:t", ns)))
            return "\n".join(output) + "\n"
    require(path.suffix.lower() in {".md", ".txt", ".json", ".csv", ".tsv", ".yaml", ".yml"}, "Supported extraction: text or DOCX. For PDFs use existing text extracts or an available PDF reader; preserve and register the extraction separately.")
    return path.read_text(encoding="utf-8")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("validate")
    query = commands.add_parser("search")
    query.add_argument("query")
    query.add_argument("--limit", type=int, default=10)
    query.add_argument("--private", action="store_true", help="Include private facts for career research, never application assembly")
    show = commands.add_parser("show")
    show.add_argument("id")
    index = commands.add_parser("index")
    index.add_argument("--output", type=Path, default=Path("build/search.jsonl"))
    index.add_argument("--private", action="store_true")
    commands.add_parser("duplicates")
    for name in ["match", "build", "audit"]:
        command = commands.add_parser(name)
        command.add_argument("application", type=Path)
        if name == "build":
            command.add_argument("--replace", action="store_true")
        if name == "match":
            command.add_argument("--limit", type=int, default=5)
    command = commands.add_parser("ingest")
    command.add_argument("path", type=Path)
    command.add_argument("--id", required=True)
    command.add_argument("--title", required=True)
    command.add_argument("--kind", choices=["owner_statement", "owner_document", "supplied_analysis", "correspondence", "artifact", "extraction"], required=True)
    command.add_argument("--date", default=date.today().isoformat())
    command.add_argument("--private", action="store_true", help="Store under ignored sources/private; requires separate backup")
    command.add_argument("--supersedes", action="append", default=[])
    command.add_argument("--derived-from", action="append", default=[])
    command = commands.add_parser("extract")
    command.add_argument("path", type=Path)
    args = parser.parse_args(argv)
    root = args.root.resolve()
    if args.command == "extract":
        print(extract(args.path), end="")
        return
    if args.command == "ingest":
        result = ingest(root, args.path, args.id, args.title, args.kind, args.date, args.private, args.supersedes, args.derived_from)
    elif args.command in {"match", "build", "audit"}:
        directory = args.application.resolve()
        require(directory.is_relative_to(root), "Application must live inside repository (use applications/private for sensitive material)")
        result = {"match": lambda: match_job(root, directory, args.limit), "build": lambda: build(root, directory, args.replace), "audit": lambda: audit(root, directory)}[args.command]()
    else:
        records, sources, _ = load_db(root)
        if args.command == "validate":
            result = {"status": "PASS", "records": len(records), "facts": sum(len(r["facts"]) for r in records.values()), "sources": len(sources), "limits": "Structural integrity, source identity and locator bounds only; not independent employer verification or semantic entailment."}
        elif args.command == "search":
            result = search(records, args.query, args.limit, args.private, root)
        elif args.command == "show":
            require(args.id in records, "Unknown record ID")
            result = records[args.id]
        elif args.command == "duplicates":
            groups = {}
            for record in records.values():
                for fact in record["facts"]:
                    key = " ".join(re.findall(r"\w+", fact["text"].lower()))
                    groups.setdefault(key, []).append(record["id"] + "#" + fact["id"])
            result = {"exact_duplicate_facts": [refs for refs in groups.values() if len(refs) > 1], "notice": "Related summaries may overlap intentionally. Review near duplicates through search; never delete evidence automatically."}
        elif args.command == "index":
            output = args.output if args.output.is_absolute() else root / args.output
            build_root = within(root, "build")
            require(output.resolve().is_relative_to(build_root), "Index must be written under ignored build/")
            rows = [{"id": r["id"], "type": r["type"], "facts": [{"ref": r["id"] + "#" + f["id"], "text": f["text"], "status": f["status"], "evidence": f["evidence"]} for f in eligible(r, args.private)]} for r in records.values()]
            write(output, "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows if row["facts"]))
            result = {"output": str(output), "notice": "Derived retrieval corpus. Optional local semantic indexers may consume it; authoritative records remain JSON. Review privacy before sharing."}
    print(encoded(result), end="")


if __name__ == "__main__":
    try:
        main()
    except (Invalid, OSError, ValueError, KeyError, TypeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
