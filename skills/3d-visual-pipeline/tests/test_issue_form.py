import unittest
from pathlib import Path


class IssueFormContractTests(unittest.TestCase):
    def test_required_execution_fields(self):
        root = Path(__file__).resolve().parents[3]
        text = (root / ".github/ISSUE_TEMPLATE/01-execution.yml").read_text(encoding="utf-8")
        required_ids = {
            "action",
            "source_url",
            "references",
            "target_url",
            "exact_base",
            "branch",
            "output",
            "write_scope",
            "protected",
            "dependencies",
            "risks",
            "acceptance",
            "checks",
            "evidence",
            "done_when",
            "safety",
        }
        for field_id in required_ids:
            self.assertIn(f"id: {field_id}", text)
        for constant in (
            "PROJECT_ID: 3D_VISUAL_PIPELINE",
            "SHORT_ID: 3DP",
            "TASK_PROFILE: execution",
            "TASK_ID: auto",
            "handoff_mode: delta-only",
        ):
            self.assertIn(constant, text)
        self.assertFalse((root / ".github/ISSUE_TEMPLATE/implementation.md").exists())


if __name__ == "__main__":
    unittest.main()
