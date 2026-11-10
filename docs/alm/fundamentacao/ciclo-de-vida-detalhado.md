# Mapeamento Detalhado do Ciclo de Vida do Desenvolvimento (Ponta a Ponta)

Este documento descreve a fundamentação conceitual detalhada de todas as etapas que compõem o ciclo de vida completo de engenharia de software no modelo ALM.

---

## 3.1. Estudo de Viabilidade (Fase Pré-Projeto - Decisão Go/No-Go)
Avaliação técnica e estratégica que antecede o investimento de recursos e o desenvolvimento:
* **Viabilidade Econômica:** Análise de Custo-Benefício, ROI (*Return on Investment*) e TCO (*Total Cost of Ownership*). Avalia se o retorno financeiro ou ganho operacional justifica os custos de desenvolvimento, infraestrutura e alocação de equipe.
* **Viabilidade Técnica:** Análise de maturidade da equipe em relação às tecnologias escolhidas, necessidade de treinamentos/contratações, complexidade de integração com sistemas legados e capacidade da infraestrutura existente.
* **Viabilidade Operacional e Legal:** Avaliação do impacto do sistema na rotina dos usuários finais e aderência às regulamentações vigentes (ex.: LGPD, ISO/IEC 27001, normas do setor).

---

## 3.2. Análise e Levantamento de Requisitos (ISO/IEC/IEEE 29148)
Entendimento aprofundado e estruturação das expectativas e regras do sistema:
* **Requisitos Funcionais (RF):** Declaração do que o sistema deve executar (comportamentos, entradas, processamentos e saídas esperadas).
* **Requisitos Não Funcionais (RNF):** Atributos de qualidade e restrições técnicas (desempenho, escalabilidade, disponibilidade, segurança e acessibilidade).
* **Alinhamento com Stakeholders:** Condução de *Product Discovery*, entrevistas com especialistas de domínio e dinâmicas de *Design Thinking* para garantir que o escopo atenda às necessidades reais de negócio.

---

## 3.3. Design e Arquitetura do Sistema
Planejamento estrutural e visual da solução de software:
* **Arquitetura de Software:** Escolha do estilo arquitetural (Microsserviços, Monólito Modular, Event-Driven, Serverless) e definição da *stack* tecnológica (bancos de dados SQL/NoSQL, linguagens, plataformas de nuvem AWS/Azure).
* **Modelagem de Dados:** Construção dos modelos Conceitual (MER), Lógico e Físico (DER), aplicando regras formais de normalização (1FN, 2FN e 3FN) e integridade referencial.
* **Design de UI/UX:** Prototipação de interface (wireframes e protótipos navegáveis em ferramentas como Figma) para validação da experiência do usuário e definição do *Design System*.

---

## 3.4. Desenvolvimento e Codificação (Implementação Incremental)
Transformação dos requisitos e desenhos arquiteturais em código executável, limpo e testável:
* **Divisão de Tarefas & Ágil:** Aplicação de metodologias ágeis (Scrum/Kanban) para decompor o projeto em *User Stories*, critérios de aceitação e ciclos curtos de entrega (*Sprints*).
* **Controle de Versão & Branching:** Uso de plataformas como Git (GitHub/GitLab/Azure DevOps) com políticas formais de ramificação (*Gitflow* ou *Trunk-Based Development*) para colaboração paralela sem regressões.
* **Revisão de Código (Code Review):** Processo de inspeção pelos pares via *Pull Requests* (PRs) para assegurar padrões de codificação, facilidade de manutenção e ausência de falhas antes da mesclagem no ramo principal.

---

## 3.5. Testes e Garantia de Qualidade (QA & Testing)
Fase crítica para mitigar falhas, garantir a estabilidade operacional e certificar o cumprimento das especificações:
* **Testes Automatizados:** Cobertura através de pirâmide de testes — testes unitários (lógica de domínio/isolada), testes de integração (banco de dados, contratos de APIs) e testes ponta a ponta (E2E).
* **Testes de Aceitação do Usuário (UAT):** Validação funcional por usuários reais ou analistas de negócios em ambiente de homologação (*staging*) para homologação das regras de negócio.
* **Testes de Carga, Estresse e Segurança:** Simulação de volume expressivo de acessos simultâneos (ferramentas como JMeter/K6) para medir pontos de ruptura, combinada com análises estáticas e dinâmicas de segurança (SAST/DAST/OWASP).

---

## 3.6. Implantação e Transição (Deployment & Release)
Mecanismos de disponibilização contínua e segura da aplicação no ambiente final de produção:
* **Pipeline de CI/CD:** Automação dos processos de compilação, teste, empacotamento em contêineres (Docker) e implantação (*GitHub Actions / Azure Pipelines*), reduzindo a intervenção manual e o risco de falhas operacionais.
* **Migração e Sanitização de Dados:** Processos de ETL (*Extract, Transform, Load*) e migração de esquemas DDL/DML para transferência íntegra e segura do histórico de dados em sistemas legados.
* **Treinamento e Documentação Técnica:** Capacitação das equipes de operação/suporte técnico e disponibilização de manuais e guias de uso para a comunidade de usuários finais.

---

## 3.7. Manutenção, Sustentação e Evolução (Pós-Lançamento)
Gestão contínua do software em produção, fase que representa a maior parcela do custo total de propriedade (TCO) no ciclo ALM:
* **Manutenção Corretiva:** Resolução tempestiva de defeitos não identificados nas fases anteriores e reportados no ambiente operacional.
* **Manutenção Adaptativa:** Ajustes necessários decorrentes de mudanças no ecossistema externo (ex.: atualizações de sistemas operacionais, navegadores, APIs de terceiros ou adequações regulatórias/fiscais).
* **Manutenção Evolutiva (Melhorias Contínuas):** Implementação de novos requisitos e refinamento de funcionalidades existentes a partir de métricas de uso e *feedback* dos usuários, realimentando o ciclo ALM em uma nova iteração.

---

## 4. Encerramento e Descomissionamento (Sunset / Decommissioning)
Fase final do ALM em que o software atinge o fim de sua vida útil:
* **Retenção e Arquivamento de Dados:** Preservação legal dos registros e dados sensíveis em conformidade com prazos regulatórios (ex.: LGPD, temporalidade de documentos).
* **Plano de Descontinuidade:** Transição orientada dos usuários para novas plataformas e desativação segura da infraestrutura de servidores, contêineres e credenciais.

---

## 🔗 Referências Cruzadas
- Para os procedimentos operacionais e ritos de cada fase, consulte o diretório [`fases/`](../fases/).
- Retorne ao [Sumário Principal](../index.md).
