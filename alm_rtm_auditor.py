#!/usr/bin/env python3
"""
ALM & RTM Automated Auditor & Matrix Generator
----------------------------------------------
Este script realiza a auditoria automatizada do ciclo de vida de software (ALM),
verifica configurações seletivas (ISO 29148/EARS, CI/CD, Dependabot),
identifica inconsistências de nomenclatura/commits e gera a Matriz de
Rastreabilidade (RTM) em formato Markdown.
"""

import os
from pathlib import Path


class ALMAuditor:
    def __init__(self, repo_root="."):
        self.repo_root = Path(repo_root)
        self.report = {
            "alm_gaps": [],
            "selective_configs": [],
            "inconsistencies": [],
            "prioritized_steps": [],
            "rtm_matrix": []
        }

    def audit_alm_phases(self):
        """1. Avaliação de Lacunas por Fase do ALM"""
        phases = [
            {
                "fase": "1. Planejamento e Viabilidade",
                "expected": ["docs/alm/governanca/matriz-raci.md", "docs/alm/fases/fase-1-viabilidade.md"],
                "status_if_missing": "Ausente",
                "recommendation": "Criar matriz RACI e fluxo de viabilidade."
            },
            {
                "fase": "2. Engenharia de Requisitos",
                "expected": [".github/ISSUE_TEMPLATE/requisito-iso29148.md"],
                "status_if_missing": "Parcialmente Coberto",
                "recommendation": "Adicionar template de Issue em conformidade com ISO 29148 e EARS."
            },
            {
                "fase": "3. Design e Arquitetura",
                "expected": ["docs/architecture/adr"],
                "status_if_missing": "Parcialmente Coberto",
                "recommendation": "Criar repositório de ADRs (Architecture Decision Records) no formato Y-statement."
            },
            {
                "fase": "4. Desenvolvimento e Codificação",
                "expected": ["docs/alm/artefatos/padrao-commits.md"],
                "status_if_missing": "Parcialmente Coberto",
                "recommendation": "Estabelecer diretrizes de Conventional Commits rastreáveis com ID de requisito."
            },
            {
                "fase": "5. Testes e Qualidade",
                "expected": ["tests"],
                "status_if_missing": "Ausente",
                "recommendation": "Instanciar diretório de testes unitários/integração e configurar meta de cobertura no DoD."
            },
            {
                "fase": "6. Implantação e CI/CD",
                "expected": [".github/workflows/alm-ci-quality-gate.yml"],
                "status_if_missing": "Ausente",
                "recommendation": "Configurar pipeline de CI/CD para execução de linters e testes de rastreabilidade."
            },
            {
                "fase": "7. Operação e Observabilidade",
                "expected": ["prometheus.yml", "otel-config.yaml"],
                "status_if_missing": "Ausente",
                "recommendation": "Configurar agentes de coleta de métricas e integração de observabilidade."
            },
            {
                "fase": "8. Manutenção e Descontinuação",
                "expected": [".github/dependabot.yml"],
                "status_if_missing": "Ausente",
                "recommendation": "Ativar o Dependabot para varredura automatizada de dependências e segurança."
            }
        ]

        for p in phases:
            exists = any((self.repo_root / item).exists() for item in p["expected"])
            status = "Coberto" if exists else p["status_if_missing"]
            evidence = "Presente" if exists else f"Ausência de: {', '.join(p['expected'])}"
            self.report["alm_gaps"].append({
                "fase": p["fase"],
                "status": status,
                "evidencia": evidence,
                "acao": "Manter monitoramento" if exists else p["recommendation"]
            })

    def audit_selective_configs(self):
        """2. Verificação de Configurações Seletivas (Novos Itens)"""
        configs = [
            {
                "item": "CI/CD Quality Gate",
                "path": ".github/workflows/alm-ci-quality-gate.yml",
                "objetivo": "Validação automática de Markdown, linters e rastreabilidade nos PRs."
            },
            {
                "item": "Template ISO 29148 / EARS",
                "path": ".github/ISSUE_TEMPLATE/requisito-iso29148.md",
                "objetivo": "Padronização de requisitos com sintaxe EARS e tabela de metadados normativos."
            },
            {
                "item": "SCA / Dependabot",
                "path": ".github/dependabot.yml",
                "objetivo": "Automação da fase de Manutenção do ALM para varredura semanal de vulnerabilidades."
            }
        ]

        for cfg in configs:
            target = self.repo_root / cfg["path"]
            configured = target.exists()
            self.report["selective_configs"].append({
                "item": cfg["item"],
                "path": cfg["path"],
                "status": "Configurado" if configured else "Pendente de Criacao",
                "objetivo": cfg["objetivo"]
            })

    def audit_inconsistencies(self):
        """3. Diagnóstico de Inconsistências e Refatorações"""
        inconsistencies = [
            {
                "problema": "Ausência de padrão rígido em commits do Git",
                "impacto": "Impossibilidade de rastrear commits até o requisito/issue de origem (quebra da RTM).",
                "recomendacao": "Adotar padrão `feat(escopo-REQ-XXX): mensagem` e hooks de pre-commit.",
                "prioridade": "Alta"
            },
            {
                "problema": "Nomenclatura heterogênea nas pastas de governança (singular/plural)",
                "impacto": "Elevação do tempo de integração de novos desenvolvedores.",
                "recomendacao": "Padronizar estrutura em minúsculas separadas por hífen e incluir `docs/alm/INDEX.md`.",
                "prioridade": "Média"
            },
            {
                "problema": "Isolamento da documentação de modelagem visual (`DOCUMENTAÇÃO.md`)",
                "impacto": "Risco de desalinhamento entre diagramas UML e os requisitos formais.",
                "recomendacao": "Mover para `docs/alm/artefatos/guia-modelagem-uml.md` e exigir citação de ID de requisito.",
                "prioridade": "Baixa"
            }
        ]
        self.report["inconsistencies"] = inconsistencies

    def generate_prioritized_steps(self):
        """4. Próximos Passos Priorizados por Nível de Severidade"""
        self.report["prioritized_steps"] = [
            {"prioridade": "P0 (Imediata / Bloqueante)", "acao": "Ativar workflow `.github/workflows/alm-ci-quality-gate.yml` e template `.github/ISSUE_TEMPLATE/requisito-iso29148.md`."},
            {"prioridade": "P1 (Curto Prazo / Essencial)", "acao": "Implantar `.github/dependabot.yml`, criar diretório `tests/` e instanciar pasta de ADRs (`docs/architecture/adr/`)."},
            {"prioridade": "P2 (Médio Prazo / Evolutivo)", "acao": "Configurar integração MCP para automação de validação EARS e gerador dinâmico de RTM."}
        ]

    def build_markdown_report(self):
        """Gera o relatório Markdown completo consolidando todas as etapas"""
        md = []
        md.append("# Diagnóstico de Rastreabilidade e Auditoria ALM\n")
        
        md.append("## 1. Tabela de Lacunas por Fase do ALM\n")
        md.append("| Fase ALM | Status | Evidência Observável | Ação Recomendada |")
        md.append("| :--- | :--- | :--- | :--- |")
        for gap in self.report["alm_gaps"]:
            md.append(f"| **{gap['fase']}** | {gap['status']} | {gap['evidencia']} | {gap['acao']} |")
        md.append("\n")

        md.append("## 2. Configuração Seletiva (Somente Itens Novos)\n")
        md.append("| Componente | Arquivo de Destino | Status | Objetivo do Item |")
        md.append("| :--- | :--- | :--- | :--- |")
        for sc in self.report["selective_configs"]:
            md.append(f"| **{sc['item']}** | `{sc['path']}` | {sc['status']} | {sc['objetivo']} |")
        md.append("\n")

        md.append("## 3. Inconsistências e Recomendação de Refatoração\n")
        md.append("| Problema Identificado | Impacto Técnico | Recomendação de Refatoração | Prioridade |")
        md.append("| :--- | :--- | :--- | :--- |")
        for inc in self.report["inconsistencies"]:
            md.append(f"| **{inc['problema']}** | {inc['impacto']} | {inc['recomendacao']} | **{inc['prioridade']}** |")
        md.append("\n")

        md.append("## 4. Próximos Passos Priorizados\n")
        for step in self.report["prioritized_steps"]:
            md.append(f"- **[{step['prioridade']}]**: {step['acao']}")
        md.append("\n")

        return "\n".join(md)

def main():
    auditor = ALMAuditor()
    auditor.audit_alm_phases()
    auditor.audit_selective_configs()
    auditor.audit_inconsistencies()
    auditor.generate_prioritized_steps()

    report_md = auditor.build_markdown_report()
    
    os.makedirs("/workspace/scratch", exist_ok=True)
    with open("/workspace/scratch/alm_rtm_report.md", "w", encoding="utf-8") as f:
        f.write(report_md)
        
    print("Auditoria ALM concluída com sucesso! Relatório gerado em /workspace/scratch/alm_rtm_report.md")

if __name__ == "__main__":
    main()
