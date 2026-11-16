## 📌 Descrição da Mudança
- **O que foi feito:** 
- **Motivação / Contexto:** 

---

## 🛡️ Checklist de Qualidade e Segurança (Definition of Done - DoD)
- [ ] Executado auditoria de dependências local (`npm audit`, `pip-audit`, `dotnet list package`).
- [ ] Gerado e validado SBOM SPDX localmente (`syft dir:. -o spdx-json`).
- [ ] Escaneamento local via Trivy executado com **0 vulnerabilidades CRITICAL ou HIGH**.
- [ ] Ausência de segredos ou chaves privadas commitadas (`gitleaks`).
- [ ] Imagens Docker utilizando tags específicas e imagens base enxutas (`slim`/`alpine`).

---

## 📄 Governança de Exceções & Falsos Positivos
- Contém exceção/falso positivo liberado via `.trivyignore`?
  - [ ] **Não**
  - [ ] **Sim** (Obrigatório registrar link da ADR em `docs/adr/` com expiração <= 30 dias).
