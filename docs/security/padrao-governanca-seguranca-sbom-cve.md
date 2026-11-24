# Padrão de Governança: Segurança em Profundidade, SBOM e Gestão de Vulnerabilidades em Repositórios

Este documento estabelece a política e a norma técnica de governança de segurança para todos os repositórios de software da organização, fundamentado nos princípios de **Segurança em Profundidade (Defense-in-Depth)**, rastreabilidade contínua de componentes (**SBOM**) e gestão automatizada de exposições conhecidas (**CVE**).

A modernização da engenharia de software acelerou o reuso de bibliotecas, frameworks e contêineres, mas expandiu significativamente a superfície de ataque da cadeia de suprimentos de software (*Software Supply Chain*). Este padrão normatiza a integração obrigatória de controles de segurança em todas as etapas do ciclo de vida do desenvolvimento de software (SDLC), garantindo que nenhum artefato seja promovido para produção sem validação de segurança verificável.

---

## 1. Visão Geral e Contexto de Riscos da Cadeia de Suprimentos

A dependência massiva de ecossistemas *open-source* (como npm, PyPI, Maven, NuGet e Docker Hub) torna a auditoria manual inviável. Conforme evidenciado por incidentes graves da indústria — como o ataque de *phishing* no ecossistema npm em setembro de 2025 (que comprometeu pacotes amplamente utilizados como `chalk`, `debug` e `worker-styles`) e a vulnerabilidade RCE `Log4Shell` no Apache Log4j em 2021 —, uma única brecha em uma dependência indireta pode comprometer toda a infraestrutura e os dados da aplicação.

Para mitigar esses riscos, a governança do repositório adota a abordagem de **Segurança por Design (Security by Design)** e **Shift-Left Security**, trazendo a identificação e mitigação de vulnerabilidades para a máquina do desenvolvedor e automatizando barreiras (*Quality Gates*) nos pipelines de Integração e Entrega Contínua (CI/CD).

---

## 2. Taxonomia de Governança e Requisitos do Repositório

### 2.1 Requisitos Funcionais (RF)
* **RF-SEC-01 (Auditoria Local de Dependências):** O repositório deve fornecer scripts e instruções padronizadas para que os desenvolvedores executem auditorias de dependências em ambiente local (ex.: `npm audit`, `pip audit`, `dotnet list package --vulnerable`).
* **RF-SEC-02 (Análise Estática Automática - SAST):** O pipeline do repositório deve executar análise estática de código automatizada (via SonarQube, GitHub CodeQL ou equivalente) a cada *Pull Request* acionado para os *branches* protegidos.
* **RF-SEC-03 (Geração de SBOM Automatizada):** Todo *build* de release ou empacotamento de imagem de contêiner deve gerar automaticamente o inventário formal de software (Software Bill of Materials - SBOM) no padrão internacional.
* **RF-SEC-04 (Notificação e Abertura Automática de PRs de Correção):** O repositório deve manter ativo o robô de dependências (ex.: Dependabot) configurado para gerar alertas e *Pull Requests* de atualização automática sempre que novas CVEs forem registradas.
* **RF-SEC-05 (Exportação de Relatórios no Formato SARIF):** Todas as ferramentas de escaneamento de vulnerabilidades utilizadas no pipeline devem exportar relatórios no formato padrão SARIF (*Static Analysis Results Interchange Format*) para integração centralizada no painel de segurança do repositório (GitHub Code Scanning / Azure Security).

### 2.2 Requisitos Não Funcionais (RNF)
* **RNF-SEC-01 (Tolerância Zero para CVEs Críticas e Altas):** O pipeline de CI/CD não deve permitir a geração de artefatos de release ou imagens de produção se houver qualquer CVE classificada com severidade *Critical* ou *High* sem mitigação aprovada.
* **RNF-SEC-02 (Integridade e Imutabilidade da Imagem):** As imagens de contêiner geradas para produção devem possuir assinatura digital e incorporar o SBOM diretamente na imagem, permitindo verificação de procedência antes do *deploy*.
* **RNF-SEC-03 (Desempenho da Esteira de CI/CD):** As etapas de escaneamento de segurança no pipeline devem utilizar estratégias de *cache* e filtragem incremental para não exceder o tempo máximo limite de execução estipulado pela política da equipe.
* **RNF-SEC-04 (Minimização da Superfície de Ataque em Contêineres):** Toda imagem Docker de produção deve ser construída a partir de imagens base enxutas, oficiais e constantemente atualizadas (ex.: distribuições `slim` ou `alpine`), adotando *multi-stage builds*.

### 2.3 Restrições Técnicas
* **REST-SEC-01 (Padrão de SBOM):** O SBOM deve ser gerado estritamente no padrão internacional **SPDX** (*Software Package Data Exchange*), mantido pela Linux Foundation, ou no padrão **CycloneDX**.
* **REST-SEC-02 (Bloqueio Automático por Exit Code):** As ferramentas de verificação de vulnerabilidades no CI/CD devem ser configuradas para retornar um código de saída diferente de zero (`exit_code != 0`) na presença de vulnerabilidades bloqueantes, forçando a falha do *build*.
* **REST-SEC-03 (Inviolabilidade das Políticas de Branch):** Fica estritamente proibido realizar *push* direto nos *branches* de produção ou integração (`main`, `master`, `release/*`). Toda alteração deve obrigatoriamente passar por *Pull Request* com aprovação de pares e verificações automáticas de segurança passadas.

### 2.4 Regras de Negócio e Gestão de Riscos (RN)
* **RN-SEC-01 (Tratamento de Falsos Positivos e Exceções):** Falsos positivos ou CVEs sem correção disponível (*unfixable*) só poderão ser ignorados no pipeline mediante documentação explícita de justificativa técnica e aceite formal pelo Arquiteto de Software/SecOps em uma ADR (*Architecture Decision Record*) ou arquivo de configuração auditável (`.dependabot.yml` / `.trivyignore`).
* **RN-SEC-02 (Agrupamento de Atualizações de Dependências):** Para reduzir o ruído na equipe, as atualizações automáticas de pacotes de severidade Baixa e Média geradas pelo Dependabot devem ser consolidadas e agrupadas por frequência semanal ou quinzenal.
* **RN-SEC-03 (Validação de Licenças de Terceiros):** O escaneamento do SBOM deve validar se as licenças das dependências utilizadas estão em conformidade com as diretrizes jurídicas da organização (bloqueando licenças altamente virais ou incompatíveis com o modelo comercial do software).

---

## 3. Diretrizes por Etapa do Ciclo de Vida do Software (SDLC)

Para estruturar a **Segurança em Profundidade**, o repositório deve aplicar os controles específicos em cada uma das cinco macroetapas do ciclo de vida:

```text
[ 1. Planejamento ] ---> [ 2. Desenvolvimento ] ---> [ 3. CI/CD Pipeline ] ---> [ 4. Empacotamento ] ---> [ 5. Operações & DAST ]
  - Req. Segurança          - Análise Estática (SAST)    - Gate de Vulnerabilidades  - Imagens Enxutas (Slim)    - DAST em Produção
  - Avaliação de Riscos     - Auditoria Local (npm)     - SBOM em formato SPDX      - Assinatura Digitais      - Monitoramento CVE
  - Compliance Normativo    - IDE Plugins (Sonar)        - Relatórios SARIF          - SBOM Embarcado            - Correções Via PR
```

### 3.1 Planejamento e Arquitetura
* Mapeamento de requisitos não funcionais de segurança e privacidade desde o refinamento da história de usuário.
* Definição da arquitetura de mitigação de riscos baseada nas normas internacionais e modelos de maturidade (ISO/IEC 27001, OWASP, CMMI).
* Seleção criteriosa de bibliotecas e frameworks de terceiros, avaliando reputação do mantenedor, suporte ativo e histórico de vulnerabilidades.

### 3.2 Desenvolvimento Local (Dev / Shift-Left)
* Instalação e execução de extensões e linters de segurança na IDE (ex.: SonarLint, GitHub Copilot Security Analysis) para identificar falhas como SQL Injection, XSS ou dados sensíveis expostos antes do *commit*.
* Execução de rotinas de auditoria de gerenciadores de pacotes (`npm audit`, `composer audit`, `dotnet list package --vulnerable`) após adição ou atualização de dependências.
* Sanitização e validação rigorosa de todas as entradas de dados externos em nível de código.

### 3.3 Integração Contínua (CI/CD) & Quality Gates
* **Compilação e Testes:** O pipeline inicia com a execução de testes unitários e de integração. Caso ocorra qualquer falha de teste, a esteira é interrompida imediatamente.
* **SAST (Static Application Security Testing):** Análise estática do código-fonte utilizando SonarQube / CodeQL.
* **SCA (Software Composition Analysis):** Escaneamento de dependências declaradas e transitivas, confrontando o inventário contra bases atualizadas de CVEs públicas.
* **Geração do Relatório SARIF:** Agregação dos achados e publicação automática no painel de segurança do GitHub / Azure DevOps.

### 3.4 Entrega e Empacotamento em Contêineres
* **Multi-Stage Builds:** Separação rígida entre o ambiente de compilação (*build stage*) e o ambiente final de execução (*runtime stage*), garantindo que ferramentas de compilação, compiladores e arquivos temporários não sejam incluídos na imagem final.
* **Escaneamento de Imagem de Contêiner:** Utilização de scanners de contêiner (ex.: Docker Scout, Trivy) no pipeline para validar não apenas as dependências do código, mas também as bibliotecas do sistema operacional da imagem base.
* **Injeção do SBOM:** Inclusão formal do arquivo SBOM no artefato compilado ou nos metadados da imagem de contêiner.

### 3.5 Operações, Monitoramento Contínuo e DAST
* **DAST (Dynamic Application Security Testing):** Execução de testes dinâmicos de segurança no ambiente de *staging* ou produção controlada para simular ataques externos no sistema em execução.
* **Monitoramento Ativo de CVEs:** Varredura periódica do inventário de SBOM em produção contra novas CVEs recém-descobertas pela comunidade global.
* **Automação de Remediação:** Utilização do Dependabot para abertura automatizada de PRs contendo as correções e atualizações de versão seguras.

---

## 4. Padrão de Geração e Distribuição do SBOM (Software Bill of Materials)

O **SBOM** é a lista formal estruturada de todos os componentes, bibliotecas, módulos e ferramentas que compõem o produto de software e seu ambiente de execução.

### 4.1 Formato e Padrão Adotado
* O repositório deve adotar o padrão **SPDX** (*Software Package Data Exchange*) em formato JSON ou o padrão **CycloneDX**.
* O SBOM deve contemplar tanto dependências diretas (declaradas nos arquivos de manifesto como `package.json`, `pom.xml`, `requirements.txt`, `csproj`) quanto dependências transitivas (subdependências).

### 4.2 Pipeline de Injeção de SBOM em Contêineres
No processo de *build* da imagem Docker via CI/CD, a geração do SBOM deve ser invocada nativamente (ex.: `docker buildx build --sbom=true` ou integração com `syft` / `trivy`), incorporando o manifesto nos metadados da imagem.

Exemplo de especificação conceitual do pipeline de CI/CD para escaneamento e geração de SBOM:

```yaml
# Trecho de Referência para Pipeline de Governança de Segurança
name: Security Pipeline & SBOM Generator

on:
  push:
    branches: [ main, release/* ]
  pull_request:
    branches: [ main ]

jobs:
  security-scan-and-sbom:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout do Código
        uses: actions/checkout@v4

      - name: Configurar Ambiente Runtime
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Instalar Dependências de Produção
        run: npm ci

      - name: Executar Auditoria de Dependências
        run: npm audit --audit-level=high

      - name: Build da Imagem de Análise
        run: docker build -f Dockerfile.prod -t app-security-analysis:latest .

      - name: Escaneamento de CVEs na Imagem (Docker Scout / Trivy)
        run: |
          # Verifica CVEs Críticas e Altas e falha caso encontradas
          docker scout cves app-security-analysis:latest --exit-code --only-severity critical,high

      - name: Gerar e Anexar SBOM (Padrão SPDX)
        run: |
          docker scout sbom --format spdx-json --output ./sbom-spdx.json app-security-analysis:latest

      - name: Upload de Artefato SBOM e Relatório SARIF
        uses: actions/upload-artifact@v4
        with:
          name: sbom-and-security-reports
          path: |
            ./sbom-spdx.json
```

---

## 5. Matriz de Severidade CVE e SLA de Remediação

Toda vulnerabilidade identificada deve ser classificada com base na pontuação **CVSS** (*Common Vulnerability Scoring System*) e no registro oficial da **CVE** (*Common Vulnerabilities and Exposures*).

| Severidade CVSS | Faixa de Pontuação | Ação no Pipeline CI/CD | SLA Máximo de Remediação em Produção |
| :--- | :--- | :--- | :--- |
| **Crítica (Critical)** | 9.0 - 10.0 | **Bloqueio Imediato** (`Exit Code != 0`). Build interrompido. | **24 Horas** (Patch emergencial / Hotfix) |
| **Alta (High)** | 7.0 - 8.9 | **Bloqueio Imediato** (`Exit Code != 0`). Build interrompido. | **72 Horas** |
| **Média (Medium)** | 4.0 - 6.9 | Alerta gerado. Notificação no PR/SARIF. Permitido com aviso. | **15 Dias Úteis** (Próxima Sprint) |
| **Baixa (Low)** | 0.1 - 3.9 | Log registrado para acompanhamento. | **30 Dias Úteis** (Manutenção Preventiva) |

### 5.1 Procedimento de Exceção e Mitigação Temporária
Quando uma CVE Crítica ou Alta for identificada, mas **não houver correção publicada pelo mantenedor upstream** (*unfixable*):
1. A equipe técnica deve aplicar um controle compensatório (ex.: regra de Web Application Firewall - WAF, desativação temporária da funcionalidade afetada, ou isolamento de rede).
2. Criar uma **ADR (Architecture Decision Record)** justificando o risco residual assumido e informando o plano de mitigação.
3. Adicionar o ID da CVE ao arquivo de bypass auditável do repositório com data de expiração pré-definida.

---

## 6. Configuração e Governança do Dependabot / Code Scanning

O repositório deve possuir o arquivo `.github/dependabot.yml` (ou equivalente no Azure DevOps / GitLab) configurado com as seguintes diretrizes:

* **Escopo de Análise:** Varredura diária para ambientes de produção e semanal para ferramentas de desenvolvimento.
* **Agrupamento de PRs:** Agrupar dependências do mesmo ecossistema (*grouping*) para evitar enxurrada de PRs individuais.
* **Aprovações Automatizadas:** PRs do Dependabot que alterem apenas versões *patch* e possuam testes automatizados com 100% de aprovação poderão ser mesclados automaticamente via *auto-merge* configurado.

Exemplo de manifesto `.github/dependabot.yml`:

```yaml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "daily"
    open-pull-requests-limit: 10
    groups:
      patch-updates:
        patterns:
          - "*"
        update-types:
          - "patch"
      minor-updates:
        patterns:
          - "*"
        update-types:
          - "minor"
    ignore:
      # Exemplo de isolamento documentado mediante ADR
      - dependency-name: "pacote-exemplo"
        versions: ["1.2.3"]
```

---

## 7. Critérios de Aceite e Definition of Done (DoD) de Segurança

Para que qualquer funcionalidade ou alteração no repositório seja considerada **Concluída (Done)**, ela deve atender obrigatoriamente aos seguintes critérios de verificação:

1. **Zero Vulnerabilidades Críticas e Altas:** Nenhum *build* em produção pode conter CVEs de severidade *Critical* ou *High*.
2. **SBOM Atualizado e Válido:** O arquivo SBOM no padrão SPDX deve ter sido gerado e validado no processo de compilação.
3. **Relatório SARIF Sem Bloqueios:** As análises estáticas (SAST) e de composição (SCA) devem ter seus relatórios anexados e sem alertas não tratados no GitHub Security / Code Scanning.
4. **Imagem Base Atualizada:** O contêiner de execução deve ter sido construído utilizando a versão mais recente e estável da imagem base corporativa aprovada.
5. **Revisão de Código (Peer Review):** O PR deve possuir aprovação de ao menos 1 Revisor Sênior ou Arquiteto de Software, confirmando a observância às práticas de codificação segura.
