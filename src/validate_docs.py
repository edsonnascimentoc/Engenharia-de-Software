"""Validate local Markdown links and basic RTM structure."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RTM_PATH = Path("docs/alm/artefatos/matriz-rastreabilidade.md")
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
REFERENCE_RE = re.compile(r"^\s*\[[^\]]+\]:\s*(\S+)", re.MULTILINE)


def markdown_files(root: Path = ROOT) -> list[Path]:
    return [
        path
        for path in root.rglob("*.md")
        if ".git" not in path.parts and ".vs" not in path.parts
    ]


def validate_links(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for source in markdown_files(root):
        # Existing legacy Markdown files may contain Windows-1252 punctuation.
        content = source.read_text(encoding="utf-8", errors="replace")
        targets = [match.group(1) for match in LINK_RE.finditer(content)]
        targets.extend(REFERENCE_RE.findall(content))
        for target in targets:
            target = target.strip().strip("<>").split(" ", 1)[0]
            if target == "link-para-alm":
                # Deliberate placeholder in a reusable PR template.
                continue
            if not target or target.startswith(
                ("https://", "http://", "mailto:", "//", "#")
            ):
                continue
            local_target = target.split("#", 1)[0]
            if not local_target:
                continue
            resolved = (source.parent / local_target).resolve()
            if not resolved.exists():
                errors.append(
                    f"{source.relative_to(root)}: link local inexistente: {target}"
                )
    return errors


def validate_rtm(root: Path = ROOT) -> list[str]:
    path = root / RTM_PATH
    if not path.is_file():
        return [f"RTM ausente: {RTM_PATH}"]
    content = path.read_text(encoding="utf-8", errors="replace")
    errors: list[str] = []
    if not re.search(r"^\| Classe \| ID \|", content, re.MULTILINE):
        errors.append(f"{RTM_PATH}: tabela de regras sem colunas Classe e ID")
    if not re.search(r"\|\s*Regra do framework\s*\|\s*(?:RF|RNF|REST|RN)-", content):
        errors.append(f"{RTM_PATH}: nenhum identificador de requisito/regra encontrado")
    return errors


def main() -> int:
    errors = validate_links() + validate_rtm()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Links Markdown locais e estrutura da RTM válidos.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
