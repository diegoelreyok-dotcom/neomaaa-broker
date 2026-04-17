# NEOMAAA Broker — Operations Portal

Portal operativo interno del broker NEOMAAA Markets. Docsify + Vercel. Sin build step.

## Stack

- **Docsify 4.13.1** — renderiza markdown en el browser, sin build
- **Vercel** — auto-deploy desde `main` (docs/ como root)
- **html2pdf.js** — descarga PDF client-side
- **CSS custom** — 1,400+ lineas, design system con variables CSS
- **Idioma UI:** espanol (search, pagination, copy-code todo localizado)

## Estructura

```
/                          ← Documentos fuente (markdown grandes originales)
docs/                      ← Portal Docsify (lo que se deploya)
  index.html               ← Config Docsify + PDF plugin + tema
  _sidebar.md              ← Navegacion principal
  README.md                ← Home page (KPIs, org chart, prioridades)
  styles/custom.css         ← Tema completo (variables, responsive, componentes)
  404.md                   ← Pagina de error
  compliance/              ← 5 docs: workflow, onboarding, A-Book, manuals
  sales/                   ← 5 docs: plan contacto, training, comisiones, objeciones, FAQ
  support/                 ← playbook + enciclopedia soporte
  operations/              ← depositos, go-live runbook, FAQ interno (87 preguntas)
  marketing/               ← retencion, funnel, copy, competidores
  hiring/                  ← 4 job descriptions (finance, support ES/EN, marketing)
  partners/                ← programa, modelo financiero, guia operativa
  encyclopedia/            ← ABC del broker (glosario)
  launch/                  ← master checklist
```

## Comandos

No hay build. No hay npm. Todo es estatico.

```bash
# Dev local
npx docsify-cli serve docs    # o simplemente abrir docs/index.html en browser

# Deploy
git push origin main          # Vercel auto-deploya desde /docs

# Nuevo documento
# 1. Crear .md en docs/{seccion}/
# 2. Agregar entrada en docs/_sidebar.md
```

## Convenciones

**Archivos:** kebab-case, descriptivos. `sales/plan-contacto.md`, `compliance/ab-book-policy.md`

**Markdown:**
- H1 = titulo de pagina (uno solo)
- H2 = secciones principales
- H3/H4 = subsecciones
- Tablas para datos estructurados
- `---` para separacion visual
- Blockquotes para callouts/notas

**Componentes HTML en markdown** (clases CSS definidas en custom.css):
- `.kpi-grid` + `.kpi-box` — metricas en grid 4 columnas
- `.card-grid` + `.card` — tarjetas de acceso rapido
- `.team-grid` + `.team-card` — cards de equipo con avatares
- `.org-pyramid` — organigrama jerarquico
- `.badge-ready` / `.badge-progress` / `.badge-pending` / `.badge-critical` — status indicators
- `.timeline` — visualizacion de proceso secuencial

**Sidebar (_sidebar.md):**
- Headers en **BOLD MAYUSCULAS** para secciones
- Items indentados con `- [texto](ruta.md)`

## Gotchas

**PDF plugin:**
- Implementacion custom en index.html (no es plugin de Docsify)
- Clona el contenido, aplica estilos inline, genera con html2pdf.js
- html2canvas REQUIERE que el elemento este attached al DOM (por eso el wrapper off-screen)
- Safari necesita blob URL approach (no window.open con data URL)
- Fallback a window.print() si falla

**Docsify:**
- `subMaxLevel: 0` — no auto-genera TOC en sidebar
- `sidebarDisplayLevel: 1` — solo muestra primer nivel
- docsify-sidebar-collapse maneja expand/collapse de secciones
- Busqueda indexa on-the-fly (no pre-build)

**CSS:**
- 25+ CSS variables para tema (--neo-primary: #00D4AA)
- Print styles separados (fondo blanco, sin sidebar, sin botones)
- Responsive: 3 breakpoints (mobile <768, tablet 768-1199, desktop 1200+)
- Animaciones: fade-in contenido 0.35s, hover en cards/KPIs

**Deploy:**
- Vercel sirve desde /docs como root
- No necesita vercel.json
- .vercel/ esta en .gitignore (no commitear)
- .nojekyll evita procesamiento Jekyll en GitHub Pages (legacy)

## Design System

| Token | Valor | Uso |
|-------|-------|-----|
| --neo-primary | #00D4AA | Headers, links, acentos |
| --neo-primary-dark | #00B894 | Hover states |
| --neo-accent | #6C5CE7 | Acentos secundarios (poco usado) |
| --neo-dark | #0A0E1A | Fondo principal |
| Fuente principal | Inter | Todo el portal |
| Fuente codigo | JetBrains Mono / Fira Code | Code blocks |
