#!/usr/bin/env node
'use strict';

const fs = require('node:fs');

const REQUIREMENT_ID = /\b(?:REQ|RF|RNF)-[A-Z0-9]+(?:-[A-Z0-9]+)*\b/i;
const METADATA_ID = /(?:\bID\b|Identificador\s+Único(?:\s*\(ID\))?)\s*\**\s*(?::|\|)\s*\|?\s*`?((?:REQ|RF|RNF)-[A-Z0-9]+(?:-[A-Z0-9]+)*)\b/i;

function runnerError(message, code) {
  const error = new Error(message);
  error.code = code;
  return error;
}

function normalizeIssueNumber(value) {
  const text = typeof value === 'number' ? String(value) : value;
  if (typeof text !== 'string' || !/^[1-9]\d*$/.test(text)) {
    throw runnerError('O número da issue deve ser um inteiro positivo.', 'INVALID_ISSUE_NUMBER');
  }

  const issueNumber = Number(text);
  if (!Number.isSafeInteger(issueNumber)) {
    throw runnerError('O número da issue está fora do intervalo permitido.', 'INVALID_ISSUE_NUMBER');
  }
  return issueNumber;
}

function extractSection(body, headingPattern) {
  const lines = body.split(/\r?\n/);
  const start = lines.findIndex((line) => headingPattern.test(line));
  if (start === -1) return '';

  const section = [];
  for (let index = start + 1; index < lines.length; index += 1) {
    if (/^\s{0,3}#{1,6}\s+/.test(lines[index])) break;
    section.push(lines[index]);
  }
  return section.join('\n');
}

function hasMeaningfulContent(section) {
  return section.split(/\r?\n/).some((line) => {
    const content = line
      .replace(/^\s*[-*+]\s*/, '')
      .replace(/[|*_`]/g, '')
      .trim();
    return content.length > 0 && !/^(?:<[^>]+>|[-—]|tbd|n\/a|descrever(?: aqui)?|preencher(?: aqui)?)$/i.test(content);
  });
}

function isEarsStatement(line) {
  const statement = line
    .trim()
    .replace(/^[-*+]\s*/, '')
    .replace(/^\*\*([^*]+)\*\*\s*/, '$1 ')
    .replace(/^Critério\s+\d+\s*:\s*/i, '')
    .replace(/[`*_]/g, '')
    .trim();

  return /^(?:QUANDO|ENQUANTO|ONDE)\s+.+,\s*O\s+.+\s+DEVE\s+.+$/iu.test(statement)
    || /^SE\s+.+,\s*ENTÃO\s+O\s+.+\s+DEVE\s+.+$/iu.test(statement)
    || /^O\s+.+\s+DEVE\s+.+$/iu.test(statement)
    || /^[\p{L}\p{N}][^\n]{1,80}\s+DEVE\s+.+$/iu.test(statement);
}

function hasVerificationMethod(body) {
  const match = body.match(/Método\s+de\s+Verificação\s*\**\s*(?::|\|)\s*\|?\s*([^|\r\n]+)/iu);
  if (!match) return false;

  const value = match[1].replace(/[*_`]/g, '').trim();
  return value.length > 0
    && !/^(?:<[^>]+>|[-—]|tbd|n\/a|teste automatizado\s*\/\s*inspeção)$/iu.test(value);
}

function reviewIssue(issueNumberValue, issueBodyValue) {
  const issueNumber = normalizeIssueNumber(issueNumberValue);
  if (issueBodyValue !== undefined && issueBodyValue !== null && typeof issueBodyValue !== 'string') {
    throw runnerError('O corpo da issue deve ser texto.', 'INVALID_ISSUE_BODY');
  }

  const issueBody = issueBodyValue || '';
  const context = extractSection(issueBody, /^\s{0,3}#{1,6}\s*(?:\d+[.)]?\s*)?(?:Contexto|Descrição|Racional)\b/iu);
  const criteria = extractSection(issueBody, /^\s{0,3}#{1,6}\s*(?:\d+[.)]?\s*)?Critérios?\s+de\s+(?:Aceite|Aceitação)\b/iu);
  const hasEarsSyntax = criteria.split(/\r?\n/).some(isEarsStatement);
  const isoChecks = {
    hasContext: hasMeaningfulContent(context),
    hasAcceptanceCriteria: criteria.length > 0,
    hasVerificationMethod: hasVerificationMethod(issueBody),
    hasMetadataID: METADATA_ID.test(issueBody) && REQUIREMENT_ID.test(issueBody)
  };
  const approved = hasEarsSyntax && Object.values(isoChecks).every(Boolean);
  const requiredActions = [];

  if (!isoChecks.hasContext) {
    requiredActions.push('Preencha a seção de contexto/racional com a origem e a necessidade do requisito.');
  }
  if (!hasEarsSyntax) {
    requiredActions.push('Inclua ao menos um critério de aceite verificável na seção de critérios, usando sintaxe EARS.');
  }
  if (!isoChecks.hasVerificationMethod) {
    requiredActions.push('Informe um método de verificação concreto (por exemplo, teste automatizado, inspeção ou demonstração).');
  }
  if (!isoChecks.hasMetadataID) {
    requiredActions.push('Informe um ID válido na tabela de metadados: REQ-..., RF-... ou RNF-... (exemplo: REQ-AUTH-001).');
  }

  return {
    issue_number: issueNumber,
    approved,
    score: approved ? 100 : Math.round((Object.values(isoChecks).filter(Boolean).length + Number(hasEarsSyntax)) / 5 * 100),
    validation_scope: 'Verificação estrutural e sintática; não substitui revisão semântica por pessoa responsável.',
    feedback_summary: approved
      ? 'A issue passou pelas verificações estruturais e sintáticas configuradas (EARS e metadados obrigatórios).'
      : 'A issue precisa de ajustes para passar pelas verificações estruturais e sintáticas configuradas.',
    ears_syntax_valid: hasEarsSyntax,
    iso_checks: isoChecks,
    required_actions: requiredActions,
    timestamp: new Date().toISOString()
  };
}

function parseArgs(args) {
  const values = {};
  for (let index = 0; index < args.length; index += 2) {
    const flag = args[index];
    const value = args[index + 1];
    if (!['--input-file', '--result-file'].includes(flag) || !value || values[flag]) {
      throw runnerError('Uso: runner.js --input-file <json> --result-file <json>', 'INVALID_ARGUMENTS');
    }
    values[flag] = value;
  }

  if (!values['--input-file'] || !values['--result-file']) {
    throw runnerError('Uso: runner.js --input-file <json> --result-file <json>', 'INVALID_ARGUMENTS');
  }
  return { inputFile: values['--input-file'], resultFile: values['--result-file'] };
}

function run(args = process.argv.slice(2)) {
  const { inputFile, resultFile } = parseArgs(args);
  let input;
  try {
    input = JSON.parse(fs.readFileSync(inputFile, 'utf8'));
  } catch (error) {
    throw runnerError(`Não foi possível ler a entrada JSON da issue: ${error.message}`, 'INVALID_INPUT_FILE');
  }

  if (!input || typeof input !== 'object' || Array.isArray(input)) {
    throw runnerError('A entrada deve ser um objeto JSON com issue_number e body.', 'INVALID_INPUT');
  }
  const result = reviewIssue(input.issue_number, input.body);
  fs.writeFileSync(resultFile, `${JSON.stringify(result, null, 2)}\n`, { encoding: 'utf8', mode: 0o600 });
  return result;
}

if (require.main === module) {
  try {
    const result = run();
    const message = `[Issue Validator] Issue #${result.issue_number}: ${result.approved ? 'aprovada' : 'requer refinamento'}.`;
    if (result.approved) {
      console.log(message);
    } else {
      console.error(message);
      process.exitCode = 1;
    }
  } catch (error) {
    console.error(`[Issue Validator] ${error.message}`);
    process.exitCode = 1;
  }
}

module.exports = { parseArgs, reviewIssue, run };
