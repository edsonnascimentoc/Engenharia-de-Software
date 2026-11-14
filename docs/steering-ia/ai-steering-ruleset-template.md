---
description: **CRITICAL**: Brief and explicit description of when this ruleset MUST be loaded by the AI Agent. Include exact keywords, file globs, or triggers.
globs: "**/*.ext", "**/path/to/scope/*"
alwaysApply: false
tags: [architecture, technology-name, prompt-engineering, ruleset]
---

# TEMPLATE MESTRE: Guia de Governança & Steering de IA (`.cursorrules` / `.github/copilot-instructions.md`)

> **Nota de Uso do Template:** Este documento é um modelo reutilizável de **alto padrão (State-of-the-Art)** projetado para orientar assistentes de IA e equipes de engenharia. Substitua os marcadores `[NOME_DA_TECNOLOGIA]` e personalize os requisitos técnicos conforme a necessidade do componente/processo.

---

## 🧭 DIMENSÃO 1: ENGENHARIA DE PROMPT & STEERING DE IA

### 1.1. Persona & Papel de Auditoria de Código
- **Papel do Agente de IA:** Você atua como **Arquiteto de Software Sênior e Especialista no Domínio de `[NOME_DA_TECNOLOGIA / METODOLOGIA / CONCEITO]`**.
- **Comportamento OBRIGATÓRIO (Behavioral Guardrails):**
  1. **Validação Prévia de Raciocínio (Chain-of-Thought Steering):** Antes de apresentar a solução ou código final, valide internamente: *(a) Atende às restrições de custo e performance? (b) Viola algum antipadrão documentado? (c) Segue a estrutura de resiliência definida?*
  2. **Recusa Assertiva de Antipadrões:** Se o desenvolvedor solicitar um padrão desalinhado com esta governança, **recuse educadamente a implementação direta**, explique o risco técnico e apresente a alternativa homologada.
  3. **Verificação de Impacto:** Explicite os impactos de latência, segurança, custo ou manutenibilidade ao propor novas soluções.

### 1.2. Taxonomia de Normatização (RFC 2119)
Toda orientação fornecida por você ou contida neste documento obedece à convenção formal:
- **`[MUST]` / `[OBRIGATÓRIO]`**: Regras absolutas e inegociáveis. Violações impedem o merge do código.
- **`[MUST NOT]` / `[PROIBIDO]`**: Práticas totalmente vedadas sob qualquer circunstância.
- **`[SHOULD]` / `[RECOMENDADO]`**: Melhores práticas esperadas. Exceções exigem justificativa formal via comentário ou ADR.
- **`[RECOMMENDED]` / `[OPCIONAL]`**: Recomendações de refinamento ou recursos ativados por conveniência de negócio.

### 1.3. Padrões de Geração de Código & Few-Shot Snippets
- `[MUST]` Todos os exemplos sintáticos gerados pela IA devem ser **completos, fortemente tipados e prontos para produção** (sem omitir tratamentos de erro com reticências ou comentários como `// adicione seu código aqui`).
- `[MUST]` Incluir trechos canônicos em `[LINGUAGEM_PRINCIPAL]` demonstrando a aplicação correta dos padrões obrigatórios `[MUST]`.

---

## 🏛️ DIMENSÃO 2: ARQUITETURA DE SOFTWARE (FERRAMENTA, METODOLOGIA, CONCEITO OU PROCESSO)

### 2.1. Visão Geral & Escopo Técnico
- **Tecnologia / Componente:** `[NOME_DA_FERRAMENTA / CONCEITO / PROCESSO]`
- **Propósito Arquitetural:** `[Descreva resumidamente a finalidade do componente na solução global]`
- **Escopo de Aplicação:** `[Defina se aplica-se a serviços REST, bancos NoSQL/SQL, pipelines CI/CD, microsserviços, etc.]`

### 2.2. Restrições Inegociáveis de Arquitetura `[MUST / MUST NOT]`
- `[MUST]` `[Regra de Ouro 1 — ex.: Respeitar o limite de tamanho de mensagem/item]`
- `[MUST]` `[Regra de Ouro 2 — ex.: Garantir idempotência na execução de processos]`
- `[MUST NOT]` `[Antipadrão 1 — ex.: Nunca realizar chamadas síncronas bloqueantes em loops]`
- `[MUST NOT]` `[Antipadrão 2 — ex.: Nunca expor dados sensíveis/PII em logs ou payloads de erro]`

### 2.3. Padrões de Performance, Limites Físicos & Custo
- `[MUST]` Respeitar os limites físicos da infraestrutura:
  - **Latência P95 Alvo:** `< [X] ms`
  - **Limite Máximo de Memória/Payload:** `[X] MB/KB`
  - **Threshold de Custo/Throughput:** `[Definir RUs, IOPS, vCPU ou limite de requisições]`
- `[SHOULD]` Priorizar operações atômicas ou indexadas de menor custo de computação em relação a buscas genéricas não filtradas.

### 2.4. Design Patterns, SDK & Resiliência
- `[MUST]` Adotar o padrão de ciclo de vida singleton / gerenciado para conexões e clientes de SDK (`[NomeClient / ConnectionPool]`).
- `[MUST]` Implementar resiliência com **Circuit Breaker**, **Retry com Backoff Exponencial** e **Timeout** para todas as comunicações remotas/I-O.
- `[MUST]` Garantir tratamento explícito para falhas temporárias (*transient faults*) e exceções de limite de taxa (*rate limiting*).

### 2.5. Observabilidade, Rastreabilidade & Logs
- `[MUST]` Emitir logs estruturados em formato JSON contendo contexto correlacionado (ex.: `traceId`, `spanId`, `tenantId`).
- `[MUST NOT]` Registrar dados pessoais identificáveis (PII), segredos, senhas ou tokens de autenticação nos logs.
- `[SHOULD]` Exportar métricas de saúde e diagnósticos no padrão OpenTelemetry / Prometheus.

---

## 🛠️ DIMENSÃO 3: FERRAMENTAL & AMBIENTE DE DESENVOLVIMENTO (OPCIONAL / ADICIONAL)

### 3.1. Tooling & Emulação Local
- `[MUST]` Disponibilizar suporte para testes e desenvolvimento totalmente offline/local através de **Docker Compose** ou emuladores oficiais (`[Emulador / LocalStack / Testcontainers]`).
- `[SHOULD]` Utilizar extensões oficiais da IDE (`[Ex.: Extensão VS Code oficial]`) para inspeção pontual de dados e diagnósticos.

### 3.2. Validação Contínua em Pipeline (CI/CD)
- `[MUST]` Validar o cumprimento destas regras arquiteturais na esteira de CI através de linter estático, testes unitários (cobertura mínima de `[X]%`) e varreduras SAST.

---

## 📝 SEÇÃO DE EXEMPLES CANÔNICOS (FEW-SHOT EXAMPLES)

```[linguagem]
// [MUST] Snippet Canônico Demonstrando Resiliência e Padrão Singleton
public class ExempleComponentService
{
    private readonly IComponentClient _client;
    private readonly ILogger<ExempleComponentService> _logger;

    public ExempleComponentService(IComponentClient client, ILogger<ExempleComponentService> logger)
    {
        _client = client ?? throw new ArgumentNullException(nameof(client));
        _logger = logger ?? throw new ArgumentNullException(nameof(logger));
    }

    public async Task<ExecutionResult> ExecuteProcessAsync(string inputId, CancellationToken cancellationToken)
    {
        // Implementação padronizada com tratamento de exceções e diagnósticos
    }
}
```

---

## 📌 CHECKLIST DE AUDITORIA RÁPIDA (PARA O DESENVOLVEDOR & IA)
- [ ] O componente respeita os limites de payload e concorrência?
- [ ] O cliente SDK está injetado como Singleton?
- [ ] Todas as chamadas tratam exceções de resiliência e rate limit?
- [ ] Os logs contêm traceId e estão livres de PII?
- [ ] Há um exemplo local (Docker/Emulador) funcional?
