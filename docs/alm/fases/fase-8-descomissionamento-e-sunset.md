# Fase 8: Descomissionamento e Sunset

## 🎯 Objetivo
Encerrar a vida útil do software de forma controlada, garantindo a segurança patrimonial, a preservação legal de dados e a transição sem impacto para a organização.

---

## 📋 Workflow de Execução
1. **Retenção e Arquivamento de Dados:** Exportação e criptografia da base de dados histórica para atendimento a requisitos de temporalidade legal e regulatória (ex.: LGPD, prazos fiscais/escolares).
2. **Plano de Descontinuidade:** Comunicação prévia orientada aos usuários finais e desativação gradual de integrações com sistemas parceiros.
3. **Desativação de Infraestrutura:** Remoção segura de servidores, contêineres, instâncias de banco de dados, entradas de DNS e revogação de segredos e chaves de acesso.

---

## 🚪 Critérios de Entrada (DoR) e Saída (DoD)

- **Critérios de Entrada (*Definition of Ready - DoR*):**
  - Decisão executiva formalizada de substituição ou descontinuidade definitiva da aplicação.

- **Critérios de Saída (*Definition of Done - DoD / Gate 8*):**
  - Termo de Descomissionamento assinado pelos responsáveis e infraestrutura de servidores e credenciais 100% desativada e sanitizada.

---

## 👥 Responsabilidades RACI na Fase
- **Responsáveis (R):** Product Owner (PO).
- **Aprovadores (A):** DevOps / SecOps e Stakeholders.
- **Consultados (C):** Arquiteto de Software, Tech Lead / Devs.
- **Informado (I):** QA / Tester.

---

## 🔗 Referências Cruzadas
- Conceito detalhado em [Ciclo de Vida Detalhado — Item 4](../fundamentacao/ciclo-de-vida-detalhado.md#4-encerramento-e-descomissionamento-sunset--decommissioning).
- Etapa anterior: [Fase 7: Operações e Observabilidade](fase-7-operacoes-e-observabilidade.md).
- Retorne ao [Sumário Principal](../index.md).
