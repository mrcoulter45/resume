#!/usr/bin/env python3
"""Build the resume PDFs, matching Markdown and a claim/source manifest.

All layout is ordinary PDF text. No tables, columns, text boxes or images.
Fonts ship with ReportLab. Content lives in resume-content.json.
"""
from __future__ import annotations

import argparse
import json
from html import escape
from pathlib import Path

import reportlab
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / "resume-content.json").read_text())
WIDTH, HEIGHT = letter
MARGIN = 36
TEXT_WIDTH = WIDTH - 2 * MARGIN
BOTTOM = 34
INK = colors.HexColor("#171B21")
MUTED = colors.HexColor("#444B54")
RULE = colors.HexColor("#A9AEB4")


def register_fonts():
    fonts = Path(reportlab.__file__).parent / "fonts"
    for name, filename in [("Resume", "Vera.ttf"), ("Resume-Bold", "VeraBd.ttf"),
                           ("Resume-Italic", "VeraIt.ttf")]:
        pdfmetrics.registerFont(TTFont(name, str(fonts / filename)))
    pdfmetrics.registerFontFamily("Resume", normal="Resume", bold="Resume-Bold", italic="Resume-Italic")
    pdfmetrics.registerFont(TTFont("Resume-Mono", str(ROOT / "fonts" / "DejaVuSansMono.ttf")))


class Resume:
    def __init__(self, stem, detailed=False):
        self.stem = stem
        self.detailed = detailed
        self.version = DATA["versions"][stem]
        self.pdf = canvas.Canvas(str(ROOT / (stem + ".pdf")), pagesize=letter, invariant=1,
                                 pageCompression=1)
        self.pdf.setTitle(f"{DATA['name']} - Resume")
        self.pdf.setAuthor(DATA["name"])
        self.pdf.setSubject(DATA["versions"][stem]["label"])
        self.pdf.setCreator("build_resume.py / ReportLab")
        # A fixed preparation date keeps builds deterministic without the
        # library's default invariant-mode January 2000 metadata timestamp.
        prepared = self.version.get("prepared_date", DATA["prepared_date"]).replace("-", "")
        self.pdf.setDateFormatter(lambda *unused: f"D:{prepared}120000-05'00'")
        self.y = HEIGHT - MARGIN
        self.used_claims = []
        self.page_bottoms = []
        self.body_size = self.version.get("body_size_pt", 11 if detailed else 10.5)
        self.leading = self.version.get("leading_pt", 15.4 if detailed else 13.6)
        self.style = ParagraphStyle("body", fontName="Resume", fontSize=self.body_size,
                                    leading=self.leading, textColor=INK, alignment=TA_LEFT)
        self.md = []

    def p(self, text, *, indent=0, size=None, leading=None, color=None, bold=False, after=0):
        style = ParagraphStyle("local", parent=self.style, fontSize=size or self.body_size,
                               leading=leading or self.leading, textColor=color or INK,
                               fontName="Resume-Bold" if bold else "Resume")
        para = Paragraph(text, style)
        _, h = para.wrap(TEXT_WIDTH - indent, HEIGHT)
        if self.y - h < BOTTOM:
            raise ValueError(f"{self.stem}: text overflows page at y={self.y:.1f}: {text[:90]}")
        para.drawOn(self.pdf, MARGIN + indent, self.y - h)
        self.y -= h + after

    def header(self, continuation=False):
        if continuation:
            self.p(escape(DATA["name"]), size=15.5, leading=19, bold=True, after=2)
            self.p("Arm | Senior Software Engineer | Continued", size=10.5, color=MUTED, after=10)
            return
        self.p(escape(DATA["name"]), size=23, leading=28, bold=True, after=5)
        line = (f'{escape(DATA["location"])} | '
                f'<link href="mailto:{DATA["email"]}">{escape(DATA["email"])}</link> | '
                f'<link href="tel:+17606946310">{escape(DATA["phone"])}</link>')
        self.p(line, size=10, leading=13.2, after=2)
        links = [
            (DATA["linkedin"], "linkedin.com/in/michael-coulter-164868153"),
            (DATA["github"], "github.com/mrcoulter45")]
        if self.version.get("include_portfolio", True):
            links.append((DATA["portfolio"], "mrcoulter45.github.io/portfolio"))
        # Readable labels keep every link identifiable on a printed resume.
        self.p(" | ".join(f'<link href="{url}">{label}</link>' for url, label in links),
               size=8.6 if self.version.get("include_portfolio", True) else 9.4,
               leading=12, after=9)
        self.md.extend([f'# {DATA["name"]}', "",
                        f'{DATA["location"]} | [{DATA["email"]}](mailto:{DATA["email"]}) | {DATA["phone"]}',
                        " | ".join(f'[{label}]({url})' for url, label in links), ""])

    def section(self, name):
        self.y -= 8
        self.p(escape(name.upper()), size=10.5, leading=13, bold=True, after=3)
        self.pdf.setStrokeColor(RULE)
        self.pdf.setLineWidth(0.45)
        self.pdf.line(MARGIN, self.y, WIDTH - MARGIN, self.y)
        self.y -= 7
        self.md.extend([f"## {name}", ""])

    def summary(self):
        summary = self.version.get("summary")
        if summary:
            self.p(escape(summary), after=4)
            self.md.extend([summary, ""])

    def role(self, key, continuation=False):
        info = DATA["roles"][key]
        text = info["title"] + (" (continued)" if continuation else "")
        self.y -= 2
        # Date is a right-aligned text run on the same baseline, not a table.
        self.pdf.setFillColor(INK)
        self.pdf.setFont("Resume-Bold", 10.7)
        baseline = self.y - 10.7
        self.pdf.drawString(MARGIN, baseline, text)
        self.pdf.setFont("Resume", 10.1)
        self.pdf.drawRightString(WIDTH - MARGIN, baseline, info["dates"])
        self.y -= 17
        if not continuation:
            self.md.extend([f'### {info["title"]} | {info["dates"]}', ""])

    def company(self):
        self.p(f'<b>{escape(DATA["employer"])}</b> | {escape(DATA["employer_location"])}',
               size=11.5, leading=15.3, after=1)
        self.md.extend([f'**{DATA["employer"]} - {DATA["employer_location"]}**', ""])

    def scope(self):
        scope = self.version.get("scope", DATA["scope"])
        self.p(escape(scope), color=MUTED, size=10.1, leading=13.2, after=4)
        self.md.extend([scope, ""])
        if self.version.get("recognition_position", "before") == "before":
            self.recognition()

    def recognition(self):
        recognition = self.version.get("recognition", DATA["recognition"]["text"])
        self.p(f'<b>Recognition:</b> {escape(recognition)}', size=10.5, leading=13.6, after=4)
        self.md.extend([f'**Recognition:** {recognition}', ""])

    def bullet(self, claim_id):
        item = DATA["claims"][claim_id]
        pdf_text, markdown_text = escape(item["text"]), item["text"]
        for term in item.get("code_spans", []):
            if not term or item["text"].count(term) != 1 or "`" in term:
                raise ValueError(f"{claim_id}: inline code must identify one unambiguous text span")
            pdf_text = pdf_text.replace(escape(term), f'<font name="Resume-Mono">{escape(term)}</font>')
            markdown_text = markdown_text.replace(term, f'`{term}`')
        child = claim_id in self.version.get("claim_parents", {})
        offset = 18 if child else 0
        # A regular ASCII hyphen is accessible in text extraction and uses no icon font.
        top = self.y
        self.pdf.setFillColor(INK)
        self.pdf.setFont("Resume", self.body_size)
        self.pdf.drawString(MARGIN + 1 + offset, top - self.body_size, "-")
        self.p(pdf_text, indent=11 + offset, after=4 if not self.detailed else 6)
        self.used_claims.append(claim_id)
        self.md.append(("    " if child else "") + f'- {markdown_text}')

    def skills(self, version):
        self.section("Technical Skills")
        for label, value in version["skills"]:
            self.p(f'<b>{escape(label)}:</b> {escape(value)}', size=10.1, leading=13.4, after=1)
            self.md.append(f'**{label}:** {value}  ')
        self.md.append("")

    def education(self):
        self.section("Education")
        edu = DATA["education"]
        self.p(f'<b>{escape(edu["institution"])}</b>', size=10.5, leading=13.6)
        # Keep the degree and date in linear reading order on their own line.
        self.p(f'{escape(edu["degree"])} | {escape(edu["date"])}', size=10.3, leading=13.6)
        self.p(escape(edu["focus"]), size=10.1, leading=13.4)
        self.md.extend([f'**{edu["institution"]}**', f'{edu["degree"]} | {edu["date"]}',
                        edu["focus"]])
        if self.version.get("include_education_award", True):
            self.p(escape(edu["award"]), size=10.1, leading=13.4)
            self.md.append(edu["award"])
        self.md.append("")

    def finish_page(self, number=None):
        self.page_bottoms.append(round(self.y, 2))
        if number:
            self.pdf.setFont("Resume", 9)
            self.pdf.setFillColor(MUTED)
            self.pdf.drawRightString(WIDTH - MARGIN, 20, f"{number} / 2")
        self.pdf.showPage()
        self.y = HEIGHT - MARGIN

    def finish(self):
        self.pdf.save()
        (ROOT / (self.stem + ".md")).write_text("\n".join(self.md).rstrip() + "\n")
        return {"claims": {key: DATA["claims"][key]["sources"] for key in self.used_claims},
                "claim_parents": self.version.get("claim_parents", {}),
                "pages": len(self.page_bottoms), "layout_bottoms_pt": self.page_bottoms,
                "body_size_pt": self.body_size, "leading_pt": self.leading,
                "identity_sources": DATA["identity_sources"],
                "history_sources": DATA["history_sources"],
                "scope_sources": self.version.get("scope_sources", DATA["scope_sources"]),
                "summary_sources": self.version.get("summary_sources", []),
                "recognition_sources": DATA["recognition"]["sources"],
                "education_sources": DATA["education"]["sources"],
                "skill_sources": self.version.get("skill_sources", DATA["skill_sources"]),
                "target": self.version.get("target"),
                "prepared_date": self.version.get("prepared_date", DATA["prepared_date"]),
                "include_portfolio": self.version.get("include_portfolio", True)}


def build(stem):
    version = DATA["versions"][stem]
    detailed = "pages" in version
    doc = Resume(stem, detailed)
    if detailed:
        for i, page in enumerate(version["pages"]):
            doc.header(continuation=i > 0)
            doc.section(page["title"])
            if i == 0:
                doc.company()
            doc.role("senior", continuation=i > 0)
            if i == 0:
                doc.scope()
            for claim in page["senior"]:
                doc.bullet(claim)
            for role in ["software", "graduate"]:
                if role in page:
                    doc.md.append("")
                    doc.role(role)
                    for claim in page[role]:
                        doc.bullet(claim)
            if page.get("internships"):
                doc.y -= 3
                doc.p(escape(DATA["claims"]["internships"]["text"]), size=9.8, leading=13.2, after=3)
                doc.md.extend(["", DATA["claims"]["internships"]["text"], ""])
                doc.used_claims.append("internships")
            if page.get("skills"):
                doc.skills(version)
            if page.get("education"):
                doc.education()
            doc.finish_page(i + 1)
    else:
        doc.header()
        doc.summary()
        doc.section("Professional Experience")
        doc.company()
        for role in ["senior", "software", "graduate"]:
            doc.role(role)
            if role == "senior":
                doc.scope()
            for claim in version[role]:
                doc.bullet(claim)
            if role == "senior" and version.get("recognition_position") == "after":
                doc.md.append("")
                doc.recognition()
            doc.md.append("")
        doc.skills(version)
        doc.education()
        doc.finish_page()
    manifest = doc.finish()
    print(f'{stem}.pdf: {manifest["pages"]} page(s); final text bottoms {manifest["layout_bottoms_pt"]} pt')
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    selection = parser.add_mutually_exclusive_group()
    selection.add_argument("--version", choices=list(DATA["versions"]), help="Build one version; default builds all")
    selection.add_argument("--applications", action="store_true", help="Build only the four company-specific application resumes")
    args = parser.parse_args()
    register_fonts()
    stems = ([args.version] if args.version else
             [stem for stem, version in DATA["versions"].items() if version.get("application")]
             if args.applications else list(DATA["versions"]))
    manifests = {stem: build(stem) for stem in stems}
    path = ROOT / "claim-manifest.json"
    existing = json.loads(path.read_text()) if path.exists() else {}
    existing.update(manifests)
    path.write_text(json.dumps(existing, indent=2) + "\n")


if __name__ == "__main__":
    main()
