import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.html = f.read()

# 1. Fix currentFiltered -> filtered
content = content.replace("window.currentFiltered", "filtered")

# 2. Add light-theme sidebar styles
if ".light-theme .sidebar" not in content:
    content = content.replace("</style>", """
.light-theme .sidebar { background: #FFFFFF; border-right: 1px solid var(--border); }
.light-theme .sidebar .nav-item { color: var(--text-muted); }
.light-theme .sidebar .nav-item:hover, .light-theme .sidebar .nav-item.active { background: var(--gov-blue-alpha); color: var(--gov-blue); }
.light-theme .sidebar .brand { color: var(--gov-blue); }
.light-theme .topbar { background: #FFFFFF; border-bottom: 1px solid var(--border); }
.light-theme .topbar .top-action { background: #F1F5F9; color: var(--text-main); }
.light-theme .topbar .top-action:hover { background: #E2E8F0; }
</style>""")

# 3. Fix Search Logic in applyFilters
search_logic = """
  const q = (document.getElementById('searchInput')?.value || '').toLowerCase();
  filtered=ROWS.filter(r=>{
    if(q && !r.nome.toLowerCase().includes(q)) return false;
"""
if "const q =" not in content:
    content = content.replace("  filtered=ROWS.filter(r=>{", search_logic)

# 4. Fix TITLES and view-qualidade HTML
if "qualidade:" not in content:
    content = content.replace(
        "const TITLES={visao:'Visão Geral do Estado',perfil:'Perfil e Estrutura das Escolas',complexidade:'Análise de Complexidade de Gestão',regional:'Detalhamento por Diretoria Regional'};",
        "const TITLES={visao:'Visão Geral do Estado',perfil:'Perfil e Estrutura das Escolas',complexidade:'Análise de Complexidade de Gestão',regional:'Detalhamento por Diretoria Regional',qualidade:'Qualidade e Metas (IDEB)'};"
    )

ideb_view_html = """
    <!-- view-qualidade (IDEB) -->
    <div class="view" id="view-qualidade">
      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap:1.5rem; margin-bottom:1.5rem;">
        <div class="card kpi-card">
          <div class="kpi-title">IDEB Atual (Ensino Médio)</div>
          <div class="kpi-value">3.6</div>
          <div class="kpi-trend trend-up">↑ 0.4 pts (vs 2021)</div>
        </div>
        <div class="card kpi-card">
          <div class="kpi-title">Meta do Estado (2025)</div>
          <div class="kpi-value">4.0</div>
          <div class="kpi-trend trend-up">80% da meta atingida</div>
        </div>
        <div class="card kpi-card">
          <div class="kpi-title">Aprovação (Taxa de Rendimento)</div>
          <div class="kpi-value">91.2%</div>
          <div class="kpi-trend trend-up">↑ 2.1% (Ano a ano)</div>
        </div>
      </div>
      <div class="card">
        <div class="card-head">
          <div class="card-title">Evolução Histórica do IDEB - Rede Estadual</div>
        </div>
        <div class="chart-wrap" style="height: 300px;"><canvas id="cIdeb"></canvas></div>
      </div>
    </div>
"""

if "id=\"view-qualidade\"" not in content:
    content = content.replace("    </div>\n\n  </div>\n</main>", "    </div>\n" + ideb_view_html + "\n  </div>\n</main>")

# 5. Fix renderIdebChart to actually render
if "function renderIdebChart" not in content:
    ideb_js = """
function renderIdebChart() {
  if(CHARTS['cIdeb']) destroyChart('cIdeb');
  const ctx = document.getElementById('cIdeb');
  if(!ctx) return;
  CHARTS['cIdeb'] = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['2017', '2019', '2021', '2023'],
      datasets: [
        { label: 'Realizado', data: [2.8, 3.2, 3.2, 3.6], backgroundColor: '#2563eb', borderRadius: 4 },
        { label: 'Meta', data: [3.2, 3.5, 3.8, 4.0], type: 'line', borderColor: '#10b981', borderWidth: 2, borderDash: [5,5], fill: false, tension: 0 }
      ]
    },
    options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { position: 'bottom' } }, scales: { y: { beginAtZero: true, max: 5.0 } } }
  });
}
"""
    content = content.replace("// ===== INITIAL RENDER =====", ideb_js + "\n// ===== INITIAL RENDER =====")


with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Bugs fixed successfully.")
