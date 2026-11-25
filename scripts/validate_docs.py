"""Compatibility entry point for the documentation validator."""

from src.validate_docs import main, validate_links, validate_rtm


if __name__ == "__main__":
    raise SystemExit(main())
