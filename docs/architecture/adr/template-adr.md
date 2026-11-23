
---

### 2. Template de Registro de Decisão Arquitetural (ADR)
**Arquivo de destino:** `docs/architecture/adr/template-adr.md`

```markdown
# [ADR-000] <Título Curto e Declarativo da Decisão Arquitetural>

| Atributo Metadado | Valor Registrado |
| :--- | :--- |
| **Status** | `Proposto` \| `Aceito` \| `Substituído por ADR-XXX` \| `Rejeitado` |
| **Data da Decisão** | YYYY-MM-DD |
| **Autores / Decisores** | <Nome do Arquiteto / Equipe Técnica> |
| **Requisitos Relacionados** | `REQ-XXX`, `REQ-YYY` (ISO/IEC/IEEE 29148) |
| **Impacto em Criticidade** | `Alta` \| `Média` \| `Baixa` (Matriz de Criticidade ALM) |

---

## 1. Contexto e Declaração do Problema (Context & Problem Statement)
<!-- Descreva a motivação técnica ou de negócio. Qual é o problema arquitetural enfrentado? Quais são as restrições e Requisitos Não-Funcionais (RNF) que pressionam esta escolha? -->

---

## 2. Sintaxe de Decisão (Y-Statement Format)

> **No contexto de** `<ambiente/requisito/domínio>`,  
> **frente ao desafio de** `<problema ou RNF específico>`,  
> **decidimos por** `<opção escolhida>`,  
> **para obter** `<benefício de qualidade/arquitetura esperado>`,  
> **aceitando** `<compromisso / trade-off / consequência negativa irremediável>`.

---

## 3. Opções Consideradas (Considered Options)

* **Opção 1:** `<Nome da Opção 1 (ex.: Banco Relacional PostgreSQL)>`
* **Opção 2:** `<Nome da Opção 2 (ex.: Banco Colunar Cassandra)>`
* **Opção 3:** `<Nome da Opção 3 (ex.: Document Store MongoDB)>`

---

## 4. Avaliação Comparativa dos Prós e Contras

### Opção 1: `<Nome da Opção 1>`
* 🟢 **Pró:** <Vantagem técnica / alinhamento com RNF>
* 🟢 **Pró:** <Vantagem operabilidade / equipe>
* 🔴 **Contra:** <Desvantagem / custo / complexidade>

### Opção 2: `<Nome da Opção 2>`
* 🟢 **Pró:** <Vantagem técnica>
* 🔴 **Contra:** <Desvantagem técnica>
* 🔴 **Contra:** <Desacoplamento do domínio>

---

## 5. Consequências e Matriz de Riscos da Decisão

### Consequências Positivas:
- `<Impacto positivo na escalabilidade, segurança ou manutenibilidade>`

### Consequências Negativas & Mitigações:
- `<Trade-off aceito e ação mitigatória correspondente no ciclo de vida>`

---

## 6. Plano de Verificação e Auditoria (DoD Arquitetural)

- [ ] **Métrica de Aceite:** `<Como esta decisão será validada em tempo de execução ou build>`
- [ ] **Método de Verificação:** `<Teste de Carga / Análise Estática / Code Review>`
- [ ] **Data de Revisão:** `<Data futura para reavaliação da eficácia da arquitetura>`
