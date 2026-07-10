from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.start_tags = []
        self.refs = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        self.start_tags.append((tag, attributes))
        for key in ("href", "src", "action"):
            value = attributes.get(key)
            if value:
                self.refs.append((key, value))


class SiteContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = (ROOT / "index.html").read_text(encoding="utf-8")
        cls.styles = (ROOT / "styles.css").read_text(encoding="utf-8")
        cls.parser = SiteParser()
        cls.parser.feed(cls.index)

    def test_insecure_static_portal_is_not_shipped(self):
        self.assertFalse((ROOT / "login.html").exists())
        self.assertFalse((ROOT / "dashboard.html").exists())
        self.assertNotIn("Account Access", self.index)
        self.assertNotRegex(self.index, r"(?:auth|dashboard)\.js")

    def test_page_has_primary_heading_and_accessible_navigation_toggle(self):
        self.assertRegex(self.index, r'<h1\b[^>]*class="hero-title"')
        toggles = [attrs for tag, attrs in self.parser.start_tags if tag == "button" and "hamburger" in attrs.get("class", "").split()]
        self.assertEqual(len(toggles), 1)
        self.assertEqual(toggles[0].get("aria-controls"), "primary-navigation")
        self.assertEqual(toggles[0].get("aria-expanded"), "false")
        self.assertTrue(toggles[0].get("aria-label"))

    def test_contact_is_email_only_and_no_form_is_shipped(self):
        forms = [attrs for tag, attrs in self.parser.start_tags if tag == "form"]
        self.assertEqual(forms, [])
        self.assertFalse((ROOT / "thanks.html").exists())
        self.assertNotIn("thanks.html", self.index)
        self.assertIn('href="mailto:admin@henryandtosh.com"', self.index)

    def test_required_trust_content_is_present(self):
        for text in (
            "Kenneth George Muir",
            "Sandra Lee Ann Muir",
            "Sherwood, Lower Seagry, Chippenham, SN15 5EP",
            "admin@henryandtosh.com",
            "Audit exemption",
            "No client assets managed",
        ):
            self.assertIn(text, self.index)

    def test_accessibility_styles_cover_focus_and_reduced_motion(self):
        self.assertIn(":focus-visible", self.styles)
        self.assertIn("prefers-reduced-motion", self.styles)
        self.assertIn("scroll-margin-top", self.styles)

    def test_feature_grid_suppresses_native_list_markers(self):
        feature_grid_rule = re.search(r"\.hero-features\s*\{(?P<body>[^}]*)\}", self.styles, re.S)
        if feature_grid_rule is None:
            self.fail("Missing .hero-features CSS rule")
        self.assertIn("list-style: none", feature_grid_rule.group("body"))

    def test_all_local_references_exist(self):
        for _, value in self.parser.refs:
            if value.startswith(("http://", "https://", "#", "mailto:", "tel:")):
                continue
            path = value.split("?", 1)[0].split("#", 1)[0].lstrip("/")
            if not path:
                continue
            self.assertTrue((ROOT / path).exists(), f"Missing local reference: {value}")

    def test_no_stale_copyright_year(self):
        for html_file in ROOT.glob("*.html"):
            self.assertNotIn("© 2024", html_file.read_text(encoding="utf-8"))

    def test_netlify_redirects_retired_portal_and_sets_security_headers(self):
        config_path = ROOT / "netlify.toml"
        self.assertTrue(config_path.exists())
        config = config_path.read_text(encoding="utf-8")
        self.assertIn('from = "/login.html"', config)
        self.assertIn('from = "/dashboard.html"', config)
        for header in (
            "Content-Security-Policy",
            "Referrer-Policy",
            "X-Content-Type-Options",
            "X-Frame-Options",
            "Permissions-Policy",
        ):
            self.assertIn(header, config)


if __name__ == "__main__":
    unittest.main()
