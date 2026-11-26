import tempfile
import unittest
from pathlib import Path

from scripts.validate_docs import markdown_files, validate_links, validate_rtm
from src.validate_docs import markdown_files as src_markdown_files


class DocumentationValidationTests(unittest.TestCase):
    def test_legacy_wrapper_reexports_canonical_markdown_files(self):
        self.assertIs(markdown_files, src_markdown_files)

    def test_detects_broken_relative_markdown_link(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "docs").mkdir()
            (root / "docs" / "page.md").write_text(
                "[missing](absent.md)", encoding="utf-8"
            )
            errors = validate_links(root)
        self.assertEqual(len(errors), 1)
        self.assertIn("absent.md", errors[0])

    def test_accepts_existing_relative_link(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "docs").mkdir()
            (root / "docs" / "target.md").write_text("# Target", encoding="utf-8")
            (root / "docs" / "page.md").write_text(
                "[target](target.md)", encoding="utf-8"
            )
            self.assertEqual(validate_links(root), [])

    def test_reports_missing_rtm(self):
        with tempfile.TemporaryDirectory() as directory:
            self.assertTrue(validate_rtm(Path(directory)))


if __name__ == "__main__":
    unittest.main()
