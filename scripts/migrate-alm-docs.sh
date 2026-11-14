#!/usr/bin/env bash
# ==============================================================================
# SCRIPT DE MIGRAÇÃO AUTOMATIZADA DE DOCUMENTAÇÃO ALM & GOVERNANÇA DE IA (v2)
# Repositório Alvo: Engenharia-de-Software
# Branch: feature/docs-alm-framework -> main
# ==============================================================================

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}======================================================================${NC}"
echo -e "${BLUE}    Iniciando a Migração da Documentação ALM e Governança (v2)        ${NC}"
echo -e "${BLUE}======================================================================${NC}"

if ! git rev-parse --is-inside-work-tree > /dev/null 2>&1; then
    echo -e "${RED}[ERRO] Este diretório não é um repositório Git válido.${NC}"
    echo "Execute este script na raiz do repositório 'Engenharia-de-Software'."
    exit 1
fi

ZIP_PATH=""
for zip_name in "alm-docs-framework-v2.zip" "alm-docs-framework.zip"; do
    if [ -f "$zip_name" ]; then
        ZIP_PATH="$zip_name"
        break
    elif [ -f "$HOME/Downloads/$zip_name" ]; then
        ZIP_PATH="$HOME/Downloads/$zip_name"
        break
    fi
done

if [ -z "$ZIP_PATH" ]; then
    echo -e "${YELLOW}[ATENÇÃO] Pacote de documentação não encontrado automaticamente.${NC}"
    read -p "Informe o caminho completo do arquivo zip (alm-docs-framework-v2.zip): " USER_ZIP_PATH
    if [ -f "$USER_ZIP_PATH" ]; then
        ZIP_PATH="$USER_ZIP_PATH"
    else
        echo -e "${RED}[ERRO] Arquivo não encontrado em: $USER_ZIP_PATH${NC}"
        exit 1
    fi
fi

echo -e "${GREEN}[OK] Pacote de documentação localizado:${NC} $ZIP_PATH"

echo -e "\n${BLUE}[1/5] Atualizando a branch main local...${NC}"
git checkout main
git pull origin main

echo -e "\n${BLUE}[2/5] Criando/Alternando para 'feature/docs-alm-framework'...${NC}"
if git show-ref --verify --quiet refs/heads/feature/docs-alm-framework; then
    git checkout feature/docs-alm-framework
else
    git checkout -b feature/docs-alm-framework
fi

echo -e "\n${BLUE}[3/5] Extraindo a estrutura completa de documentação para o repositório...${NC}"
mkdir -p docs
unzip -o "$ZIP_PATH" -d . > /dev/null
echo -e "${GREEN}[OK] Estrutura completa extraída com sucesso em 'docs/' e 'scripts/'.${NC}"

echo -e "\n${BLUE}[4/5] Atualizando o README.md principal...${NC}"
if [ -f "README.md" ]; then
    if ! grep -q "docs/alm/index.md" README.md; then
        cat << 'EOF' >> README.md

---

## 📚 Governança, Framework ALM e Diretrizes de IA

A governança do Ciclo de Vida de Aplicações e os padrões de IA do projeto são guiados pela nossa documentação:

- 🚀 **[Guia e Playbook Operacional de ALM](docs/alm/index.md)**
  - 📖 [Fundamentação Conceitual](docs/alm/fundamentacao/conceito-e-fases-macro.md)
  - 📋 [Matriz RACI Global](docs/alm/governanca/matriz-raci.md) & [Matriz de Criticidade](docs/alm/governanca/matriz-criticidade.md)
  - 🔄 [Workflow das 8 Fases Operacionais (Gates DoR / DoD)](docs/alm/fases/fase-1-viabilidade.md)
  - 📄 [Templates Padrão (ADR, SRS ISO 29148, PR Template)](docs/templates/adr-template-specification.md)
  - 🤖 [Steering & Governança para IA](docs/steering-ia/ai-steering-ruleset-template.md)
EOF
        echo -e "${GREEN}[OK] README.md atualizado.${NC}"
    fi
fi

echo -e "\n${BLUE}[5/5] Adicionando novos arquivos ao staging do Git...${NC}"
git add docs/ scripts/ README.md

echo -e "\n${GREEN}======================================================================${NC}"
echo -e "${GREEN}    MIGRAÇÃO CONCLUÍDA COM SUCESSO!                                   ${NC}"
echo -e "${GREEN}======================================================================${NC}"
git status --short
