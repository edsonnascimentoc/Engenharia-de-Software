# PLAYBOOK OPERACIONAL DE ALM (Application Lifecycle Management)
## Guia Prático de Governança e Execução do Ciclo de Vida do Software

---

## 1. PROPÓSITO E DIRETRIZES DE USO

### 1.1. Objetivo do Playbook
Este Playbook estabelece o padrão operacional obrigatório para a gestão do ciclo de vida de aplicações (ALM) na organização. Seu propósito é guiar equipes de produto, arquitetura, engenharia e operações desde a validação da viabilidade de uma ideia até o descomissionamento seguro da aplicação, garantindo previsibilidade, alta qualidade, conformidade regulatória e eficiência técnica.

### 1.2. Escopo e Aplicabilidade
Este guia aplica-se a todos os projetos de desenvolvimento de software (Monólitos, Microsserviços, Aplicações Mobile, APIs e Plataformas SaaS), devendo ter sua formalidade dimensionada segundo a **Matriz de Criticidade do Projeto**:

* **Porte P (MVP / PoC Interna):** Foco em agilidade, requisitos essenciais, testes unitários automatizados e CI/CD básico.
* **Porte M (Sistema Corporativo / Negócio):** Governança ágil, revisões de código obrigatórias, análise estática de segurança (SAST) e testes integrados.
* **Porte G (Sistema Core / Regulado / Bancário):** Governança estrita, rastreabilidade completa de requisitos (ISO 29148), testes de carga, SAST/DAST, auditoria e redundância de produção.

---

## 2. MATRIZ DE RESPONSABILIDADES (RACI GLOBAL)

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

*Legenda: **R** = Responsável (quem faz); **A** = Accountable (quem aprova/responde); **C** = Consultado (especialista); **I** = Informado.*

---

## 3. ESTÁGIOS DO PLAYBOOK: PROCEDIMENTOS, GATES E ENTREGÁVEIS

---

### FASE 1: ESTUDO DE VIABILIDADE E ALINHAMENTO ESTRATÉGICO
**Objetivo:** Decidir rigorosamente a aprovação ou cancelamento do projeto (*Go/No-Go*) antes do investimento de recursos.

#### 📋 Workflow de Execução:
1. **Análise Econômica:** Estimar Custo Total de Propriedade (TCO - licenças, nuvem, time) versus Retorno sobre Investimento (ROI / economia gerada).
2. **Avaliação de Viabilidade Técnica:** Avaliar a curva de aprendizado da equipe, compatibilidade com a stack institucional e necessidade de integrações legadas.
3. **Avaliação Operacional e Legal:** Verificar impacto em processos existentes e compliance (LGPD, normas fiscais e setoriais).

#### 🚪 Criteria de Entrada (DoR) e Saída (DoD):
* **Entrada:** Solicitação de Negócio ou Oportunidade de Mercado formalizada pelo PO.
* **Saída (Gate 1 - Go/No-Go):** Documento de Viabilidade Aprovado por Sponsor e Arquiteto-Chefe.

---

### FASE 2: ENGENHARIA DE REQUISITOS E DISCOVERY (ISO/IEC/IEEE 29148)
**Objetivo:** Transformar necessidades de negócio em especificações não ambíguas, testáveis e rastreáveis.

#### 📋 Workflow de Execução:
1. Conduzir sessões de *Product Discovery* e *Design Thinking* com stakeholders.
2. Especificar **Requisitos Funcionais (RF)** utilizando a sintaxe formal: *"O sistema DEVE permitir [ação] para [ator] quando [condição]"*.
3. Especificar **Requisitos Não Funcionais (RNF)** com limites mensuráveis (Ex.: Latência P95 < 2s, Disponibilidade 99.5%).
4. Construir a **Matriz de Rastreabilidade** vinculando cada RF/RNF às regras de negócio e casos de teste.

#### 🚪 Criteria de Entrada (DoR) e Saída (DoD):
* **Entrada:** Decisão *Go* aprovada na Fase 1.
* **Saída (Gate 2):** Especificação de Requisitos (SRS) revisada e aprovada pelo Arquiteto e PO.

---

### FASE 3: DESIGN ARQUITETURAL, ESTRUTURAÇÃO DE DADOS E UX/UI
**Objetivo:** Projetar a solução técnica, visual e estrutural garantindo escalabilidade, segurança e usabilidade.

#### 📋 Workflow de Execução:
1. **Decisão Arquitetural:** Definir padrão (Microsserviços, Monólito Modular, Serverless) e registrar justificativa via **ADR (Architecture Decision Record)**.
2. **Modelagem de Dados:** Desenvolver MER/DER aplicando regras formais de normalização (1FN, 2FN e 3FN) e índices de performance.
3. **UI/UX & Design System:** Criar protótipos de alta fidelidade (Figma) e mapear fluxos de navegação validados com usuários.

#### 🚪 Criteria de Entrada (DoR) e Saída (DoD):
* **Entrada:** SRS formalizado na Fase 2.
* **Saída (Gate 3):** ADRs aprovadas, Schema DDL inicial validado e Protótipos de UX aceitos.

---

### FASE 4: DESENVOLVIMENTO INCREMENTAL E CODIFICAÇÃO ÁGIL
**Objetivo:** Construir o software em ciclos curtos (*Sprints*), priorizando qualidade interna do código.

#### 📋 Workflow de Execução:
1. **Gestão de Sprints:** Decompor demandas em *User Stories* com critérios de aceitação claros.
2. **Estratégia de Branching:** Adotar *Gitflow* ou *Trunk-Based Development* conforme a maturidade do time.
3. **Revisão de Código (Code Review):** Exigir aprovação de ao menos 2 desenvolvedores por Pull Request (PR) com foco em Clean Code, SOLID e segurança.

#### 🚪 Criteria de Entrada (DoR) e Saída (DoD):
* **Entrada:** Task com critérios de aceitação (DoR) preenchidos.
* **Saída (Gate 4):** Código mesclado na branch `develop`, aprovado em Code Review e sem regressões.

---

### FASE 5: GARANTIA DE QUALIDADE (QA) E TESTES AUTOMATIZADOS
**Objetivo:** Garantir a ausência de defeitos críticos, estabilidade e conformidade com os requisitos.

#### 📋 Workflow de Execução:
1. **Pirâmide de Testes:**
   - **Unitários:** Mínimo de 80% de cobertura de código em regras de negócio.
   - **Integração:** Validação de contratos de API e comunicação com banco de dados.
   - **E2E / Interface:** Automação dos fluxos críticos de usuário.
2. **Testes de Segurança & Carga:** Executar varreduras SAST/DAST (Trivy/SonarQube) e testes de estresse (K6/JMeter).
3. **UAT (User Acceptance Testing):** Validação formal das entregas no ambiente de Homologação.

#### 🚪 Criteria de Entrada (DoR) e Saída (DoD):
* **Entrada:** Build gerada e implantada no ambiente de QA/Staging.
* **Saída (Gate 5):** Relatório de Testes sem bugs críticos (Blocker/High) e Quality Gate aprovado.

---

### FASE 6: IMPLANTAÇÃO E TRANSIÇÃO (CI/CD E DEPLOYMENT)
**Objetivo:** Colocar a aplicação no ar no ambiente de Produção com zero *downtime* e alta automação.

#### 📋 Workflow de Execução:
1. **Pipeline de CI/CD:** Automação do build multi-stage em Docker e deploy automatizado (GitHub Actions / Azure Pipelines).
2. **Estratégia de Release:** Utilizar estratégias de *Blue-Green* ou *Canary Deployment* para possibilitar *rollback* instantâneo se necessário.
3. **Migração de Dados:** Executar scripts de DDL/DML automatizados (Flyway/Liquibase) pré-deploy.

#### 🚪 Criteria de Entrada (DoR) e Saída (DoD):
* **Entrada:** Tag de Release gerada e homologada em Staging.
* **Saída (Gate 6):** Aplicação operacional em Produção, com fumaça (Smoke Test) 100% verde.

---

### FASE 7: OPERAÇÕES, OBSERVABILIDADE E EVOLUÇÃO CONTÍNUA
**Objetivo:** Garantir disponibilidade, performance contínua e sustentação evolutiva do sistema.

#### 📋 Workflow de Execução:
1. **Observabilidade (OpenTelemetry):** Monitorar a tríade Métrica, Logs Estruturados (JSON) e Traces Distribuídos (W3C).
2. **Gestão de Incidentes & SLAs:** Operar com suporte N1/N2/N3 respeitando SLAs acordados de MTTR (Mean Time to Repair).
3. **Manutenção Cíclica:**
   - *Corretiva:* Correção rápida de defeitos operacionais.
   - *Adaptativa:* Atualização de bibliotecas, SO e segurança.
   - *Evolutiva:* Início de novo ciclo ALM para grandes novas funcionalidades.

#### 🚪 Criteria de Entrada (DoR) e Saída (DoD):
* **Entrada:** Sistema operando em ambiente de Produção.
* **Saída (Gate 7):** Relatórios mensais de SLA/SLO aprovados e sustentação estabilizada.

---

### FASE 8: DESCOMISSIONAMENTO E SUNSET
**Objetivo:** Encerrar a vida útil do software garantindo segurança patrimonial, legal e transição fluida.

#### 📋 Workflow de Execução:
1. **Retenção de Dados:** Exportação e criptografia da base histórica para cumprimento de requisitos de temporalidade da LGPD/Legislação.
2. **Plano de Descontinuidade:** Comunicação prévia a usuários e desativação gradual de integrações.
3. **Desativação de Infraestrutura:** Remoção de recursos em nuvem, contêineres, entradas de DNS e revogação de segredos/chaves.

#### 🚪 Criteria de Entrada (DoR) e Saída (DoD):
* **Entrada:** Decisão executiva de substituição ou descontinuidade da solução.
* **Saída (Gate 8):** Termo de Descomissionamento assinado e infraestrutura 100% limpa.

---

## 4. MÉTRICAS E INDICADORES CHAVE DE ALM (KPIs DORA & QUALIDADE)

Para garantir a melhoria contínua da governança de ALM em todos os projetos, cada equipe deve acompanhar mensalmente:

1. **Deployment Frequency (DF):** Frequência de implantações com sucesso em Produção.
2. **Lead Time for Changes (LTC):** Tempo desde o commit inicial até a chegada do código em Produção.
3. **Mean Time to Restore (MTTR):** Tempo médio para restabelecer o sistema após uma falha em Produção.
4. **Change Failure Rate (CFR):** Percentual de implantações que causam degradação ou falhas em Produção.
5. **Cobertura de Testes (Code Coverage):** Mínimo exigido de 80% em módulos de domínio.
6. **Débito Técnico (Technical Debt Ratio):** Índice SonarQube mantido abaixo of 5%.

---

## 5. TEMPLATES E ARTEFATOS PADRÃO

Todo projeto sob a governança deste Playbook deve adotar os seguintes modelos padrões:
* **ADR (Architecture Decision Record):** Registro de decisões técnicas relevantes.
* **SRS (Software Requirements Specification):** Padrão ISO 29148.
* **PR Template:** Checklist de validação de qualidade, testes e impacto de segurança.
* **Runbook de Operações:** Manual de incidentes e procedimentos de contingência.
