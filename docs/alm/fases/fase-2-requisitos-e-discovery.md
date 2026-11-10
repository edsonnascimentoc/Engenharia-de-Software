# Fase 2: Engenharia de Requisitos e Discovery (ISO/IEC/IEEE 29148)

## 🎯 Objetivo
Transformar necessidades e expectativas de negócio em especificações técnicas não ambíguas, testáveis, mensuráveis e rastreáveis.

---

## 📋 Workflow de Execução
1. Conduzir sessões de *Product Discovery*, entrevistas com especialistas de domínio e dinâmicas de *Design Thinking* com stakeholders.
2. Especificar **Requisitos Funcionais (RF)** utilizando a sintaxe formal:
   > *"O sistema DEVE permitir [ação] para [ator] quando [condição]"*.
3. Especificar **Requisitos Não Funcionais (RNF)** com limites mensuráveis (Ex.: Latência P95 < 2s, Disponibilidade 99.5%).
4. Construir a **Matriz de Rastreabilidade** vinculando cada RF e RNF às regras de negócio e aos futuros casos de teste.

---

## 🚪 Critérios de Entrada (DoR) e Saída (DoD)

- **Critérios de Entrada (*Definition of Ready - DoR*):**
  - Decisão *Go* aprovada no Gate 1 da Fase 1.

- **Critérios de Saída (*Definition of Done - DoD / Gate 2*):**
  - Especificação de Requisitos do Software (SRS) conforme norma ISO/IEC/IEEE 29148 revisada e formalmente aprovada pelo Arquiteto de Software e pelo Product Owner.

---

## 👥 Responsabilidades RACI na Fase
- **Responsável (R):** Product Owner (PO).
- **Aprovadores (A):** Product Owner.
- **Consultados (C):** Arquiteto de Software, Tech Lead / Devs, QA / Tester, Stakeholders.
- **Informado (I):** DevOps / SecOps.

---

## 🔗 Referências Cruzadas
- Conceito detalhado em [Ciclo de Vida Detalhado — Item 3.2](../fundamentacao/ciclo-de-vida-detalhado.md#32-análise-e-levantamento-de-requisitos-isoicieee-29148).
- Etapa anterior: [Fase 1: Estudo de Viabilidade](fase-1-viabilidade.md).
- Próxima etapa: [Fase 3: Design Arquitetural, Dados e UX](fase-3-arquitetura-dados-e-ux.md).
- Retorne ao [Sumário Principal](../index.md).
