# Automação de Governança Multiagente (MCP + ISO 29148 + EARS)

Este pacote contém os artefatos de automação para integrar a arquitetura multiagente ao ciclo de vida de desenvolvimento do repositório.

## Estrutura de Arquivos

- `.github/agents/runner.js`: Script Node.js validador de Issues.
- `.github/agents/mcp.json`: Configuração dos servidores MCP para GitHub e Discord.
- `.github/agents/prompts/issue-reviewer-prompt.txt`: Prompt do agente auditor (ISO 29148 / EARS).
- `.github/agents/prompts/issue-drafter-prompt.txt`: Prompt do agente gerador de rascunhos.
- `.github/workflows/mcp-agent-validation.yml`: Pipeline de CI/CD do GitHub Actions.

## Como Instalar no Repositório

1. Extraia o conteúdo deste arquivo na raiz do seu repositório Git.
2. Certifique-se de ter os secrets `GITHUB_TOKEN` e `DISCORD_BOT_TOKEN` configurados nas definições do repositório no GitHub.
3. Ao abrir ou editar qualquer Issue, o workflow `.github/workflows/mcp-agent-validation.yml` será disparado automaticamente para validar a especificação.

## Desenvolvimento local

O gate Python da CI usa Ruff `0.17.6`, fixado em `requirements-dev.txt`. Configure um ambiente virtual na raiz do repositório para instalar a mesma versão usada pela CI.

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
```

Execute os checks Ruff usados pela CI:

```bash
python -m ruff --version
python -m ruff check alm_rtm_auditor.py scripts/validate_docs.py tests/python
python -m ruff format --check scripts/validate_docs.py tests/python
```

Para aplicar a formatação localmente, remova `--check` do comando `ruff format`. A pasta `.venv` é ignorada pelo Git.
