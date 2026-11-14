# ==============================================================================
# SCRIPT DE MIGRAÇÃO AUTOMATIZADA DE DOCUMENTAÇÃO ALM & GOVERNANÇA DE IA (PowerShell v2)
# Repositório Alvo: Engenharia-de-Software
# Branch: feature/docs-alm-framework -> main
# ==============================================================================

$ErrorActionPreference = "Stop"

Write-Host "======================================================================" -ForegroundColor Blue
Write-Host "    Iniciando a Migração da Documentação ALM e Governança (v2)        " -ForegroundColor Blue
Write-Host "======================================================================" -ForegroundColor Blue

if (-not (Test-Path ".git")) {
    Write-Host "[ERRO] Este diretório não é um repositório Git válido." -ForegroundColor Red
    Write-Host "Execute este script na raiz do repositório 'Engenharia-de-Software'."
    exit 1
}

$ZipPath = ""
$CandidateNames = @("alm-docs-framework-v2.zip", "alm-docs-framework.zip")

foreach ($Name in $CandidateNames) {
    if (Test-Path $Name) {
        $ZipPath = Resolve-Path $Name
        break
    }
    $UserDownloads = Join-Path $HOME "Downloads\$Name"
    if (Test-Path $UserDownloads) {
        $ZipPath = $UserDownloads
        break
    }
}

if (-not $ZipPath) {
    Write-Host "[ATENÇÃO] Pacote 'alm-docs-framework-v2.zip' não encontrado automaticamente." -ForegroundColor Yellow
    $ZipPath = Read-Host "Informe o caminho completo do arquivo zip"
    if (-not (Test-Path $ZipPath)) {
        Write-Host "[ERRO] Arquivo não encontrado em: $ZipPath" -ForegroundColor Red
        exit 1
    }
}

Write-Host "[OK] Pacote de documentação localizado: $ZipPath" -ForegroundColor Green

Write-Host "`n[1/5] Atualizando a branch main local..." -ForegroundColor Blue
git checkout main
git pull origin main

Write-Host "`n[2/5] Criando/Alternando para 'feature/docs-alm-framework'..." -ForegroundColor Blue
$BranchExists = git branch --list feature/docs-alm-framework
if ($BranchExists) {
    git checkout feature/docs-alm-framework
} else {
    git checkout -b feature/docs-alm-framework
}

Write-Host "`n[3/5] Extraindo a estrutura completa de documentação..." -ForegroundColor Blue
Expand-Archive -Path $ZipPath -DestinationPath "." -Force
Write-Host "[OK] Estrutura extraída com sucesso." -ForegroundColor Green

Write-Host "`n[4/5] Atualizando o README.md principal..." -ForegroundColor Blue
if (Test-Path "README.md") {
    $ReadmeContent = Get-Content "README.md" -Raw
    if ($ReadmeContent -notmatch "docs/alm/index.md") {
        $Block = @"

---

## 📚 Governança, Framework ALM e Diretrizes de IA

A governança do Ciclo de Vida de Aplicações e os padrões de IA do projeto são guiados pela nossa documentação:

- 🚀 **[Guia e Playbook Operacional de ALM](docs/alm/index.md)**
  - 📖 [Fundamentação Conceitual](docs/alm/fundamentacao/conceito-e-fases-macro.md)
  - 📋 [Matriz RACI Global](docs/alm/governanca/matriz-raci.md) & [Matriz de Criticidade](docs/alm/governanca/matriz-criticidade.md)
  - 🔄 [Workflow das 8 Fases Operacionais (Gates DoR / DoD)](docs/alm/fases/fase-1-viabilidade.md)
  - 📄 [Templates Padrão (ADR, SRS ISO 29148, PR Template)](docs/templates/adr-template-specification.md)
  - 🤖 [Steering & Governança para IA](docs/steering-ia/ai-steering-ruleset-template.md)
"@
        Add-Content -Path "README.md" -Value $Block
        Write-Host "[OK] README.md atualizado." -ForegroundColor Green
    }
}

Write-Host "`n[5/5] Adicionando novos arquivos ao staging do Git..." -ForegroundColor Blue
git add docs/ scripts/ README.md

Write-Host "`n======================================================================" -ForegroundColor Green
Write-Host "    MIGRAÇÃO CONCLUÍDA COM SUCESSO!                                   " -ForegroundColor Green
Write-Host "======================================================================" -ForegroundColor Green
git status --short
