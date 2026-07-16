import sys
import unittest
from copy import deepcopy
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
import validate_release as mod


def candidate_manifest():
    return {
        "version": "1.0.0",
        "intended_tag": "v1.0.0",
        "status": "candidate",
        "hosted_ci": {"status": "not_run", "run_url": None, "commit_sha": None},
        "tag_target": None,
        "tagged_validation": None,
        "release_url": None,
        "legacy_release": {
            "tag": "v0.2.0",
            "target": "3d2cdea9f651f7641ec1f805519a777f013dd6ec",
            "immutable": True,
        },
    }


class ReleaseLifecycleTests(unittest.TestCase):
    def test_candidate_passes(self):
        self.assertEqual(mod.validate_manifest(candidate_manifest()), [])

    def test_legacy_pass_state_rejected(self):
        manifest = candidate_manifest()
        manifest["status"] = "pass"
        self.assertIn("release status invalid", mod.validate_manifest(manifest))

    def test_candidate_publication_evidence_rejected(self):
        manifest = candidate_manifest()
        manifest["tag_target"] = "1" * 40
        self.assertIn("candidate contains publication evidence", mod.validate_manifest(manifest))

    def test_hosted_success_requires_url_and_commit(self):
        manifest = candidate_manifest()
        manifest["hosted_ci"] = {"status": "passed", "run_url": None, "commit_sha": None}
        self.assertIn("hosted CI pass lacks run URL or exact commit", mod.validate_manifest(manifest))

    def test_tagged_validation_must_bind_to_target(self):
        manifest = candidate_manifest()
        manifest["status"] = "tagged-validated"
        manifest["tag_target"] = "1" * 40
        manifest["tagged_validation"] = {"status": "pass", "checkout_sha": "2" * 40}
        self.assertIn("tagged validation is not bound to tag target", mod.validate_manifest(manifest))

    def test_published_requires_canonical_release_url(self):
        manifest = candidate_manifest()
        manifest["status"] = "published"
        manifest["tag_target"] = "1" * 40
        manifest["tagged_validation"] = {"status": "pass", "checkout_sha": "1" * 40}
        manifest["release_url"] = "https://example.test/release"
        self.assertIn("published state lacks canonical release URL", mod.validate_manifest(manifest))

    def test_legacy_boundary_is_immutable(self):
        manifest = deepcopy(candidate_manifest())
        manifest["legacy_release"]["immutable"] = False
        self.assertIn("legacy release must remain immutable", mod.validate_manifest(manifest))


if __name__ == "__main__":
    unittest.main()
