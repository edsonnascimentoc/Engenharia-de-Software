# Como contribuir

Este repositório mantém documentação e automação do framework ALM. Antes de
abrir uma demanda, consulte a [RTM](docs/alm/artefatos/matriz-rastreabilidade.md)
e classifique-a como requisito de produto, regra do framework ou exemplo
documental. Não crie IDs de produto para exemplos.

## Manutenção das instruções de IA

Edite as instruções compartilhadas em [`.github/copilot-instructions.md`](.github/copilot-instructions.md), a fonte canônica. Não edite `.cursorrules` manualmente: gere a cópia compatível com Cursor executando:

```bash
python scripts/sync_ai_instructions.py
python scripts/sync_ai_instructions.py --check
```

A verificação também é executada pelo quality gate.

## Fluxo de contribuição

1. **Issue:** abra uma issue usando o template de [bug](.github/ISSUE_TEMPLATE/bug_report.md),
   [funcionalidade](.github/ISSUE_TEMPLATE/feature_request.md) ou requisito. Registre
   problema/objetivo, contexto, resultado esperado e critérios verificáveis.
   Requisitos de produto devem ter ID `REQ-...` aprovado e critérios de aceite.
2. **Branch:** crie uma branch a partir de `main`, por exemplo
   `fix/123-validacao-rtm` ou `feat/123-novo-template`. Para manutenção sem issue,
   use `docs/...`, `chore/...` ou `ci/...` com nome descritivo.
3. **Commit:** use Conventional Commits: `tipo(escopo): descrição` ou
   `tipo(escopo-REQ-ID): descrição`. Inclua `#123` no corpo ou assunto quando
   houver issue aplicável. Exemplos: `fix(rtm-REQ-42): rejeita requisito sem critério`
   e `docs(alm): esclarece fluxo de contribuição`. Tipos usuais: `feat`, `fix`,
   `docs`, `test`, `refactor`, `arch`, `ci` e `chore`. Consulte o
   [padrão detalhado](docs/alm/artefatos/padrao-commits.md).
4. **PR:** abra PR para `main`, use o [template](.github/PULL_REQUEST_TEMPLATE.md),
   vincule a issue com `Closes #123`/`Fixes #123` e informe o requisito `REQ-...`
   quando a mudança implementar ou corrigir comportamento requerido. Explique a
   motivação, escopo, critérios atendidos e evidências. Mudanças de documentação,
   manutenção e automação sem requisito de produto podem declarar a exceção no PR.
5. **Teste:** execute os comandos aplicáveis listados no README. Descreva no PR
   os testes executados e seus resultados. Para documentação, valide links e
   estrutura da RTM quando aplicável.
6. **Release:** mantenedores seguem o [checklist de release](docs/alm/artefatos/checklist-release.md),
   consolidam mudanças no changelog e versionam conforme SemVer. A tag anotada usa
   `vMAJOR.MINOR.PATCH` (por exemplo, `v1.2.3`) e as notas são preparadas a partir
   do changelog e dos PRs incluídos. A criação da tag e a publicação da release são
   ações manuais; nenhum workflow publica automaticamente.

## Critérios verificáveis

- Issues de bug descrevem passos para reproduzir, resultado atual e esperado,
  ambiente e ao menos um resultado observável para confirmar a correção.
- Issues de funcionalidade descrevem objetivo/escopo e critérios de aceite
  observáveis, incluindo casos relevantes de sucesso e erro.
- PRs identificam issue/requisito aplicável ou justificam por que a mudança de
  documentação/manutenção não precisa desses vínculos; incluem testes e evidência
  compatíveis com o escopo.
- CI exige referência a issue e requisito para mudanças de comportamento em
  `src/` ou `tests/`. Para documentação, manutenção de dependências e automação,
  a referência pode ser omitida quando não fizer sentido.
