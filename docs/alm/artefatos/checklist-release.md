# Checklist de release

Este checklist orienta releases manuais. Não há publicação automática de release,
tag ou deploy neste repositório.

## Antes da release

- [ ] Definir a versão SemVer após revisar as mudanças: MAJOR para incompatibilidade,
  MINOR para funcionalidade compatível e PATCH para correção compatível.
- [ ] Revisar os commits desde a última tag (ou todo o histórico, na primeira
  release), confirmar que seguem `docs/alm/artefatos/padrao-commits.md` e agrupar
  as mudanças por impacto para decidir a versão. Commits `ci`, `refactor`, `docs`
  e `chore` também devem ser avaliados; o tipo do commit, isoladamente, não define
  a versão.
- [ ] Confirmar que a branch de release está atualizada e que CI, testes, lint e
  validação documental passaram no commit candidato.
- [ ] Revisar `CHANGELOG.md`: mover as entradas relevantes de `Unreleased` para
  `## [MAJOR.MINOR.PATCH] - AAAA-MM-DD`, corrigir links e remover itens que não
  fazem parte da versão. Conferir que cada mudança incluída aparece uma vez e que
  cada entrada publicada corresponde a um commit/PR da versão.
- [ ] Preparar release notes em Markdown, resumindo alterações visíveis, correções,
  incompatibilidades, migração necessária e créditos. Não inclua segredos, PII ou
  logs privados.
- [ ] Revisar o diff e confirmar licença, documentação, exemplos e artefatos da
  versão. Não alegar cobertura ou demo que ainda não esteja publicada e verificada.

## Aprovação e publicação manual

- [ ] Obter revisão/aprovação dos mantenedores para o commit, versão e notas.
- [ ] Criar e enviar uma tag Git anotada `vMAJOR.MINOR.PATCH` apontando para o
  commit aprovado (por exemplo, `git tag -a v1.2.3 -m "Release v1.2.3"`).
- [ ] Criar a release no GitHub a partir dessa tag e publicar as notas revisadas.
- [ ] Conferir que a tag local e `origin` apontam para o mesmo commit aprovado,
  que a release do GitHub usa essa tag e que versão, data, notas e compare link
  coincidem com a seção publicada em `CHANGELOG.md`.
- [ ] Conferir a página da release, tag, changelog e links após a publicação.
- [ ] Abrir uma PR separada para iniciar a próxima seção `Unreleased` se ela tiver
  sido removida durante a preparação.

## Depois da release

- [ ] Registrar a versão e a URL da release na matriz de rastreabilidade quando
  houver requisitos ou mudanças rastreadas aplicáveis.
- [ ] Comunicar a release pelos canais do projeto, se houver um canal definido.
- [ ] Anotar problemas conhecidos e decisões de correção para a próxima versão.
