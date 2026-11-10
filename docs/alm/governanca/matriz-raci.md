# Matriz RACI Global do ALM

A Matriz RACI define as responsabilidades dos diferentes papéis corporativos ao longo de cada uma das 8 fases operacionais do ALM.

---

## 📊 Matriz de Responsabilidades

| Fase de ALM | Product Owner (PO) | Arquiteto de Software | Tech Lead / Devs | QA / Tester | DevOps / SecOps | Stakeholders |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **1. Viabilidade (Go/No-Go)** | **R / A** | C | C | I | C | **A** |
| **2. Requisitos & Scope** | **R / A** | C | C | C | I | C |
| **3. Arquitetura & UX/UI** | C | **R / A** | C | I | C | I |
| **4. Desenvolvimento (Dev)** | I | C | **R / A** | C | C | I |
| **5. Garantia de Qualidade (QA)**| I | C | C | **R / A** | C | I |
| **6. Implantação (Deploy)** | I | C | C | C | **R / A** | I |
| **7. Operações (Ops/Sustentação)**| C | C | C | I | **R / A** | I |
| **8. Sunset (Descomissionamento)**| **R** | C | C | I | **A** | **A** |

---

## 📌 Legenda de Papéis
- **R — Responsável (*Responsible*):** Quem executa a atividade e produz o entregável da fase.
- **A — Aprovador (*Accountable*):** Quem possui a palavra final, aprova a fase e responde pelo resultado (Gate Approval).
- **C — Consultado (*Consulted*):** Especialista ou papel que deve ser consultado antes ou durante a execução.
- **I — Informado (*Informed*):** Papel mantido atualizado sobre o progresso e conclusões da fase.

---

## 🔗 Referências Cruzadas
- Para o fluxo operacional detalhado de cada fase, acesse o diretório [`fases/`](../fases/).
- Retorne ao [Sumário Principal](../index.md).
