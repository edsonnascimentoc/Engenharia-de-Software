# Template Padrão de Pull Request (PR)

> **Instruções:** Copie este conteúdo para `.github/PULL_REQUEST_TEMPLATE.md` (em repositórios GitHub) ou para a raiz do repositório `.azuredevops/pull_request_template.md` (no Azure DevOps).

---

## 📌 Descrição da Mudança
*Forneça um resumo claro e conciso sobre o motivo e o escopo desta alteração. Explique QUAL problema está sendo resolvido ou QUAL funcionalidade está sendo entregue.*

- **O que foi feito:** 
- **Motivação / Contexto:** 

---

## 🔗 Vínculo com Histórias / Issues (Rastreabilidade ALM)
- Refers to: `#<NUMERO_DA_ISSUE>` ou `[US-<ID_DO_CARDO>](link-para-alm)`
- Tipo de Tarefa: 
  - [ ] `feat`: Nova funcionalidade
  - [ ] `fix`: Correção de bug / defeito
  - [ ] `refactor`: Refatoração de código sem alteração funcional
  - [ ] `docs`: Atualização de documentação
  - [ ] `style`: Formatação, ponto e vírgula, sem alteração de lógica
  - [ ] `test`: Adição ou correção de testes
  - [ ] `chore`: Atualização de dependências, build ou infraestrutura
  - [ ] `breaking change`: Alteração que quebra compatibilidade com versões anteriores

---

## 🛡️ Checklist de Qualidade e Segurança (Definition of Done - DoD)

### 1. Testes & Cobertura
- [ ] Testes unitários foram criados/atualizados e estão passando localmente.
- [ ] Cobertura de código mantida ou elevada acima do limiar do projeto (mínimo de 80%).
- [ ] Testes de integração/contrato de API validados (quando aplicável).

### 2. Segurança e LGPD (OWASP Top 10)
- [ ] Nenhum segredo, chave privada, senha ou token foi commitado no código.
- [ ] Entradas de dados sanitizadas e validadas contra Injection (SQL/NoSQL/Code).
- [ ] Dados PII (Informações Pessoais de Alunos/Usuários) anonimizados/descaracterizados no envio para APIs externas.
- [ ] Permissões e controle de acesso RBAC aplicados nas rotas modificadas.

### 3. Banco de Dados e Migrações (DDL/DML)
- [ ] Contém alteração no esquema do banco de dados?
- [ ] Script de migração (Flyway/Liquibase) criado com suporte a rollback.
- [ ] Modelagem de dados mantida em 3FN ou justificada por ADR.

### 4. Documentação & Contratos
- [ ] Documentação de APIs (Swagger/OpenAPI 3.0) atualizada.
- [ ] `README.md` ou variáveis de ambiente (`.env.example`) atualizados.
- [ ] Registrado Architectural Decision Record (ADR) caso tenha havido mudança de arquitetura.

---

## 🧪 Como Testar esta Alteração
*Descreva o passo a passo prático para que o revisor/QA possa validar esta mudança em ambiente local ou staging.*

1. Executar a rota/fluxo: `...`
2. Payload / Parâmetros de Entrada:
   ```json
   {
     "exemplo": "valor"
   }
   ```
3. Comportamento Esperado: `...`

---

## 📸 Evidências de Teste (Screenshots / Logs)
*Anexe imagens de telas modificadas, relatórios de testes (Jest/JUnit) ou logs relevantes que comprovem o funcionamento correto.*

| Teste | Evidência / Captura |
| :--- | :--- |
| **Testes Unitários/Cobertura** | *(Anexar imagem do terminal/report)* |
| **Fluxo Funcional / UI** | *(Anexar imagem da tela ou GIF)* |

---

## 👤 Atribuições e Revisão
- **Autor(es):** @desenvolvedor
- **Revisores Obrigatórios (CODEOWNERS):** @tech-lead, @arquiteto-software
