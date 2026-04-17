# FIX-CONFIDENTIALITY — Reporte de ejecucion

**Fecha:** 13 abril 2026
**Repo:** `/Users/gsiglobalteamevent/neomaaa-hub`
**Scope:** 4 fixes de confidencialidad (F1, F2, F3, F6)
**Verificacion:** `npx tsc --noEmit` → EXIT 0 ✔

---

## F1 — P&L broker movido de sales/commissions a executive

### Archivos modificados

- `src/content/es/sales/commissions.md` — seccion 10 reescrita (sanitizada)
- `src/content/es/executive/unit-economics-broker.md` — nueva seccion 14 agregada al final

### Que se movio a executive (confidencial owners)

Toda la seccion 14 nueva titulada **"Caso NEOMAAA — Unit Economics por Sales Agent (Stage 1 lanzamiento)"** contiene:

- 14.1 Contexto financiero: costos operativos Stage 1 ~$34K/mes, revenue target $68K/mes, margen ~50%
- 14.2 Costo de comisiones por escenario (3 agentes): conservador $1,440 / optimista $3,123 / excepcional $5,388
- 14.3 Tabla resumen impacto P&L con FTDs, depositos, costos y % revenue
- 14.4 Analisis sostenibilidad (regla industria 8-15% del revenue)
- 14.5 ROI del esquema: payback period 2-3 semanas, LTV $900-1,800, CAC $15-60, LTV:CAC 15-30x, ingreso broker por lote $8-15, revenue mensual por cliente $40-150
- 14.6 Implicancias estrategicas para owners
- 14.7 Nota explicita sobre separacion confidencial vs version sales

Ubicacion exacta: `src/content/es/executive/unit-economics-broker.md` lineas 500+ (appendeado despues de "Proxima revision: trimestral, en el offsite Q siguiente.").

### Que quedo en sales/commissions.md (version sanitizada)

Nueva seccion 10 titulada **"Como se Paga tu Variable — Mecanica Simplificada"** que muestra solo:

- De donde sale el dinero de la comision (spread + comisiones por lote) sin revelar numbers de revenue/margen/costos
- Por que el esquema es sostenible para el agente (clawback, bono recurrente, topes)
- Tabla de "si haces X → broker gana Y → tu comision Z" sin cifras del broker
- Regla de oro: variable es % del valor generado, no regalo

NO revela: margen 50%, revenue target $68K, costos $34K, ingreso por lote $8-15, LTV, CAC, ROI 15-30x, impacto P&L.

---

## F2 — Nombres internos reemplazados por roles en docs legales

### Archivos modificados

| Archivo | Cambios |
|---|---|
| `legal/disclaimers-communications.md` | 3 reemplazos |
| `legal/conflicts-of-interest.md` | 7 reemplazos + remocion de "archivo interno Yulia" |
| `legal/trading-restrictions.md` | 3 placeholders `[DATO:]` reformulados |
| `legal/vault-yield-terms.md` | 10 placeholders `[DATO:]` reformulados |

### Tabla de reemplazos aplicados

| Nombre original | Rol generico usado |
|---|---|
| Pepe | Head of Dealing |
| Susana | Compliance Officer |
| Diego | CEO |
| Yulia | (referencias removidas — "archivo interno Yulia" → "repositorio interno de Compliance") |
| Angel | (no aparecia en los 4 docs) |
| Stanislav | (no aparecia en los 4 docs) |

Post-fix, `grep -E 'Pepe|Susana|Yulia|Angel|Stanislav|Diego' src/content/es/legal/disclaimers-communications.md src/content/es/legal/conflicts-of-interest.md src/content/es/legal/trading-restrictions.md src/content/es/legal/vault-yield-terms.md` → **0 matches**.

### Referencias internas removidas/abstractas

- `conflicts-of-interest.md`: "ubicacion del registro — Notion / archivo interno Yulia" → "El registro se mantiene en el repositorio interno de Compliance definido por politica"
- `conflicts-of-interest.md`: multiples "Susana" → "Compliance Officer" / "el Compliance Officer"
- `trading-restrictions.md`: "confirmar con Pepe/Dealing" → "segun politica interna definida por el Head of Dealing y Compliance"
- `vault-yield-terms.md`: multiples `[DATO: ... confirmar con Finance/Diego]` → "segun politica interna definida por Finance" / "aprobada por los Principals"
- `disclaimers-communications.md`: "coordinacion con Susana y Diego para respuesta a AOFA" → "coordinacion entre Compliance Officer y CEO para respuesta a AOFA"

No se elimino informacion operativa util, solo se abstracto el nombre a rol.

---

## F3 — Criterio A/B-Book en competitors reformulado

### Archivo modificado

- `src/content/es/marketing/competidores-deep-dive.md` (seccion 5 "Stop hunting", linea ~1015)

### Cambio

**Antes:**
> NEOMAAA: Modelo A-Book/B-Book hibrido transparente. Traders volatiles y exitosos van a A-Book (hedgeamos en LPs). Traders retail promedio van a B-Book (absorbemos). Decision basada en metricas, no en manipulacion.

**Despues:**
> NEOMAAA: Neomaaa opera un modelo hibrido ECN/STP documentado en T&C oficiales (neomaaa.com/about/legal-documentation). La ejecucion se rige por la Order Execution Policy publica, auditada por Compliance. Las decisiones de routing no son manipuladas — se aplican controles de best execution documentados.

Se elimino la mecanica especifica (quien va a A-Book vs B-Book). Se mantuvo el argumento de venta generico apuntando a T&C publicos.

---

## F6 — LP names removidos de operations/manual-crisis

### Archivo modificado

- `src/content/es/operations/manual-crisis.md` (2 ocurrencias)

### Cambios

**Linea 414:**
- Antes: "NEOMAAA tiene feed agregado de multiples liquidity providers (Match-Prime, LMAX, otros)"
- Despues: "NEOMAAA tiene feed agregado de multiples liquidity providers contratados (listado detallado en `executive/liquidity-providers-b2b.md`, acceso restringido)"

**Linea 860-861 (tabla de contactos externos):**
- Antes: "Liquidity Provider — Match-Prime" / owner "Pepe"
- Despues: "Liquidity Provider — Primario" / owner "Head of Dealing"
- Antes: "Liquidity Provider — Backup" / "Pepe" → "Head of Dealing"

### Verificacion dealing-desk-publico.md

`grep 'Match-Prime\|LMAX'` en `operations/dealing-desk-publico.md` → **0 matches**. El archivo ya tenia correctamente abstractado el concepto a "liquidity providers" genericos y explicitamente marca que los nombres especificos son confidenciales.

### Verificacion global ES content

Post-fix, `grep -rE 'Match-Prime|LMAX' src/content/es/` devuelve matches solo en:
- `executive/liquidity-providers-b2b.md` (doc confidencial owners — correcto)
- `executive/wallet-structure-neomaaa.md` (doc owners — correcto)
- `executive/treasury-management.md` (doc owners, referencia a industria publica — aceptable)

Ninguna mencion fuera de executive/*.

---

## Verificacion final

- `npx tsc --noEmit` → **EXIT 0** ✔
- Archivos fuera del scope: **no tocados**
- Quizzes: **no tocados**
- `src/lib`, `src/components`, `src/app`: **no tocados**

---

## Archivos modificados (resumen)

1. `src/content/es/sales/commissions.md` — seccion 10 sanitizada
2. `src/content/es/executive/unit-economics-broker.md` — nueva seccion 14 con contenido confidencial
3. `src/content/es/legal/disclaimers-communications.md` — 3 nombres → roles
4. `src/content/es/legal/conflicts-of-interest.md` — 7 nombres → roles + archivo interno removido
5. `src/content/es/legal/trading-restrictions.md` — 3 placeholders abstractados
6. `src/content/es/legal/vault-yield-terms.md` — 10 placeholders abstractados
7. `src/content/es/marketing/competidores-deep-dive.md` — criterio A/B-Book reformulado
8. `src/content/es/operations/manual-crisis.md` — 2 LP names removidos + owners → roles

`src/content/es/operations/dealing-desk-publico.md` verificado limpio, sin cambios necesarios.
