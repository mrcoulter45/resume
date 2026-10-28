#!/usr/bin/env python3
"""Check final PDFs against their canonical content; write a human-readable QA report.

Run build_resume.py first. Visual inspection of rendered PNGs remains required.
"""
import json
import re
from hashlib import sha256
from pathlib import Path
from urllib.parse import urlparse

import pdfplumber
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / "resume-content.json").read_text())
MANIFEST = json.loads((ROOT / "claim-manifest.json").read_text())
QA = ROOT / "qa"
QA.mkdir(exist_ok=True)


def evidence_path(name):
    """README line references belong to the immutable pre-KB career profile.

    Keep historical audit keys/hashes unchanged while the repository README
    becomes navigation for the knowledge base.
    """
    if name == "README.md":
        name = "sources/originals/README-before-knowledge-base.md"
    return ROOT.parent / name


def norm(text):
    return re.sub(r"\s+", " ", text).strip()


def check(stem):
    path = ROOT / f"{stem}.pdf"
    version = DATA["versions"][stem]
    parents = version.get("claim_parents", {})
    assert MANIFEST[stem].get("claim_parents", {}) == parents, (stem, "group manifest mismatch")
    if parents:
        assert "pages" not in version, (stem, "grouping currently supported for single-page versions")
        selected = [key for role in ["senior", "software", "graduate"] for key in version[role]]
        assert set(parents).issubset(selected), (stem, "grouped claim not selected")
        assert set(parents.values()).issubset(selected), (stem, "group parent not selected")
        assert not set(parents).intersection(parents.values()), (stem, "only one child indentation level is supported")
        for role in ["senior", "software", "graduate"]:
            active_parent = None
            for key in version[role]:
                if key in parents:
                    assert parents[key] == active_parent, (stem, "child must immediately follow its parent group", key)
                else:
                    active_parent = key
    reader = PdfReader(path)
    expected_pages = len(version["pages"]) if "pages" in version else 1
    assert len(reader.pages) == expected_pages, (stem, "wrong page count")
    raw = "\n".join(p.extract_text(extraction_mode="plain") for p in reader.pages)
    text = norm(raw)
    assert "\ufffd" not in text and "\x00" not in text, (stem, "corrupt text")
    assert DATA["name"] in text
    assert DATA["email"] in text
    assert DATA["education"]["institution"] in text
    assert DATA["education"]["degree"] in text
    assert DATA["education"]["focus"] in text
    assert "Bachelor of Science, Computer Engineering" not in text
    if version.get("include_education_award", True):
        assert DATA["education"]["award"] in text
    assert version.get("recognition", DATA["recognition"]["text"]) in text
    assert version.get("scope", DATA["scope"]) in text and "CMN GUI Lead" in text
    if version.get("summary"):
        assert norm(version["summary"]) in text, (stem, "missing summary")
        assert version.get("summary_sources"), (stem, "summary needs provenance")
        assert text.index(norm(version["summary"])) < text.index("PROFESSIONAL EXPERIENCE")
    assert "Interconnect Assistant" not in text
    assert not any(name in text for name in ["Cyprus", "Delphi", "Tower", "Twain", "Chariot"]), (stem, "internal codename in application copy")
    for role in DATA["roles"].values():
        assert role["title"] in text and role["dates"] in text, (stem, role)
    claim_positions = []
    markdown_lines = (ROOT / f"{stem}.md").read_text().splitlines()
    for claim_id in MANIFEST[stem]["claims"]:
        claim = norm(DATA["claims"][claim_id]["text"])
        assert claim in text, (stem, "missing/altered claim", claim_id)
        claim_positions.append(text.index(claim))
        prefix = "" if claim_id == "internships" else ("    " if claim_id in parents else "") + "- "
        markdown_text = DATA["claims"][claim_id]["text"]
        for term in DATA["claims"][claim_id].get("code_spans", []):
            markdown_text = markdown_text.replace(term, f'`{term}`')
        expected_md = prefix + markdown_text
        assert expected_md in markdown_lines, (stem, "Markdown claim or indentation mismatch", claim_id)
    assert claim_positions == sorted(claim_positions), (stem, "claim reading order")
    for label, skills in DATA["versions"][stem]["skills"]:
        assert norm(f"{label}: {skills}") in text, (stem, "missing skills", label)
    uris = []
    fonts = []
    for i, page in enumerate(reader.pages):
        assert abs(float(page.mediabox.width) - 612) < .01
        assert abs(float(page.mediabox.height) - 792) < .01
        assert not page.images, (stem, "unexpected embedded image")
        for obj in page.get("/Annots", []):
            annotation = obj.get_object()
            action = annotation.get("/A", {})
            if action.get("/S") == "/URI":
                uri = str(action["/URI"])
                assert urlparse(uri).scheme in ["https", "mailto", "tel"]
                uris.append(uri)
            rect = list(map(float, annotation["/Rect"]))
            assert 0 <= min(rect[0], rect[2]) < max(rect[0], rect[2]) <= 612
            assert 0 <= min(rect[1], rect[3]) < max(rect[1], rect[3]) <= 792
        for obj in page["/Resources"].get("/Font", {}).values():
            font = obj.get_object()
            if font.get("/Subtype") == "/TrueType":
                assert "/ToUnicode" in font, (stem, "missing Unicode map")
                assert "/FontFile2" in font["/FontDescriptor"], (stem, "unembedded TrueType font")
                fonts.append(str(font["/BaseFont"]))
    expected_uris = [f'mailto:{DATA["email"]}', "tel:+17606946310", DATA["linkedin"], DATA["github"]]
    if version.get("include_portfolio", True):
        expected_uris.append(DATA["portfolio"])
    else:
        assert DATA["portfolio"].removeprefix("https://").rstrip("/") not in text
        assert "portfolio" not in text.lower(), (stem, "removed portfolio text remains")
    assert sorted(uris) == sorted(expected_uris), (stem, "unexpected link targets", uris)
    bounds = []
    with pdfplumber.open(path) as pdf:
        code_terms = [term for claim_id in MANIFEST[stem]["claims"]
                      for term in DATA["claims"][claim_id].get("code_spans", [])]
        words = [word for page in pdf.pages for word in page.extract_words(extra_attrs=["fontname"])] if code_terms else []
        for term in set(code_terms):
            matches = [word for word in words if word["text"] == term]
            assert len(matches) == code_terms.count(term) and all("DejaVuSansMono" in word["fontname"] for word in matches), (stem, "inline code font missing", term)
        for page in pdf.pages:
            chars = [c for c in page.chars if c["text"].strip()]
            assert chars, (stem, "no text layer")
            assert all(c["x0"] >= 35 and c["x1"] <= 577 for c in chars), (stem, "horizontal overflow")
            assert all(c["top"] >= 25 and c["bottom"] <= 776 for c in chars), (stem, "vertical overflow")
            # Core accomplishment text must retain the authored body size.
            assert any(abs(c["size"] - MANIFEST[stem]["body_size_pt"]) < .01 for c in chars)
            lines = page.extract_text_lines()
            if parents:
                for claim_id in MANIFEST[stem]["claims"]:
                    prefix = "- " + " ".join(DATA["claims"][claim_id]["text"].split()[:5])
                    matches = [line for line in lines if norm(line["text"]).startswith(prefix)]
                    assert len(matches) == 1, (stem, "grouped bullet start not found", claim_id)
                    expected_x = 55 if claim_id in parents else 37
                    assert abs(matches[0]["x0"] - expected_x) < .1, (stem, "PDF bullet indentation mismatch", claim_id)
            for previous, current in zip(lines, lines[1:]):
                assert current["top"] > previous["top"] + 1, (stem, "line order/overlap")
            bounds.append({"left": round(min(c["x0"] for c in chars), 2),
                           "right": round(max(c["x1"] for c in chars), 2),
                           "top": round(min(c["top"] for c in chars), 2),
                           "bottom": round(max(c["bottom"] for c in chars), 2),
                           "font_sizes": sorted(set(round(c["size"], 2) for c in chars)),
                           "line_count": len(lines)})
    (QA / f"{stem}-extracted.txt").write_text(raw)
    return {"pages": expected_pages, "page_size": "612 x 792 pt (US Letter)",
            "body_font_pt": MANIFEST[stem]["body_size_pt"], "fonts": sorted(set(fonts)), "links": uris,
            "text_bounds_from_top_pt": bounds, "word_count": len(text.split()),
            "sha256": sha256(path.read_bytes()).hexdigest(),
            "grouped_claims_checked": len(parents),
            "all_selected_claims_present_and_ordered": True}


def main():
    source_files = {"README": "README.md", "LINKS": "links.md", "DOCX": "2020-Sep.docx",
                    "IA": "Interconnect-Architect-resume.md", "AI": "AI-System-resume.md",
                    "CLARIFICATIONS": "career-clarifications.md",
                    "CURRENT": "career-clarifications-2026-10-21.md",
                    "WORKFLOW": "career-clarifications-workflows-and-embedded.md",
                    "RUNTIME": "career-clarifications-grouping-and-runtime-2026-10-22.md",
                    "IMPACT": "career-clarifications-agent-impact-and-e2e-2026-10-22.md",
                    "TESTING": "source-archive/ia-mcp-testing-correspondence-2026-10-22.txt",
                    "DUAL_RUNTIME": "source-archive/ia-mcp-runtime-correspondence-2026-10-22.txt",
                    "ROLE_FIT": "career-clarifications-netflix-fit-2026-10-22.md",
                    "REPAIR_SCOPE": "career-clarifications-repair-scope-2026-10-23.md",
                    "README_ARCHIVE": "source-archive/README-before-2026-10-20-clarifications.md",
                    "IA_ARCHIVE": "source-archive/Interconnect-Architect-resume-before-2026-10-20-clarifications.md",
                    "LI": "LinkedIn-Profile-Export/Profile.pdf",
                    "AI_AWARD": "LinkedIn-Profile-Export/Engineering AI Showcase Most Innovative Award.jpeg",
                    "QUALITY_AWARD": "LinkedIn-Profile-Export/Arm Quality Award 2020 for the Mbed OS FPGA CI Test Shield.png",
                    "CAPSTONE_AWARD": "LinkedIn-Profile-Export/UT ECE Senior Design First Place.jpeg",
                    "COHERENT_RELEASE": "LinkedIn-Profile-Export/Coherent interconnect product release.jpeg",
                    "NONCOHERENT_RELEASE": "LinkedIn-Profile-Export/Non-coherent interconnect product release .jpeg"}
    refs = [ref for claim in DATA["claims"].values() for ref in claim["sources"]]
    for key in ["identity_sources", "history_sources", "scope_sources", "skill_sources"]:
        refs.extend(DATA[key])
    refs.extend(DATA["education"]["sources"])
    refs.extend(DATA["recognition"]["sources"])
    for version in DATA["versions"].values():
        for key in ["scope_sources", "summary_sources", "skill_sources"]:
            refs.extend(version.get(key, []))
    for ref in refs:
        source, locator = ref.split(":", 1)
        assert source in source_files and locator, ("Unknown evidence reference", ref)
        path = evidence_path(source_files[source])
        assert path.is_file(), ("Missing original evidence", ref)
        if path.suffix.lower() == ".pdf":
            match = re.fullmatch(r"p(\d+)(?:-(\d+))?", locator)
            assert match, ("Invalid PDF evidence page range", ref)
            start, end = int(match.group(1)), int(match.group(2) or match.group(1))
            assert 1 <= start <= end <= len(PdfReader(path).pages), ref
        elif path.suffix.lower() in [".png", ".jpeg", ".jpg"]:
            assert locator == "visual", ("Invalid image evidence locator", ref)
        elif source != "DOCX":
            match = re.fullmatch(r"(\d+)(?:-(\d+))?", locator)
            assert match, ("Invalid evidence line range", ref)
            start = int(match.group(1))
            end = int(match.group(2) or match.group(1))
            assert 1 <= start <= end <= len(path.read_text().splitlines()), ref
    results = {stem: check(stem) for stem in DATA["versions"]}
    # Registered fingerprints include the two explicitly authorized corrections,
    # their untouched before-edit snapshots, and the direct user clarification.
    source_hashes = {name: sha256(evidence_path(name).read_bytes()).hexdigest()
                     for name in source_files.values()}
    baseline = {
        "2020-Sep.docx": "6f93ce76078b10e54da1f867ae17fce1075a9a5671c13c0ab1771bf338ecc1ee",
        "Interconnect-Architect-resume.md": "eba6b043b39fc4f3456c40de266237847adbc5a29a8be593b5278ff9cec243f8",
        "README.md": "5571780b90c180616fd432990fb1b39f82443c4089c944dd3818e548e2d09280",
        "links.md": "a2466ff512929bd981608219f452e638a86be912aa1bdf87774bd859712d5927",
        "AI-System-resume.md": "3fbf27818a84d1a33430fe738b953864f79e267284c2049244279749d41e3892",
        "LinkedIn-Profile-Export/Profile.pdf": "cfcd5a380e353458f360c15d2ed75127822c7796e905683e454690f7a7517d54",
        "LinkedIn-Profile-Export/Engineering AI Showcase Most Innovative Award.jpeg": "b75bb09984419a6d74b3aab657144e11667441dd586d96a3ba3731627d9169ee",
        "LinkedIn-Profile-Export/Arm Quality Award 2020 for the Mbed OS FPGA CI Test Shield.png": "f303b842985ed8de0b6b27b2e8562d405d5434ccdf7e38508a12a690e2e93f1f",
        "LinkedIn-Profile-Export/UT ECE Senior Design First Place.jpeg": "51486660a9bdf0529f24df443f6c23ab401d7a7221dad73cfe2e0da1a6f1c7fb",
        "LinkedIn-Profile-Export/Coherent interconnect product release.jpeg": "8e331e6db8696e6bcd97bc94576abeaf268d3746ff8b5da5614a8da7936a3729",
        "LinkedIn-Profile-Export/Non-coherent interconnect product release .jpeg": "8c9dd3da111c965f6b7b0c78adc507a0980a31abe1eca7eb951a5e5a6f2c11ac"}
    baseline.update({
        "career-clarifications-repair-scope-2026-10-23.md": "4edf76abb99706a91f1ede35cac67b446e16d828094da405df80d21a273b107d",
        "career-clarifications-netflix-fit-2026-10-22.md": "68dbe86988a6e44e1af5cffff63b528a175f1c2ce796c3def9490c46deb31008",
        "source-archive/ia-mcp-runtime-correspondence-2026-10-22.txt": "a8e041f1c84fa15864edc88200c023dba06afff52203b488ff3d71f2fbdd5832",
        "source-archive/ia-mcp-testing-correspondence-2026-10-22.txt": "bef296728ff56a57ffb158a7d9014da95f3ffe3188ae66b5bb8a3eada9b7f3e4",
        "career-clarifications-agent-impact-and-e2e-2026-10-22.md": "f43efce49cc2202ad223c8767d56cce4fd2a4c0cb4cd8cec1e118a87830635a1",
        "career-clarifications-grouping-and-runtime-2026-10-22.md": "85dbc8722edf69093a49b131bf66e93941a2fbf08d446fa7f19a40f927b4d32f",
        "career-clarifications-workflows-and-embedded.md": "1935ce52a058acd58a08685290b5d9c01b10132dde1c28bc368652220ec0c8e4",
        "career-clarifications-2026-10-21.md": "62728ee656cb3dac7556c98a7bfdf5589526ade7b21d9370aa1106e8e4b702f7",
        "career-clarifications.md": "afc449155ff3f2f26f160e12b6eeb918005421beeaf6a56714c251a652018d22",
        "source-archive/README-before-2026-10-20-clarifications.md": "f45c065ea94c7cd941c8d914606a47958e2df81a72000d1ebce20e8e6be52c83",
        "source-archive/Interconnect-Architect-resume-before-2026-10-20-clarifications.md": "447ff5cded12ad04917850727de035d50adaecf44635ee2de776c9977607c54f"})
    assert source_hashes == baseline, "Registered career evidence changed without an audited baseline update"
    audit = json.loads((QA / "source-update-audit.json").read_text())
    assert {change["path"] for change in audit["changes"]} == {"README.md", "Interconnect-Architect-resume.md"}
    for change in audit["changes"]:
        assert source_hashes[change["path"]] == change["after_sha256"]
        assert source_hashes[change["original_snapshot"]] == change["before_sha256"]
        assert change["authorization"]
    for update in audit.get("clarification_updates", []):
        assert source_hashes[update["path"]] == update["after_sha256"]
        assert update["authorization"]
    for change in audit["changes"] + audit.get("clarification_updates", []):
        revisions = change.get("revisions", [])
        if revisions:
            assert revisions[0]["before_sha256"] == change["before_sha256"]
            assert revisions[-1]["after_sha256"] == change["after_sha256"]
            assert all(a["after_sha256"] == b["before_sha256"] for a, b in zip(revisions, revisions[1:]))
    active_text_files = [ROOT.parent / "README.md", ROOT.parent / "career-clarifications.md",
                         ROOT / "master-career-profile.md", ROOT / "resume-review.md", ROOT / "README.md"]
    for path in active_text_files:
        assert "created waveform viewer tools" not in path.read_text().lower(), (path.name, "rejected viewer-creation claim")
    assert "Used waveform viewers to debug" in (ROOT.parent / "career-clarifications.md").read_text()
    report = {"pdfs": results, "source_hashes": source_hashes,
              "registered_source_fingerprints_match": True,
              "authorized_source_updates": audit["changes"],
              "clarification_updates": audit.get("clarification_updates", []),
              "other_original_source_files_unchanged": 9,
              "checks": ["expected page counts", "US Letter", "text layer and Unicode",
                         "all canonical claims and skills present", "logical claim reading order",
                         "contiguous project grouping, Markdown nesting and PDF bullet indentation",
                         "contact/title/date/degree integrity", "exact per-version clickable link targets",
                         "embedded TrueType fonts", "no page images", "text and link bounds",
                         "line order", "source fingerprints", "evidence reference files, line/page ranges and image locators",
                         "per-version showcase recognition and capstone category when selected",
                         "CMN GUI Lead scope and corrected application name",
                         "no internal codenames in application PDFs",
                         "authorized source corrections match preserved original snapshots",
                         "waveform debugging resolved as tool use in active career documents",
                         "corrected Electrical and Computer Engineering degree and both academic focus areas"],
              "limits": ["ATS vendor parsing is not independently tested",
                         "rendered pages require separate visual inspection",
                         "destination availability is separate from PDF annotation validation"]}
    (QA / "validation.json").write_text(json.dumps(report, indent=2) + "\n")
    for stem, result in results.items():
        print(f'{stem}: PASS ({result["pages"]} page(s), {result["word_count"]} extracted words)')
    print("Registered source fingerprints and authorized-correction audit: PASS")


if __name__ == "__main__":
    main()
