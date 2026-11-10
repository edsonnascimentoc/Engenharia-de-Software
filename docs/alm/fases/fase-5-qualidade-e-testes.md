# Fase 5: Garantia de Qualidade (QA) e Testes Automatizados

## 🎯 Objetivo
Garantir a ausência de defeitos críticos, a estabilidade operacional, a segurança da aplicação e a conformidade funcional com os requisitos estabelecidos.

---

## 📋 Workflow de Execução
1. **Pirâmide de Testes Automatizados:**
   - **Testes Unitários:** Mínimo de 80% de cobertura de código em regras de negócio isoladas.
   - **Testes de Integração:** Validação dos contratos de API e comunicação com o banco de dados.
   - **Testes E2E / Interface:** Automação dos fluxos críticos de jornada do usuário.
2. **Testes de Segurança & Carga:** Executar varreduras estáticas e dinâmicas (SAST/DAST com ferramentas como Trivy/SonarQube) e simulações de estresse de carga (K6/JMeter).
3. **UAT (*User Acceptance Testing*):** Validação funcional por usuários reais ou analistas de negócios no ambiente de Homologação (*Staging*).

---

## 🚪 Critérios de Entrada (DoR) e Saída (DoD)

- **Critérios de Entrada (*Definition of Ready - DoR*):**
  - Versão da aplicação (Build) compilada, testada em nível unitário e implantada no ambiente de QA/Staging.

- **Critérios de Saída (*Definition of Done - DoD / Gate 5*):**
  - Relatório de Testes sem defeitos abertos de severidade Alta/Bloqueante (*Blocker/High*) e aprovação formal no Quality Gate de segurança e cobertura.

---

## 👥 Responsabilidades RACI na Fase
- **Responsável (R):** QA / Tester.
- **Aprovadores (A):** QA / Tester.
- **Consultados (C):** Arquiteto de Software, Tech Lead / Devs, DevOps / SecOps.
- **Informados (I):** Product Owner, Stakeholders.

---

## 🔗 Referências Cruzadas
- Conceito detalhado em [Ciclo de Vida Detalhado — Item 3.5](../fundamentacao/ciclo-de-vida-detalhado.md#35-testes-e-garantia-de-qualidade-qa--testing).
- Métricas associadas em [KPIs e Métricas DORA](../governanca/kpis-e-metricas-dora.md).
- Etapa anterior: [Fase 4: Desenvolvimento Incremental](fase-4-desenvolvimento-agil.md).
- Próxima etapa: [Fase 6: Implantação e Transição](fase-6-implantacao-e-cicd.md).
- Retorne ao [Sumário Principal](../index.md).
