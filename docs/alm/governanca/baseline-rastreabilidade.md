# Baseline do Repositório e Referências ALM

**Data da coleta:** 2026-11-24
**Repositório:** [edsonnascimentoc/Engenharia-de-Software](https://github.com/edsonnascimentoc/Engenharia-de-Software)
**Branch local inspecionada:** `main`
**Método:** inventário do checkout local, histórico Git e leitura dos metadados públicos do GitHub. Itens sem acesso suficiente estão marcados como não verificados.

## Identidade e escopo observado

O conteúdo versionado é majoritariamente documentação e automação de governança ALM. Há um auditor Python e um runner Node.js para validação de issues, mas não foi identificado código de uma aplicação de negócio que implemente login ou autenticação. Por isso, os issues de login abaixo são candidatos a requisitos/problemas de produto e aguardam triagem de escopo; não são associados a código inexistente.

## Inventário local

| Área | Arquivos/pastas observados | Papel e observação |
|---|---|---|
| Workflows | `.github/workflows/alm-ci-quality-gate.yml`; `mcp-agent-validation.yml`; `pr-governance-check.yml`; `security-governance-pipeline.yml`; `validar-governança-e-qualidade.yml` | Cinco fluxos de CI/segurança/governança; existem verificações duplicadas de Markdown e etapas que apenas imprimem mensagens. |
| Agentes | `src/agents/runner.js` (`.github/agents/runner.js` é wrapper compatível); `.github/agents/mcp.json`; `prompts/issue-drafter-prompt.txt`; `prompts/issue-reviewer-prompt.txt` | Runner de revisão de issues, configuração e prompts. |
| Templates GitHub | `.github/ISSUE_TEMPLATE/requisito-iso29148.md`; `.github/PULL_REQUEST_TEMPLATE.md` | Template de requisito e template principal de PR. |
| Código Python | `src/alm_rtm_auditor.py`; `src/validate_docs.py` (wrappers compatíveis na raiz e em `scripts/`) | Auditoria RTM e validação documental. |
| Scripts operacionais | `bootstrap-security.ps1`; `bootstrap-security.sh`; `scripts/migrate-alm-docs.ps1`; `scripts/migrate-alm-docs.sh` | Bootstrap de segurança e migração documental multiplataforma. |
| Documentação ALM | `docs/alm/` (fundamentação, governança, fases 1–8 e artefatos) | Playbook e padrões de ciclo de vida. A matriz operacional está em `artefatos/matriz-rastreabilidade.md`. |
| Segurança e orientação | `docs/security/`; `docs/orientacao/`; `docs/steering-ia/`; `docs/templates/`; `docs/architecture/adr/` | Políticas, guias, templates e arquitetura. |
| Raiz e configurações | `README.md`; `LICENSE`; `.gitignore`; `.trivyignore`; `.cursorrules`; `.github/dependabot.yml`; `mcp-agent-architecture.md` | README é introdutório; licença é GNU GPL versão 3; `.gitignore` contém apenas `.vs/`; Dependabot monitora GitHub Actions semanalmente. |

## Branches, histórico e versionamento

Branches observadas no GitHub em 2026-11-24:

| Branch | Protegida segundo API do GitHub | Observação |
|---|---:|---|
| `main` | Sim | Branch padrão e branch local atual. O campo `protected` não revela por si só quais revisões e checks são exigidos. |
| `feat/security-governance` | Não | Branch de feature observada. |
| `feature/docs-alm-framework` | Não | Branch de feature observada. |
| `dependabot/github_actions/gitleaks/gitleaks-action-3` | Não | Branch de atualização de dependência. |

Os cinco commits mais recentes no checkout no momento da coleta foram atualizações `chore(deps)` de Actions e `ci: adiciona workflow de governanca e qualidade para markdown`. O histórico recente contém também mensagens rastreáveis como `feat(alm-REQ-CONFIG)` e `arch(adr-REQ-INIT)`. A política de commits está documentada em `docs/alm/artefatos/padrao-commits.md`.

Não foram encontradas tags Git locais nem releases publicadas na consulta ao endpoint de releases do GitHub em 2026-11-24.

## Fluxos GitHub Actions registrados

| Workflow | Disparo/configuração observada | Papel indicado pelo arquivo |
|---|---|---|
| `alm-ci-quality-gate.yml` | push em `main`/`develop`; PR para `main` | Lint de Markdown e etapa declarada de rastreabilidade de commits. Run mais recente consultado: [falha, 2026-11-23](https://github.com/edsonnascimentoc/Engenharia-de-Software/actions/runs/45261573904). |
| `mcp-agent-validation.yml` | issues abertas/editadas e `workflow_dispatch` | Revisão de especificação de issues e comentário/label. Execuções recentes não foram localizadas na primeira página consultada. |
| `pr-governance-check.yml` | PR para `main`/`master`/`develop` | Verificações de steering, título e secrets; parte dos checks é atualmente `echo`. Execução não identificada na página consultada. |
| `security-governance-pipeline.yml` | push, PR e agenda semanal | TruffleHog, geração SBOM SPDX, Trivy e upload SARIF. Run mais recente consultado: [sucesso, 2026-11-23](https://github.com/edsonnascimentoc/Engenharia-de-Software/actions/runs/45261573838). |
| `validar-governança-e-qualidade.yml` | push/PR em `main`/`develop` | Lint de Markdown; sobrepõe parte do workflow ALM. Run mais recente consultado: [falha, 2026-11-23](https://github.com/edsonnascimentoc/Engenharia-de-Software/actions/runs/45261573876). |

Os nomes e gatilhos foram lidos dos arquivos locais. As URLs acima registram os resultados mais recentes da primeira página de execuções consultada (2026-11-24); o estado é volátil e deve ser atualizado ao iniciar cada etapa que dependa dele.

## Referências GitHub e limitações de consulta

Consulta pública do repositório retornou visibilidade pública, branch padrão `main`, não arquivado e branch `main` marcada como protegida.

| Referência | Estado observado | Classificação para a RTM |
|---|---|---|
| [Issue #4 — Falha na autenticação](https://github.com/edsonnascimentoc/Engenharia-de-Software/issues/4) | Aberta; label `status: needs-refinement`; sem milestone. Corpo: “O login não está funcionando às vezes quando digita a senha.” | Candidato a requisito/defeito de produto, aguardando triagem; sem ID aprovado, código ou teste associado neste repositório. |
| [Issue #5 — Falha no login](https://github.com/edsonnascimentoc/Engenharia-de-Software/issues/5) | Aberta; label `status: needs-refinement`; sem milestone. Corpo: “O login falha.” | Candidato a requisito/defeito de produto, aguardando triagem; sem ID aprovado, código ou teste associado neste repositório. |
| PRs #1, #2 e #3 | Fechados e mesclados; descrevem introdução do framework ALM e governança de segurança. | Evidência de mudanças de governança; não são requisitos de produto. |
| PRs #6–#10 | Fechados e mesclados; títulos indicam atualizações de GitHub Actions via Dependabot. | Evidência de manutenção/dependências. |
| Referências `#ALM-GOV-001` e `#ALM-GOV-002` | Aparecem em documentos de PR em `docs/orientacao/`; não correspondem ao formato numérico dos issues reais consultados. | Identificadores internos legados ainda não reconciliados com issue canônica; preservar e reconciliar em etapa própria. |

O endpoint de issues retornou os registros acima. A consulta direta de labels gerais, milestones gerais, projetos e regras detalhadas de proteção não pôde ser confirmada com a conexão disponível. O campo `milestone: null` está confirmado apenas para as issues #4 e #5. Não inferir inexistência global desses recursos.

## Critério de classificação da rastreabilidade

1. **Requisito de produto:** comportamento que uma aplicação de negócio deve oferecer; exige issue de origem aprovada, ID único, critério verificável, código e teste. Se não há aplicação no escopo do repositório, manter como candidato não triado.
2. **Regra do framework:** requisito sobre o próprio processo, documentação, CI/CD, segurança ou manutenção do repositório. Usar IDs normativos da documentação quando existirem e ligar a política a workflow/script e evidência de verificação.
3. **Exemplo documental:** requisito, issue, sistema ou métrica usado para demonstrar um formato. Não incluir como demanda ativa na RTM.

Exemplo: `REQ-BUG-20261116-001` descreve `PaymentGatewayService` dentro de um exemplo de fluxo no `mcp-agent-architecture.md`; classificá-lo como exemplo documental, sem criar item ativo nem supor que esse serviço exista aqui.

## Baseline de rastreabilidade

Detalhamento de IDs de política, implementações, testes e lacunas: [Matriz de Rastreabilidade](../artefatos/matriz-rastreabilidade.md).
