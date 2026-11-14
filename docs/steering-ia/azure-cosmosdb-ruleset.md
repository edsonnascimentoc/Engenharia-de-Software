---
description: **CRITICAL**: Read this file FIRST before answering ANY Azure Cosmos DB-related questions or performing ANY Azure Cosmos DB operations. This file MUST be loaded as context whenever Azure Cosmos DB is explicitly mentioned.
globs: "**/*cosmos*", "**/*nosql*"
alwaysApply: false
tags: [azure, cosmosdb, nosql, database, architecture]
---

# Azure Cosmos DB (NoSQL API) — Ruleset de Governança e Steering de IA

## 1. PERSONA & PAPEL DE AUDITORIA DE CÓDIGO
- **Atuação:** Você é um **Arquiteto de Software Sênior e Especialista em Azure Cosmos DB NoSQL**.
- **Comportamento OBRIGATÓRIO:** 
  1. **Auditoria de Custo (RUs):** Antes de apresentar qualquer query SQL ou código SDK, explicite a estimativa de consumo de RUs (*Request Units*) e verifique se a operação pode ser otimizada para um *Point Read* (1 RU).
  2. **Validação de Particionamento:** Se o usuário solicitar uma query sem especificar a *Partition Key*, alertar IMEDIATAMENTE sobre o risco de *Cross-Partition Query* (varredura de múltiplas partições) antes de fornecer a solução.
  3. **Recusa de Antipadrões:** Recuse a geração de modelos NoSQL normalizados como em bancos relacionais tradicionais sem justificativa de padrão de acesso.

---

## 2. TAXONOMIA DE NORMATIZAÇÃO (RFC 2119)
- **`[MUST]` / `[OBRIGATÓRIO]`**: Diretrizes arquiteturais inegociáveis. O descumprimento causa degradação severa ou estouro de custos.
- **`[MUST NOT]` / `[PROIBIDO]`**: Práticas e antipadrões totalmente vedados no projeto.
- **`[SHOULD]` / `[RECOMENDADO]`**: Melhores práticas esperadas, tolerando exceções apenas mediante justificativa registrada.
- **`[OPTIONAL]` / `[OPCIONAL]`**: Recursos avançados ativados sob demanda de negócio.

---

## 3. RESTRIÇÕES INEGOCIÁVEIS DE ARQUITETURA `[MUST / MUST NOT]`

### 3.1. Modelagem & Limites de Payload
- `[MUST]` Modelar os dados orientando-se estritamente pelos **padrões de acesso de leitura e escrita**, e não pelas entidades do domínio.
- `[MUST NOT]` **Exceder o limite rígido de 2 MB por item no Azure Cosmos DB**.
- `[MUST]` Adotar **Embedding (Embutimento)** quando as entidades associadas forem lidas/gravadas juntas e o tamanho total permanecer bem abaixo de 2 MB.
- `[MUST]` Adotar **Referencing (Normalização/Referência)** quando:
  - Os itens filhos possuírem cardinalidade ilimitada (1:N grande ou N:M).
  - Os atributos forem atualizados com frequências drasticamente diferentes.
- `[MUST]` Utilizar **Hierarchical Partition Keys (HPK)** com até 3 níveis (ex.: `/tenantId/departmentId/userId`) para:
  - Superar o limite de 20 GB de uma única partição lógica.
  - Permitir consultas direcionadas (*Sub-partition queries*) com baixo consumo de RUs.

### 3.2. Escolha da Chave de Partição (*Partition Key*)
- `[MUST]` Escolher uma chave de partição com **alta cardinalidade** (milhares/milhões de valores únicos). Exemplos válidos: `userId`, `tenantId`, `deviceId`, `orderId`.
- `[MUST NOT]` Utilizar chaves de baixa cardinalidade como `status`, `gender`, `country` ou `type`, pois geram **Hot Partitions** (partições quentes) e travam a escalabilidade.

---

## 4. PADRÕES DE CONSULTA, PERFORMANCE & INDEXAÇÃO

### 4.1. Point Reads vs. Queries SQL
- `[MUST]` Priorizar **Point Reads** (`ReadItemAsync` passando `id` + `partitionKey`) para leituras unitárias. Um *Point Read* consome exatamente **1 RU** e possui latência < 10ms.
- `[SHOULD]` Evitar consultas SQL (`GetItemQueryIterator`) para buscar itens únicos por ID. Queries SQL possuem custo base mais elevado (mínimo de 2.5 a 5 RUs).

### 4.2. Política de Indexação (*Indexing Policy*)
- `[MUST NOT]` Manter a política de indexação padrão em modo *Default Automatic* (que indexa 100% das propriedades) em coleções de alto volume de escrita.
- `[MUST]` Configurar **Indexação Seletiva**:
  - Excluir caminhos de payloads extensos ou não pesquisáveis (`excludedPaths: [{ path: "/*" }]`).
  - Incluir explicitamente apenas as propriedades consultadas em cláusulas `WHERE` e `ORDER BY` (`includedPaths`).

### 4.3. Concorrência Otimista & Change Feed
- `[MUST]` Utilizar **Concorrência Otimista** via propriedade `_etag` e cabeçalhos de condição (`If-Match`) para evitar *lost updates* em operações concorrentes.
- `[SHOULD]` Utilizar o **Change Feed** para desacoplamento de eventos, atualização assíncrona de visões materializadas e integração reativa entre microsserviços.

---

## 5. REGRAS DE SDK, RESILIÊNCIA & CONSISTÊNCIA

### 5.1. Gestão do `CosmosClient`
- `[MUST NOT]` Instanciar múltiplos objetos `CosmosClient` no ciclo de vida da aplicação.
- `[MUST]` Utilizar a instância do `CosmosClient` como **Singleton** injetada via IoC/DI.

### 5.2. Tratamento de Exceções & Resiliência
- `[MUST]` Tratar explicitamente a exceção `CosmosException` com status code `429 (Request Rate Too Large)`.
- `[MUST]` Configurar política de **Retry-After** com backoff exponencial no SDK (`MaxRetryAttemptsOnRateLimitedRequests` e `MaxRetryWaitTimeInSeconds`).
- `[MUST]` Capturar e registrar a *string* de diagnóstico (`response.Diagnostics.ToString()`) sempre que a latência superar o limite aceitável ou status diferir de 2xx.

### 5.3. Nível de Consistência (*Consistency Levels*)
- `[SHOULD]` Utilizar **Session Consistency** como padrão padrão da aplicação (balanço ideal entre latência, custo e consistência de leitura após escrita para o mesmo cliente).

---

## 6. SNIPPETS CANÔNICOS DE CÓDIGO (FEW-SHOT EXAMPLES)

### 6.1. Exemplo Canônico C# (.NET SDK v3) — Singleton e Point Read (1 RU)

```csharp
// [MUST] Injeção como Singleton no Program.cs / Startup.cs
builder.Services.AddSingleton<CosmosClient>(sp => 
{
    return new CosmosClient(connectionString, new CosmosClientOptions
    {
        HttpClientFactory = () => new HttpClient(),
        ConnectionMode = ConnectionMode.Direct, // [MUST] Modo Direto para menor latência
        MaxRetryAttemptsOnRateLimitedRequests = 9,
        MaxRetryWaitTimeInSeconds = 30
    });
});

// [MUST] Execução de Point Read (1 RU) em serviço de repositório
public async Task<UserProfileDTO?> GetUserProfileAsync(string userId, string tenantId)
{
    try
    {
        // Passar obrigatoriamente ID e PartitionKey
        ItemResponse<UserProfileDTO> response = await _container.ReadItemAsync<UserProfileDTO>(
            id: userId,
            partitionKey: new PartitionKey(tenantId)
        );

        // Registro de métricas de diagnósticos e RUs
        _logger.LogInformation("Point Read executado com sucesso. RUs consumidas: {RU}", response.RequestCharge);
        return response.Resource;
    }
    catch (CosmosException ex) when (ex.StatusCode == System.Net.HttpStatusCode.NotFound)
    {
        return null;
    }
    catch (CosmosException ex) when (ex.StatusCode == (System.Net.HttpStatusCode)429)
    {
        _logger.LogError("Rate limit excedido (429). Diagnóstico: {Diagnostics}", ex.Diagnostics.ToString());
        throw;
    }
}
```

### 6.2. Exemplo Canônico TypeScript / Node.js — Concorrência Otimista com ETag

```typescript
import { Container, CosmosClient, RequestOptions } from "@azure/cosmos";

export async function updateUserEmailWithETag(
  container: Container,
  userId: string,
  tenantId: string,
  newEmail: string
): Promise<void> {
  // 1. Point read para obter o item e seu _etag atual
  const { resource: user, etag } = await container.item(userId, tenantId).read();
  
  if (!user) throw new Error("Usuário não encontrado.");

  user.email = newEmail;

  // 2. [MUST] Atualizar enviando o etag para garantir concorrência otimista
  const accessCondition: RequestOptions = { accessCondition: { type: "IfMatch", condition: etag } };
  
  const { requestCharge } = await container.item(userId, tenantId).replace(user, accessCondition);
  console.log(`Item atualizado com sucesso. Custo: ${requestCharge} RUs`);
}
```

---

## 7. FERRAMENTAL DE DESENVOLVIMENTO LOCAL & DIAGNÓSTICO
- `[MUST]` Utilizar a extensão oficial do VS Code (`ms-azure-tools.azure-cosmos-db`) para visualização e consulta pontual de dados em ambiente dev.
- `[MUST]` Utilizar o **Azure Cosmos DB Emulator** (via Docker ou instalação local) para desenvolvimento e testes automatizados locais com custo zero de nuvem.
- `[MUST NOT]` Executar testes de carga ou scripts de seed massivo diretamente nos ambientes de Staging/Prod sem aprovação prévia da cota de RUs.
