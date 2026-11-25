# Matriz de Rastreabilidade (RTM)

## Objetivo e escopo

Esta RTM mantém separadas as demandas de uma aplicação de negócio das regras
normativas do próprio framework/repositório e dos exemplos usados na
documentação. O baseline foi levantado em 2026-11-24; o inventário e as fontes
estão em [Baseline do Repositório e Referências ALM](../governanca/baseline-rastreabilidade.md).

Não atribua IDs artificiais nem trate um exemplo como funcionalidade existente.
Uma linha sem evidência de implementação ou teste permanece pendente.

## Como manter

1. Classifique o registro antes de atribuir ID: `Produto`, `Regra do framework`
   ou `Exemplo documental`.
2. Para requisitos de produto, use issue canônica, ID aprovado e critério
   verificável antes de vincular código/testes.
3. Para regras do framework, cite a seção normativa e os controles locais que
   as implementam (workflow, script ou configuração).
4. Registre links e caminhos relativos com precisão; use `Não verificado` quando
   a evidência não puder ser acessada e `Não aplicável` apenas com justificativa.
5. Atualize status após validação, release, substituição ou descontinuação.

## A. Candidatos a requisitos de produto

O repositório inspecionado não contém uma aplicação de login/autenticação. Os
issues abaixo são reais, mas não foram convertidos em requisitos aprovados nem
associados a código/testes deste repositório.

| Classe | ID aprovado | Origem | Descrição/critério verificável | Código | Teste | PR/commit/release | Status e próxima ação |
|---|---|---|---|---|---|---|---|
| Produto — candidato | Não atribuído | [Issue #4](https://github.com/edsonnascimentoc/Engenharia-de-Software/issues/4) | “O login não está funcionando às vezes quando digita a senha.” Critério e escopo de produto ainda não especificados. | Não identificado neste repositório | Não identificado | Não vinculado | Aberta, `status: needs-refinement`; triagem para confirmar sistema/projeto, formalizar ID e critérios ou fechar como issue fora de escopo. |
| Produto — candidato | Não atribuído | [Issue #5](https://github.com/edsonnascimentoc/Engenharia-de-Software/issues/5) | “O login falha.” Critério e escopo de produto ainda não especificados. | Não identificado neste repositório | Não identificado | Não vinculado | Aberta, `status: needs-refinement`; triagem para confirmar sistema/projeto, formalizar ID e critérios ou fechar como issue fora de escopo. |

## B. Regras normativas do framework/repositório

Fonte normativa: `docs/security/padrao-governanca-seguranca-sbom-cve.md`. A coluna
de evidência resume os controles encontrados no baseline; `Parcial` significa
que o documento requer mais do que foi comprovado no repositório. Não significa
conformidade organizacional nem validação em produção.

| Classe | ID | Controle requerido | Evidência local | Verificação automatizada | Status no baseline |
|---|---|---|---|---|---|
| Regra do framework | RF-SEC-01 | Auditoria local de dependências e instruções padronizadas. | Template de PR cita `npm audit`, `pip-audit` e `dotnet list package`; não foi identificado comando comum configurado. | Nenhum teste/CI local encontrado para esse requisito. | Parcial — instrução existe, execução padronizada não confirmada. |
| Regra do framework | RF-SEC-02 | SAST a cada PR em branches protegidas. | Há upload SARIF no workflow de segurança, mas não há etapa local identificada executando CodeQL/SAST. | Não comprovada. | Pendente — o upload SARIF não prova que SAST foi executado. |
| Regra do framework | RF-SEC-03 | Gerar SBOM em build de release/empacotamento. | `security-governance-pipeline.yml` gera SPDX em push/PR/agenda; não há workflow de release identificado. | Execução configurada no workflow; release não verificada. | Parcial — SBOM em CI, release não mapeada. |
| Regra do framework | RF-SEC-04 | Dependabot ativo para alertas/PRs de dependência. | `.github/dependabot.yml` monitora GitHub Actions semanalmente; PRs remotos #6–#10 são atualizações de Actions. | Dependabot demonstrado por configuração e PRs. | Implementado para GitHub Actions; outros ecossistemas não declarados. |
| Regra do framework | RF-SEC-05 | Exportar scans de segurança em SARIF. | Workflow gera SARIF do Trivy e tenta upload via `codeql-action/upload-sarif`. | Configuração presente; execução recente de segurança foi reportada como sucesso na coleta. | Implementado no fluxo de segurança; cobertura de outras ferramentas não comprovada. |
| Regra do framework | RNF-SEC-01 | Bloquear artefato/release com CVE Critical/High sem mitigação. | Trivy usa severidades `CRITICAL,HIGH` e `exit-code: 1`; não há release/deploy do produto identificado. | Falha do job configurada; promoção de release não existente/não verificada. | Parcial — bloqueio no scan, promoção de release não mapeada. |
| Regra do framework | RNF-SEC-02 | Assinar imagens de produção e incorporar SBOM. | Não foi encontrada configuração de build/assinatura de imagem. | Não aplicável a artefato de imagem identificado; confirmar escopo do padrão. | Não implementado no repositório atual. |
| Regra do framework | RNF-SEC-03 | Definir limite de duração e cache/filtro incremental na CI. | Workflows inspecionados não documentam SLO de duração nem cache correspondente. | Não comprovada. | Pendente. |
| Regra do framework | RNF-SEC-04 | Usar imagens Docker enxutas e multi-stage em produção. | Não foi encontrado Dockerfile/build de imagem do produto. | Não aplicável a imagem não identificada; confirmar escopo do padrão. | Não implementado/não aplicável ao conteúdo atual. |
| Regra do framework | REST-SEC-01 | Usar SPDX ou CycloneDX para SBOM. | Workflow configura `format: spdx-json`. | Configuração presente; validação de artefato em execução deve ser mantida na CI. | Implementado na configuração local. |
| Regra do framework | REST-SEC-02 | Retornar exit code não zero para vulnerabilidade bloqueante. | Trivy configura `exit-code: '1'` para Critical/High. | Configuração presente. | Implementado na configuração local. |
| Regra do framework | REST-SEC-03 | Proibir push direto em branches protegidas e exigir PR/revisão/checks. | API do GitHub retorna `main` como protegida; configuração detalhada (revisões/checks) não foi acessível. | Workflows de PR existem; enforcement completo não verificado. | Parcial/não verificado — consultar regras de branch no GitHub. |
| Regra do framework | RN-SEC-01 | Documentar exceções de CVE com justificativa, ADR e expiração. | `.trivyignore` contém instrução e exemplo; não há exceções ativas registradas no arquivo inspecionado. | Nenhum validador de expiração encontrado. | Parcial — regra descrita, enforcement não comprovado. |
| Regra do framework | RN-SEC-02 | Agrupar atualizações Dependabot semanal/quinzenalmente. | Dependabot está semanal, sem configuração `groups` observada. | Nenhuma validação de agrupamento encontrada. | Parcial — frequência presente, agrupamento ausente. |
| Regra do framework | RN-SEC-03 | Validar licenças das dependências por SBOM. | Geração SBOM presente; etapa de política/licença não identificada. | Não comprovada. | Pendente. |
| Regra do framework | RF-ALM-TRACE-01 | Classificar demandas; ligar requisito a issue, mudança, teste, PR e release quando aplicável; permitir justificativa para manutenção/documentação sem ID. | [Política de contribuição](../../../CONTRIBUTING.md), [templates de issue](../../../.github/ISSUE_TEMPLATE/) e [template de PR](../../../.github/PULL_REQUEST_TEMPLATE.md). | `scripts/validate_pr_traceability.py` no job `docs-and-traceability` do workflow `alm-ci-quality-gate.yml`; verifica referências em PRs `feat`/`fix` que alterem `src/` ou `tests/`. | Implementado no repositório; aprovação do vínculo semântico permanece responsabilidade de revisão. |

## C. Exemplos documentais excluídos do baseline ativo

| Classe | Identificador mencionado | Fonte | Motivo da exclusão |
|---|---|---|---|
| Exemplo documental | `REQ-BUG-20261116-001` | `mcp-agent-architecture.md`, exemplo de fluxo para `PaymentGatewayService` | Está dentro de um exemplo de demonstração. Não há evidência de que o serviço exista neste repositório. |
| Referência legada | `#ALM-GOV-001`, `#ALM-GOV-002` | `docs/orientacao/pr-docs-alm-framework.md` e descrições históricas de PR | Chaves não numéricas não foram reconciliadas com issues canônicas; mantê-las como referências pendentes, sem fingir vínculo. |

## Critérios de completude

- Requisito de produto aprovado tem origem, ID único, critério observável, código
  e teste de aceite ou uma justificativa explícita para evidência ainda pendente.
- Regra do framework aponta para a fonte normativa e para o controle local que a
  implementa; documento normativo sozinho não prova execução.
- Todo teste de aceite aponta para pelo menos um requisito ou regra aplicável.
- PR/commit e release são registrados quando existirem; campos ausentes ficam
  como pendentes, não são preenchidos por inferência.
- Exemplos de sistemas, IDs e issues ficam fora da lista ativa até serem
  confirmados como demanda real.
