# Cerebro Digital: Obsidian + Claude — Design Spec

**Fecha:** 2026-04-09
**Autor:** Diego + Claude
**Estado:** Aprobado para implementación

---

## 1. Problema

El conocimiento de Diego está fragmentado entre su cabeza, chats de Telegram, conversaciones con Claude, y un vault de Obsidian sin estructura. Resultado: pierde tareas prometidas, contexto de decisiones, y estado real de proyectos. Cada conversación con Claude empieza de cero.

## 2. Solución

Un cerebro digital en 3 capas donde:
- **Capa 1 (Memory):** Perfil de Diego, preferencias, feedback — se carga automático.
- **Capa 2 (Vault Obsidian vía MCP):** Proyectos, personas, decisiones, playbooks, diario, trading, ideas, personal — Claude busca, lee, crea y edita.
- **Capa 3 (CLAUDE.md por repo):** Contexto técnico de cada repositorio de código.

## 3. Enfoque Técnico: Híbrido

- **MCP Server** para Obsidian (búsqueda inteligente + acceso estructurado)
- **File I/O directo** para operaciones rápidas y templates
- **Auto-memory de Claude** para perfil y preferencias persistentes

## 4. Vault Target

- **Ubicación:** `/Users/gsiglobalteamevent/Desktop/obsidiandiego/Sincro/`
- **Estado actual:** 18 notas sueltas sin estructura, 4 canvas, cero plugins
- **Sincronización:** Obsidian Sync activo

## 5. Estructura del Vault

```
Sincro/
├── 00-INBOX/                    ← Brain dump libre
├── 01-PROYECTOS/                ← Un directorio por proyecto (escalable)
│   ├── neomaaa-broker/
│   │   ├── _estado.md
│   │   ├── decisiones/
│   │   ├── tareas.md
│   │   └── notas/
│   ├── neomaaa-funded/
│   ├── topstep/
│   ├── zendm/
│   ├── oxonntech/
│   ├── crm/
│   ├── crm-interno/
│   ├── mapa-estrategico/
│   ├── analisis-competencia/
│   └── _template-proyecto/
├── 02-PERSONAS/
├── 03-PLAYBOOKS/
├── 04-DIARIO/
├── 05-DECISIONES/
├── 06-TRADING/
├── 07-DELEGADO/
├── 08-IDEAS/
├── 09-PERSONAL/
└── 99-TEMPLATES/
```

### 5.1 Proyectos (01-PROYECTOS/)

Cada proyecto es una carpeta autónoma con estructura interna idéntica:

```
proyecto-x/
├── _estado.md       ← Dashboard: estado, velocidad, equipo, pendientes, decisiones
├── decisiones/      ← Log de decisiones del proyecto
├── tareas.md        ← Pendientes activos
└── notas/           ← Notas relacionadas al proyecto
```

**Proyectos iniciales (9):**

| Proyecto | Descripción | Links |
|----------|-------------|-------|
| neomaaa-broker | Broker forex/CFD | neomaaa.com, neomaaa-broker.vercel.app |
| neomaaa-funded | Prop firm de fondeo | neomaaafunded.com, neomaaa-dashboard.vercel.app |
| topstep | Vencer empresas de fondeo (personal) | proptrading-research repo |
| zendm | SaaS Discord DM marketing | zendm.io |
| oxonntech | Sitio tech + blog | oxonntech repo |
| crm | CRM Dashboard | crmntmv9 repo |
| crm-interno | CRM personal de Diego | Por crear |
| mapa-estrategico | Mapa estratégico del negocio | Por crear |
| analisis-competencia | Análisis de competidores | Por crear |

**Escalabilidad:** Nuevos proyectos se crean clonando `_template-proyecto/`.

### 5.2 Personas (02-PERSONAS/)

Una nota por persona o grupo. Campos: nombre, rol, proyecto(s), contacto, último compromiso, historial de interacciones.

### 5.3 Playbooks (03-PLAYBOOKS/)

Procesos repetibles probados. Campos: qué es, cuándo usarlo, pasos, lecciones aprendidas.

### 5.4 Diario (04-DIARIO/)

Daily notes con estructura:
1. Panorama del día + sugerencia de prioridades (Claude genera)
2. Espacio libre para escribir (Diego escribe)
3. Delegado pendiente de follow-up (Claude genera)
4. Decisiones del día (Claude detecta y llena)
5. Cierre del día (Claude genera resumen)

### 5.5 Decisiones (05-DECISIONES/)

Log global de decisiones cross-proyecto. Campos: qué se decidió, por qué, qué se descartó, quién estuvo, fecha. Las decisiones específicas de un proyecto también se linkean desde la carpeta del proyecto.

### 5.6 Trading (06-TRADING/)

Journal de trading separado. Operaciones, reglas operativas, análisis post-trade, evolución.

### 5.7 Delegado (07-DELEGADO/)

Tracking de tareas delegadas. Campos: a quién, cuándo, deadline, status, proyecto relacionado.

### 5.8 Ideas (08-IDEAS/)

Capturas rápidas de oportunidades y ideas de negocio.

### 5.9 Personal (09-PERSONAL/)

Metas de vida, fitness (Muay Thai), finanzas personales, hábitos.

### 5.10 Templates (99-TEMPLATES/)

Plantillas que Claude usa para crear notas consistentes:
- tpl-proyecto.md (estructura _estado.md)
- tpl-persona.md
- tpl-decision.md
- tpl-daily.md
- tpl-delegado.md
- tpl-idea.md
- tpl-playbook.md

## 6. Auto-organización Inteligente

### Flujo:
1. Diego escribe libre (INBOX, daily, nota nueva — como piense)
2. Claude analiza la nota y detecta: proyecto, personas, decisiones, tareas, delegaciones
3. Claude clasifica: mueve/linkea a la carpeta correcta
4. Claude actualiza: `_estado.md` del proyecto, notas de personas, log de decisiones
5. Claude agrega frontmatter YAML y [[wikilinks]]

### Frontmatter estándar:
```yaml
---
proyecto: neomaaa-broker
personas: [Andrea, Franco]
tipo: update | decision | task | idea | personal
fecha: 2026-04-09
tags: [ventas, comisiones]
---
```

## 7. Configuración Técnica

### 7.1 MCP Server para Obsidian
- Instalar MCP server compatible con Obsidian (investigar mejor opción: obsidian-mcp o file-based)
- Configurar en `~/.claude/settings.json` o `settings.local.json`
- Capacidades requeridas: read, search, create, edit notas del vault

### 7.2 Plugins de Obsidian a instalar
- **Templater** — templates dinámicos con variables
- **Calendar** — navegación de daily notes
- **Dataview** — queries dinámicos sobre las notas (dashboards)
- **Tags** — gestión de tags para clasificación

### 7.3 Claude Memory
- Ya configurada. Actualizar con perfil completo de productividad de Diego (hecho).

## 8. Perfil de Productividad de Diego

- **Priorización:** Sin sistema fijo. Quiere híbrido: Claude sugiere, Diego decide.
- **Proyectos:** Independientes entre sí. Clasificación mental por proyecto.
- **Decisiones:** No las registra → mayor pain point a resolver.
- **Equipo:** 16+ personas, algunos comparten proyectos. Comunicación por Telegram.
- **Rutina:** Semi-estructurada. Trading en horas de mercado, resto fluye.
- **Métrica de éxito:** Velocidad de ejecución (momentum).
- **Delegación:** Follow-up manual sin sistema.
- **Tiempo disponible:** 30+ min/día para Obsidian.
- **Hábito actual:** Todavía no consolidado — diseño debe ser de baja fricción.

## 9. Migración de Notas Existentes

Las 18 notas actuales del vault serán leídas, clasificadas, y distribuidas en la nueva estructura por Claude. Nada se borra — todo se mueve.

## 10. Evolución Esperada

- **Mes 1:** Proyectos organizados, equipo documentado, daily notes funcionando.
- **Mes 2:** Historial de decisiones acumulado, follow-up de delegación automatizado.
- **Mes 3:** Claude conoce patrones, puede anticipar bloqueos y sugerir con contexto real.
- **Mes 6:** Cerebro digital completo — chief of staff digital operativo.
