"""Integrity regressions use ONLY synthetic fixtures in temporary repositories."""
from concurrent.futures import ThreadPoolExecutor
import copy
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import threading
import unittest
from unittest.mock import patch
import zipfile

REPO = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("career", REPO / "scripts/career.py")
c = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(c)


class CareerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="career-test-")
        self.root = Path(self.temp.name)
        for name in ["schemas", "config"]:
            shutil.copytree(REPO / name, self.root / name)
        (self.root / "scripts").mkdir()
        shutil.copyfile(REPO / "scripts/career.py", self.root / "scripts/career.py")
        (self.root / "sources/originals").mkdir(parents=True)
        self.source = self.root / "sources/originals/synthetic.txt"
        shutil.copyfile(REPO / "tests/fixtures/synthetic-source.txt", self.source)
        self.record_path = self.root / "knowledge/projects/project-synthetic-widget.json"
        self.record = c.read(REPO / "tests/fixtures/synthetic-record.json")
        c.write(self.record_path, c.encoded(self.record))
        self.registry = {"schema_version": 1, "sources": [{"id": "src-synthetic", "path": "sources/originals/synthetic.txt", "sha256": c.digest(self.source), "title": "SYNTHETIC fixture", "kind": "owner_statement", "visibility": "private", "added": "2026-10-27", "derived_from": [], "supersedes": [], "notes": "Synthetic test data."}]}
        c.write(self.root / "sources/registry.json", c.encoded(self.registry))
        self.app = self.root / "applications/synthetic"
        self.app.mkdir(parents=True)
        (self.app / "job.md").write_text("SYNTHETIC JOB\nRequires Python widget development.\n")
        self.job = {"schema_version": 1, "company": "SYNTHETIC Corp", "role": "Test role", "example": True, "source": "job.md", "source_sha256": c.digest(self.app / "job.md"), "captured": "2026-10-27", "requirements": [{"id": "python", "text": "Python widget development", "importance": "required", "terms": ["Python", "widget"], "locator": "L2-L2"}]}
        claim = {"text": self.record["facts"][0]["text"], "refs": ["project-synthetic-widget#widget"], "verbatim": True}
        self.plan = {"schema_version": 1, "company": self.job["company"], "role": self.job["role"], "example": True, "prepared_date": "2026-10-27", "positioning": "Synthetic test positioning.", "identity": [claim], "sections": [{"heading": "Selected Projects", "entries": [{**claim, "kind": "bullet"}]}], "matches": [{"requirement_id": "python", "coverage": "strong", "refs": claim["refs"], "reason": "Synthetic support."}], "decisions": ["Synthetic selection."], "follow_up": [], "review_notes": "Synthetic literal fact review."}
        self.save_app()

    def tearDown(self):
        self.temp.cleanup()

    def save_app(self):
        c.write(self.app / "job.json", c.encoded(self.job))
        c.write(self.app / "selection.json", c.encoded(self.plan))

    def test_valid_database_and_retrieval(self):
        records, _, _ = c.load_db(self.root)
        result = c.search(records, "Python rollback", root=self.root, as_of="2026-10-27")
        self.assertEqual(result[0]["id"], self.record["id"])
        self.assertEqual(result[0]["signals"]["recency_date"], "2026-10-27")
        self.assertEqual(c.search(records, "SecretTool", root=self.root), [])
        self.assertTrue(c.search(records, "SecretTool", private=True, root=self.root))
        self.assertEqual(c.search(records, "MetadataOnlyTool", root=self.root), [])

    def test_malformed_records_are_rejected(self):
        cases = []
        for mutate in [lambda r: r.update(facts=[]), lambda r: r.update(unrecognized=True), lambda r: r["facts"][0].update(text=" "), lambda r: r["facts"][0].update(evidence=[]), lambda r: r["facts"][0].update(status="proven"), lambda r: r["dates"].update(start="2026-99-99"), lambda r: r["dates"].update(start="2026-04", end="2026-03", ongoing=False), lambda r: r["dates"].update(end="2026-01"), lambda r: r.update(related=["missing-id"]), lambda r: r.update(related=[r["id"]]), lambda r: r["facts"][0]["evidence"][0].update(source_id="missing-source"), lambda r: r["facts"][0]["evidence"][0].update(locator="L99-L100"), lambda r: r["facts"].append(copy.deepcopy(r["facts"][0]))]:
            record = copy.deepcopy(self.record)
            mutate(record)
            cases.append(record)
        for i, record in enumerate(cases):
            with self.subTest(case=i):
                c.write(self.record_path, c.encoded(record))
                with self.assertRaises((c.Invalid, ValueError)):
                    c.load_db(self.root)

    def test_source_drift_and_duplicate_json_keys(self):
        self.source.write_text("Changed original")
        with self.assertRaisesRegex(c.Invalid, "Source changed"):
            c.load_db(self.root)
        path = self.root / "duplicate.json"
        path.write_text('{"fact": 1, "fact": 2}')
        with self.assertRaisesRegex(c.Invalid, "duplicate JSON key"):
            c.read(path)

    def test_docx_extraction_preserves_paragraph_and_header_text(self):
        path = self.root / "synthetic.docx"
        prefix = '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        with zipfile.ZipFile(path, "w") as archive:
            archive.writestr("word/document.xml", prefix + '<w:p><w:r><w:t>SYNTHETIC A &amp; B</w:t></w:r></w:p></w:document>')
            archive.writestr("word/header1.xml", prefix + '<w:p><w:r><w:t>SYNTHETIC header</w:t></w:r></w:p></w:document>')
        result = c.extract(path)
        self.assertIn("SYNTHETIC A & B", result)
        self.assertIn("SYNTHETIC header", result)

    def test_build_is_reproducible_traceable_and_refuses_overwrite(self):
        first = c.render(self.root, self.app)
        self.assertEqual(first, c.render(self.root, self.app))
        c.build(self.root, self.app)
        self.assertEqual(c.audit(self.root, self.app)["status"], "PASS")
        trace = c.read(self.app / "claims.json")["claims"]
        lines = (self.app / "resume.md").read_text().splitlines()
        self.assertIn(trace[0]["text"], lines[trace[0]["line"] - 1])
        self.assertEqual(trace[0]["facts"][0]["evidence"][0]["sha256"], c.digest(self.source))
        with self.assertRaisesRegex(c.Invalid, "exists"):
            c.build(self.root, self.app)

    def test_application_output_and_input_drift(self):
        c.build(self.root, self.app)
        (self.app / "resume.md").write_text("Untraced edit")
        with self.assertRaisesRegex(c.Invalid, "drift"):
            c.audit(self.root, self.app)
        c.build(self.root, self.app, replace=True)
        self.plan["positioning"] = "Changed positioning."
        self.save_app()
        with self.assertRaisesRegex(c.Invalid, "drift"):
            c.audit(self.root, self.app)

    def test_ineligible_claims_and_unknown_fact_references(self):
        for status in ["estimated", "needs_clarification", "superseded"]:
            with self.subTest(status=status):
                record = copy.deepcopy(self.record)
                record["facts"][0]["status"] = status
                c.write(self.record_path, c.encoded(record))
                with self.assertRaisesRegex(c.Invalid, "Not eligible"):
                    c.render(self.root, self.app)
        c.write(self.record_path, c.encoded(self.record))
        for ref in ["project-synthetic-widget#private", "project-synthetic-widget#missing", "missing#fact"]:
            self.plan["identity"][0]["refs"] = [ref]
            self.save_app()
            with self.assertRaises(c.Invalid):
                c.render(self.root, self.app)

    def test_verbatim_and_job_completeness_guards(self):
        self.plan["identity"][0]["text"] = "Invented result"
        self.save_app()
        with self.assertRaisesRegex(c.Invalid, "Verbatim"):
            c.render(self.root, self.app)
        self.plan["identity"][0]["text"] = self.record["facts"][0]["text"]
        self.plan["matches"] = []
        self.save_app()
        with self.assertRaises(c.Invalid):
            c.render(self.root, self.app)

    def test_job_date_source_collision_and_traversal(self):
        self.job["captured"] = "2026-99-99"
        self.save_app()
        with self.assertRaises(ValueError):
            c.load_job(self.root, self.app)
        self.job["captured"] = "2026-10-27"
        for source in ["resume.md", "selection.json", "../outside.md"]:
            self.job["source"] = source
            self.save_app()
            with self.assertRaises(c.Invalid):
                c.load_job(self.root, self.app)

    def test_ingest_preserves_bytes_deduplicates_and_rejects_bad_revision(self):
        incoming = self.root / "incoming.txt"
        incoming.write_text("SYNTHETIC new evidence\n")
        result = c.ingest(self.root, incoming, "src-new", "Synthetic", "owner_statement", "2026-10-27")
        self.assertEqual(result["status"], "ingested")
        destination = self.root / result["source"]["path"]
        self.assertEqual(destination.read_bytes(), incoming.read_bytes())
        self.assertEqual(c.ingest(self.root, incoming, "src-other", "Duplicate", "owner_statement", "2026-10-27")["status"], "duplicate")
        incoming.write_text("Different revision\n")
        with self.assertRaisesRegex(c.Invalid, "already exists"):
            c.ingest(self.root, incoming, "src-new", "Revision", "owner_statement", "2026-10-27")
        with self.assertRaisesRegex(c.Invalid, "Unknown superseded"):
            c.ingest(self.root, incoming, "src-revision", "Revision", "owner_statement", "2026-10-27", supersedes=["missing"])
        self.assertEqual(destination.read_text(), "SYNTHETIC new evidence\n")
        c.load_db(self.root)

    def test_ingest_rejects_symlink_directory_escape(self):
        with tempfile.TemporaryDirectory(prefix="career-outside-") as outside:
            incoming = self.root / "incoming.txt"
            incoming.write_text("SYNTHETIC new evidence")
            (self.root / "sources/private").symlink_to(outside, target_is_directory=True)
            with self.assertRaisesRegex(c.Invalid, "escapes root"):
                c.ingest(self.root, incoming, "src-new", "Synthetic", "owner_statement", "2026-10-27", private=True)
            self.assertEqual(list(Path(outside).iterdir()), [])

    def test_index_rejects_external_build_symlink(self):
        with tempfile.TemporaryDirectory(prefix="career-index-outside-") as outside:
            (self.root / "build").symlink_to(outside, target_is_directory=True)
            with self.assertRaisesRegex(c.Invalid, "escapes root"):
                c.main(["--root", str(self.root), "index"])
            self.assertEqual(list(Path(outside).iterdir()), [])

    def test_source_provenance_cycles_are_rejected(self):
        self.registry["sources"][0]["derived_from"] = ["src-other"]
        other = copy.deepcopy(self.registry["sources"][0])
        other.update(id="src-other", derived_from=["src-synthetic"])
        self.registry["sources"].append(other)
        c.write(self.root / "sources/registry.json", c.encoded(self.registry))
        with self.assertRaisesRegex(c.Invalid, "Cyclic source"):
            c.load_db(self.root)

    def test_concurrent_ingest_does_not_lose_registry_entries(self):
        first, second = self.root / "first.txt", self.root / "second.txt"
        first.write_text("SYNTHETIC first")
        second.write_text("SYNTHETIC second")
        entered, release = threading.Event(), threading.Event()
        copyfile = shutil.copyfile

        def blocked_copy(source, destination):
            entered.set()
            self.assertTrue(release.wait(5))
            return copyfile(source, destination)

        with patch.object(c.shutil, "copyfile", side_effect=blocked_copy), ThreadPoolExecutor(max_workers=2) as pool:
            future = pool.submit(c.ingest, self.root, first, "src-first", "First", "owner_statement", "2026-10-27")
            self.assertTrue(entered.wait(5))
            try:
                with self.assertRaisesRegex(c.Invalid, "Another ingestion"):
                    c.ingest(self.root, second, "src-second", "Second", "owner_statement", "2026-10-27")
            finally:
                release.set()
            self.assertEqual(future.result()["status"], "ingested")
        self.assertEqual(c.ingest(self.root, second, "src-second", "Second", "owner_statement", "2026-10-27")["status"], "ingested")
        _, sources, _ = c.load_db(self.root)
        self.assertTrue({"src-first", "src-second"}.issubset(sources))


if __name__ == "__main__":
    unittest.main()
