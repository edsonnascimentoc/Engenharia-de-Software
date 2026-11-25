# Evidências de verificação ponta a ponta

Registro da verificação do item 9 do plano de governança ALM. As execuções locais
foram feitas em 2026-11-24 no checkout `chore-alm-quality-gate`; a verificação
remota consultou somente a API pública do GitHub.

## Captura reproduzível

A imagem [Execução sintética do auditor](../../media/alm-governance-demo.svg) é
gerada por `python scripts/capture_alm_demo.py`. O script cria uma fixture temporária
com arquivos fictícios, executa `python alm_rtm_auditor.py` nessa fixture e usa a
saída do processo e o relatório recém-gerado. O caminho temporário local é omitido
da imagem. Nenhuma issue, dado pessoal, token ou log de CI é usado.

O auditor passou a gravar o relatório em `Path(tempfile.gettempdir())`, em vez de
exigir o caminho Linux `/workspace/scratch`; assim, a instrução de execução também
funciona no setup Windows documentado.

## Resultados

| Verificação | Evidência observada | Resultado |
| --- | --- | --- |
| Auditor no checkout | `python alm_rtm_auditor.py` concluiu e gerou `alm_rtm_report.md` no diretório temporário do sistema. | Passou |
| Auditor com dados sintéticos | A fixture criada pelo script foi auditada pelo entry point legado; a saída e quatro linhas do relatório são exibidas na imagem. | Passou |
| Links locais e estrutura da RTM | `python -m src.validate_docs` retornou “Links Markdown locais e estrutura da RTM válidos.” | Passou |
| Regras Markdown locais | Verificação equivalente às regras habilitadas `MD040`/`MD047` em 48 arquivos Markdown. O executável `markdownlint-cli2` não está instalado localmente. | Passou para as regras configuradas |
| Testes Python e cobertura local | `.venv\Scripts\python.exe -m coverage run --branch -m unittest discover -s tests/python -v`: 3 testes passaram. `coverage report --show-missing`: 29% total; o auditor está com 0% de cobertura. | Passou, cobertura baixa |
| Testes Node | `node --test tests/node/*.test.js`: 8 testes passaram, nenhum falhou. | Passou |
| Ruff e formatação | `ruff check src tests/python` e `ruff format --check src tests/python`, no `.venv` do projeto. | Passou após corrigir import/formatação identificados nesta verificação |
| Quality gate no GitHub | [Execução #17](https://github.com/edsonnascimentoc/Engenharia-de-Software/actions/runs/45506394020): jobs `tests`, `lint` e `docs-and-traceability` concluídos com sucesso; os passos de Markdownlint e validação de links/RTM também passaram. | Passou no commit consultado |
| Setup | README requer Python ≥3.12 e Node ≥20. Ambiente local observado: Python 3.13.3 no `.venv` e Node 22.15.0; execução remota do gate configura Python 3.12 e Node 20. | Passou |
| Badge de CI | O caminho do badge no README corresponde a `.github/workflows/alm-ci-quality-gate.yml`, e a execução do workflow acima está verde. | Confirmado |
| Badge de licença | `LICENSE` declara GPL-3.0 e o badge do README declara GPL v3. | Confirmado |
| Badge de cobertura | O link do Codecov está configurado, mas a execução remota consultada não tem passo de upload de cobertura; a tentativa de abrir o badge/serviço não foi acessível nesta verificação. O relatório de 29% foi produzido localmente. | Não confirmado no serviço |
| Checklist de release | `docs/alm/artefatos/checklist-release.md` foi conferido: release, tag e publicação continuam ações manuais; os itens permanecem por marcar até uma release real. | Conferido; publicação não aplicável |

## Checklist de Definition of Done

- [x] Há uma captura vinculada à execução real do auditor, com fixture sintética e
  sem dados de usuários.
- [x] Comandos de setup, testes, lint, links/RTM e nomes dos jobs foram comparados
  às instruções locais e ao workflow.
- [x] Badge de CI, badge de licença, checklist de release e limitações foram
  conferidos e registrados.
- [x] A licença existente GPL-3 foi preservada.
- [ ] Badge/relatório de cobertura publicado e confirmado no Codecov.
- [ ] Regras administrativas de proteção de `main` e checks obrigatórios; não
  verificáveis por este checkout e não alteradas.

## Limitações

- O resultado do GitHub é da execução remota associada ao commit consultado; ele
  não executa alterações ainda não enviadas deste checkout. A imagem local demonstra
  o auditor isoladamente, não uma execução de CI nem proteção de branch.
- Não há `actionlint` nem parser YAML instalado no ambiente local. A execução remota
  confirma a versão de workflow existente no commit consultado, não alterações locais
  posteriores.
- O relatório de cobertura local mostra que `src/alm_rtm_auditor.py` não tem testes
  de cobertura; 29% não deve ser interpretado como meta de qualidade atingida.
- O serviço Codecov e a renderização externa do badge não puderam ser confirmados.
- Permissões, regras de branch e exigência administrativa de checks não são
  inferidas a partir de uma execução verde.
