"""Compatibility entry point for the documentation validator."""

import importlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

_validator = importlib.import_module("src.validate_docs")
main = _validator.main
markdown_files = _validator.markdown_files
validate_links = _validator.validate_links
validate_rtm = _validator.validate_rtm


if __name__ == "__main__":
    raise SystemExit(main())