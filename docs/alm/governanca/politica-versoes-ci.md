# Política de versões e dependências de CI

**Status:** adotada
**Aplicação:** workflows GitHub Actions e ferramentas Python de desenvolvimento

## Política

- Referencie Actions de terceiros pelo SHA completo de 40 caracteres e mantenha
  ao lado um comentário com a versão/tag humana correspondente. Não execute Actions
  por tags mutáveis como `v4`, `main` ou `master`.
- Use o Dependabot semanal para propor atualizações de Actions e dependências Python.
  Revise o SHA e a versão associados, as notas da versão e o impacto no workflow antes
  de integrar a atualização.
- Fixe as ferramentas Python de desenvolvimento/CI em versões exatas no
  `requirements-dev.txt`. Alterações de versão são deliberadas e devem ser verificadas
  no CI.
- `python-version: "3.12"` e `node-version: "20"` selecionam linhas de compatibilidade
  das linguagens. A política não fixa patches de runtimes instalados pelo runner.
- SemVer (`vMAJOR.MINOR.PATCH`) em releases do repositório continua descrevendo as
  versões do próprio produto; não é política para referenciar Actions.

## Aplicação inicial

- Todas as referências externas `uses:` dos três workflows foram convertidas de
  tags ou branches para SHAs completos, com comentário da versão associada.
- `requirements-dev.txt` já fixa Ruff em `0.17.6` e Coverage em `7.10.6`; não foi
  necessário alterar os pins existentes.
- O Dependabot já atualizava GitHub Actions semanalmente. Foi habilitado também o
  ecossistema `pip`, com a mesma frequência e os rótulos de dependência/manutenção.

## Manutenção

Analise e integre as atualizações propostas pelo Dependabot regularmente. Se uma
atualização não puder ser integrada, registre o motivo e o prazo para revisão. Não
retorne a uma tag móvel para contornar falha de compatibilidade; atualize a versão
fixada após revisar o release.
