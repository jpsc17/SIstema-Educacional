# SGEP - Sistema de Gestão Escolar e Planejamento

**Relatório Final do Projeto Acadêmico (PoC)**

Este documento apresenta a reflexão final sobre a concepção e entrega do SGEP (Sistema de Gestão Escolar e Planejamento), um painel gerencial estático de alta performance desenvolvido sob medida para a Secretaria de Estado de Educação do Pará (SEDUC/PA). O ciclo de vida do software foi gerenciado no Jira, dividindo o escopo do MVP em 3 Sprints com entregas incrementais de valor.

## 1. Desafios da Gestão Pública Identificados

O projeto foi idealizado para resolver gargalos históricos na administração educacional do estado:

- **Mitigação da Complexidade:** Havia o desafio de mitigar a complexidade na leitura de grandes volumes de dados governamentais. O SGEP resolveu isso transformando planilhas brutas em indicadores visuais e acionáveis para tomadas de decisão estratégica.
- **Democratização dos Dados:** Havia a necessidade de atuar diretamente na democratização interna dos dados de infraestrutura, matrículas e complexidade de gestão escolar. O sistema permitiu que servidores e diretores regionais filtrassem informações em tempo real sem a necessidade de softwares proprietários ou infraestruturas caras de banco de dados.
- **Acessibilidade e Resiliência de Rede:** O sistema precisava garantir funcionamento 100% offline ou via redes móveis instáveis. Isso foi solucionado embutindo os dados diretamente no cliente em formato JSON, o que eliminou a latência de requisições de rede.

## 2. Reflexão sobre o Uso de Dados na Tomada de Decisão

A transição de um modelo de gestão baseado em suposições para uma cultura *data-driven* foi o principal impacto de negócio do SGEP:

- **Fim do "Achismo":** O uso do SGEP na Gestão Educacional extingue o "achismo" gerencial.
- **Identificação de Assimetrias:** O cruzamento visual de dados permite identificar instantaneamente assimetrias na rede, como Diretorias Regionais com alta densidade de alunos por escola rural.
- **Monitoramento de Complexidade:** O sistema acompanha as migrações drásticas nos níveis de Complexidade de Gestão Escolar, focando exclusivamente nos indicadores históricos do Inep de 2023 ao Reformulado de 2025, sem usar dados da base da SEDUC para esta finalidade.
- **Otimização de Recursos:** A leitura visual das assimetrias otimiza a alocação de recursos financeiros, merenda escolar, rotas de transporte e distribuição de professores.

## 3. Lições sobre Transparência e Eficiência (Metodologia Ágil)

O desenvolvimento do SGEP provou que o setor público pode inovar com agilidade e eficiência tecnológica:

- **Inovação no Setor Público:** O projeto serve como prova de conceito de que soluções governamentais robustas e de alto impacto visual podem ser desenvolvidas em ciclos ágeis rápidos. Soluções governamentais podem ser feitas sem onerar o orçamento público com licenças de software ou infraestruturas complexas de servidores.
- **Arquitetura de Custo Zero:** A arquitetura foi concebida sob o princípio de custo zero de infraestrutura, utilizando uma *Single Page Application* (SPA) construída de forma enxuta em HTML5, CSS3 e JavaScript Nativo.
- **Ferramentas de Transparência:** A transparência e o uso em processos administrativos foram facilitados pela inclusão do "Modo Exportar PDF", que gera relatórios perfeitos em formato A4. O sistema também incluiu um "Modo Apresentação" para eliminação de distrações em reuniões diretivas.
- **Ciclos de Entrega (Sprints):** As entregas de valor foram eficientes devido à divisão em ciclos:
  - **Sprint 1:** Tratamento da base de 951 registros escolares.
  - **Sprint 2:** Desenvolvimento da lógica de negócio, herança de dados e filtros.
  - **Sprint 3:** Finalização da integração visual com Chart.js, UI/UX e design responsivo.
