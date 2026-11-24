# Especificação Arquitetural: Sistema Multiagente MCP com Validação Normativa ISO/IEC/IEEE 29148 e Sintaxe EARS

## 1. Visão Geral e Arquitetura da Solução Multiagente

A evolução da Engenharia de Software moderna exige a transição de especificações estáticas e manuais para ecossistemas dinâmicos orientados a *Spec-Driven Development* (SDD) e *Application Lifecycle Management* (ALM). Para elevar o repositório ao estado da arte em qualidade e rastreabilidade, esta arquitetura estabelece uma pipeline automatizada de triagem, especificação formal e notificação de incidentes utilizando o **Model Context Protocol (MCP)**.

O sistema intercepta anomalias de execução (logs de exceção), realiza a triagem de relevância técnica, elabora rascunhos de *issues*, submete a especificação ao crivo de qualidade formal (ISO/IEC/IEEE 29148:2018 e EARS), refina eventuais lacunas e publica o artefato no GitHub, notificando simultaneamente os engenheiros de software através do Discord.

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                               CAMADA DE OBSERVABILIDADE                                │
│ [Log de Exceção/Anomalia] ──► [Logger Receiver Agent] ──► [Bug Analyzer Agent]        │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │ (Log Crítico Identificado)
                                            ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                          CAMADA DE ESPECIFICAÇÃO & GOVERNANÇA                          │
│ [Issue Drafter Agent] ──► [Issue Reviewer Agent (DoR)] ──► [Issue Refiner Agent]       │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │ (Aprovado na Validação EARS / ISO 29148)
                                            ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                            CAMADA DE EXECUÇÃO & NOTIFICAÇÃO                            │
│ [Issue Creator Agent (GitHub MCP)] ───────┬───────► [Notification Agent (Discord MCP)] │
│                                           │                                            │
│                                           ▼                                            │
│                             [GitHub Issue Rastreável]                                  │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Papéis dos Agentes na Pipeline Multiagente

1. **Logger Receiver Agent:** Atua como o ponto de entrada (*ingestion pipeline*), escutando o fluxo de dados de logs da aplicação em tempo de execução.
2. **Bug Analyzer Agent:** Aplica filtros heurísticos e de *machine learning* para isolar alertas irrelevantes ou comportamentos esperados (como alternâncias de *feature flags*), retendo apenas falhas críticas e exceções não tratadas.
3. **Issue Drafter Agent:** Compila a pilha de execução (*stack trace*), o contexto de ambiente e a carga útil do erro, estruturando um rascunho inicial de *issue*.
4. **Issue Reviewer Agent (Portão de Qualidade Formal):** Examina o rascunho contra as normas **ISO/IEC/IEEE 29148:2018** e a sintaxe **EARS**, exigindo atomicidade, ausência de ambiguidade, racional claro, método de verificação explícito e metadados de rastreabilidade.
5. **Issue Refiner Agent:** Caso o `Issue Reviewer` identifique violações formais ou ambiguidades, o `Issue Refiner` ajusta o texto, reescreve os critérios de aceite na sintaxe EARS apropriada e reapresenta o rascunho.
6. **Issue Creator Agent (GitHub MCP):** Consome a API do GitHub via protocolo MCP para registrar a *issue* oficial no repositório com etiquetas (*labels*), marcos (*milestones*) e atribuição de responsabilidades.
7. **Notification Agent (Discord MCP):** Transmite um alerta formatado em Rich Embed para o canal de engenharia no Discord, permitindo o acompanhamento em tempo real do ciclo de vida da aplicação.

---

## 2. Layout do Repositório e Estrutura de Arquivos

Para garantir que a infraestrutura de agentes seja versionada e auditável como código (*Agents as Code*), o repositório deve adotar a seguinte topologia na pasta `.github/`:

```text
.github/
├── mcp.json                         # Configuração dos servidores MCP (GitHub e Discord)
├── agents/
│   ├── logger-receiver.md           # Diretrizes do agente leitor de logs
│   ├── bug-analyzer.md              # Regras de triagem e classificação de severidade
│   ├── issue-drafter.md             # Template de estruturação de rascunhos
│   ├── issue-reviewer.md            # Motor de validação ISO 29148 e EARS (Quality Gate)
│   ├── issue-refiner.md             # Motor de correção sintática e refinamento
│   ├── issue-creator-mcp.md         # Instruções de integração com GitHub MCP
│   └── notification-discord-mcp.md  # Instruções de formatação e envio ao Discord MCP
└── workflows/
    └── agent-incident-pipeline.yml  # Pipeline CI/CD que orquestra a execução dos agentes
```

---

## 3. Configuração do Model Context Protocol (`.github/mcp.json`)

O arquivo `.github/mcp.json` declara a conexão com os servidores MCP oficiais do GitHub e do Discord, disponibilizando ferramentas padronizadas (*tools*) para os agentes atuarem na infraestrutura remota.

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-github"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${{ secrets.GH_PAT_AGENT_PIPELINE }}"
      },
      "description": "Servidor MCP para gerenciamento automatizado de issues, PRs e rastreabilidade no GitHub."
    },
    "discord": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-discord"
      ],
      "env": {
        "DISCORD_BOT_TOKEN": "${{ secrets.DISCORD_BOT_TOKEN }}",
        "DISCORD_CHANNEL_ID": "${{ secrets.DISCORD_ENGINEERING_CHANNEL_ID }}"
      },
      "description": "Servidor MCP para despacho de notificações em tempo real no Discord."
    }
  }
}
```

---

## 4. Agente `Issue Reviewer`: Validador de Qualidade ISO 29148 & EARS

O agente **`Issue Reviewer`** atua como o componente de governança mais crítico do sistema. Sua função é impedir que chamados imprecisos ou mal especificados ingressem no repositório.

### Prompt do Sistema (`.github/agents/issue-reviewer.md`)

```markdown
# Role: Senior Software Quality Architect & Requirements Governance Agent (ISO 29148 & EARS Validator)

## Objective
Você é o agente validador rigoroso da infraestrutura de engenharia. Sua única responsabilidade é avaliar os rascunhos de issues gerados pelo `Issue Drafter` e determinar se eles cumprem estritamente os critérios de qualidade da norma **ISO/IEC/IEEE 29148:2018** e os padrões sintáticos de **EARS (Easy Approach to Requirements Syntax)**.

## Validation Protocol (Definition of Ready - DoR)

### 1. Verificação de Atributos Específicos do Requisito (ISO 29148 Clause 5.2)
Para que a issue seja APROVADA, ela deve satisfazer simultaneamente todos os seguintes critérios de qualidade:

- **Singularidade (Singular):** A issue/requisito deve descrever exatamente UMA falha observável ou UMA capacidade necessária. Se contiver múltiplas solicitações independentes ("e também", "além disso"), deve ser REPROVADA e dividida.
- **Inambiguidade (Unambiguous):** O texto não pode conter adjetivos subjetivos ou vagos (ex.: "rápido", "eficiente", "amigável", "robusto", "apropriado"). Todas as métricas devem ser quantificáveis.
- **Verificabilidade (Verifiable):** A issue DEVE incluir uma seção de "Método de Verificação" indicando explicitamente como o ajuste será testado (ex.: Teste Unitário, Teste de Carga, Inspeção de Código ou Teste de Integração) com critérios objetivamente passíveis de asserção.
- **Racional (Rationale):** A issue deve apresentar a justificativa técnica do impacto da falha no negócio ou no sistema.
- **Exequibilidade (Feasible):** A correção proposta deve ser realizável dentro da arquitetura e das restrições do sistema.
- **Completo (Complete):** Contém todas as condições necessárias (contexto de execução, dados de entrada, resultado esperado e pilha de erros).

### 2. Validação da Sintaxe EARS (Easy Approach to Requirements Syntax)
Os critérios de aceite e o comportamento esperado do sistema DEVEM utilizar estritamente um dos 6 padrões formais EARS descritos abaixo:

1. **Ubíquo (Ubiquitous):** Aplica-se a regras permanentes e invariantes.
   * *Sintaxe:* O `[Nome do Sistema]` deve `[Resposta/Comportamento Observável]`.
2. **Orientado a Eventos (Event-driven):** Disparado por um evento discreto na interface ou API.
   * *Sintaxe:* **WHEN** `[Gatilho de Evento]`, o `[Nome do Sistema]` deve `[Resposta Observável]`.
3. **Orientado a Estado (State-driven):** Comportamento ativo enquanto um estado for verdadeiro.
   * *Sintaxe:* **WHILE** `[Pré-condição de Estado]`, o `[Nome do Sistema]` deve `[Resposta Observável]`.
4. **Recurso Opcional (Optional Feature):** Aplica-se apenas quando um módulo específico estiver habilitado.
   * *Sintaxe:* **WHERE** `[Recurso/Módulo Habilitado]`, o `[Nome do Sistema]` deve `[Resposta Observável]`.
5. **Comportamento Indesejado / Exceção (Unwanted Behaviour):** Tratamento formal de erros e anomalias.
   * *Sintaxe:* **IF** `[Condição de Erro/Falha]`, **THEN** o `[Nome do Sistema]` deve `[Comportamento de Mitigação/Resposta]`.
6. **Complexo (Complex Requirement):** Combinação temporal restrita de estado e gatilho.
   * *Sintaxe:* **WHILE** `[Estado]`, **WHEN** `[Gatilho]`, o `[Nome do Sistema]` deve `[Resposta Observável]`.

### 3. Esquema Obrigatório de Metadados de Rastreabilidade
A issue deve conter o bloco final de metadados no formato de tabela Markdown:

| Atributo ISO 29148 | Valor Registrado |
| :--- | :--- |
| **Identificador Único (ID)** | `REQ-BUG-YYYYMMDD-XXX` |
| **Tipo de Objeto** | Defeito de Execução / Requisito Não-Funcional (Confiabilidade) |
| **Fonte (Source)** | Pipeline de Observabilidade / Log Ingestion Agent |
| **Prioridade (Priority)** | `P0-Crítico` / `P1-Alto` / `P2-Médio` / `P3-Baixo` |
| **Método de Verificação** | Teste Automatizado de Integração / Suíte SAST |
| **Status de Homologação** | Rascunho Validado / Pronto para Abertura |

## Decision Rules

- **SE** todos os requisitos de ISO 29148 forem satisfeitos **E** os critérios de aceite seguirem estritamente a sintaxe EARS **E** a tabela de metadados estiver completa:
  * **Ação:** Retornar `STATUS: APPROVED`. Anexar o parecer descritivo de conformidade.
- **SE** houver qualquer violação de singularidade, ambiguidade, ausência de racional ou desvio da sintaxe EARS:
  * **Ação:** Retornar `STATUS: REJECTED`. Fornecer a lista estruturada de não-conformidades e instruções diretas ao `Issue Refiner` para correção.
```

---

## 5. Especificação dos Demais Agentes do Pipeline

Para garantir a coesão da infraestrutura multiagente, apresenta-se o detalhamento funcional de cada um dos demais agentes da cadeia:

### 5.1 Logger Receiver & Bug Analyzer Agent (`.github/agents/bug-analyzer.md`)
* **Função:** Capturar os *payloads* de log brutos do ambiente, extrair o *stack trace*, identificar o componente atingido e classificar o erro em termos de severidade.
* **Filtro de Exclusão:** Descarta requisições HTTP 404 de varredura web, *warnings* de depreciação de pacotes e alterações deliberadas de *feature flags*.

### 5.2 Issue Drafter Agent (`.github/agents/issue-drafter.md`)
* **Função:** Traduzir os dados estruturados pelo `Bug Analyzer` em um primeiro rascunho de *issue*.
* **Diretriz:** Preencher as seções de Descrição do Problema, Passos para Reprodução, Comportamento Observado vs. Esperado e Anexo do Log Sanitizado.

### 5.3 Issue Refiner Agent (`.github/agents/issue-refiner.md`)
* **Função:** Atuar em resposta a um retorno de `STATUS: REJECTED` emitido pelo `Issue Reviewer`.
* **Mecanismo:** Reescreve as frases ambíguas, converte os critérios de aceitação não-conformes para as palavras-chave EARS (**WHEN**, **WHILE**, **IF...THEN**) e adiciona os metadados faltantes.

### 5.4 Issue Creator Agent (GitHub MCP) (`.github/agents/issue-creator-mcp.md`)
* **Função:** Receber a *issue* aprovada com `STATUS: APPROVED` e invocar a ferramenta `github.create_issue` do protocolo MCP.
* **Parâmetros da Chamada MCP:**
  * `owner`: `edsonnascimentoc`
  * `repo`: `Engenharia-de-Software`
  * `title`: `[BUG-AUTO] <Identificador EARS do Erro>`
  * `body`: Conteúdo Markdown validado.
  * `labels`: `["bug", "automated-triage", "iso-29148-compliant"]`

### 5.5 Notification Agent (Discord MCP) (`.github/agents/notification-discord-mcp.md`)
* **Função:** Após a confirmação da abertura da *issue* no GitHub, o agente invoca o servidor MCP do Discord para publicar um embed no canal da equipe.
* **Formato da Mensagem:** Embed em cor vermelha (se P0/P1) com o título da *issue*, número do REQ, severidade, resumo em sintaxe EARS e botão de acesso direto ao repositório.

---

## 6. Exemplo Prático de Fluxo End-to-End

Abaixo ilustra-se a execução real do fluxo multiagente diante de uma falha de conexão de banco de dados durante um pico de acessos.

### Step 1: Entrada de Log de Exceção Capturado (Logger Receiver / Bug Analyzer)
```json
{
  "timestamp": "2026-11-16T15:48:12Z",
  "level": "FATAL",
  "service": "PaymentGatewayService",
  "exception": "Npgsql.NpgsqlException: Timeout during connection acquisition",
  "stack_trace": "at Npgsql.ConnectorSource.Get(...) in /src/Npgsql/ConnectorSource.cs:line 124",
  "active_connections": 100,
  "max_pool_size": 100
}
```

### Step 2: Rascunho Inicial Rejeitado pelo `Issue Reviewer` (Exemplo de Rejeição)
O `Issue Drafter` gerou um rascunho informando: *"O serviço de pagamento está lento e caindo quando tem muita gente acessando ao mesmo tempo."*

**Parecer do `Issue Reviewer`:**
```markdown
STATUS: REJECTED
MOTIVO DA REJEIÇÃO:
1. ISO 29148 Ambiguidade: Termos "lento" e "muita gente" são subjetivos e não quantificáveis.
2. Violação EARS: O critério de aceite não utiliza o padrão EARS formal.
3. Metadados Faltantes: Ausência do Método de Verificação e Racional de Negócio.
```

### Step 3: Versão Refinada pelo `Issue Refiner` e Aprovada (`STATUS: APPROVED`)

Após a correção efetuada pelo `Issue Refiner`, o documento atinge a seguinte especificação final:

```markdown
# [BUG-AUTO] Estouro de Pool de Conexões no PaymentGatewayService

## 1. Descrição da Anomalia
Durante picos de concorrência que atingem a capacidade máxima do pool de conexões (100 conexões ativas), o serviço `PaymentGatewayService` lança a exceção `NpgsqlException`, resultando na interrupção do processamento de transações.

## 2. Racional e Impacto no Negócio
A falha no aquisição de conexões impede a finalização do *checkout*, gerando perda imediata de receita e degradação da confiabilidade da aplicação.

## 3. Critérios de Aceite Sintáticos (EARS)

- **Comportamento Indesejado (IF...THEN):**
  **IF** a taxa de conexões ativas do banco de dados atingir 90% da capacidade máxima do pool, **THEN** o `PaymentGatewayService` deve enfileirar as novas requisições em um cache distribuído temporário por até 5000 milissegundos antes de lançar exceção.

- **Orientado a Estado (WHILE):**
  **WHILE** a conexão com o banco de dados principal estiver indisponível ou em estado de degradação, o `PaymentGatewayService` deve operar em modo de degradação graciosa, retornando o código HTTP 503 com o cabeçalho `Retry-After: 10`.

## 4. Método de Verificação
- **Tipo de Teste:** Teste de Carga e Estresse Automatizado com k6.
- **Métrica de Aceite:** Submeter o serviço a 150 conexões simultâneas por 3 minutos. O sistema deve manter taxa de erro 0% em requisições perdidas sem exceções não tratadas de *timeout* de driver.

## 5. Metadados de Rastreabilidade (ISO/IEC/IEEE 29148:2018)

| Atributo ISO 29148 | Valor Registrado |
| :--- | :--- |
| **Identificador Único (ID)** | `REQ-BUG-20261116-001` |
| **Tipo de Objeto** | Defeito de Execução (Resiliência / Infraestrutura) |
| **Fonte (Source)** | Pipeline de Observabilidade / Logger Receiver Agent |
| **Prioridade (Priority)** | `P0-Crítico` |
| **Método de Verificação** | Teste Automatizado de Carga (k6) |
| **Status de Homologação** | Aprovado pelo Issue Reviewer Agent |
```

---

## 7. Roteiro de Implantação e Boas Práticas para a Equipe Sênior

1. **Provisionamento de Segredos no GitHub:**
   Configurar nos *Secrets* do repositório os valores para `GH_PAT_AGENT_PIPELINE` (com escopo `repo`), `DISCORD_BOT_TOKEN` e `DISCORD_ENGINEERING_CHANNEL_ID`.
2. **Versionamento dos Prompts dos Agentes:**
   Manter todos os arquivos de instruções contidos em `.github/agents/` sob revisão de código obrigatória (*Code Review*), garantindo que alterações na governança sintática sejam discutidas e aprovadas pela equipe sênior.
3. **Observabilidade e Avaliação de IA (*Evals*):**
   Implementar testes de validação regressiva nos agentes utilizando suítes de teste de prompts para verificar se o agente `Issue Reviewer` mantém a taxa de detecção de não-conformidades acima de 98% perante *inputs* ambíguos.
