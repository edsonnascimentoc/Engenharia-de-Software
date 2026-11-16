#!/usr/bin/env bash
# ==============================================================================
# Script de Inicialização de Governança de Segurança em Repositórios
# Automação de Segurança em Profundidade (SCA, SBOM, CVEs e Quality Gates)
# ==============================================================================

set -euo pipefail

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}======================================================================${NC}"
echo -e "${BLUE}    INICIALIZANDO ESTRUTURA DE GOVERNANÇA DE SEGURANÇA (Shift-Left)   ${NC}"
echo -e "${BLUE}======================================================================${NC}"

# 1. Criação da Estrutura de Diretórios
echo -e "\n${YELLOW}[1/4] Criando estrutura de diretórios padrão...${NC}"
mkdir -p .github/workflows
mkdir -p docs/security
mkdir -p docs/adr

echo -e "${GREEN}✓ Diretórios (.github/workflows, docs/security, docs/adr) criados com sucesso.${NC}"

# 2. Instalação do Pipeline CI/CD e Template de Pull Request
echo -e "\n${YELLOW}[2/4] Instalando automação de CI/CD e Templates de PR...${NC}"

cat << 'EOF' > .github/workflows/security-governance-pipeline.yml
name: Security Governance Pipeline (SCA, SBOM & CVE Check)

on:
  push:
    branches: [ "main", "master", "develop" ]
  pull_request:
    branches: [ "main", "master", "develop" ]
  schedule:
    - cron: '0 4 * * 1'

permissions:
  contents: read
  security-events: write
  actions: read

jobs:
  sca-sbom-cve-scan:
    name: SCA, SBOM & Vulnerability Audit
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Generate Software Bill of Materials (SBOM)
        uses: anchore/sbom-action@v0
        with:
          format: spdx-json
          output-file: sbom.spdx.json

      - name: Scan Repository & SBOM for CVEs (Trivy)
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'fs'
          scan-ref: '.'
          format: 'sarif'
          output: 'trivy-results.sarif'
          severity: 'CRITICAL,HIGH,MEDIUM'
          exit-code: '1'
          ignore-unfixed: false

      - name: Upload SARIF report to GitHub Security Tab
        uses: github/codeql-action/upload-sarif@v3
        if: always()
        with:
          sarif_file: 'trivy-results.sarif'
EOF

cat << 'EOF' > .github/PULL_REQUEST_TEMPLATE.md
## 📌 Descrição da Mudança
- **O que foi feito:** 
- **Motivação / Contexto:** 

---

## 🛡️ Checklist de Qualidade e Segurança (Definition of Done - DoD)
- [ ] Executado auditoria de dependências local (`npm audit`, `pip-audit`, `dotnet list package`).
- [ ] Gerado e validado SBOM SPDX localmente (`syft dir:. -o spdx-json`).
- [ ] Escaneamento local via Trivy executado com **0 vulnerabilidades CRITICAL ou HIGH**.
- [ ] Ausência de segredos ou chaves privadas commitadas (`gitleaks`).
- [ ] Imagens Docker utilizando tags específicas e imagens base enxutas (`slim`/`alpine`).

---

## 📄 Governança de Exceções & Falsos Positivos
- Contém exceção/falso positivo liberado via `.trivyignore`?
  - [ ] **Não**
  - [ ] **Sim** (Obrigatório registrar link da ADR em `docs/adr/` com expiração <= 30 dias).
EOF

echo -e "${GREEN}✓ Arquivos (.github/workflows/security-governance-pipeline.yml e .github/PULL_REQUEST_TEMPLATE.md) instalados.${NC}"

# 3. Configuração do Arquivo de Ignorar Vulnerabilidades (.trivyignore)
echo -e "\n${YELLOW}[3/4] Configurando arquivo de exceções temporárias (.trivyignore)...${NC}"

if [ ! -f .trivyignore ]; then
  cat << 'EOF' > .trivyignore
# Arquivo de Exceções Temporárias de Vulnerabilidades (Trivy)
# REGRA: Toda entrada DEVE conter a justificativa técnica, o link da ADR correspondente e a data limite de expiração (máx 30 dias).
# Exemplo:
# CVE-2023-XXXXX # Justificativa: Falso positivo em lib interna. ADR: docs/adr/0002-excecao-cve.md. Expira em: 2026-12-15
EOF
  echo -e "${GREEN}✓ Arquivo .trivyignore criado com template de boas práticas.${NC}"
else
  echo -e "${YELLOW}! Arquivo .trivyignore já existente mantido sem alterações.${NC}"
fi

# 4. Finalização e Instruções para a Squad
echo -e "\n${BLUE}======================================================================${NC}"
echo -e "${GREEN}    BOOTSTRAP DE SEGURANÇA CONCLUÍDO COM SUCESSO!                     ${NC}"
echo -e "${BLUE}======================================================================${NC}"
echo -e "Próximos passos recomendados para os desenvolvedores:"
echo -e "  1. Adicionar os arquivos ao repositório: git add . && git commit -m 'chore: bootstrap security governance'"
echo -e "  2. Ativar as Branch Protection Rules no GitHub para exigir o status check 'SCA, SBOM & Vulnerability Audit'."
echo -e "  3. Consultar as normas em 'docs/security/' para regras de SLA e gestão de CVEs.\n"
