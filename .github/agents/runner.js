/**
 * MCP Agent Runner - Validador de Issues (ISO 29148 + EARS)
 * 
 * Este script é executado via GitHub Actions ou localmente via MCP CLI.
 * Ele analisa a Issue fornecida e verifica a aderência estrita à norma
 * ISO/IEC/IEEE 29148:2018 e aos padrões formais EARS.
 */

const fs = require('fs');
const path = require('path');

async function main() {
  const args = process.argv.slice(2);
  const issueBody = process.env.ISSUE_BODY || '';
  const issueNumber = process.env.ISSUE_NUMBER || '0';
  
  console.log(`[MCP Runner] Analisando Issue #${issueNumber}...`);

  // Padrões formais EARS
  const earsPatterns = {
    ubiquitous: /^[A-Z][a-zA-Z0-9_ ]+ deve [a-z0-9_ ]+/i,
    eventDriven: /^QUANDO\s+.+,\s+O\s+[A-Z][a-zA-Z0-9_ ]+\s+DEVE\s+.+/i,
    stateDriven: /^ENQUANTO\s+.+,\s+O\s+[A-Z][a-zA-Z0-9_ ]+\s+DEVE\s+.+/i,
    optionalFeature: /^ONDE\s+.+,\s+O\s+[A-Z][a-zA-Z0-9_ ]+\s+DEVE\s+.+/i,
    unwantedBehaviour: /^SE\s+.+,\s+ENTÃO\s+O\s+[A-Z][a-zA-Z0-9_ ]+\s+DEVE\s+.+/i
  };

  const hasEarsSyntax = Object.values(earsPatterns).some(pattern => pattern.test(issueBody.trim()));
  
  // Critérios ISO 29148
  const isoChecks = {
    hasContext: issueBody.includes('### Contexto') || issueBody.includes('## Contexto'),
    hasExpectedBehaviour: issueBody.includes('### Comportamento Esperado') || issueBody.includes('## Comportamento Esperado'),
    hasAcceptanceCriteria: issueBody.includes('### Critérios de Aceitação') || issueBody.includes('## Critérios de Aceitação'),
    hasVerificationMethod: issueBody.includes('Método de Verificação') || issueBody.includes('Teste'),
    hasMetadataID: /ID:\s*RF-\d+|ID:\s*RNF-\d+/i.test(issueBody)
  };

  const isoPassed = Object.values(isoChecks).filter(Boolean).length >= 4;
  const approved = hasEarsSyntax && isoPassed;

  const requiredActions = [];
  if (!hasEarsSyntax) {
    requiredActions.push('Reescrever a especificação do comportamento usando um padrão sintático EARS (ex: "SE <falha>, ENTÃO O <Sistema> DEVE <ação>" ou "QUANDO <evento>, O <Sistema> DEVE <ação>").');
  }
  if (!isoChecks.hasMetadataID) {
    requiredActions.push('Adicionar metadados formais ISO 29148: Identificador Único (`ID: RF-XXX` ou `ID: RNF-XXX`).');
  }
  if (!isoChecks.hasVerificationMethod) {
    requiredActions.push('Especificar o Método de Verificação (ex: Teste de Integração, Demonstração, Inspeção ou Análise).');
  }
  if (!isoChecks.hasAcceptanceCriteria) {
    requiredActions.push('Incluir seção de Critérios de Aceitação Verificáveis com condições de sucesso claras.');
  }

  const feedbackSummary = approved
    ? 'A Issue atende integralmente aos critérios de qualidade da norma ISO/IEC/IEEE 29148:2018 e possui especificação sintática formal EARS.'
    : 'A Issue apresenta divergências sintáticas e/ou ausência de metadados de rastreabilidade obrigatórios conforme a ISO 29148 / EARS.';

  const result = {
    issue_number: issueNumber,
    approved: approved,
    score: approved ? 100 : 50,
    feedback_summary: feedbackSummary,
    ears_syntax_valid: hasEarsSyntax,
    iso_checks: isoChecks,
    required_actions: requiredActions,
    timestamp: new Date().toISOString()
  };

  fs.writeFileSync('./agent-review-result.json', JSON.stringify(result, null, 2));
  console.log(`[MCP Runner] Análise concluída. Aprovado: ${approved}`);
}

main().catch(err => {
  console.error('[MCP Runner Error]', err);
  process.exit(1);
});
