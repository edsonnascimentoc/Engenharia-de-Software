# Pipeline GitHub Actions: Validação Automática de ADR em Pull Requests

Este workflow de CI/CD automatiza a governança de arquitetura no **GitHub Actions**. Ele verifica se qualquer Pull Request que altere arquivos críticos de arquitetura (schemas de banco de dados, contratos de API, infraestrutura como código ou módulos core de domínio) inclui obrigatoriamente a criação ou atualização de um **ADR (Architectural Decision Record)**.

---

## 1. Arquivo de Workflow (`.github/workflows/adr-validator.yml`)

```yaml
name: ADR Architectural Governance Check

on:
  pull_request:
    types: [opened, synchronize, reopened, labeled, unlabeled]
    paths:
      - 'src/domain/**'
      - 'src/infrastructure/**'
      - 'db/migrations/**'
      - 'api/openapi.yaml'
      - 'terraform/**'
      - 'docker-compose.yml'

jobs:
  validate-adr:
    name: Validar Presença de ADR em Mudanças Arquiteturais
    runs-on: ubuntu-latest
    steps:
      - name: Checkout do Código
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Obter Lista de Arquivos Alterados no PR
        id: changed-files
        uses: tj-actions/changed-files@v44
        with:
          files_yaml: |
            architecture_paths:
              - 'src/domain/**'
              - 'src/infrastructure/**'
              - 'db/migrations/**'
              - 'api/openapi.yaml'
              - 'terraform/**'
            adr_paths:
              - 'docs/adrs/*.md'
              - 'docs/architecture/decisions/*.md'

      - name: Verificar Conformidade de ADR
        run: |
          HAS_ARCH_CHANGES="${{ steps.changed-files.outputs.architecture_paths_any_changed }}"
          HAS_ADR_CHANGES="${{ steps.changed-files.outputs.adr_paths_any_changed }}"
          PR_BODY="${{ github.event.pull_request.body }}"

          echo "=================================================="
          echo "Relatório de Análise de Impacto Arquitetural"
          echo "=================================================="
          echo "Alterações em componentes de arquitetura: $HAS_ARCH_CHANGES"
          echo "ADR incluído/atualizado neste PR: $HAS_ADR_CHANGES"

          # Validação 1: Se houve mudança em arquivos de arquitetura, deve haver um ADR no commit/PR
          if [ "$HAS_ARCH_CHANGES" = "true" ]; then
            if [ "$HAS_ADR_CHANGES" = "true" ]; then
              echo "✅ SUCESSO: Mudança arquitetural detectada e acompanhada de atualização de ADR."
              exit 0
            fi

            # Validação 2: Checagem de isenção explícita no corpo do PR via tag de bypass aprovada
            if echo "$PR_BODY" | grep -Eiq '\[x\]\s*Isenção de ADR|\[x\]\s*No ADR Required'; then
              echo "⚠️ AVISO: Mudança arquitetural detectada sem ADR, porém justificada via bypass no PR."
              exit 0
            fi

            echo "❌ ERRO DE GOVERNANÇA:"
            echo "Foram detectadas alterações em arquivos críticos de arquitetura/banco de dados,"
            echo "mas nenhum arquivo em 'docs/adrs/' foi criado ou modificado neste Pull Request."
            echo ""
            echo "Por favor, adicione um novo registro de decisão técnica utilizando o template 'adr-template-specification.md'"
            echo "ou marque a justificativa de isenção no checklist do PR."
            exit 1
          else
            echo "ℹ️ INFORMAÇÃO: Nenhuma alteração em arquivos de arquitetura crítica detectada. Validação concluída."
            exit 0
          fi
```

---

## 2. Regras de Disparo e Caminhos Monitorados

A esteira monitora automaticamente alterações nos seguintes caminhos críticos:

* `src/domain/**` — Alterações na camada primária de regras de negócio e agregados DDD.
* `src/infrastructure/**` — Ajustes em drivers de persistência, integrações com LLMs e gateways.
* `db/migrations/**` — Alterações em schemas de banco de dados (DDL/DML).
* `api/openapi.yaml` — Modificações em contratos REST públicos.
* `terraform/**` / `docker-compose.yml` — Alterações na infraestrutura e provisionamento.

---

## 3. Fluxo de Execução e Bloqueio de Merges

```
[Desenvolvedor abre PR]
         │
         ▼
[GitHub Actions dispara 'adr-validator.yml']
         │
         ├─► [Sem mudanças em arquivos críticos] ──► Status: PASS ✅ (Merge Liberado)
         │
         └─► [Com mudanças em arquivos críticos]
                   │
                   ├──► [Novo/Alterado arquivo em docs/adrs/*.md?] ──► Status: PASS ✅
                   │
                   └──► [Nenhum ADR alterado?] 
                             │
                             ├──► [Checkbox 'Isenção de ADR' marcado?] ──► Status: PASS ⚠️ (Com aviso)
                             │
                             └──► [Sem justificativa] ──► Status: FAIL ❌ (Merge Bloqueado)
```

---

## 4. Integração com as Branch Rulesets do GitHub

Para garantir a aplicação compulsória deste controle:

1. Acesse **Settings > Branches / Rulesets** no repositório GitHub.
2. Na regra da branch `main` e `develop`, habilite a opção **Require status checks to pass before merging**.
3. Adicione o check `Validar Presença de ADR em Mudanças Arquiteturais` à lista de verificações obrigatórias.

Com essa configuração, nenhum Pull Request que altere a arquitetura do sistema poderá sofrer *merge* sem a correspondente documentação no padrão ADR.
