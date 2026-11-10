# Matriz de Criticidade de Projetos

## 1. Diretrizes de Uso e Aplicabilidade
Este guia aplica-se a todos os projetos de desenvolvimento de software (Monólitos, Microsserviços, Aplicações Mobile, APIs e Plataformas SaaS), devendo ter sua formalidade dimensionada segundo o enquadramento na **Matriz de Criticidade do Projeto**.

O objetivo desta classificação é evitar overhead burocrático em projetos simples e garantir o rigor necessário em sistemas críticos.

---

## 2. Níveis de Enquadramento de Porte

### 🔹 Porte P (MVP / PoC Interna)
- **Foco:** Agilidade e validação rápida de hipóteses.
- **Exigências:** Requisitos essenciais, testes unitários automatizados nos módulos de domínio e pipeline de CI/CD básico.
- **Ritos:** Code review simplificado (1 aprovador).

### 🔹 Porte M (Sistema Corporativo / Negócio)
- **Foco:** Sustentabilidade operacional e governança ágil.
- **Exigências:** Especificação de requisitos funcionais e não funcionais, revisões de código obrigatórias (mínimo 2 aprovadores), análise estática de segurança (SAST) e testes integrados.
- **Ritos:** Ambientes segregados (Dev, Staging, Prod) e deploy automatizado via CI/CD.

### 🔹 Porte G (Sistema Core / Regulado / Bancário)
- **Foco:** Governança estrita, alta disponibilidade e compliance legal.
- **Exigências:** Rastreabilidade completa de requisitos conforme norma ISO 29148, testes de carga e estresse (K6/JMeter), análises SAST/DAST, auditoria, plano formal de desastre e redundância de infraestrutura em produção.
- **Ritos:** Gates rígidos de homologação UAT e aprovação formal de arquitetura via ADR.

---

## 🔗 Referências Cruzadas
- Consulte as responsabilidades de cada papel no enquadramento em [Matriz RACI Global](matriz-raci.md).
- Retorne ao [Sumário Principal](../index.md).
