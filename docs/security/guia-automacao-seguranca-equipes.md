# Guia de Implementação: Automação da Governança de Segurança, SBOM e CVEs

Este guia fornece o passo a passo operacional para que as equipes de desenvolvimento integrem e automatizem o **Padrão de Governança de Segurança em Profundidade** em seus repositórios no GitHub e Azure DevOps.

---

## 1. Estrutura de Arquivos no Repositório

Para ativar a governança automatizada, cada repositório de produto ou microsserviço deve possuir os seguintes artefatos configurados:

```text
.
├── .github/
│   └── workflows/
│       └── security-governance-pipeline.yml   # Esteira automatizada de SCA, SBOM e CVEs
├── docs/
│   └── adr/                                  # Architectural Decision Records (Falsos Positivos / Exceções)
│       └── ADR-000-template.md
├── .trivyignore                               # Registro de exceções auditadas com prazo limite
└── README.md
```

---

## 2. Passo a Passo de Implantação

### Passo 1: Adicionar o Workflow de Segurança
Copie o arquivo `security-governance-pipeline.yml` para o diretório `.github/workflows/` da branch principal do seu repositório.

### Passo 2: Configurar Proteção de Branch (Branch Protection Rules)
No repositório do GitHub (`Settings > Branches > Branch Protection Rules`), adicione uma regra para a branch `main` ou `master`:
1. Marque **"Require a pull request before merging"**.
2. Marque **"Require status checks to pass before merging"**.
3. Pesquise e adicione as seguintes verificações obrigatórias:
   - `SCA, SBOM SPDX & Vulnerability Audit`
   - `Container Image & Embedded SBOM Security` (quando houver Dockerfile).

### Passo 3: Ativar o Upload de SARIF e Code Scanning
Garantir que as permissões do repositório (`Settings > Actions > General > Workflow permissions`) estejam configuradas para **Read and Write permissions** para eventos de segurança (`security-events: write`).

---

## 3. Guia Shift-Left para Desenvolvedores (Execução Local)

Antes de abrir um Pull Request, os desenvolvedores devem executar as seguintes verificações localmente:

### A. Auditoria de Dependências por Stack
- **Node.js**: `npm audit --audit-level=high`
- **Python**: `pip-audit`
- **.NET**: `dotnet list package --vulnerable --severity high`
- **Java (Maven/Gradle)**: `./mvnw dependency-check:check` ou `./gradlew dependencyCheckAnalyze`

### B. Geração Local de SBOM com Syft
```bash
# Geração de SBOM em formato SPDX JSON usando a CLI do Syft
syft dir:. -o spdx-json=./sbom.spdx.json
```

### C. Varredura Local de CVEs com Trivy
```bash
# Escanear o SBOM gerado usando a CLI do Trivy
trivy sbom ./sbom.spdx.json --severity CRITICAL,HIGH
```

---

## 4. Governança de Exceções e Falsos Positivos

Se uma vulnerabilidade Alta ou Crítica for identificada como **Falso Positivo** ou **Não Exequível (Unreachable)** no contexto da aplicação:

1. **Abertura de ADR (Architecture Decision Record)**:
   - Crie uma ADR no repositório em `docs/adr/ADR-XXXX-excecao-cve.md` justificando a análise de risco técnica e o plano de mitigação compensatória.
2. **Atualização do `.trivyignore`**:
   - Adicione a CVE no arquivo `.trivyignore` indicando a data de expiração (máximo 30 dias) e o link da ADR:
   ```text
   # ADR-0012: CVE-2024-XXXXX declarada como inofensiva no escopo de runtime
   # Expira em: 2026-12-15
   CVE-2024-XXXXX
   ```
3. **Aprovação**:
   - O Pull Request com a inclusão no `.trivyignore` exige aprovação obrigatória do **Arquiteto de Software** ou **Security Champion** da equipe.

---

## 5. Matriz de SLA e Operação

| Severidade CVSS | Ação na Pipeline | SLA de Remediação | Responsável |
| :--- | :--- | :--- | :--- |
| **CRITICAL (9.0 - 10.0)** | Bloqueia Merge | **24 horas** | Squad Dev + SecOps |
| **HIGH (7.0 - 8.9)** | Bloqueia Merge | **72 horas** | Squad Dev |
| **MEDIUM (4.0 - 6.9)** | Alerta SARIF (Warning) | **15 dias úteis** | Tech Lead (Backlog) |
| **LOW (0.1 - 3.9)** | Registro de Log | **30 dias úteis** | Backlog Técnico |
