import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
import validate_debrand as mod


class DebrandTests(unittest.TestCase):
    def test_generic_text_passes(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "README.md").write_text("generic three-dimensional pipeline")
            self.assertEqual(mod.scan(root), [])

    def test_legacy_text_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            token = "".join(["fin", "us", "lugi"])
            (root / "README.md").write_text(token)
            self.assertTrue(mod.scan(root))

    def test_legacy_filename_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            token = "".join(["f", "3", "d"])
            (root / (token + ".md")).write_text("x")
            self.assertTrue(mod.scan(root))

    def test_legacy_url_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            token = "".join(["fin", "us", "lugi"])
            (root / "a.md").write_text("https://example.test/" + token)
            self.assertTrue(mod.scan(root))

    def test_legacy_color_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            color = "#" + "".join(["ff", "05", "08"])
            (root / "a.md").write_text(color)
            self.assertTrue(mod.scan(root))

    def test_active_previous_short_id_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            token = "".join(["d", "v", "p"])
            (root / "README.md").write_text("active context " + token)
            self.assertTrue(mod.scan(root))

    def test_marked_historical_short_id_allowed(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            token = "".join(["d", "v", "p"])
            (root / "CHANGELOG.md").write_text("Legacy historical identifier " + token)
            self.assertEqual(mod.scan(root), [])

    def test_marked_historical_sha_allowed_in_incident_record(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            incident = root / "docs/debt/3dp-027-governance-incident.md"
            incident.parent.mkdir(parents=True)
            token = "".join(["f", "3", "d"])
            incident.write_text("historical merge abc" + token + "123")
            self.assertEqual(mod.scan(root), [])

    def test_unmarked_historical_sha_rejected_in_incident_record(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            incident = root / "docs/debt/3dp-027-governance-incident.md"
            incident.parent.mkdir(parents=True)
            token = "".join(["f", "3", "d"])
            incident.write_text("merge abc" + token + "123")
            self.assertTrue(mod.scan(root))

    def test_non_allowlisted_historical_short_id_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            token = "".join(["d", "v", "p"])
            (root / "README.md").write_text("Legacy historical identifier " + token)
            self.assertTrue(mod.scan(root))


if __name__ == "__main__":
    unittest.main()
