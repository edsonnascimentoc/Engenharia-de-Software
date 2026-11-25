# Padrão de commits rastreáveis

Use o formato Conventional Commits:

```text
<tipo>(<escopo>): <descrição no imperativo>
<corpo opcional com contexto e referência à issue>
```

Use tipo e escopo em minúsculas, descrição curta no imperativo e sem ponto final.
Separe assunto e corpo com uma linha em branco; no corpo explique contexto e
impacto quando não forem óbvios. Para mudanças incompatíveis, sinalize `!` no
assunto (`feat(api)!: ...`) e explique `BREAKING CHANGE:` no rodapé. Um commit deve
representar uma alteração coerente e revisável.

Quando houver requisito aplicável, inclua seu ID no escopo, por exemplo
`feat(alm-REQ-42): valida critérios de aceite`. Inclua também `Closes #123` ou
`Refs #123` no corpo para ligar o commit à issue. Para manutenção, documentação
ou automação sem demanda aplicável, o ID e a issue podem ser omitidos.

Tipos recomendados: `feat` (funcionalidade), `fix` (correção), `docs`
(documentação), `test` (testes), `refactor` (estrutura sem mudança de
comportamento), `arch` (decisão arquitetural), `ci` (automação) e `chore`
(manutenção/dependências).

Use `feat` para capacidade nova e `fix` para corrigir comportamento. Alterações
incompatíveis em qualquer tipo incrementam a versão MAJOR; funcionalidades
compatíveis incrementam MINOR; correções compatíveis incrementam PATCH. A versão
de release segue `vMAJOR.MINOR.PATCH`, sem prefixos ou sufixos adicionais na tag
(exemplos: `v1.0.0`, `v1.1.0`, `v1.1.1`). Não crie tag para cada merge: a tag é
criada pelo mantenedor após concluir o checklist de release.

## Release notes

Use o `CHANGELOG.md` como fonte e organize as notas para usuários em **Added**,
**Changed**, **Deprecated**, **Removed**, **Fixed** e **Security**, omitindo
seções vazias. Resuma impacto e migração necessária, quando houver; agrupe PRs
relacionados e credite contribuidores quando apropriado. A versão publicada deve
ligar ao compare entre a tag anterior e a nova. Para a primeira versão, indique
que não há tag anterior. Nunca declare uma versão lançada antes da criação manual
da tag e da release correspondente. O roteiro está em
[Checklist de release](checklist-release.md).

O título do PR segue o mesmo formato. PRs `feat` e `fix` que alterem `src/` ou
`tests/` devem conter referência a issue e requisito; o quality gate verifica os
vínculos. Veja o [guia de contribuição](../../../CONTRIBUTING.md).
