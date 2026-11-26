# Política de compatibilidade

## Escopo e prazo

Esta política cobre os caminhos de compatibilidade mantidos para migração das
implementações para `src/`:

| Caminho legado | Caminho oficial | Migração |
|---|---|---|
| `alm_rtm_auditor.py` | `src/alm_rtm_auditor.py` | Use `python -m src.alm_rtm_auditor`. |
| `.github/agents/runner.js` | `src/agents/runner.js` | Atualize workflows e chamadas para apontar ao caminho oficial. |

Os wrappers permanecem disponíveis até **30/06/2027**, inclusive. Até essa data,
recebem somente correções necessárias para preservar compatibilidade e segurança.
Novas funcionalidades devem ser implementadas no caminho oficial.

## Revisão e encerramento

Os mantenedores revisarão a necessidade dos wrappers em junho de 2027. A remoção
será feita em uma mudança anunciada no changelog e na documentação, após confirmar
que workflows e referências mantidos neste repositório já usam os caminhos oficiais.
Consumidores externos devem migrar antes de 30/06/2027.

Uma extensão exige decisão explícita dos mantenedores registrada no changelog e
nesta política, com justificativa e uma nova data final. Sem essa decisão, o prazo
acima permanece válido e os wrappers podem ser removidos na primeira versão após
30/06/2027.

## Orientação para consumidores

- Auditor ALM: substitua `python alm_rtm_auditor.py` por
  `python -m src.alm_rtm_auditor`.
- Validador de issues: substitua `.github/agents/runner.js` por
  `src/agents/runner.js` nos comandos e workflows que você mantém.
- Não dependa de detalhes internos dos wrappers; eles existem apenas para
  encaminhar a execução às implementações em `src/`.