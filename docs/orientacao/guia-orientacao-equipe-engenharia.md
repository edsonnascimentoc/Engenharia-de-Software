# 📘 Guia de Orientação e Onboarding: Nova Documentação e Governança de Engenharia

Este documento consolida a estrutura atualizada do repositório **Engenharia-de-Software**, o mapa completo de artefatos técnicos gerados e o guia de navegação para desenvolvedores, arquitetos, analistas e QAs.

---

## 📂 1. Arquitetura de Diretórios Proposta para o Repositório

```text
Engenharia-de-Software/
├── README.md                              <-- Guia Principal e Índice Geral do Repositório
├── .github/
│   ├── PULL_REQUEST_TEMPLATE.md            <-- Template Obrigatório de Pull Request (DoD)
│   ├── copilot-instructions.md            <-- Regras Globais de Steering de IA (Copilot/Cursor)
│   └── workflows/
│       └── adr-validator.yml              <-- Pipeline de Validação Automatizada de ADRs
├── docs/
│   ├── alm/                               <-- Framework e Playbook Operacional de ALM
│   │   ├── index.md                       <-- Porta de Entrada da Documentação ALM
│   │   ├── fundamentacao/                 <-- Conceitos, Fases Macro e Ciclo de Vida
│   │   ├── governanca/                    <-- Matriz de Criticidade, RACI e DORA Metrics
│   │   ├── fases/                         <-- Fases 01 a 08 com Gates DoR e DoD
│   │   └── artefatos/                     <-- Especificações de ADRs, SRS e Runbooks
│   ├── projetos/
│   │   └── eduplanner/                    <-- Documentação Técnica Completa do EduPlanner
│   │       ├── especificacoes/            <-- Requisitos (RF/RNF), Use Cases e UML
│   │       ├── arquitetura/               <-- OpenAPI 3.0, DER 3FN e ADR 001 (IA)
│   │       ├── devops/                    <-- Gitflow, CI/CD e SAST/SCA
│   │       └── fases-implementacao/       <-- Fases 01 a 09 (Scaffold, LGPD, Kumon, etc.)
│   ├── templates/                         <-- Modelos Oficiais da Organização
│   │   ├── adr-template.md                <-- Modelo Nygard/MADR para Decisões Arquiteturais
│   │   └── srs-template-iso29148.md       <-- Modelo ISO/IEC/IEEE 29148 para Requisitos
│   └── steering-ia/                       <-- Governança e Regras para Assistentes de IA
│       ├── ai-steering-ruleset-template.md<-- Template Mestre de Governança de IA
│       └── azure-cosmosdb-ruleset.md      <-- Steering Ruleset para Azure Cosmos DB NoSQL
└── scripts/
    └── migrate-alm-docs.sh                <-- Script de Automação de Migração
```

---

## 🎯 2. Mapeamento de Artefatos Gerados e Sua Aplicação

| Categoria | Arquivos Criados | Finalidade & Público-Alvo |
| :--- | :--- | :--- |
| **Projeto EduPlanner** | `eduplanner-etapa-01-04.md`<br>`eduplanner-fase-01-09.md` | Especificações completas do sistema EduPlanner (Domain Model, Clean Architecture, LGPD Privacy Gateway, TimescaleDB Kumon, Redis Cache e Dashboards). |
| **Governança ALM** | `ALM_Playbook.md`<br>`alm-docs-framework.zip` | Guia operacional das 8 fases do ciclo de vida, matriz RACI, matriz de criticidade (Portes P, M, G) e métricas DORA. |
| **Padrões & CI/CD** | `pull-request-template.md`<br>`github-action-adr-validator.md` | Checklist de *Definition of Done* (DoD) e esteira do GitHub Actions para auditoria automática de ADRs em PRs. |
| **Decisões Arquiteturais** | `adr-template-specification.md` | Padrão formal para registro de decisões de arquitetura de software (ADR). |
| **Steering de IA** | `azure-cosmosdb-steering-ruleset.md`<br>`ai-steering-ruleset-template.md` | Regras normativas (RFC 2119) para calibração de assistentes de IA no VS Code / Copilot / Cursor. |
| **Automação** | `migrate-alm-docs.sh`<br>`pr-docs-alm-framework.md` | Automação via Shell Script Bash e especificação de Pull Request para integração no GitHub. |

---

## 📜 3. Notas de Orientação para a Equipe de Desenvolvimento

### 3.1. Para Desenvolvedores (Engenharia e Codificação)
- **Abertura de PRs:** Todo Pull Request DEVE utilizar o modelo `PULL_REQUEST_TEMPLATE.md`. PRs que alterem arquivos de domínio ou infraestrutura sem um ADR correspondente serão bloqueados na esteira CI/CD.
- **Configuração da IDE:** Importe os arquivos da pasta `docs/steering-ia/` no seu ambiente do VS Code / Cursor para garantir que o assistente de IA proponha códigos alinhados às decisões do projeto.
- **Cobertura de Testes:** Todo código submetido deve possuir cobertura de testes unitários $\ge 80\%$ nos módulos de domínio.

### 3.2. Para Arquitetos e Tech Leads
- **Registro de Decisões (ADRs):** Novas decisões de banco de dados, comunicação ou frameworks devem ser formalizadas na pasta `docs/adrs/` utilizando o modelo `adr-template.md`.
- **Governança de IA:** Utilize o `ai-steering-ruleset-template.md` para criar regras de direcionamento de IA para novas ferramentas ou serviços NoSQL/SQL adotados.

### 3.3. Para Product Owners (POs) e Analistas
- **Sintaxe de Requisitos:** A especificação de novos requisitos funcionais deve obrigatoriamente seguir a sintaxe EARS / ISO 29148 (*"O sistema DEVE permitir..."*).
- **Rastreabilidade:** Mantenha a vinculação bidirecional entre histórias de usuário, códigos BNCC e casos de teste.

---

## 🛠️ 4. Procedimento de Sincronização com o GitHub

Para aplicar a nova estrutura no repositório remoto:
1. Execute o script `./scripts/migrate-alm-docs.sh` no seu terminal local.
2. Abra um Pull Request utilizando o modelo `pr-docs-alm-framework.md`.
3. Solicite o Code Review dos líderes técnicos antes do merge na branch `main`.
