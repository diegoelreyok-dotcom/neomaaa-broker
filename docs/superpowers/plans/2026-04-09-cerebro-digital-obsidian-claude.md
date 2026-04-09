# Cerebro Digital: Obsidian + Claude — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Set up Diego's Obsidian vault as a structured digital brain connected to Claude Code via MCP, with templates, migrated notes, and auto-organization capabilities.

**Architecture:** Hybrid 3-layer system — Claude Memory (profile/preferences), Obsidian vault via MCP server (projects/people/decisions/diary), and per-repo CLAUDE.md files (technical context). The MCP server (`obsidian-mcp`) provides Claude with 12 tools to read, search, create, edit, and manage notes directly from the vault files without Obsidian running.

**Tech Stack:** Obsidian (vault), obsidian-mcp (MCP server via npx), Claude Code (consumer), Obsidian plugins (Templater, Calendar, Dataview)

---

## File Structure

All files are created inside the Obsidian vault at:
`/Users/gsiglobalteamevent/Desktop/obsidiandiego/Sincro/`

**Directories to create:**
```
00-INBOX/
01-PROYECTOS/neomaaa-broker/decisiones/
01-PROYECTOS/neomaaa-broker/notas/
01-PROYECTOS/neomaaa-funded/decisiones/
01-PROYECTOS/neomaaa-funded/notas/
01-PROYECTOS/topstep/decisiones/
01-PROYECTOS/topstep/notas/
01-PROYECTOS/zendm/decisiones/
01-PROYECTOS/zendm/notas/
01-PROYECTOS/oxonntech/decisiones/
01-PROYECTOS/oxonntech/notas/
01-PROYECTOS/crm/decisiones/
01-PROYECTOS/crm/notas/
01-PROYECTOS/crm-interno/decisiones/
01-PROYECTOS/crm-interno/notas/
01-PROYECTOS/mapa-estrategico/decisiones/
01-PROYECTOS/mapa-estrategico/notas/
01-PROYECTOS/analisis-competencia/decisiones/
01-PROYECTOS/analisis-competencia/notas/
01-PROYECTOS/_template-proyecto/decisiones/
01-PROYECTOS/_template-proyecto/notas/
02-PERSONAS/
03-PLAYBOOKS/
04-DIARIO/
05-DECISIONES/
06-TRADING/
07-DELEGADO/
08-IDEAS/
09-PERSONAL/
99-TEMPLATES/
```

**Files to create (templates):**
```
99-TEMPLATES/tpl-proyecto.md
99-TEMPLATES/tpl-persona.md
99-TEMPLATES/tpl-decision.md
99-TEMPLATES/tpl-daily.md
99-TEMPLATES/tpl-delegado.md
99-TEMPLATES/tpl-idea.md
99-TEMPLATES/tpl-playbook.md
```

**Files to create (project dashboards):**
```
01-PROYECTOS/neomaaa-broker/_estado.md
01-PROYECTOS/neomaaa-broker/tareas.md
01-PROYECTOS/neomaaa-funded/_estado.md
01-PROYECTOS/neomaaa-funded/tareas.md
01-PROYECTOS/topstep/_estado.md
01-PROYECTOS/topstep/tareas.md
01-PROYECTOS/zendm/_estado.md
01-PROYECTOS/zendm/tareas.md
01-PROYECTOS/oxonntech/_estado.md
01-PROYECTOS/oxonntech/tareas.md
01-PROYECTOS/crm/_estado.md
01-PROYECTOS/crm/tareas.md
01-PROYECTOS/crm-interno/_estado.md
01-PROYECTOS/crm-interno/tareas.md
01-PROYECTOS/mapa-estrategico/_estado.md
01-PROYECTOS/mapa-estrategico/tareas.md
01-PROYECTOS/analisis-competencia/_estado.md
01-PROYECTOS/analisis-competencia/tareas.md
01-PROYECTOS/_template-proyecto/_estado.md
01-PROYECTOS/_template-proyecto/tareas.md
```

**Config file to modify:**
```
~/.claude/settings.local.json (create — MCP server config)
```

**Existing files to migrate (18 notes + 4 canvas):**
```
Vault root → classified and moved to appropriate folders
```

---

## Task 1: Install and Configure MCP Server

**Files:**
- Create: `~/.claude/settings.local.json`

- [ ] **Step 1: Verify Node.js and npx are available**

Run: `node --version && npx --version`
Expected: Version numbers (v18+ for Node)

- [ ] **Step 2: Test obsidian-mcp runs correctly**

Run: `npx -y obsidian-mcp "/Users/gsiglobalteamevent/Desktop/obsidiandiego/Sincro/" --help 2>&1 | head -20`
Expected: MCP server starts or shows help/usage info (confirms package installs and recognizes the vault path)

- [ ] **Step 3: Create settings.local.json with MCP server config**

Create file `~/.claude/settings.local.json`:
```json
{
  "mcpServers": {
    "obsidian": {
      "command": "npx",
      "args": ["-y", "obsidian-mcp", "/Users/gsiglobalteamevent/Desktop/obsidiandiego/Sincro/"]
    }
  }
}
```

- [ ] **Step 4: Verify Claude Code sees the MCP server**

Run: `claude mcp list`
Expected: Shows "obsidian" in the server list with status

- [ ] **Step 5: Test MCP connection by listing vault contents**

In a Claude Code session, test that the obsidian MCP tools are available by asking Claude to use `search-vault` or `read-note` to read a known note from the vault.

Run: `claude -p "Use the obsidian MCP tools to search the vault for notes containing 'NEOMAAA'. List what you find."`
Expected: Returns results from the vault showing existing notes

---

## Task 2: Create Vault Directory Structure

**Files:**
- Create: All directories listed in File Structure above

- [ ] **Step 1: Create all top-level directories**

```bash
VAULT="/Users/gsiglobalteamevent/Desktop/obsidiandiego/Sincro"
mkdir -p "$VAULT/00-INBOX"
mkdir -p "$VAULT/02-PERSONAS"
mkdir -p "$VAULT/03-PLAYBOOKS"
mkdir -p "$VAULT/04-DIARIO"
mkdir -p "$VAULT/05-DECISIONES"
mkdir -p "$VAULT/06-TRADING"
mkdir -p "$VAULT/07-DELEGADO"
mkdir -p "$VAULT/08-IDEAS"
mkdir -p "$VAULT/09-PERSONAL"
mkdir -p "$VAULT/99-TEMPLATES"
```

- [ ] **Step 2: Create project directories for all 9 projects + template**

```bash
VAULT="/Users/gsiglobalteamevent/Desktop/obsidiandiego/Sincro"
for proj in neomaaa-broker neomaaa-funded topstep zendm oxonntech crm crm-interno mapa-estrategico analisis-competencia _template-proyecto; do
  mkdir -p "$VAULT/01-PROYECTOS/$proj/decisiones"
  mkdir -p "$VAULT/01-PROYECTOS/$proj/notas"
done
```

- [ ] **Step 3: Add .gitkeep to empty directories so Obsidian Sync preserves them**

Obsidian syncs files, not empty folders. Create a placeholder `.gitkeep` in each empty leaf directory:

```bash
VAULT="/Users/gsiglobalteamevent/Desktop/obsidiandiego/Sincro"
for dir in 00-INBOX 02-PERSONAS 03-PLAYBOOKS 05-DECISIONES 06-TRADING 07-DELEGADO 08-IDEAS 09-PERSONAL; do
  touch "$VAULT/$dir/.gitkeep"
done
for proj in neomaaa-broker neomaaa-funded topstep zendm oxonntech crm crm-interno mapa-estrategico analisis-competencia _template-proyecto; do
  touch "$VAULT/01-PROYECTOS/$proj/decisiones/.gitkeep"
  touch "$VAULT/01-PROYECTOS/$proj/notas/.gitkeep"
done
```

- [ ] **Step 4: Verify structure**

Run: `find "$VAULT" -maxdepth 3 -type d | grep -v .obsidian | sort`
Expected: All directories from the spec visible and correctly nested

---

## Task 3: Create Templates

**Files:**
- Create: All 7 template files in `99-TEMPLATES/`

- [ ] **Step 1: Create tpl-proyecto.md (project dashboard template)**

Create file `$VAULT/99-TEMPLATES/tpl-proyecto.md`:
```markdown
---
tipo: proyecto
fecha-creacion: {{date}}
tags: [proyecto]
---

# {{nombre}}
{{descripcion}}

## Estado: 🟡 Por definir
## Velocidad: —

## Links
- Web: 
- Repo: 
- Dashboard: 

## Equipo
| Persona | Rol | Contacto |
|---------|-----|----------|
| | | |

## Pendientes criticos
- [ ] 

## Ultimas decisiones
- 

## Notas recientes
- 
```

- [ ] **Step 2: Create tpl-persona.md**

Create file `$VAULT/99-TEMPLATES/tpl-persona.md`:
```markdown
---
tipo: persona
proyectos: []
fecha-creacion: {{date}}
tags: [persona]
---

# {{nombre}}

## Datos
- **Rol:** 
- **Proyecto(s):** 
- **Contacto:** 
- **Telegram:** 

## Compromisos activos
- [ ] 

## Historial de interacciones
### {{date}}
- 
```

- [ ] **Step 3: Create tpl-decision.md**

Create file `$VAULT/99-TEMPLATES/tpl-decision.md`:
```markdown
---
tipo: decision
proyecto: 
personas: []
fecha: {{date}}
tags: [decision]
---

# Decision: {{titulo}}

## Que se decidio
- 

## Por que
- 

## Que se descarto
- 

## Quien estuvo
- 

## Impacto esperado
- 
```

- [ ] **Step 4: Create tpl-daily.md**

Create file `$VAULT/99-TEMPLATES/tpl-daily.md`:
```markdown
---
tipo: diario
fecha: {{date}}
tags: [daily]
---

# {{date}}

## Panorama + Prioridades sugeridas
<!-- Claude genera esta seccion -->

## Notas del dia
<!-- Escribes libre aqui -->

## Delegado pendiente de follow-up
<!-- Claude genera -->

## Decisiones de hoy
<!-- Claude detecta y llena -->

## Cierre del dia
<!-- Claude genera resumen al final -->
```

- [ ] **Step 5: Create tpl-delegado.md**

Create file `$VAULT/99-TEMPLATES/tpl-delegado.md`:
```markdown
---
tipo: delegado
proyecto: 
persona: 
fecha: {{date}}
deadline: 
status: pendiente
tags: [delegado]
---

# Delegado: {{titulo}}

## Que se delego
- 

## A quien
- 

## Deadline
- 

## Contexto
- 

## Follow-up
### {{date}}
- Status: pendiente
```

- [ ] **Step 6: Create tpl-idea.md**

Create file `$VAULT/99-TEMPLATES/tpl-idea.md`:
```markdown
---
tipo: idea
proyecto: 
fecha: {{date}}
tags: [idea]
---

# Idea: {{titulo}}

## Descripcion
- 

## Por que es interesante
- 

## Siguiente paso
- [ ] 
```

- [ ] **Step 7: Create tpl-playbook.md**

Create file `$VAULT/99-TEMPLATES/tpl-playbook.md`:
```markdown
---
tipo: playbook
proyecto: 
fecha-creacion: {{date}}
tags: [playbook]
---

# Playbook: {{titulo}}

## Cuando usar esto
- 

## Pasos
1. 
2. 
3. 

## Lecciones aprendidas
- 

## Ultima vez que se uso
- {{date}}: 
```

- [ ] **Step 8: Verify all templates exist**

Run: `ls -la "$VAULT/99-TEMPLATES/"`
Expected: 7 .md files (tpl-proyecto, tpl-persona, tpl-decision, tpl-daily, tpl-delegado, tpl-idea, tpl-playbook)

---

## Task 4: Create Project Dashboards (_estado.md) for All 9 Projects

**Files:**
- Create: `_estado.md` and `tareas.md` for each of the 9 projects + template

- [ ] **Step 1: Create _estado.md and tareas.md for neomaaa-broker**

Create file `$VAULT/01-PROYECTOS/neomaaa-broker/_estado.md`:
```markdown
---
tipo: proyecto
fecha-creacion: 2026-04-09
tags: [proyecto, broker, forex]
---

# NEOMAAA Broker
Broker forex/CFD con licencia Anjouan, MT5

## Estado: 🟡 Pre-lanzamiento
## Velocidad: Media

## Links
- Web: https://neomaaa.com
- Dashboard: https://neomaaa-broker.vercel.app/#/
- Repo: /Users/gsiglobalteamevent/neomaaa-broker

## Equipo
| Persona | Rol | Contacto |
|---------|-----|----------|
| Diego | CEO | — |
| Yulia | Principal | — |
| Stanislav | Principal | — |

## Pendientes criticos
- [ ] Definir estructura final de comisiones
- [ ] Completar KYC flow
- [ ] Lanzamiento con meta de 100k depositos en 30 dias

## Ultimas decisiones
- 

## Notas recientes
- 
```

Create file `$VAULT/01-PROYECTOS/neomaaa-broker/tareas.md`:
```markdown
---
tipo: tareas
proyecto: neomaaa-broker
fecha-actualizacion: 2026-04-09
tags: [tareas, broker]
---

# Tareas: NEOMAAA Broker

## Criticas
- [ ] 

## En progreso
- [ ] 

## Backlog
- [ ] 
```

- [ ] **Step 2: Create _estado.md and tareas.md for neomaaa-funded**

Create file `$VAULT/01-PROYECTOS/neomaaa-funded/_estado.md`:
```markdown
---
tipo: proyecto
fecha-creacion: 2026-04-09
tags: [proyecto, proptrading, fondeo]
---

# NEOMAAA Funded
Prop trading firm / empresa de fondeo

## Estado: 🟢 Operativo
## Velocidad: Alta

## Links
- Web: https://neomaaafunded.com
- Dashboard: https://neomaaa-dashboard.vercel.app
- Repo: /Users/gsiglobalteamevent/neomaaa-proptrading

## Equipo
| Persona | Rol | Contacto |
|---------|-----|----------|
| Diego | CEO | — |
| Andrea Rodriguez | Ventas | — |
| Franco | Ventas (top performer) | — |
| Luis Espinoza | Ventas | — |
| Edward Chestryp | Ventas | — |
| Camila Balsante | Ventas | — |

## Pendientes criticos
- [ ] 

## Ultimas decisiones
- 

## Notas recientes
- 
```

Create file `$VAULT/01-PROYECTOS/neomaaa-funded/tareas.md`:
```markdown
---
tipo: tareas
proyecto: neomaaa-funded
fecha-actualizacion: 2026-04-09
tags: [tareas, proptrading]
---

# Tareas: NEOMAAA Funded

## Criticas
- [ ] 

## En progreso
- [ ] 

## Backlog
- [ ] 
```

- [ ] **Step 3: Create _estado.md and tareas.md for topstep**

Create file `$VAULT/01-PROYECTOS/topstep/_estado.md`:
```markdown
---
tipo: proyecto
fecha-creacion: 2026-04-09
tags: [proyecto, trading, topstep]
---

# TopStep
Proyecto personal — estrategia para vencer empresas de fondeo

## Estado: 🟢 Activo
## Velocidad: Media

## Links
- Repo: /Users/gsiglobalteamevent/proptrading-research

## Equipo
| Persona | Rol | Contacto |
|---------|-----|----------|
| Diego | Trader | — |

## Pendientes criticos
- [ ] 

## Ultimas decisiones
- 

## Notas recientes
- 
```

Create file `$VAULT/01-PROYECTOS/topstep/tareas.md`:
```markdown
---
tipo: tareas
proyecto: topstep
fecha-actualizacion: 2026-04-09
tags: [tareas, trading]
---

# Tareas: TopStep

## Criticas
- [ ] 

## En progreso
- [ ] 

## Backlog
- [ ] 
```

- [ ] **Step 4: Create _estado.md and tareas.md for zendm**

Create file `$VAULT/01-PROYECTOS/zendm/_estado.md`:
```markdown
---
tipo: proyecto
fecha-creacion: 2026-04-09
tags: [proyecto, saas, discord]
---

# ZenDM
SaaS de marketing por DM en Discord — $385/mo

## Estado: 🟡 En desarrollo
## Velocidad: Media

## Links
- Web: zendm.io
- Repo: /Users/gsiglobalteamevent/zendm

## Equipo
| Persona | Rol | Contacto |
|---------|-----|----------|
| Diego | CEO / Co-founder | — |
| Kwel | CTO / Co-founder (implementacion) | — |

## Pendientes criticos
- [ ] Dashboard al 80%, falta integracion Stripe
- [ ] Completar assets de contenido

## Ultimas decisiones
- 

## Notas recientes
- 
```

Create file `$VAULT/01-PROYECTOS/zendm/tareas.md`:
```markdown
---
tipo: tareas
proyecto: zendm
fecha-actualizacion: 2026-04-09
tags: [tareas, saas]
---

# Tareas: ZenDM

## Criticas
- [ ] 

## En progreso
- [ ] 

## Backlog
- [ ] 
```

- [ ] **Step 5: Create _estado.md and tareas.md for oxonntech**

Create file `$VAULT/01-PROYECTOS/oxonntech/_estado.md`:
```markdown
---
tipo: proyecto
fecha-creacion: 2026-04-09
tags: [proyecto, tech, web]
---

# OxonnTech
Sitio tech con blog (Next.js + MDX)

## Estado: 🟢 Operativo
## Velocidad: Baja

## Links
- Repo: /Users/gsiglobalteamevent/oxonntech

## Equipo
| Persona | Rol | Contacto |
|---------|-----|----------|
| Diego | Owner | — |

## Pendientes criticos
- [ ] 

## Ultimas decisiones
- 

## Notas recientes
- 
```

Create file `$VAULT/01-PROYECTOS/oxonntech/tareas.md`:
```markdown
---
tipo: tareas
proyecto: oxonntech
fecha-actualizacion: 2026-04-09
tags: [tareas, tech]
---

# Tareas: OxonnTech

## Criticas
- [ ] 

## En progreso
- [ ] 

## Backlog
- [ ] 
```

- [ ] **Step 6: Create _estado.md and tareas.md for crm**

Create file `$VAULT/01-PROYECTOS/crm/_estado.md`:
```markdown
---
tipo: proyecto
fecha-creacion: 2026-04-09
tags: [proyecto, crm, dashboard]
---

# CRM
CRM Dashboard (React/Vite) — crmntmv9

## Estado: 🟢 Operativo
## Velocidad: Baja

## Links
- Repo: /Users/gsiglobalteamevent/crmntmv9

## Equipo
| Persona | Rol | Contacto |
|---------|-----|----------|
| Diego | Owner | — |

## Pendientes criticos
- [ ] 

## Ultimas decisiones
- 

## Notas recientes
- 
```

Create file `$VAULT/01-PROYECTOS/crm/tareas.md`:
```markdown
---
tipo: tareas
proyecto: crm
fecha-actualizacion: 2026-04-09
tags: [tareas, crm]
---

# Tareas: CRM

## Criticas
- [ ] 

## En progreso
- [ ] 

## Backlog
- [ ] 
```

- [ ] **Step 7: Create _estado.md and tareas.md for crm-interno, mapa-estrategico, analisis-competencia**

Create file `$VAULT/01-PROYECTOS/crm-interno/_estado.md`:
```markdown
---
tipo: proyecto
fecha-creacion: 2026-04-09
tags: [proyecto, crm, personal]
---

# CRM Interno Diego
CRM personal para gestion de contactos y relaciones

## Estado: 🔴 Por crear
## Velocidad: —

## Links
- Repo: Por definir

## Equipo
| Persona | Rol | Contacto |
|---------|-----|----------|
| Diego | Owner | — |

## Pendientes criticos
- [ ] Definir alcance y features

## Ultimas decisiones
- 

## Notas recientes
- 
```

Create file `$VAULT/01-PROYECTOS/crm-interno/tareas.md`:
```markdown
---
tipo: tareas
proyecto: crm-interno
fecha-actualizacion: 2026-04-09
tags: [tareas, crm]
---

# Tareas: CRM Interno Diego

## Criticas
- [ ] 

## En progreso
- [ ] 

## Backlog
- [ ] 
```

Create file `$VAULT/01-PROYECTOS/mapa-estrategico/_estado.md`:
```markdown
---
tipo: proyecto
fecha-creacion: 2026-04-09
tags: [proyecto, estrategia]
---

# Mapa Estrategico
Vision y estrategia general del ecosistema de negocios

## Estado: 🔴 Por crear
## Velocidad: —

## Links
- 

## Equipo
| Persona | Rol | Contacto |
|---------|-----|----------|
| Diego | Owner | — |

## Pendientes criticos
- [ ] Definir estructura del mapa

## Ultimas decisiones
- 

## Notas recientes
- 
```

Create file `$VAULT/01-PROYECTOS/mapa-estrategico/tareas.md`:
```markdown
---
tipo: tareas
proyecto: mapa-estrategico
fecha-actualizacion: 2026-04-09
tags: [tareas, estrategia]
---

# Tareas: Mapa Estrategico

## Criticas
- [ ] 

## En progreso
- [ ] 

## Backlog
- [ ] 
```

Create file `$VAULT/01-PROYECTOS/analisis-competencia/_estado.md`:
```markdown
---
tipo: proyecto
fecha-creacion: 2026-04-09
tags: [proyecto, competencia, research]
---

# Analisis de Competencia
Inteligencia competitiva del mercado prop trading / broker / SaaS

## Estado: 🔴 Por crear
## Velocidad: —

## Links
- 

## Equipo
| Persona | Rol | Contacto |
|---------|-----|----------|
| Diego | Owner | — |

## Pendientes criticos
- [ ] Definir competidores clave por vertical

## Ultimas decisiones
- 

## Notas recientes
- 
```

Create file `$VAULT/01-PROYECTOS/analisis-competencia/tareas.md`:
```markdown
---
tipo: tareas
proyecto: analisis-competencia
fecha-actualizacion: 2026-04-09
tags: [tareas, competencia]
---

# Tareas: Analisis de Competencia

## Criticas
- [ ] 

## En progreso
- [ ] 

## Backlog
- [ ] 
```

- [ ] **Step 8: Create _template-proyecto (for future projects)**

Create file `$VAULT/01-PROYECTOS/_template-proyecto/_estado.md`:
```markdown
---
tipo: proyecto
fecha-creacion: {{date}}
tags: [proyecto]
---

# {{NOMBRE_PROYECTO}}
{{DESCRIPCION}}

## Estado: 🔴 Por definir
## Velocidad: —

## Links
- Web: 
- Repo: 
- Dashboard: 

## Equipo
| Persona | Rol | Contacto |
|---------|-----|----------|
| | | |

## Pendientes criticos
- [ ] 

## Ultimas decisiones
- 

## Notas recientes
- 
```

Create file `$VAULT/01-PROYECTOS/_template-proyecto/tareas.md`:
```markdown
---
tipo: tareas
proyecto: {{NOMBRE_PROYECTO}}
fecha-actualizacion: {{date}}
tags: [tareas]
---

# Tareas: {{NOMBRE_PROYECTO}}

## Criticas
- [ ] 

## En progreso
- [ ] 

## Backlog
- [ ] 
```

- [ ] **Step 9: Verify all project files exist**

Run: `find "$VAULT/01-PROYECTOS" -name "_estado.md" -o -name "tareas.md" | sort`
Expected: 20 files (2 per project x 10 projects including template)

---

## Task 5: Migrate Existing Notes

**Files:**
- Move: 18 existing .md files from vault root to appropriate folders
- Move: 4 .canvas files to appropriate location

The migration map below is based on reading each note's content:

- [ ] **Step 1: Migrate broker-related notes**

```bash
VAULT="/Users/gsiglobalteamevent/Desktop/obsidiandiego/Sincro"

# NEOMAAA Broker tasks → project folder
mv "$VAULT/Sin nombre/NEOMAAA BROKER TAREAS.md" "$VAULT/01-PROYECTOS/neomaaa-broker/notas/tareas-originales.md"

# Broker launch prep
mv "$VAULT/PREPARAR IDEA DE OFERTA PARA EL LANZAMIENTO DE BROKER EN ZOOM EN VIVO!.md" "$VAULT/01-PROYECTOS/neomaaa-broker/notas/oferta-lanzamiento-zoom.md"

# Support improvement idea
mv "$VAULT/HABLAR CON LA IA SOBRE TODAS LAS IDEAS DE MEJORAR EL SOPORTE DE NEOMAAA MAS PROFESIONAL, COMO DEBERIA DE SER REALMENTE BIEN PROLIJO MEJORANDO TODO LO QUE TENEMOS.md" "$VAULT/01-PROYECTOS/neomaaa-broker/notas/mejora-soporte-neomaaa.md"

# WhatsApp promo automation idea
mv "$VAULT/podriamos hacer una plataforma o automatizacion que cada vez que lancemos un descuento nuevo, le reenvie la promocion a todos por privado para que la empiecen a promoveer, todos los numeros de whatsapp podrian ser..md" "$VAULT/08-IDEAS/automatizacion-promos-whatsapp.md"
```

- [ ] **Step 2: Migrate team and operations notes**

```bash
VAULT="/Users/gsiglobalteamevent/Desktop/obsidiandiego/Sincro"

# Sales team structure → personas
mv "$VAULT/EQUIPO DE VENTAS PROPFIRM & BROKER 2026..md" "$VAULT/02-PERSONAS/equipo-ventas-2026.md"

# Call organization → delegado
mv "$VAULT/ORGANIZAR LLAMADA HOY Y PONERLOS A EJECUTAR..md" "$VAULT/07-DELEGADO/llamada-equipo-ejecucion.md"

# Weekly work structure → diario
mv "$VAULT/ESTUCTURA DE TRABAJO SEMANA 23.03 a 30.03.md" "$VAULT/04-DIARIO/estructura-semana-2026-03-23.md"

# Monday tasks → diario
mv "$VAULT/TAREAS DE LUNES 23.03.md" "$VAULT/04-DIARIO/tareas-2026-03-23.md"
```

- [ ] **Step 3: Migrate personal and Thailand notes**

```bash
VAULT="/Users/gsiglobalteamevent/Desktop/obsidiandiego/Sincro"

# Thailand work objectives → personal
mv "$VAULT/OBJETIVOS THAILANDIA DE TRABAJO 🇹🇭.md" "$VAULT/09-PERSONAL/objetivos-thailand-trabajo.md"

# Thailand personal objectives → personal
mv "$VAULT/OBJETIVOS PERSONALES EN THAILANDIA 🇹🇭.md" "$VAULT/09-PERSONAL/objetivos-thailand-personal.md"

# Thailand expenses → personal
mv "$VAULT/Gastos Thai.md" "$VAULT/09-PERSONAL/gastos-thailand.md"

# Currency exchange → personal
mv "$VAULT/Cambio 1500$ thailandia.md" "$VAULT/09-PERSONAL/cambio-usd-thailand.md"

# Vlog creation → ideas
mv "$VAULT/CREACION DE VLOG PARA TRADERS HUB - SEMANA 1 THAILAND RETIRANDO 50K CON SANTI AMADO..md" "$VAULT/08-IDEAS/vlog-traders-hub-thailand.md"
```

- [ ] **Step 4: Migrate remaining notes**

```bash
VAULT="/Users/gsiglobalteamevent/Desktop/obsidiandiego/Sincro"

# GSI inventory tasks → project (its own thing)
mv "$VAULT/GSI TAREAS PENDIENTES.md" "$VAULT/00-INBOX/gsi-tareas-pendientes.md"

# Daily note (keep in diario)
mv "$VAULT/2026-04-08.md" "$VAULT/04-DIARIO/2026-04-08.md"

# Untitled notes → inbox for later classification
mv "$VAULT/Sin título.md" "$VAULT/00-INBOX/sin-titulo-1.md"
mv "$VAULT/Sin título 1.md" "$VAULT/00-INBOX/sin-titulo-2.md"

# Crypto seed phrase note (SENSITIVE) → personal
mv "$VAULT/chef run benefit small friend fold wool file shrimp pottery multiply timber.md" "$VAULT/09-PERSONAL/crypto-seed-MOVER-A-LUGAR-SEGURO.md"
```

- [ ] **Step 5: Move canvas files to inbox**

```bash
VAULT="/Users/gsiglobalteamevent/Desktop/obsidiandiego/Sincro"

mv "$VAULT/COSAS PENDIENTES A EJECUTAR 2026 —->.canvas" "$VAULT/00-INBOX/pendientes-2026.canvas"
mv "$VAULT/Sin título.canvas" "$VAULT/00-INBOX/canvas-1.canvas"
mv "$VAULT/Sin título 1.canvas" "$VAULT/00-INBOX/canvas-2.canvas"
mv "$VAULT/Sin título 2.canvas" "$VAULT/00-INBOX/canvas-3.canvas"
```

- [ ] **Step 6: Move .base file and clean up empty "Sin nombre" folder**

```bash
VAULT="/Users/gsiglobalteamevent/Desktop/obsidiandiego/Sincro"

mv "$VAULT/Sin título.base" "$VAULT/00-INBOX/base-datos-1.base"
rmdir "$VAULT/Sin nombre" 2>/dev/null  # Remove only if empty
rmdir "$VAULT/Sin nombre 1" 2>/dev/null
```

- [ ] **Step 7: Verify vault root is clean**

Run: `ls "$VAULT"/*.md "$VAULT"/*.canvas "$VAULT"/*.base 2>/dev/null`
Expected: No files at root level (everything moved to folders)

Run: `find "$VAULT" -maxdepth 1 -type d | grep -v .obsidian | sort`
Expected: Only numbered folders (00-INBOX through 99-TEMPLATES)

---

## Task 6: Configure Obsidian Daily Notes

**Files:**
- Modify: `$VAULT/.obsidian/daily-notes.json`

- [ ] **Step 1: Configure daily notes to use 04-DIARIO folder**

Create/update file `$VAULT/.obsidian/daily-notes.json`:
```json
{
  "folder": "04-DIARIO",
  "format": "YYYY-MM-DD",
  "template": "99-TEMPLATES/tpl-daily"
}
```

- [ ] **Step 2: Verify by checking Obsidian recognizes the config**

Open Obsidian → Settings → Core Plugins → Daily Notes
Expected: Shows folder as "04-DIARIO" and template as "99-TEMPLATES/tpl-daily"

---

## Task 7: Document Obsidian Plugin Recommendations

Obsidian plugins must be installed through the Obsidian app UI (Settings → Community Plugins). This task creates a guide note in the vault.

**Files:**
- Create: `$VAULT/99-TEMPLATES/SETUP-PLUGINS.md`

- [ ] **Step 1: Create plugin installation guide**

Create file `$VAULT/99-TEMPLATES/SETUP-PLUGINS.md`:
```markdown
# Plugins Recomendados para Instalar

Abre Obsidian → Settings (gear icon) → Community Plugins → Browse

## Obligatorios

### 1. Templater
- **Buscar:** "Templater"
- **Por que:** Templates dinamicos con variables (fecha, titulo, etc.)
- **Config:** Settings → Templater → Template Folder: `99-TEMPLATES`

### 2. Calendar
- **Buscar:** "Calendar"
- **Por que:** Navegacion visual de daily notes en sidebar
- **Config:** Automatic (usa la config de Daily Notes)

### 3. Dataview
- **Buscar:** "Dataview"
- **Por que:** Queries dinamicos — ver todas las tareas delegadas, decisiones por proyecto, etc.
- **Config:** Enable JavaScript Queries = ON

## Opcionales (instalar despues)

### 4. Tasks
- **Buscar:** "Tasks"
- **Por que:** Gestion avanzada de tareas con fechas y prioridades

### 5. Tag Wrangler
- **Buscar:** "Tag Wrangler"
- **Por que:** Renombrar tags en batch, gestionar taxonomia
```

- [ ] **Step 2: Enable community plugins in Obsidian**

Open Obsidian → Settings → Community Plugins → Turn on community plugins (if not already enabled)
Then install: Templater, Calendar, Dataview (following the guide above)

---

## Task 8: Update Claude Memory with Obsidian Context

**Files:**
- Create: `~/.claude/projects/-Users-gsiglobalteamevent/memory/reference_obsidian_vault.md`
- Modify: `~/.claude/projects/-Users-gsiglobalteamevent/memory/MEMORY.md`

- [ ] **Step 1: Create reference memory for the vault**

Create file `~/.claude/projects/-Users-gsiglobalteamevent/memory/reference_obsidian_vault.md`:
```markdown
---
name: Obsidian Vault — Cerebro Digital
description: Diego's Obsidian vault structure and how Claude should interact with it via MCP
type: reference
---

## Vault Location
`/Users/gsiglobalteamevent/Desktop/obsidiandiego/Sincro/`

## MCP Server
`obsidian-mcp` configured in `~/.claude/settings.local.json`
Tools: read-note, create-note, edit-note, search-vault, move-note, create-directory, add-tags, manage-tags, list-available-vaults

## Structure
- 00-INBOX — brain dump, unclassified notes
- 01-PROYECTOS/{name}/_estado.md — project dashboards (each has decisiones/, notas/, tareas.md)
- 02-PERSONAS — team members and contacts
- 03-PLAYBOOKS — proven processes
- 04-DIARIO — daily notes (YYYY-MM-DD.md)
- 05-DECISIONES — cross-project decision log
- 06-TRADING — trading journal
- 07-DELEGADO — delegated task tracking
- 08-IDEAS — business ideas and opportunities
- 09-PERSONAL — goals, fitness, finances
- 99-TEMPLATES — note templates (tpl-*.md)

## Projects (as of 2026-04-09)
neomaaa-broker, neomaaa-funded, topstep, zendm, oxonntech, crm, crm-interno, mapa-estrategico, analisis-competencia

## How to Use
- When Diego mentions a project → check 01-PROYECTOS/{project}/_estado.md
- When he mentions a person → check 02-PERSONAS/
- When he makes a decision → log in 05-DECISIONES/ AND in the project's decisiones/ folder
- When he delegates → create note in 07-DELEGADO/
- When he writes in INBOX → classify and move to correct folder
- New project → clone _template-proyecto/ structure
```

- [ ] **Step 2: Update MEMORY.md index**

Add to `~/.claude/projects/-Users-gsiglobalteamevent/memory/MEMORY.md`:
```markdown
## References
- [reference_obsidian_vault.md](reference_obsidian_vault.md) — Obsidian vault structure, MCP config, and how Claude should interact with the digital brain
```

---

## Task 9: End-to-End Verification

- [ ] **Step 1: Verify MCP can read a project dashboard**

Run in Claude Code:
```
claude -p "Use the obsidian MCP to read the note at '01-PROYECTOS/neomaaa-broker/_estado.md'. Show me its contents."
```
Expected: Returns the full content of the broker _estado.md file

- [ ] **Step 2: Verify MCP can search the vault**

Run in Claude Code:
```
claude -p "Use the obsidian MCP to search the vault for 'Andrea'. List all notes that mention her."
```
Expected: Returns at least equipo-ventas-2026.md and neomaaa-funded/_estado.md

- [ ] **Step 3: Verify MCP can create a new note**

Run in Claude Code:
```
claude -p "Use the obsidian MCP to create a test note at '00-INBOX/test-mcp-connection.md' with content: 'MCP connection verified on 2026-04-09. This note was created by Claude.'"
```
Expected: Note created successfully

Then verify: `cat "$VAULT/00-INBOX/test-mcp-connection.md"`
Expected: Shows the content Claude wrote

- [ ] **Step 4: Verify MCP can edit a note**

Run in Claude Code:
```
claude -p "Use the obsidian MCP to edit the note at '00-INBOX/test-mcp-connection.md' and add a second line: 'Edit also works.'"
```
Expected: Note updated with the additional line

- [ ] **Step 5: Clean up test note**

```bash
rm "$VAULT/00-INBOX/test-mcp-connection.md"
```

- [ ] **Step 6: Final structure verification**

Run: `find "$VAULT" -maxdepth 1 -type d | grep -v .obsidian | sort`
Expected:
```
00-INBOX
01-PROYECTOS
02-PERSONAS
03-PLAYBOOKS
04-DIARIO
05-DECISIONES
06-TRADING
07-DELEGADO
08-IDEAS
09-PERSONAL
99-TEMPLATES
```

Run: `find "$VAULT/01-PROYECTOS" -maxdepth 1 -type d | sort`
Expected: 10 project directories (9 projects + _template-proyecto)

Run: `ls "$VAULT/99-TEMPLATES/"*.md | wc -l`
Expected: 8 (7 templates + SETUP-PLUGINS.md)
