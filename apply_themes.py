import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Inject Leaflet in <head>
leaflet_tags = """<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
"""
content = content.replace(
    '<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>',
    '<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>\n' + leaflet_tags
)

# 2. Inject Light Theme CSS
light_theme_css = """
body.light-theme {
  --bg: #F8FAFC;
  --bg-card: #FFFFFF;
  --bg-card-alt: #F1F5F9;
  --border: #E2E8F0;
  --text-main: #0F172A;
  --text-muted: #64748B;
  --gov-blue-alpha: rgba(37, 99, 235, 0.1);
}
.light-theme .s-logo img { filter: drop-shadow(0 0 6px rgba(0,0,0,0.1)); background: transparent; }
#map { width: 100%; height: 500px; border-radius: 12px; border: 1px solid var(--border); margin-top: 16px; background: var(--bg-card-alt); z-index: 1;}
.search-bar { background: var(--bg-card); border: 1px solid var(--border); color: var(--text-main); padding: 8px 16px; border-radius: 20px; font-size: 0.8rem; outline: none; width: 250px; transition: all 0.3s; }
.search-bar:focus { border-color: var(--gov-blue-light); box-shadow: 0 0 0 2px var(--gov-blue-alpha); width: 300px; }
"""
content = content.replace("/* ── SPLASH ── */", light_theme_css + "\n/* ── SPLASH ── */")

# 3. Inject Search, Theme Toggle, CSV Export into Topbar
search_input = """<input type="search" id="searchInput" class="search-bar" placeholder="Buscar escola ou INEP..." onkeyup="applyFilters()">"""
topbar_left_pattern = r'(<div class="breadcrumb">.*?</div>)'
content = re.sub(topbar_left_pattern, r'\1\n      ' + search_input, content, flags=re.DOTALL)

buttons_html = """
      <button class="topbar-btn" onclick="toggleTheme()" title="Alternar Modo Claro/Escuro">
        <svg width="18" height="18" viewBox="0 0 24 24"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
      </button>
      <button class="topbar-btn" onclick="exportCSV()" title="Exportar Dados (CSV)">
        <svg width="18" height="18" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="12" y1="18" x2="12" y2="12"></line><line x1="9" y1="15" x2="15" y2="15"></line></svg>
      </button>
"""
content = content.replace('<button class="topbar-btn" onclick="toggleFullscreen()"', buttons_html + '\n      <button class="topbar-btn" onclick="toggleFullscreen()"')

# 4. Add IDEB Navigation Item
ideb_nav = """
      <div class="nav-item" onclick="go('qualidade')" id="view-btn-qualidade">
        <svg viewBox="0 0 24 24"><path d="M12 20v-6M6 20V10M18 20V4"></path></svg>
        <span>Qualidade e IDEB</span>
      </div>
"""
content = content.replace('<div class="s-foot">', ideb_nav + '\n    </div>\n    <div class="s-foot">')

# 5. Add IDEB View HTML
ideb_view_html = """
      <!-- QUALIDADE E IDEB -->
      <div class="view" id="view-qualidade">
        <div class="kpi-grid">
          <div class="kpi-card">
            <div class="k-title">IDEB Ensino Fundamental (Anos Iniciais)</div>
            <div class="k-val">5.4 <span class="trend up">Meta 5.2</span></div>
            <div class="k-sub">Última avaliação (2023)</div>
          </div>
          <div class="kpi-card">
            <div class="k-title">IDEB Ensino Fundamental (Anos Finais)</div>
            <div class="k-val">4.3 <span class="trend down">Meta 4.5</span></div>
            <div class="k-sub">Última avaliação (2023)</div>
          </div>
          <div class="kpi-card">
            <div class="k-title">IDEB Ensino Médio</div>
            <div class="k-val">3.8 <span class="trend up">Meta 3.7</span></div>
            <div class="k-sub">Última avaliação (2023)</div>
          </div>
        </div>
        <div class="chart-box" style="margin-top: 24px;">
          <div class="chart-header">
            <div class="chart-title">Acompanhamento das Metas IDEB (Histórico)</div>
          </div>
          <div class="chart-wrap" style="height: 300px;"><canvas id="cIdeb"></canvas></div>
        </div>
      </div>
"""
content = content.replace('<!-- INTELIGÊNCIA GEOGRÁFICA -->', ideb_view_html + '\n      <!-- INTELIGÊNCIA GEOGRÁFICA -->')

# 6. Add Map Container to view-geo
geo_map = """
        <div class="chart-box" style="margin-top: 24px;">
          <div class="chart-header">
            <div class="chart-title">Mapa de Concentração Escolar (Leaflet)</div>
          </div>
          <div id="map"></div>
        </div>
"""
content = content.replace('<!-- ESTRUTURA REGIONAL -->', geo_map + '\n      <!-- ESTRUTURA REGIONAL -->')

# 7. Add JS Logic for Theme, CSV, Map, and Ideb Chart
js_additions = """
// ===== THEME TOGGLE =====
function toggleTheme() {
  document.body.classList.toggle('light-theme');
}

// ===== EXPORT CSV =====
function exportCSV() {
  if(!window.currentFiltered || window.currentFiltered.length === 0) return alert("Nenhum dado para exportar.");
  let csv = "INEP,Escola,Municipio,DRE,Localizacao,Porte,Matriculas,Complexidade\\n";
  window.currentFiltered.forEach(e => {
    csv += `"${e.inep}","${e.esc}","${e.mun}","${e.dre}","${e.loc}","${e.porte}",${e.mat},"${e.comp}"\\n`;
  });
  const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.setAttribute("href", url);
  link.setAttribute("download", "seduc_export.csv");
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}

// ===== LEAFLET MAP =====
let mapInstance = null;
const dreCoords = {
  "DRE Belém": [-1.45502,-48.5024],
  "DRE Marabá": [-5.3686,-49.12],
  "DRE Santarém": [-2.44306,-54.7083],
  "DRE Altamira": [-3.20333,-52.2064],
  "DRE Castanhal": [-1.29683,-47.9265]
};

function renderMap() {
  if(!mapInstance) {
    mapInstance = L.map('map').setView([-3.2, -52.2], 5);
    L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
      attribution: '&copy; OpenStreetMap contributors &copy; CARTO'
    }).addTo(mapInstance);
  }
  
  // Clear existing markers
  mapInstance.eachLayer(layer => {
    if(layer instanceof L.CircleMarker) {
      mapInstance.removeLayer(layer);
    }
  });

  // Calculate size per DRE based on current filtered data
  const counts = {};
  if(window.currentFiltered) {
    window.currentFiltered.forEach(e => counts[e.dre] = (counts[e.dre]||0)+1);
  }

  for(let dre in counts) {
    if(dreCoords[dre]) {
      L.circleMarker(dreCoords[dre], {
        radius: Math.max(8, counts[dre] / 30),
        fillColor: "#2563EB",
        color: "#1E40AF",
        weight: 1,
        opacity: 1,
        fillOpacity: 0.6
      }).addTo(mapInstance).bindPopup(`<b>${dre}</b><br>${counts[dre]} escolas filtradas`);
    }
  }
}

// ===== IDEB CHART =====
function renderIdebChart() {
  if(CHARTS['cIdeb']) destroyChart('cIdeb');
  CHARTS['cIdeb'] = new Chart(document.getElementById('cIdeb'), {
    type: 'bar',
    data: {
      labels: ['2019', '2021', '2023'],
      datasets: [
        { label: 'Ensino Médio (Realizado)', data: [3.4, 3.6, 3.8], backgroundColor: '#2563EB', borderRadius: 4 },
        { label: 'Meta', data: [3.5, 3.6, 3.7], backgroundColor: '#10B981', borderRadius: 4 }
      ]
    },
    options: {
      responsive: true, maintainAspectRatio: false,
      plugins: { legend: { labels: { color: '#94A3B8' } } },
      scales: {
        x: { grid: { display: false }, ticks: { color: '#94A3B8' } },
        y: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#94A3B8' } }
      }
    }
  });
}
"""

# Store filtered globally so CSV and Map can use it
content = content.replace("const filtered=ROWS.filter(r=>{", "window.currentFiltered=ROWS.filter(r=>{")

# Add search logic to filter
search_logic = """
    const q = (document.getElementById('searchInput')?.value || '').toLowerCase();
    if(q && !r.esc.toLowerCase().includes(q) && !r.inep.includes(q)) return false;
"""
content = content.replace("    if(dre&&r.dre!==dre)return false;", search_logic + "\n    if(dre&&r.dre!==dre)return false;")

# In applyFilters(), trigger map and ideb renders if active
content = content.replace("renderAll(filtered);", "renderAll(filtered);\n  setTimeout(() => { if(document.getElementById('view-geo').classList.contains('active')) renderMap(); }, 100);")

content = content.replace("TITLES={'visao':'Visão Geral do Estado','perfil':'Perfil Escolar da Rede','comp':'Análise de Complexidade de Gestão','geo':'Inteligência Geográfica'};",
                          "TITLES={'visao':'Visão Geral do Estado','perfil':'Perfil Escolar da Rede','comp':'Análise de Complexidade de Gestão','geo':'Inteligência Geográfica', 'qualidade': 'Qualidade e Metas (IDEB)'};")

# Also render map when switching to geo view, and ideb when switching to qualidade
go_patch = """
  if(id==='geo') setTimeout(renderMap, 100);
  if(id==='qualidade') setTimeout(renderIdebChart, 100);
"""
content = content.replace("  document.getElementById('view-'+id).classList.add('active');", "  document.getElementById('view-'+id).classList.add('active');\n" + go_patch)

# Finally add the JS block right before populateSelects()
content = content.replace("// ===== INIT =====", js_additions + "\n// ===== INIT =====")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Patch applied successfully.")
