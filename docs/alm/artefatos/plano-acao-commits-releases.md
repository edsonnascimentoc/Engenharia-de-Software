# Plano de ação: commits, changelog e releases

## Objetivo

Manter o histórico Conventional Commits útil para revisão e garantir que cada
release publicada tenha a mesma versão, conteúdo e commit no changelog, na tag
local/remota e nas notas do GitHub. Releases continuam manuais e dependem de
aprovação dos mantenedores.

## Diagnóstico

- `CONTRIBUTING.md` e `padrao-commits.md` já definem Conventional Commits e SemVer.
- O histórico recente contém mensagens convencionais como `ci(alm): ...` e
  `refactor(alm): ...`; esses tipos também precisam ser avaliados na classificação
  da release, sem inferir o incremento SemVer apenas pelo prefixo.
- O changelog local e o remoto consultado têm apenas a seção `Unreleased`. Não há
  tag local visível e o acesso Git direto ao remoto não estava disponível durante
  este diagnóstico. Nenhuma versão ou release será presumida ou criada com base
  nesse estado.

## Execução

| Etapa | Ação | Evidência de conclusão |
| --- | --- | --- |
| 1. Preparar mudanças | Manter commits coerentes no formato documentado; usar escopo e referência de issue/requisito quando aplicáveis. | Títulos de commits e PRs revisáveis e compatíveis com o padrão. |
| 2. Fechar escopo | No início de uma release, comparar todos os commits desde a última tag; na primeira release, revisar o histórico completo. Classificar mudanças por impacto, incluindo `ci`, `refactor`, `docs` e `chore`. | Versão SemVer proposta e lista de PRs/commits incluídos. |
| 3. Atualizar changelog | Revisar `Unreleased`, remover itens fora do escopo e publicar uma seção datada com links para a tag anterior e a nova; manter `Unreleased` disponível para o ciclo seguinte. | Cada mudança aprovada aparece uma vez na seção da versão. |
| 4. Revisar e aprovar | Validar CI, testes, lint, documentos, notas de release, migração e commit candidato; obter aprovação dos mantenedores. | Commit candidato e notas aprovados antes da publicação. |
| 5. Publicar manualmente | Criar tag anotada `vMAJOR.MINOR.PATCH` no commit aprovado, enviar a tag e criar a release GitHub usando-a. | Tag local/remota e release apontam para o commit aprovado. |
| 6. Conferir e registrar | Comparar versão, data, notas, changelog e URLs; registrar URL/versionamento na RTM quando aplicável. | Checklist concluído e referências pós-release acessíveis. |

## Critérios de aceite

- O checklist de release exige auditoria do histórico desde a última tag e
  comparação explícita entre changelog, tags e release do GitHub.
- Nenhuma tag é criada antes da aprovação manual do commit, da versão e das notas.
- Uma release publicada corresponde a uma única seção datada do changelog e à
  mesma tag anotada no remoto.
- A próxima seção `Unreleased` fica preparada para receber mudanças posteriores.
- O plano e suas alterações são versionados no repositório e encaminhados ao
  remoto por branch/PR, respeitando o fluxo normal de revisão do projeto.

## Aplicação neste ciclo

O checklist foi atualizado para tornar obrigatória a auditoria e a conferência de
sincronização. Como não há uma versão aprovada nem evidência local de tags, este
ciclo não cria tag ou release. A alteração do checklist e este plano devem ser
mantidos em `Unreleased` até serem revisados e publicados conforme o processo.
