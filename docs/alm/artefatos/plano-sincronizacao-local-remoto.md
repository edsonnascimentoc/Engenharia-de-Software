# Plano de sincronização entre repositórios

## Objetivo

Manter o checkout local e os branches do GitHub consistentes sem sobrescrever
trabalho local, perder commits ou enviar mudanças não revisadas diretamente para
`main`.

## Diagnóstico deste ciclo

- O checkout local está em `chore-alm-quality-gate`, com quatro commits além da
  referência remota local conhecida e quatro arquivos modificados fora do índice.
- O branch remoto `chore-alm-quality-gate` avançou depois da última atualização
  local. O PR #17 aponta para `main`, é reportado como mergeável e aguarda os checks
  obrigatórios.
- O `main` remoto está protegido e requer `tests`, `lint` e
  `docs-and-traceability`.
- `git fetch --prune origin` falhou por indisponibilidade de conexão HTTPS ao
  GitHub. Portanto, as referências Git locais não puderam ser atualizadas neste
  ambiente. Nenhum reset, force push ou descarte de alteração foi executado.

## Procedimento padrão

### 1. Proteger o trabalho local

1. Execute `git status --short --branch` e revise `git diff` e
   `git diff --cached`.
2. Committe arquivos relacionados em commits Conventional Commits ou guarde o
   trabalho com `git stash push -u -m "<motivo>"`; nunca use `reset --hard` ou
   `clean -fd` para resolver divergência sem autorização e backup.
3. Confirme que o diretório de trabalho está limpo antes de trocar ou integrar
   branches.

### 2. Buscar antes de integrar

1. Atualize referências com `git fetch --prune origin`.
2. Compare `git status -sb`, `git log --oneline --left-right HEAD...@{upstream}` e
   `git diff --stat HEAD...@{upstream}` antes de alterar a branch.
3. Atualize `main` somente por fast-forward: `git switch main` seguido de
   `git merge --ff-only origin/main`.
4. Em branch privada ainda não publicada, rebaseie sobre `origin/main`. Em branch
   já publicada/compartilhada, integre `origin/main` por merge para preservar os
   commits que outros consumidores já referenciam. Não reescreva histórico
   compartilhado sem coordenação.

### 3. Resolver conflitos

1. Liste os caminhos em conflito com `git diff --name-only --diff-filter=U`.
2. Revise os dois lados de cada conflito, edite o arquivo final e valide o diff.
3. Continue com `git rebase --continue` ou `git merge --continue`, conforme a
   operação iniciada. Use `git rebase --abort` ou `git merge --abort` se a
   resolução não estiver clara; não force uma resolução automática.
4. Execute os checks do projeto e reveja o histórico após a integração.

### 4. Atualizar o GitHub

1. Publique alterações em branch de trabalho com `git push --dry-run` e depois
   `git push -u origin HEAD` na primeira publicação; use `git push` nas seguintes.
2. Abra ou atualize um PR para `main`, descreva conflitos resolvidos e evidências,
   e aguarde revisão e checks obrigatórios.
3. Não faça push direto em `main`. Não use `--force`; se uma reescrita de branch
   privada for indispensável, coordene-a e use `--force-with-lease` após buscar e
   conferir o SHA remoto esperado.
4. Prefira commits pequenos e claros a automações que escrevam diretamente no
   branch protegido. Um workflow que precise publicar artefatos deve ter
   permissões mínimas, branch/ref explícita e prevenção contra loops de push.

### 5. Confirmar sincronização

Após o push ou merge, faça novo fetch e confirme que a branch local acompanha a
referência remota (`ahead 0, behind 0`), que o PR aponta para o commit esperado e
que os checks estão verdes. Registre qualquer limitação de rede ou aprovação
pendente; não declare a sincronização concluída com base apenas em arquivos iguais.

## Aplicação atual

As configurações locais deste repositório passam a podar referências remotas
obsoletas, exigir fast-forward para `pull`, usar push simples e configurar upstream
automaticamente no primeiro push. O PR #17 continua como o caminho de integração no
remoto. O fetch será repetido quando houver conectividade Git direta para confirmar
a igualdade das referências locais e remotas.
