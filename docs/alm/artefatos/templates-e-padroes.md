# Templates e Artefatos Padrão de ALM

Todo projeto desenvolvido sob a governança deste framework de ALM deve adotar os modelos padronizados abaixo para garantir auditabilidade, rastreabilidade e consistência técnica.

---

## 📄 Artefatos Obrigatórios

### 1. ADR (Architecture Decision Record)
- **Finalidade:** Registrar decisões arquiteturais relevantes, suas justificativas, opções consideradas, trade-offs e consequências.
- **Aplicação:** Obrigatório na Fase 3 para escolhas de padrões, bancos de dados, frameworks e integrações.

### 2. SRS (Software Requirements Specification - ISO/IEC/IEEE 29148)
- **Finalidade:** Especificar a visão geral, escopo, requisitos funcionais (RF) em sintaxe formal e requisitos não funcionais (RNF) com limites mensuráveis.
- **Aplicação:** Obrigatório na Fase 2 para alinhamento entre PO, Arquiteto e Engenharia.

### 3. Templates de issue e PR
- **Finalidade:** Capturar bug e funcionalidade com critérios verificáveis e oferecer checklist de rastreabilidade, teste e evidência para PRs.
- **Aplicação:** Use os templates em [`.github/ISSUE_TEMPLATE/`](../../../.github/ISSUE_TEMPLATE/) para novas demandas e [`.github/PULL_REQUEST_TEMPLATE.md`](../../../.github/PULL_REQUEST_TEMPLATE.md) na revisão por pares. Consulte a [política de contribuição](../../../CONTRIBUTING.md).

### 4. Runbook de Operações
- **Finalidade:** Documentar o manual de operação do sistema em produção, procedimentos de sustentação, contingência, recuperação de desastres (*disaster recovery*) e contatos de escalonamento.
- **Aplicação:** Obrigatório nas Fases 6 e 7 para o time de DevOps e suporte N1/N2/N3.

---

## 🔗 Referências Cruzadas
- Consulte o enquadramento de uso dos artefatos em [Matriz de Criticidade](../governanca/matriz-criticidade.md).
- Retorne ao [Sumário Principal](../index.md).
