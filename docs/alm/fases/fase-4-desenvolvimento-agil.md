# Fase 4: Desenvolvimento Incremental e Codificação Ágil

## 🎯 Objetivo
Construir o software de forma incremental através de ciclos curtos (*Sprints*), priorizando a qualidade interna do código, manutenibilidade e entrega continuada de valor.

---

## 📋 Workflow de Execução
1. **Gestão de Sprints:** Decompor as demandas da fase de requisitos em *User Stories* com critérios de aceitação claros (Scrum/Kanban).
2. **Estratégia de Branching:** Adotar políticas formais de ramificação no controle de versão Git (*Gitflow* ou *Trunk-Based Development*) conforme a maturidade da equipe.
3. **Revisão de Código (*Code Review*):** Exigir inspeção e aprovação de ao menos 2 desenvolvedores por *Pull Request* (PR), com foco em Clean Code, SOLID e padrões de segurança.

---

## 🚪 Critérios de Entrada (DoR) e Saída (DoD)

- **Critérios de Entrada (*Definition of Ready - DoR*):**
  - Tarefa/Story com requisitos técnicos e critérios de aceitação (DoR) devidamente preenchidos.

- **Critérios de Saída (*Definition of Done - DoD / Gate 4*):**
  - Código integrado e mesclado na branch `develop`, aprovado no processo de Code Review via PR e sem regressões identificadas na compilação.

---

## 👥 Responsabilidades RACI na Fase
- **Responsável (R):** Tech Lead / Devs.
- **Aprovadores (A):** Tech Lead / Devs.
- **Consultados (C):** Arquiteto de Software, QA / Tester, DevOps / SecOps.
- **Informados (I):** Product Owner, Stakeholders.

---

## 🔗 Referências Cruzadas
- Conceito detalhado em [Ciclo de Vida Detalhado — Item 3.4](../fundamentacao/ciclo-de-vida-detalhado.md#34-desenvolvimento-e-codificação-implementação-incremental).
- Modelo de artefato PR Template em [Templates e Artefatos Padrão](../artefatos/templates-e-padroes.md).
- Etapa anterior: [Fase 3: Design Arquitetural e UX](fase-3-arquitetura-dados-e-ux.md).
- Próxima etapa: [Fase 5: Garantia de Qualidade e Testes](fase-5-qualidade-e-testes.md).
- Retorne ao [Sumário Principal](../index.md).
