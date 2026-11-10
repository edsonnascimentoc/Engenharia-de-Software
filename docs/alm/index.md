# Application Lifecycle Management (ALM) — Guia e Playbook Operacional

Este repositório contém o arcabouço conceitual e operacional para o **Gerenciamento do Ciclo de Vida de Aplicações (ALM)**. O modelo enxerga o software não como um ato isolado de codificação, mas como um **produto contínuo** sob governança, sustentação e evolução constante, cobrindo da concepção ao descomissionamento.

---

## 📁 Estrutura de Navegação do Repositório

A documentação está organizada de forma modular para facilitar a consulta, a manutenção e a expansão:

### 1. Fundamentação Conceitual
- [Conceito e Fases Macro](fundamentacao/conceito-e-fases-macro.md): Definição de ALM, a visão de produto contínuo e as 5 fases macro.
- [Ciclo de Vida Detalhado](fundamentacao/ciclo-de-vida-detalhado.md): Mapeamento conceitual de ponta a ponta das etapas do ciclo de desenvolvimento.

### 2. Governança e Diretrizes
- [Matriz de Criticidade](governanca/matriz-criticidade.md): Enquadramento do nível de formalidade segundo o porte do projeto (Porte P, M e G).
- [Matriz RACI Global](governanca/matriz-raci.md): Mapeamento formal de responsabilidades dos papéis corporativos em cada fase.
- [KPIs e Métricas DORA](governanca/kpis-e-metricas-dora.md): Indicadores-chave de desempenho, velocidade, estabilidade e qualidade.

### 3. Fases Operacionais do Playbook (Procedimentos, Gates DoR/DoD)
- [Fase 1: Estudo de Viabilidade e Alinhamento Estratégico](fases/fase-1-viabilidade.md)
- [Fase 2: Engenharia de Requisitos e Discovery (ISO 29148)](fases/fase-2-requisitos-e-discovery.md)
- [Fase 3: Design Arquitetural, Estruturação de Dados e UX/UI](fases/fase-3-arquitetura-dados-e-ux.md)
- [Fase 4: Desenvolvimento Incremental e Codificação Ágil](fases/fase-4-desenvolvimento-agil.md)
- [Fase 5: Garantia de Qualidade (QA) e Testes Automatizados](fases/fase-5-qualidade-e-testes.md)
- [Fase 6: Implantação e Transição (CI/CD e Deployment)](fases/fase-6-implantacao-e-cicd.md)
- [Fase 7: Operações, Observabilidade e Evolução Contínua](fases/fase-7-operacoes-e-observabilidade.md)
- [Fase 8: Descomissionamento e Sunset](fases/fase-8-descomissionamento-e-sunset.md)

### 4. Artefatos e Modelos Padrão
- [Templates e Artefatos Padrão](artefatos/templates-e-padroes.md): Modelos obrigatórios (ADR, SRS ISO 29148, PR Template e Runbook de Operações).

---

## 🎯 Como Utilizar este Framework
1. **Identifique a Criticidade do Projeto:** Consulte a [Matriz de Criticidade](governanca/matriz-criticidade.md) para determinar quais ritos e artefatos são obrigatórios.
2. **Defina as Responsabilidades:** Utilize a [Matriz RACI](governanca/matriz-raci.md) para alinhar o envolvimento de PO, Arquiteto, Devs, QA, DevOps e Stakeholders.
3. **Execute os Gates por Fase:** Acompanhe os critérios de entrada (*Definition of Ready - DoR*) e saída (*Definition of Done - DoD*) de cada etapa listada na pasta [`fases/`](fases/).
