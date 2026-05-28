# SGEP - Painel de Inteligência Educacional

![Status](https://img.shields.io/badge/Status-Concluído-success)
![Vanilla JS](https://img.shields.io/badge/JavaScript-Vanilla-F7DF1E?logo=javascript&logoColor=black)
![Python Tooling](https://img.shields.io/badge/Python-Tooling-3776AB?logo=python&logoColor=white)

Um painel gerencial estático (dashboard) de alta performance desenvolvido para a Secretaria de Estado de Educação do Pará (SEDUC/PA), com foco na análise visual de métricas da rede escolar, inteligência geográfica e acompanhamento de metas do IDEB.

## 🚀 Arquitetura e Tecnologias

Este projeto foi construído sob o princípio de **Custo Zero de Infraestrutura** e resiliência máxima, utilizando uma abordagem Single Page Application (SPA) totalmente estática, sem a necessidade de um backend ou banco de dados ativo.

### 💻 Frontend
* **HTML5 & CSS3:** Interface responsiva construída nativamente (Vanilla), sem uso de frameworks pesados, garantindo carregamento instantâneo.
* **JavaScript (Vanilla):** Lógica de estado, renderização condicional e manipulação de DOM nativos.
* **[Chart.js](https://www.chartjs.org/):** Utilizado para renderização de todas as métricas analíticas e visuais (gráficos de barras, linhas, rosca).
* **[Leaflet.js](https://leafletjs.com/):** Motor de inteligência geográfica utilizado para plotagem da concentração escolar e densidade de matrículas no mapa do estado.

### 🛠️ Tooling & Scripts (Python)
Para facilitar a manutenção de um arquivo monolítico, o projeto utiliza scripts **Python** como ferramentas de *build* e *patch*. Esses scripts leem o `index.html` e injetam novas lógicas programaticamente:
* `apply_themes.py`: Injeta a dependência do Leaflet, adiciona o CSS dinâmico (Light/Dark mode) e regras de negócio para renderização geográfica.
* `update_charts.py`: Manipula as propriedades do Chart.js injetadas no arquivo principal para modernizar o visual (bordas arredondadas, refinamento de grids e paletas de cores).
* Outros scripts (`fix_all.py`, `merge.py`): Utilitários para gestão de DOM e versionamento do painel.

### 🗄️ Estrutura de Dados (Offline-First)
Para garantir funcionamento 100% offline ou em redes instáveis no interior do estado, o banco de dados (matrículas, histórico do IDEB, níveis de complexidade) é embarcado diretamente no cliente como um **JSON estático** (`ROWS`). Isso elimina a latência de requisições HTTPS e consultas SQL.

## ✨ Funcionalidades Principais

* **Filtros Dinâmicos e Herança:** Filtragem em tempo real por Diretoria Regional (DRE), Município, Tipo Administrativo, Zonamento (Urbano/Rural), Porte e Complexidade.
* **Inteligência Geográfica:** Mapeamento em tempo real das escolas filtradas, exibindo o volume e densidade escolar via Leaflet.
* **Exportação Dinâmica (CSV):** Geração local de arquivos CSV a partir dos dados atualmente filtrados na tela, sem chamadas a servidores.
* **Temas e Acessibilidade:** Suporte nativo a *Light Theme* e *Dark Theme*.
* **Modos de Visualização:** 
  * *Modo Apresentação (Fullscreen):* Focado em reuniões de diretoria.
  * *Modo Exportar PDF:* O CSS do sistema adapta automaticamente os gráficos e as quebras de página para impressão física (A4) ou geração de relatórios PDF.

## 📦 Como Executar

Por ser uma aplicação totalmente estática, não há necessidade de `npm install` ou servidores complexos.

1. Clone o repositório:
   ```bash
   git clone https://github.com/jpsc17/SIstema-Educacional.git
   ```
2. Abra o arquivo `index.html` diretamente em qualquer navegador moderno (Chrome, Edge, Firefox, Safari).
3. Para rodar os scripts de atualização em Python (caso deseje modificar algo estrutural):
   ```bash
   python apply_themes.py
   python update_charts.py
   ```

---
*Nota: Este é um projeto acadêmico (Prova de Conceito) desenvolvido com o intuito de demonstrar a viabilidade tecnológica de dashboards de alto impacto e baixo custo no setor público, não possuindo vínculo oficial ou acesso a dados sensíveis/fechados da SEDUC/PA.*
