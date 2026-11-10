# Métricas e Indicadores Chave de ALM (KPIs DORA & Qualidade)

Para garantir a melhoria contínua da governança do ciclo de vida de aplicações em todos os projetos, cada equipe deve acompanhar mensalmente o conjunto de métricas **DORA (DevOps Research and Assessment)** alinhado aos indicadores de qualidade de código.

---

## 📈 Indicadores DORA & Qualidade

1. **Deployment Frequency (DF):**
   - **Descrição:** Frequência de implantações com sucesso em ambiente de Produção.
   - **Objetivo:** Avaliar o fluxo contínuo de entrega de valor.

2. **Lead Time for Changes (LTC):**
   - **Descrição:** Tempo transcorrido desde o commit inicial do código até a sua disponibilização efetiva em Produção.
   - **Objetivo:** Medir a eficiência da esteira de CI/CD e a agilidade do processo.

3. **Mean Time to Restore (MTTR):**
   - **Descrição:** Tempo médio necessário para restabelecer o sistema após a ocorrência de uma falha em Produção.
   - **Objetivo:** Avaliar a resiliência operacional e eficácia de planos de contingência.

4. **Change Failure Rate (CFR):**
   - **Descrição:** Percentual de implantações em Produção que causam degradação ou requerem correções imediatas (*hotfixes* / *rollbacks*).
   - **Objetivo:** Garantir que a velocidade de release não comprometa a estabilidade.

5. **Cobertura de Testes (*Code Coverage*):**
   - **Descrição:** Percentual de código coberto por testes automatizados.
   - **Meta:** Mínimo exigido de **80% de cobertura** nos módulos contendo regras de negócio de domínio.

6. **Débito Técnico (*Technical Debt Ratio*):**
   - **Descrição:** Índice mensurado por ferramentas de análise estática (ex.: SonarQube).
   - **Meta:** Mantido estritamente **abaixo de 5%**.

---

## 🔗 Referências Cruzadas
- Veja a fase de garantia de qualidade em [Fase 5: Qualidade e Testes](../fases/fase-5-qualidade-e-testes.md).
- Veja a fase de sustentação em [Fase 7: Operações e Observabilidade](../fases/fase-7-operacoes-e-observabilidade.md).
- Retorne ao [Sumário Principal](../index.md).
