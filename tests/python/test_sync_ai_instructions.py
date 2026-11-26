import contextlib
import io
import tempfile
import unittest
from pathlib import Path

from scripts.sync_ai_instructions import sync_instructions


class InstructionSynchronizationTests(unittest.TestCase):
    def test_sync_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "canonical.md"
            mirror = root / ".cursorrules"
            source.write_bytes(b"# Canonical instructions\n")
            mirror.write_bytes(b"outdated")

            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(sync_instructions(source, mirror, check=False), 0)
                first_sync = mirror.read_bytes()
                self.assertEqual(sync_instructions(source, mirror, check=False), 0)

            self.assertEqual(first_sync, source.read_bytes())
            self.assertEqual(mirror.read_bytes(), source.read_bytes())

    def test_check_accepts_synchronized_mirror(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "canonical.md"
            mirror = root / ".cursorrules"
            source.write_bytes(b"# Canonical instructions\n")
            mirror.write_bytes(source.read_bytes())

            with contextlib.redirect_stdout(io.StringIO()):
                result = sync_instructions(source, mirror, check=True)

            self.assertEqual(result, 0)

    def test_check_rejects_divergence_without_writing(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "canonical.md"
            mirror = root / ".cursorrules"
            source.write_bytes(b"# Canonical instructions\n")
            mirror.write_bytes(b"# Divergent instructions\n")
            original_mirror = mirror.read_bytes()

            error = io.StringIO()
            with contextlib.redirect_stderr(error):
                result = sync_instructions(source, mirror, check=True)

            self.assertEqual(result, 1)
            self.assertIn("out of date", error.getvalue())
            self.assertEqual(mirror.read_bytes(), original_mirror)


if __name__ == "__main__":
    unittest.main()
