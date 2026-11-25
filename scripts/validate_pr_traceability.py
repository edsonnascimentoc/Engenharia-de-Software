"""Require issue and requirement references for behavioral pull requests."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ISSUE_RE = re.compile(r"(?:#\d+|/issues/\d+)", re.IGNORECASE)
REQUIREMENT_RE = re.compile(r"\b(?:REQ|RF|RNF|REST|RN)-[A-Z0-9][A-Z0-9-]*\b", re.IGNORECASE)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--title", required=True)
    parser.add_argument("--changed-files", nargs="*", default=[])
    parser.add_argument("--changed-files-file")
    parser.add_argument("--body", default="")
    args = parser.parse_args()

    # Docs, dependency updates and CI-only changes do not represent behavior.
    changed_files = args.changed_files
    if args.changed_files_file:
        changed_files += Path(args.changed_files_file).read_text(encoding="utf-8").splitlines()
    behavioral = any(path.startswith(("src/", "tests/")) for path in changed_files) and bool(
        re.match(r"^(feat|fix)(?:\([^)]*\))?!?:", args.title, re.IGNORECASE)
    )
    if not behavioral:
        print("Rastreabilidade dispensada: PR sem mudanças comportamentais em src/ ou tests/.")
        return 0

    content = f"{args.title}\n{args.body}"
    errors = []
    if not ISSUE_RE.search(content):
        errors.append("adicione vínculo à issue (por exemplo, `Closes #123`) no título ou corpo do PR")
    if not REQUIREMENT_RE.search(content):
        errors.append("adicione o ID do requisito aplicável (`REQ-...`, `RF-...` etc.) no título ou corpo do PR")
    if errors:
        print("Falha na validação de rastreabilidade do PR:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        print("Se a alteração não implementar comportamento requerido, mova-a para escopo de documentação/manutenção ou registre a justificativa e ajuste o escopo do PR.", file=sys.stderr)
        return 1

    print("Vínculos de issue e requisito encontrados.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
