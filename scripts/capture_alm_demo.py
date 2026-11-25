"""Capture a sanitized auditor run against a synthetic repository fixture."""

from __future__ import annotations

import html
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs/media/alm-governance-demo.svg"


def create_fixture(root: Path) -> None:
    files = [
        "docs/alm/governanca/matriz-raci.md",
        "docs/alm/fases/fase-1-viabilidade.md",
        ".github/ISSUE_TEMPLATE/requisito-iso29148.md",
        "docs/architecture/adr/README.md",
        "docs/alm/artefatos/padrao-commits.md",
        "tests/README.md",
        ".github/workflows/alm-ci-quality-gate.yml",
    ]
    for relative_path in files:
        target = root / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("Fixture sintética para demonstração.\n", encoding="utf-8")


def capture() -> list[str]:
    with tempfile.TemporaryDirectory(prefix="alm-demo-") as temp_dir:
        fixture = Path(temp_dir)
        create_fixture(fixture)
        result = subprocess.run(
            [sys.executable, str(ROOT / "alm_rtm_auditor.py")],
            cwd=fixture,
            capture_output=True,
            check=True,
            env={**os.environ, "PYTHONUTF8": "1"},
            text=True,
            encoding="utf-8",
        )

    report_path = Path(tempfile.gettempdir()) / "alm_rtm_report.md"
    report_lines = report_path.read_text(encoding="utf-8").splitlines()
    sample_lines = [line for line in report_lines if line.startswith("| **")][:4]
    wrapped_sample_lines = [
        line[index : index + 128]
        for line in sample_lines
        for index in range(0, len(line), 128)
    ]
    output = result.stdout.strip().replace(str(report_path), "$TEMP/alm_rtm_report.md")
    return [
        "$ python alm_rtm_auditor.py (fixture sintética)",
        output,
        "",
        "Amostra do relatório gerado:",
        *wrapped_sample_lines,
    ]


def write_svg(lines: list[str]) -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    text = "\n".join(
        f'<text x="32" y="{88 + index * 25}" class="line">{html.escape(line)}</text>'
        for index, line in enumerate(lines)
    )
    height = 112 + len(lines) * 25
    OUTPUT.write_text(
        "\n".join(
            [
                '<svg xmlns="http://www.w3.org/2000/svg" '
                f'viewBox="0 0 1440 {height}" role="img" '
                'aria-labelledby="title description">',
                '<title id="title">Execução do auditor ALM</title>',
                '<desc id="description">'
                "Saída real do auditor em fixture sintética.</desc>",
                f'<rect width="1440" height="{height}" rx="16" fill="#111827"/>',
                '<rect width="1440" height="48" rx="16" fill="#1f2937"/>',
                '<circle cx="28" cy="24" r="7" fill="#f87171"/>',
                '<circle cx="52" cy="24" r="7" fill="#fbbf24"/>',
                '<circle cx="76" cy="24" r="7" fill="#34d399"/>',
                '<text x="105" y="30" class="title">'
                "Demonstração sintética · ALM Auditor</text>",
                "<style>.title{font:600 16px Segoe UI,Arial,sans-serif;fill:#e5e7eb}"
                ".line{font:15px Consolas,Menlo,monospace;fill:#d1d5db}</style>",
                text,
                "</svg>",
            ]
        ),
        encoding="utf-8",
    )


if __name__ == "__main__":
    write_svg(capture())
    print(f"Captura sintética atualizada: {OUTPUT.relative_to(ROOT)}")
