# Plano de Implementação — Governança ALM do Repositório

**Objetivo:** Tornar o repositório de framework ALM documentado, rastreável, testável, seguro e pronto para contribuições e releases, atendendo aos requisitos inegociáveis solicitados.

**Abordagem:** Evoluir a automação de governança já existente, em incrementos pequenos e verificáveis. Preservar configurações válidas, consolidar verificações duplicadas, criar testes para as ferramentas existentes e documentar o ciclo de contribuição e release. O repositório não é uma aplicação web; a demonstração visual será um GIF ou captura real do fluxo do auditor/CI, sem inventar telas de produto.

**Escopo de referência:** Diagnóstico técnico produzido na conversa e checkout atual. O arquivo `diagnostico-governanca-alm.md` não foi localizado no repositório.

## Restrições globais

- Não remover ou substituir configurações sem confirmar sua função e cobertura atual.
- Manter a licença GNU GPL versão 3 existente; validar texto e escopo antes de qualquer alteração legal.
- Não expor tokens, segredos, PII, logs privados ou conteúdo de issues nas demonstrações.
- Proteger `main` com checks obrigatórios após estabilizar e nomear os checks; mudanças em regras do GitHub são configurações administrativas fora deste plano de arquivos.
- Não publicar releases ou ativar deploy de produto automaticamente: o repositório não contém uma aplicação implantável identificada.
- Cobertura só pode ser divulgada como badge depois que o relatório de cobertura for produzido por CI.

## Estrutura alvo

```text
src/
  alm_rtm_auditor.py
  agents/runner.js
tests/
  python/
  node/
docs/
  alm/artefatos/matriz-rastreabilidade.md
  media/alm-governance-demo.gif
  superpowers/plans/2026-11-23-governanca-alm.md
scripts/
.github/
  ISSUE_TEMPLATE/
  workflows/
```

Manter o comando legado `python alm_rtm_auditor.py` por meio de um wrapper fino na raiz, ou documentar e migrar todas as referências no mesmo PR. Atualizar o caminho do runner em workflow e README se ele for movido.

## Plano de trabalho

| # | Prioridade | Entrega | Estimativa | Dependências | Critério de aceite |
|---|---|---|---:|---|---|
| 1 | P0 | Inventário, baseline e mapa de rastreabilidade | 0,5 dia | — | Branch, workflows, scripts, licença e referências GitHub são registrados; a RTM diferencia requisito de produto de regra do framework; nada é sobrescrito sem comparação. |
| 2 | P0 | Testes e validação real da automação de issues | 1–2 dias | 1 | `runner.js` recebe corpo e ID da issue de forma definida; processa os argumentos/documento de regras ou a interface é simplificada; testes cobrem aceite, rejeição, corpo vazio e ID inválido; workflow falha com erro e só aplica labels existentes/verificadas. |
| 3 | P0 | Quality Gate real e CI consolidada | 1–2 dias | 2 | Um workflow de CI executa testes Python e Node, Ruff/format check, markdownlint e validação de RTM/links; removidos os `echo` usados como falsos checks; PR e push para `main` executam o mesmo gate requerido. Falha em qualquer verificação retorna status não zero. |
| 4 | P1 | Estrutura de código e ferramentas de estilo | 1 dia | 2 | Código de produção e testes ficam em `src/` e `tests/`; `.editorconfig`, `pyproject.toml` (Ruff/pytest/coverage) e configuração JS/Markdown estão versionados; wrapper legado ou migração de referências evita quebrar usos existentes. |
| 5 | P1 | Política de rastreabilidade e contribuição | 1 dia | 1, 3 | RTM existente fica ligada no índice; templates cobrem bug, funcionalidade e PR com critérios verificáveis; `CONTRIBUTING.md` define issue → branch → commit Conventional Commits com ID quando aplicável → PR → teste → release; CI valida vínculo a issue e requisito sem exigir ID para mudanças de manutenção/documentação quando não fizer sentido. |
| 6 | P1 | Segurança e convivência | 0,5–1 dia | 1, 3 | `SECURITY.md` define canal privado e escopo de reporte; `CODE_OF_CONDUCT.md` adota Contributor Covenant com versão e contato do responsável; `.gitignore` inclui `.env`, ambientes virtuais, dependências, caches e arquivos de SO; Dependabot atual continua habilitado e é verificado, sem duplicá-lo. |
| 7 | P2 | Vitrine documental e licença | 1 dia | 3, 4, 5, 6 | README apresenta nome, problema resolvido, badges reais de CI/cobertura/licença, pré-requisitos, instalação, exemplos, navegação, GIF/captura demonstrativa e limitações; `CHANGELOG.md` segue Keep a Changelog e SemVer; LICENSE GPL-3 é verificada, sem troca inadvertida. |
| 8 | P2 | Histórico, versão, release e metadados GitHub | 0,5–1 dia | 5, 7 | Documentar padrão de commits, tags `vMAJOR.MINOR.PATCH` e release notes; preparar checklist de release sem publicar automaticamente; preencher descrição curta e topics pertinentes; registrar demo pública apenas se existir. Validar labels/milestones antes de propor ajustes. |
| 9 | P2 | Evidências e verificação de ponta a ponta | 0,5–1 dia | 2–8 | Capturar GIF/captura real do auditor ou de uma execução de CI com dados sintéticos; validar links locais, workflows, instruções de setup, badges e checklist de DoD; registrar resultados e limitações. |

## Detalhamento das entregas

### 1. Baseline e arquitetura de teste

- Mapear chamadas a `alm_rtm_auditor.py`, `.github/agents/runner.js` e workflows antes de mover arquivos.
- Identificar dependências efetivamente usadas e estabelecer comandos locais únicos para Python, Node e Markdown.
- Inventariar issues, labels, milestones, branch rules e releases via GitHub; marcar indisponível quando o acesso não permitir verificação.
- Revisar a matriz RTM existente para que registre requisitos reais e links de evidência, sem converter conteúdo do framework em requisitos artificiais.

### 2. Auditor e issue reviewer

- Corrigir a interface do runner e a transmissão do corpo da issue sem interpolação insegura de conteúdo em shell.
- Separar validação pura de EARS/metadados da chamada de rede do workflow, permitindo teste local determinístico.
- Testes unitários: requisito válido, falta de ID, falta de critério verificável, texto vazio, markdown com múltiplos parágrafos e issue sem corpo.
- Garantir que falhas de API/JSON não sejam interpretadas como aprovação nem comentadas como sucesso.

### 3. CI e qualidade

- Manter o pipeline de segurança/SBOM existente como fluxo próprio, corrigindo permissões/condições se necessário.
- Consolidar os dois workflows de Markdown/ALM depois de reproduzir e compreender as falhas atuais.
- Definir jobs nomeados estavelmente: `tests`, `lint`, `docs-and-traceability`; usar esses nomes para branch protection.
- Retirar `continue-on-error` dos controles que devem bloquear merge; exceções devem ser explícitas, justificadas e expiradas.
- Validar o formato de título de PR e o vínculo issue/requisito por regra executável, com exceções adequadas para docs/chore.

### 4. Documentação e operação do projeto

- README terá instalação reproduzível, comandos de teste/lint/auditoria, saída de exemplo sanitizada e links para governança.
- Badge de cobertura aponta para relatório/serviço realmente configurado; não exibir percentuais inventados.
- O GIF demonstrará uma execução local ou CI do auditor, já que não existe interface de usuário do produto.
- `CHANGELOG.md` inicia com `Unreleased`; a primeira release só recebe versão após critérios de release satisfeitos.
- Preservar GPL-3. Qualquer mudança de licença exige decisão dos mantenedores e revisão jurídica fora desta implementação técnica.

## Configuração administrativa no GitHub

Após o CI passar continuamente na branch de integração, administrador deverá:

1. Exigir checks estáveis de CI em `main`.
2. Exigir PR, revisão mínima e resolução das conversas, se compatível com o modelo de colaboração.
3. Confirmar que Dependabot pode abrir PRs com labels configuradas e definir política de merge/revisão.
4. Confirmar canal privado de reporte no `SECURITY.md` e permissões para issues/discussions.
5. Preencher a descrição e topics do repositório e associar uma demo somente se publicada.

Essas configurações não são alteradas por commits de arquivos e dependem de permissão administrativa no GitHub.

## Definição de pronto

- Todos os itens obrigatórios dos cinco grupos solicitados têm arquivo ou configuração verificável e instrução de uso.
- Testes, linters, validações de documentação e build do pacote/tooling passam localmente e em PR.
- CI bloqueia merges por falha real; branch protection aponta para os nomes corretos dos checks.
- README, badges, links, instalação, demo e licença foram conferidos; a licença atual foi preservada.
- Matriz de rastreabilidade liga requisito → issue → código → teste → PR/commit → release quando aplicável.
- Não há segredos no diff, arquivos de ambiente rastreados, checks fictícios ou exceções sem responsável e validade.
- Changelog e tags permitem identificar a versão liberada e reproduzir as notas de lançamento.

## Riscos e decisões de escopo

- **Sem aplicação de produto:** cobertura refere-se aos utilitários de governança; não usar o limiar de 80% como alegação até definir métrica e escopo.
- **Mudança de caminhos:** mover scripts pode quebrar comandos/documentos externos; manter wrapper ou fazer migração atômica de referências.
- **Licença GPL-3:** README deve refletir a licença existente, não substituí-la pelo exemplo MIT/Apache.
- **Settings fora do Git:** status checks, topics, labels e configurações de segurança precisam de confirmação em GitHub e de acesso administrativo.
- **Actions externas:** Dependabot atualiza versões; pinning de actions por SHA e política de atualização precisam ser decididos sem interromper atualizações automáticas.
