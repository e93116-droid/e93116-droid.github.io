#!/usr/bin/env python3
"""Offline checks for the OAuth information website."""
import re
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
PAGES = ["index.html", "privacy.html", "terms.html"]

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.tags = []
        self.headings = []
        self.title_text = []
        self.in_title = False
    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        self.tags.append((tag, data))
        if tag == "a":
            self.links.append(data.get("href", ""))
        if tag == "h1":
            self.headings.append("h1")
        if tag == "title":
            self.in_title = True
    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
    def handle_data(self, value):
        if self.in_title:
            self.title_text.append(value)

class PublicSiteTest(unittest.TestCase):
    def test_every_page_self_contained_with_working_local_links(self):
        for name in PAGES:
            with self.subTest(name=name):
                content=(ROOT/name).read_text(encoding="utf-8")
                p=PageParser()
                p.feed(content)
                self.assertEqual(p.headings.count("h1"), 1)
                self.assertTrue("Sean Personal Assistant" in "".join(p.title_text))
                self.assertIn("styles.css", content)
                self.assertNotIn("<script", content.lower())
                self.assertNotIn("http-equiv=\"refresh\"", content.lower())
                for link in p.links:
                    if not link or link.startswith(("mailto:", "https://", "#")):
                        continue
                    local = link.split("#")[0].split("?")[0]
                    path = ROOT / ("index.html" if local in ("./", "/") else local)
                    self.assertTrue(path.is_file(), f"broken {name} -> {link}")

    def test_google_data_disclosure_and_contact(self):
        p=(ROOT/"privacy.html").read_text(encoding="utf-8")
        for expected in ["Gmail", "Calendar", "AI service provider", "revoking", "not sold", "Limited Use", "Retention", "e93116@gmail.com", "繁體中文"]:
            self.assertIn(expected.lower(), p.lower())
        self.assertIn("Privacy Policy", (ROOT/"index.html").read_text())

    def test_no_credentials_or_unexpected_external_assets(self):
        for file in ROOT.iterdir():
            if file.suffix not in (".html", ".css", ".md"):
                continue
            text=file.read_text(encoding="utf-8")
            self.assertNotRegex(text, r"ghp_[A-Za-z0-9]{25,}|AIza[A-Za-z0-9_-]{30}|-----BEGIN PRIVATE KEY-----")
        self.assertFalse((ROOT/".env").exists())

if __name__=="__main__":
    unittest.main(verbosity=2)
