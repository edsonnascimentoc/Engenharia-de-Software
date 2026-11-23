# Guia de Padronização de Commits Rastreáveis (ALM & Conventional Commits)

## 1. Objetivo e Escopo
Este documento estabelece o padrão obrigatório de mensagens de commit do Git para o repositório Engenharia-de-Software. A padronização garante a rastreabilidade bidirecional contínua entre os requisitos funcionais/não-funcionais (especificados sob a norma ISO/IEC/IEEE 29148 e EARS), as issues registradas e os artefatos de código ou teste alterados.

## 2. Estrutura da Mensagem de Commit
<tipo>(<escopo>-<ID_REQUISITO>): <descrição sucinta no imperativo>

## 3. Tipos Permitidos
- feat: Nova funcionalidade vinculada a um requisito.
- fix: Correção de bug ou anomalia.
- docs: Alteração exclusiva em documentação.
- test: Adição de testes automatizados.
- refactor: Refatoração de código sem alterar funcionalidade.
- arch: Registro de decisão arquitetural (ADR).
- ci: Alterações nos fluxos de automação.
- chore: Tarefas de build ou dependências.
