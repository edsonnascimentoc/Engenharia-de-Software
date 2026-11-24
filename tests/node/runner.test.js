const assert = require('node:assert/strict');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { spawnSync } = require('node:child_process');
const test = require('node:test');

const runnerPath = path.resolve(__dirname, '../../.github/agents/runner.js');
const { parseArgs, reviewIssue } = require('../../.github/agents/runner.js');

const validIssueBody = `
## Contexto e racional
O acesso ao sistema deve ser validado para cada usuário.

## Critérios de Aceite em Sintaxe EARS
- QUANDO o usuário envia credenciais válidas, O sistema DEVE conceder acesso.

## Método de Verificação
- Método de Verificação: Teste automatizado de integração.

## Metadados de Rastreabilidade
| Identificador Único (ID) | REQ-AUTH-001 |
`;

test('approves a structurally complete EARS issue with a valid requirement ID', () => {
  const result = reviewIssue(42, validIssueBody);

  assert.equal(result.issue_number, 42);
  assert.equal(result.approved, true);
  assert.equal(result.ears_syntax_valid, true);
  assert.deepEqual(result.required_actions, []);
});

test('rejects an issue without EARS acceptance criteria', () => {
  const result = reviewIssue(42, `
## Contexto
Descrever o contexto.
## Critérios de Aceite
Precisa funcionar bem.
## Método de Verificação
Teste automatizado.
## Metadados
ID: REQ-AUTH-001
`);

  assert.equal(result.approved, false);
  assert.equal(result.ears_syntax_valid, false);
  assert.ok(result.required_actions.some((action) => action.includes('EARS')));
});

test('rejects an empty issue body with actionable feedback', () => {
  const result = reviewIssue(42, '  \n  ');

  assert.equal(result.approved, false);
  assert.ok(result.required_actions.length > 0);
});

test('rejects malformed requirement IDs', () => {
  const result = reviewIssue(42, validIssueBody.replace('REQ-AUTH-001', 'REQ-'));

  assert.equal(result.approved, false);
  assert.equal(result.iso_checks.hasMetadataID, false);
});

test('rejects invalid GitHub issue numbers before reviewing content', () => {
  for (const issueNumber of [undefined, '', 'abc', '0', 0, -1, 1.5]) {
    assert.throws(
      () => reviewIssue(issueNumber, validIssueBody),
      { code: 'INVALID_ISSUE_NUMBER' },
    );
  }
});

test('accepts only the simplified input/output file CLI', () => {
  assert.deepEqual(
    parseArgs(['--input-file', 'input.json', '--result-file', 'result.json']),
    { inputFile: 'input.json', resultFile: 'result.json' },
  );
  assert.throws(() => parseArgs(['--issue-id', '42']), {
    code: 'INVALID_ARGUMENTS',
  });
});

test('writes a rejected review result and exits non-zero for the workflow gate', (context) => {
  const tempDirectory = fs.mkdtempSync(path.join(os.tmpdir(), 'issue-review-'));
  context.after(() => fs.rmSync(tempDirectory, { recursive: true, force: true }));

  const inputFile = path.join(tempDirectory, 'input.json');
  const resultFile = path.join(tempDirectory, 'result.json');
  fs.writeFileSync(inputFile, JSON.stringify({ issue_number: 42, body: '' }));

  const execution = spawnSync(process.execPath, [
    runnerPath,
    '--input-file', inputFile,
    '--result-file', resultFile,
  ], { encoding: 'utf8' });

  assert.equal(execution.status, 1);
  assert.match(execution.stderr, /requer refinamento/);
  const result = JSON.parse(fs.readFileSync(resultFile, 'utf8'));
  assert.equal(result.issue_number, 42);
  assert.equal(result.approved, false);
});

test('does not write a review result when the issue number is invalid', (context) => {
  const tempDirectory = fs.mkdtempSync(path.join(os.tmpdir(), 'issue-review-'));
  context.after(() => fs.rmSync(tempDirectory, { recursive: true, force: true }));

  const inputFile = path.join(tempDirectory, 'input.json');
  const resultFile = path.join(tempDirectory, 'result.json');
  fs.writeFileSync(inputFile, JSON.stringify({ issue_number: 'abc', body: validIssueBody }));

  const execution = spawnSync(process.execPath, [
    runnerPath,
    '--input-file', inputFile,
    '--result-file', resultFile,
  ], { encoding: 'utf8' });

  assert.equal(execution.status, 1);
  assert.match(execution.stderr, /inteiro positivo/);
  assert.equal(fs.existsSync(resultFile), false);
});
