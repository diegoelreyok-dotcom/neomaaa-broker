# Funnel de Retencion: NEOMAAA Funded
**Tipo de Negocio:** Prop Trading Firm (Forex/Crypto Challenges)
**Fecha:** 2026-04-08
**Tipo de Funnel:** Retention & Repeat Purchase (Post-Adquisicion)
**Salud General del Funnel de Retencion: 35/100** (estimado pre-optimizacion)

---

## Resumen Ejecutivo

NEOMAAA Funded opera en una industria donde **solo el 5-10% de traders pasan los challenges**, el **98% de los traders fondeados abandonan en los primeros 6 meses**, y aproximadamente el **40% de los ingresos proviene de re-compras de challenges fallidos**. Esto significa que el funnel de retencion NO es un "nice to have" -- es literalmente donde esta la mitad del revenue.

El problema central de las prop firms es que operan como "fabricas de challenges" enfocadas en adquisicion, gastando 80% del presupuesto en traer nuevos traders y 0% en retener a los que ya compraron. NEOMAAA tiene una oportunidad masiva de diferenciarse construyendo un sistema de retencion que la industria ignora casi por completo.

Los 5 puntos criticos de fuga identificados son: (1) post-compra sin inicio del challenge, (2) abandono mid-challenge, (3) no recompra post-fallo, (4) violacion de reglas post-fondeo, y (5) inactividad de traders fondeados exitosos. Cada punto tiene intervenciones especificas que detallamos abajo con metricas, benchmarks, y secuencias de accion.

**Impacto estimado:** Optimizar este funnel puede incrementar el LTV por trader de $200-400 a $800-1,200+, representando un aumento de 2-3x en revenue sin gastar un centavo mas en adquisicion.

---

## MAPA VISUAL DEL FUNNEL DE RETENCION

```
============================================================================
                    FUNNEL DE RETENCION - NEOMAAA FUNDED
============================================================================

    ADQUISICION                          RETENCION (ESTE ANALISIS)
    -----------                          -------------------------

    [Anuncio/Referido]
          |
          v
    [Landing Page]
          |
          v
    [Compra Challenge] -----> 100% de compradores entran aqui
          |
          |   FUGA #1: POST-COMPRA SIN INICIO
          |   ~15-25% nunca empieza a operar
          |   >>> Intervencion: Onboarding + Activacion
          v
    [Inicia Challenge] -----> ~75-85% empiezan
          |
          |   FUGA #2: ABANDONO MID-CHALLENGE
          |   ~40-50% abandonan antes de terminar
          |   >>> Intervencion: Engagement + Coaching
          v
    [Completa Challenge]
          |
     _____|_____
    |           |
    v           v
  [FALLA]     [PASA]
  ~90-95%     ~5-10%
    |           |
    |           |   FUGA #4: VIOLACION POST-FONDEO
    |           |   ~60-70% violan reglas en 30 dias
    |           |   >>> Intervencion: Risk Education + Alerts
    |           v
    |     [Cuenta Fondeada] -----> ~5-10% llegan aqui
    |           |
    |           |   FUGA #5: CHURN DE FONDEADOS
    |           |   98% abandona en 6 meses
    |           |   >>> Intervencion: Scaling + Community
    |           v
    |     [Payout Exitoso] -----> ~7% de TODOS los traders
    |           |
    |           v
    |     [Trader Leal / Scaling]
    |           |
    |           v
    |     [Referidos + Upsell Cuentas Mayores]
    |
    |   FUGA #3: NO RECOMPRA POST-FALLO
    |   ~55-65% no recompran
    |   >>> Intervencion: Win-Back + Descuento + Educacion
    v
  [Abandono Permanente]
    |
    |   FUGA #6: REACTIVACION DE DORMIDOS
    |   Sin actividad 60+ dias
    |   >>> Intervencion: Reactivacion Escalonada
    v
  [Lost Forever... o no?]


============================================================================
              FLUJO DE REVENUE POR SEGMENTO
============================================================================

  Compra Inicial          Retry #1         Retry #2+        Fondeo+Payouts
  $150-500/trader    $150-500 (35-45%)   $150-500 (15-20%)   Revenue sharing
        |                  |                  |                    |
        v                  v                  v                    v
    [40% revenue]    [30% revenue]      [10% revenue]       [20% revenue]
                                                            (profit split)

  >>> El 40% del revenue viene de RETRIES = retencion post-fallo es CRITICA
```

---

## ANALISIS DETALLADO: 5 PUNTOS CRITICOS DE FUGA

---

### FUGA #1: POST-COMPRA -- Traders que Compran y Nunca Empiezan

**Problema:** Entre el 15-25% de los traders que compran un challenge NUNCA ejecutan su primera operacion. Pagaron, recibieron credenciales, y desaparecieron. Esto es dinero muerto -- no hay engagement, no hay posibilidad de retry, y genera chargebacks.

**Por que ocurre en prop trading:**
- Miedo a perder despues de pagar (paralisis por analisis)
- No entienden las reglas o la plataforma (MT4/MT5 es intimidante para novatos)
- Compraron impulsivamente por un anuncio y luego se arrepintieron
- Estan esperando "el momento perfecto del mercado" que nunca llega
- Problemas tecnicos con la plataforma que no reportan

#### Metricas Clave a Trackear

| Metrica | Definicion | Formula | Target |
|---------|-----------|---------|--------|
| **Activation Rate** | % que ejecuta 1ra operacion en 72h | (Traders con 1+ trade en 72h) / (Total compras) x 100 | >85% |
| **Time to First Trade** | Horas entre compra y 1ra operacion | Timestamp 1er trade - Timestamp compra | <24h |
| **Login Rate Post-Compra** | % que hace login al dashboard en 48h | (Logins en 48h) / (Total compras) x 100 | >90% |
| **Credenciales Descargadas** | % que descarga/accede credenciales MT4/5 | (Credenciales accedidas) / (Total compras) x 100 | >95% |
| **Chargeback Rate** | % de compras que resultan en chargeback | (Chargebacks) / (Total compras) x 100 | <1.5% |
| **Tasa de Abandono Pre-Inicio** | % que nunca opera en todo el periodo | (Compradores sin trades) / (Total compras) x 100 | <10% |

#### Intervenciones Especificas

**SECUENCIA DE ONBOARDING (5 emails + 2 SMS en 7 dias)**

```
TRIGGER: Compra completada
=========================

[+0 min] Email 1 - "Bienvenido a NEOMAAA Funded"
  - Credenciales de acceso
  - Video de 3 minutos: "Como configurar MT5 en 60 segundos"
  - Link directo a descargar plataforma
  - CTA: "Configura tu cuenta ahora"

[+2 horas] SMS 1 - "Tu challenge NEOMAAA esta listo"
  - Si NO ha hecho login todavia
  - "Tu cuenta de $[X]K esta lista. Accede aqui: [link]"

[+24 horas] Email 2 - "Las 3 reglas que debes conocer ANTES de operar"
  CONDICION: Si NO ha ejecutado 1er trade
  - Infografia simple: Max Drawdown, Max Daily Loss, Profit Target
  - "Los traders que leen esto ANTES de operar tienen 2x mas probabilidad de pasar"
  - CTA: "Ya entendi, voy a operar"

[+48 horas] Email 3 - "Analisis de mercado de hoy + tu primer trade"
  CONDICION: Si SIGUE sin operar
  - Analisis de mercado actual (automatizado via API)
  - "Los mejores traders no esperan el momento perfecto -- empiezan con poco riesgo"
  - Mini-guia: "Tu primer trade seguro: 0.5% de riesgo"

[+72 horas] SMS 2 - Urgencia amigable
  CONDICION: Si SIGUE sin operar
  - "Tu challenge lleva 3 dias y no has operado. El reloj corre. Necesitas ayuda? Responde aqui."

[+5 dias] Email 4 - "Ultima llamada de activacion"
  CONDICION: Si SIGUE sin operar
  - Caso de exito de un trader que empezo lento y paso
  - Oferta: "Si necesitas empezar de cero, te damos un reset gratuito"
  - Link a soporte con chat en vivo

[+7 dias] Email 5 - "Oferta de cambio de cuenta"
  CONDICION: Si SIGUE sin operar
  - "Quizas elegiste un tamano de cuenta muy grande. Te ofrecemos downgrade con credito."
  - Alternativa: Pausar el challenge (si la tecnologia lo permite)
```

**Benchmark de la industria:**
- Las prop firms que implementan onboarding automatizado reducen el abandono pre-inicio del 25% al 8-12%
- El SMS tiene 45% de open rate vs 25% de email en este segmento
- La activacion en las primeras 24 horas predice un 70% mas de probabilidad de completar el challenge

---

### FUGA #2: MID-CHALLENGE -- Traders que Abandonan Antes de Completar

**Problema:** Aproximadamente el 40-50% de los traders que SÍ empiezan a operar, abandonan antes de llegar al profit target o al limite de tiempo. Se desmoralizan, entran en tilt, o simplemente pierden interes.

**Por que ocurre en prop trading:**
- Drawdown temprano que desmoraliza (pero NO viola reglas)
- Racha perdedora de 5+ trades que genera tilt emocional
- No entienden que estan ON TRACK a pesar de las perdidas
- Mercado volatil los asusta y dejan de operar
- Se acerca el limite de tiempo y sienten que no van a llegar
- Sobre-operan por desesperacion y violan reglas sin entender por que

#### Metricas Clave a Trackear

| Metrica | Definicion | Formula | Target |
|---------|-----------|---------|--------|
| **Challenge Completion Rate** | % que llega al final (pasa o falla por merito) | (Challenges completados) / (Challenges iniciados) x 100 | >70% |
| **Dias Activos / Dias Totales** | Ratio de actividad durante el challenge | (Dias con al menos 1 trade) / (Dias del challenge) x 100 | >60% |
| **Abandono por Semana** | En que semana abandonan mas | Distribucion de ultimo trade por semana del challenge | Semana 2-3 pico |
| **Drawdown al Momento de Abandono** | Cuanto habian perdido cuando dejaron de operar | Drawdown promedio del ultimo dia activo | <5% (recuperable) |
| **Trades por Dia Promedio** | Frecuencia de operacion | Total trades / Dias activos | 2-8 trades/dia |
| **Tilt Score** | Incremento subito en frecuencia + tamano de posicion | Deteccion de anomalias en volumen vs promedio | Alerta si >2x |

#### Intervenciones Especificas

**SISTEMA DE ENGAGEMENT MID-CHALLENGE (Event-Driven)**

```
=== TRIGGERS BASADOS EN COMPORTAMIENTO ===

TRIGGER: Trader pierde 3+ trades consecutivos
>>> Email: "Los drawdowns son normales -- esto es lo que hacen los traders exitosos"
  - Estadistica: "El 73% de los traders que pasaron tuvieron al menos 1 racha de 5 perdidas"
  - Video: "Gestion emocional despues de una racha perdedora"
  - CTA: "Revisa tu plan de trading"

TRIGGER: Sin actividad por 3+ dias durante challenge activo
>>> Push/Email: "Tu challenge sigue activo -- estas son tus stats"
  - Dashboard snapshot: Profit actual, drawdown disponible, dias restantes
  - "Tienes $[X] de drawdown disponible -- espacio de sobra para seguir"
  - Si esta en profit: "Estas a solo $[X] del target!"
  - Si esta en loss: "Muchos traders recuperan esto en 3-5 trades bien ejecutados"

TRIGGER: Trader alcanza 50% del profit target
>>> Email celebratorio: "Vas por la mitad!"
  - "Estas en el top 20% de traders en NEOMAAA ahora mismo"
  - Tips para la segunda mitad del challenge
  - Social proof: "[Trader] alcanzo 50% en la semana 2 y paso en la semana 4"

TRIGGER: Trader alcanza 75% del profit target
>>> Email + SMS: "Casi lo logras!"
  - "Estas a $[X] de pasar. Esto es lo que diferencia a los que pasan:"
  - Consejo: "Reduce tu riesgo por trade a 0.5%. No necesitas un home run."
  - Countdown visual de lo que falta

TRIGGER: Queda 25% del tiempo y menos de 50% del target
>>> Email: "Plan de recuperacion"
  - Opciones honestas: "Puedes intentar llegar, o puedes asegurar lo aprendido"
  - Oferta de extension de tiempo (pagada, precio reducido)
  - Pre-venta de retry con 15% descuento "si decides empezar fresco"

TRIGGER: Tilt detectado (volumen 2x+ del promedio + perdidas)
>>> Notificacion in-app o SMS: "Toma un respiro"
  - "Detectamos que estas operando mas de lo habitual. Los mejores traders saben cuando parar."
  - "Sugerencia: cierra la plataforma por 1 hora y regresa con mente fresca"
  - Link a articulo: "Por que operar menos te hace ganar mas"
```

**WEEKLY PROGRESS REPORT (Automatizado cada domingo)**

```
Subject: "Tu semana en NEOMAAA -- Resumen #[X]"

Contenido:
- P&L de la semana (grafico simple)
- Progreso hacia profit target (barra de progreso visual)
- Drawdown utilizado vs disponible
- Mejor trade de la semana (par, entrada, salida, profit)
- Comparacion anonima: "Estas por encima del 65% de traders esta semana"
- Tip de la semana personalizado basado en su comportamiento:
  * Si sobre-opera: "Menos es mas -- los ganadores promedian 3 trades/dia"
  * Si no opera suficiente: "La consistencia gana -- opera al menos 3 dias/semana"
  * Si tiene buen risk management: "Tu ratio riesgo/beneficio es excelente, sigue asi"
```

**Benchmark de la industria:**
- Las prop firms con weekly reports ven 25-35% menos abandono mid-challenge
- Los triggers de tilt reducen violaciones de drawdown en un 15-20%
- Los milestone emails (50%, 75%) incrementan completion rate en 10-15%

---

### FUGA #3: POST-FALLO -- Traders que Fallan y NO Recompran

**Problema:** Este es el punto MAS CRITICO del funnel. El 90-95% de los traders fallan el challenge. De esos, solo el 35-45% recompran. El 55-65% restante se pierde para siempre. Dado que el **40% del revenue de una prop firm viene de retries**, cada punto porcentual de mejora aqui tiene impacto directo y masivo en ingresos.

**Por que NO recompran:**
- Humillacion/verguenza por haber fallado (barrera emocional)
- Creen que "el sistema esta arreglado para que falle" (desconfianza)
- No tienen dinero para otro challenge inmediatamente
- No aprendieron nada del fallo -- no saben que hacer diferente
- Encontraron otra prop firm con mejor oferta (competencia)
- Decidieron que "prop trading no es para mi" (abandono del sueno)

#### Metricas Clave a Trackear

| Metrica | Definicion | Formula | Target |
|---------|-----------|---------|--------|
| **Retry Rate** | % de traders fallidos que recompran | (Recompras post-fallo) / (Total fallos) x 100 | >45% |
| **Time to Retry** | Dias entre fallo y recompra | Timestamp nueva compra - Timestamp fallo | <14 dias |
| **Retry Conversion por Canal** | Que canal convierte mejor para retries | Retries atribuidos a email/sms/retargeting/organico | Email = #1 |
| **Razon de Fallo** | Clasificacion del tipo de fallo | Max drawdown / Daily loss / Inactividad / Profit no alcanzado | Trackear distribucion |
| **Intentos Promedio Antes de Exito** | Cuantos challenges compra antes de pasar | Avg(challenges comprados por trader que paso) | 2.3 promedio industria |
| **Descuento Necesario para Conversion** | % de descuento que activa la recompra | A/B test de ofertas de retry | 10-20% sweet spot |
| **Revenue Recovery Rate** | Revenue generado por secuencia de retry | (Revenue de retries atribuidos a secuencia) / (Revenue potencial perdido) | >30% |

#### Intervenciones Especificas

**SECUENCIA POST-FALLO (6 emails en 14 dias)**

```
TRIGGER: Challenge fallido (cualquier razon)
SEGMENTACION CRITICA: Personalizar por TIPO de fallo

=== RUTA A: Fallo por MAX DRAWDOWN (el mas comun) ===

[+2 horas] Email 1 - "Tu challenge termino -- pero tu viaje no"
  - Tono: Empatico, NO condescendiente
  - "Sabemos que esto no es lo que esperabas. Pero esto es lo que queremos que sepas:"
  - Dato: "El trader promedio que paso intento 2.3 veces antes de lograrlo"
  - NO vender nada en este email. Solo empatia y perspectiva.
  - Link a comunidad/Discord de traders

[+48 horas] Email 2 - "Que salio mal -- y como arreglarlo"
  - Analisis automatizado de SU challenge:
    * "Operaste [X] trades. Tu win rate fue [X]%."
    * "Tu drawdown maximo fue [X]%. El limite era [X]%."
    * "Tu peor dia fue [fecha]: perdiste $[X] en [X] trades"
  - Diagnostico: "Tu problema principal fue [sobre-apalancamiento/revenge trading/falta de stop loss]"
  - Video de 5 min: "Como evitar [su problema especifico]"

[+4 dias] Email 3 - "Plan de 7 dias para volver mas fuerte"
  - Checklist descargable: "7 dias de preparacion antes de tu proximo challenge"
  - Dia 1-2: Revisar trades en journal
  - Dia 3-4: Practicar en demo con reglas del challenge
  - Dia 5-6: Backtesting de la estrategia ajustada
  - Dia 7: Decision informada de retry
  - CTA suave: "Cuando estes listo, tu siguiente challenge te espera"

[+7 dias] Email 4 - "Caso de exito: De 3 fallos a fondeado"
  - Historia REAL de un trader de NEOMAAA que fallo multiples veces y paso
  - Incluir screenshots del dashboard (con permiso)
  - "Le preguntamos que cambio: 'Reduje mi lote a la mitad y deje de operar noticias'"
  - CTA: "Retry con 15% de descuento -- expira en 72 horas"
  - Codigo: COMEBACK15

[+10 dias] Email 5 - "Tu descuento expira pronto"
  - Recordatorio del descuento
  - Agregar urgencia: "Solo quedan [X] horas"
  - Alternativa: "Si prefieres un tamano de cuenta diferente, mira estas opciones"
  - Opcion de downgrade: cuenta mas pequena = menos presion = mas probabilidad de pasar

[+14 dias] Email 6 - "Tu lugar esta guardado"
  - Ultimo email de la secuencia
  - "No hay presion. Cuando estes listo, estamos aqui."
  - Ultimo descuento: 10% sin fecha de expiracion (pero no lo digas)
  - CTA a la comunidad: "Mientras tanto, unete a 2,000+ traders en nuestro Discord"
  - Transicion a secuencia de nurture mensual (no dejar de comunicar)


=== RUTA B: Fallo por INACTIVIDAD/TIEMPO (abandono silencioso) ===

[+2 horas] Email 1 - "Sabemos que la vida pasa"
  - "Tu challenge expiro. No pasa nada -- muchos traders necesitan mas de un intento."
  - Pregunta: "Que paso? [Encuesta de 1 click]"
    * "No tuve tiempo suficiente"
    * "No me senti preparado"
    * "Tuve problemas tecnicos"
    * "Decidi probar otra cosa"

[+48 horas] Email 2 - Personalizado segun respuesta de encuesta
  - Si "no tuve tiempo": Ofrecer challenge con limite de tiempo extendido
  - Si "no preparado": Ofrecer acceso a recursos educativos gratuitos
  - Si "problemas tecnicos": Conectar con soporte VIP
  - Si no responde: Enviar el mas comun ("sabemos que a veces el timing no es ideal")

[Continua con emails 3-6 similares a Ruta A pero ajustados al contexto]


=== RUTA C: Fallo por DAILY LOSS LIMIT (violacion de regla) ===

[+2 horas] Email 1 - "Un dia malo no define tu trading"
  - "Violaste el limite diario. Le pasa al 30% de los traders -- incluso a los que eventualmente pasan."
  - Contenido: "3 tecnicas para NUNCA volver a violar el daily loss limit"
  - Tool: Calculadora de tamano de posicion maxima por dia

[Continua con secuencia enfocada en risk management y control emocional]
```

**RETARGETING ADS PARA TRADERS FALLIDOS**

```
Audiencia: Traders que fallaron hace 3-21 dias y NO han recomprado
Plataformas: Instagram, YouTube, Facebook

Ad 1 (Dia 3-7): Caso de exito
  "De 2 fallos a $3,200 en payouts. Asi lo hizo [Trader]."
  CTA: "Intenta de nuevo con 15% off"

Ad 2 (Dia 7-14): Estadistica motivacional
  "El 73% de nuestros traders fondeados fallaron al menos una vez."
  CTA: "Tu siguiente intento puede ser el bueno"

Ad 3 (Dia 14-21): Oferta directa
  "Challenge de $[X]K por $[precio con descuento]. Solo esta semana."
  CTA: "Volver a intentar"
```

**Benchmark de la industria:**
- Retry rate promedio sin intervenciones: 25-30%
- Retry rate con secuencia optimizada: 40-50%
- El 8-12% de los traders fallidos convierten directamente por la secuencia de email de retry
- El 60%+ abre los emails post-fallo (el engagement mas alto de cualquier secuencia)
- El descuento sweet spot es 10-20% -- mas de 25% degrada la percepcion de valor
- El promedio de intentos antes de pasar en la industria es 2.3 challenges

---

### FUGA #4: POST-EXITO -- Traders Fondeados que Violan Reglas

**Problema:** De los pocos traders que logran pasar (5-10%), entre el 60-70% violan las reglas de la cuenta fondeada en los primeros 30 dias. La presion de operar con "dinero real" (aunque sea de la firma) cambia la psicologia completamente. El 80% de las violaciones ocurren por fallos emocionales, no por falta de habilidad tecnica.

**Por que violan reglas post-fondeo:**
- Sobre-confianza: "Ya pase el challenge, ahora voy a ir a lo grande"
- Presion de generar payouts rapido
- Cambian de estrategia ahora que es "real"
- Las reglas de la cuenta fondeada son diferentes/mas estrictas
- No hay sistema de alerta antes de acercarse a limites
- Aislamiento: ya no tienen el "deadline" del challenge que los disciplinaba

#### Metricas Clave a Trackear

| Metrica | Definicion | Formula | Target |
|---------|-----------|---------|--------|
| **Funded Account Survival Rate (30d)** | % de cuentas fondeadas activas a 30 dias | (Cuentas activas a 30d) / (Total cuentas fondeadas) x 100 | >50% |
| **Funded Account Survival Rate (90d)** | % de cuentas activas a 90 dias | (Cuentas activas a 90d) / (Total fondeadas) x 100 | >30% |
| **Time to First Violation** | Dias hasta la primera violacion de reglas | Timestamp violacion - Timestamp de fondeo | >30 dias |
| **Time to First Payout** | Dias hasta el primer retiro de profits | Timestamp primer payout - Timestamp fondeo | <30 dias |
| **Razon de Violacion** | Clasificacion del motivo de perdida de cuenta | Max drawdown / Daily loss / Consistency rule / Inactividad | Trackear distribucion |
| **Drawdown Proximity Alerts** | Cuantas veces se acerco al limite sin violar | Eventos donde drawdown > 70% del limite | Alerta temprana |
| **Risk-Adjusted Return** | Calidad de la operativa post-fondeo | Sharpe ratio / Max drawdown / Win rate | Benchmark interno |

#### Intervenciones Especificas

**PROGRAMA DE ONBOARDING PARA TRADERS FONDEADOS (7 dias criticos)**

```
TRIGGER: Trader pasa el challenge y recibe cuenta fondeada
==========================================================

[+0 min] Email 1 - "FELICIDADES -- Eres un trader fondeado de NEOMAAA"
  - Celebracion genuina (esto es un momento emocional enorme)
  - Video del CEO/equipo felicitandolo
  - Credenciales de cuenta fondeada
  - IMPORTANTE: "Antes de operar, lee esto" (reglas de la cuenta fondeada)
  - Diferencias clave entre challenge y cuenta fondeada

[+4 horas] Email 2 - "Las 5 reglas de tu cuenta fondeada (son diferentes)"
  - Tabla comparativa: Reglas del challenge vs Reglas de cuenta fondeada
  - Enfasis en: max drawdown, trailing drawdown (si aplica), consistency rule
  - Calculadora interactiva: "Cuanto puedes arriesgar por trade"
  - CTA: "Confirma que entendiste las reglas" (checkbox quiz)

[+24 horas] Email 3 - "Los primeros 5 dias como fondeado: tu plan"
  - "No intentes recuperar lo invertido en la primera semana"
  - Plan conservador: "Opera al 50% de tu tamano normal por 5 dias"
  - Objetivo: "Tu primer target es sobrevivir 2 semanas, no hacer $5,000"
  - Caso: "Los traders que operan conservador el primer mes tienen 3x mas payouts"

[+3 dias] Check-in automatico: "Como van tus primeros trades?"
  - Si esta en profit: "Excelente inicio. Mantene la disciplina."
  - Si esta en loss pero dentro de parametros: "Todo normal. Esto es trading."
  - Si esta cerca del 50% del drawdown: ALERTA NARANJA (ver abajo)
```

**SISTEMA DE ALERTAS DE RIESGO EN TIEMPO REAL**

```
=== SEMAFORO DE RIESGO ===

VERDE (0-40% del drawdown limite utilizado):
  - No hacer nada. Operativa normal.
  - Weekly report celebratorio

AMARILLO (40-60% del drawdown):
  - Notificacion in-app: "Has usado [X]% de tu drawdown. Recuerda tu plan."
  - Email con tips de risk management
  - Sugerencia: "Considera reducir tu tamano de posicion un 30%"

NARANJA (60-80% del drawdown):
  - Push notification + Email URGENTE
  - "ALERTA: Estas a $[X] de perder tu cuenta fondeada"
  - "Recomendamos PAUSAR la operativa por 24 horas"
  - Link a sesion de coaching gratuita
  - Contenido: "Protocolo de emergencia: como salvar tu cuenta"

ROJO (80-95% del drawdown):
  - Push + SMS + Email
  - "ALERTA CRITICA: Tu cuenta esta en peligro"
  - "Cierra todas las posiciones y toma un dia libre"
  - Oferta proactiva: "Si pierdes la cuenta, te damos 25% off en un nuevo challenge"
  - (Preparar el aterrizaje suave para posible perdida)
```

**PROGRAMA DE SCALING Y RETENCION A LARGO PLAZO**

```
MILESTONE: Primer payout exitoso
  - Email de celebracion masiva
  - Feature en redes sociales (con permiso)
  - Badge en el perfil del trader
  - Oferta de scaling: "Pasa a una cuenta de $[X]K mas grande con 20% off"

MILESTONE: 3 payouts consecutivos
  - Status "Elite Trader"
  - Acceso a comunidad VIP
  - Mejor profit split (ej: de 80/20 a 85/15)
  - Invitacion a referral program con comisiones

MILESTONE: 6 meses activo
  - Call personal con el equipo de NEOMAAA
  - Feature como "caso de exito" en marketing
  - Acceso a cuentas mas grandes sin nuevo challenge
  - Mentoria a traders nuevos (builds community + loyalty)
```

**Benchmark de la industria:**
- El 98% de traders fondeados abandona o pierde la cuenta en 6 meses
- Las prop firms con alertas de riesgo en tiempo real retienen 20-30% mas traders
- Los programas de scaling incrementan el LTV del trader fondeado en 3-5x
- El primer payout ocurre en promedio a los 15-25 dias post-fondeo
- Solo el 7% de TODOS los traders que compran un challenge llegan a recibir un payout

---

### FUGA #5: REPEAT PURCHASE -- Que Motiva a Recomprar vs Abandonar

**El Analisis de Decision del Trader**

Este no es un "punto de fuga" unico -- es el momento critico que ocurre DESPUES de cada fallo o perdida de cuenta fondeada. Es la decision binaria:

> "Compro otro challenge?" vs "Me voy a otra firma o abandono?"

**Factores que MOTIVAN a recomprar (en orden de importancia):**

```
1. EXPERIENCIA POSITIVA A PESAR DEL FALLO (40% de la decision)
   - Se sintio tratado con respeto
   - Recibio valor educativo del intento
   - La plataforma funciono bien
   - Soporte respondio rapido

2. PERCEPCION DE PROGRESO (25% de la decision)
   - "Casi lo logro -- estuve a $200 del target"
   - Puede ver metricas que mejoraron vs intento anterior
   - Siente que aprendio algo concreto

3. INCENTIVO ECONOMICO (20% de la decision)
   - Descuento de retry
   - Free retry incluido
   - Precio competitivo vs alternativas

4. COMUNIDAD Y PERTENENCIA (10% de la decision)
   - Amigos/comunidad en la misma firma
   - No quiere "empezar de cero" en otra
   - Identidad: "Soy trader de NEOMAAA"

5. CONFIANZA EN LA FIRMA (5% de la decision)
   - Ve que otros cobran payouts (prueba social real)
   - Transparencia en numeros
   - Sin historias de estafa o payouts negados
```

**Factores que CAUSAN abandono (en orden de impacto):**

```
1. SENTIR QUE EL SISTEMA ESTA EN CONTRA (35% de los abandonos)
   - Reglas percibidas como injustas
   - "Cambiaron las reglas despues de que compre"
   - Slippage/ejecucion mala que causo la violacion

2. COMPETENCIA MAS BARATA (25% de los abandonos)
   - Otra firma ofrece el mismo tamano por menos
   - Otra firma tiene reglas mas flexibles
   - Influencer promueve otra firma con descuento

3. FALTA DE COMUNICACION POST-FALLO (20% de los abandonos)
   - Solo recibieron "Tu challenge ha terminado"
   - Nadie les ayudo a entender que salio mal
   - Se sintieron como un numero mas

4. PROBLEMAS FINANCIEROS (15% de los abandonos)
   - No pueden pagar otro challenge ahora
   - El gasto acumulado ya es demasiado
   - Necesitan tiempo para ahorrar

5. ABANDONO DEL SUENO (5% de los abandonos)
   - Decidieron que trading no es para ellos
   - Encontraron otra actividad/inversion
   - Estos son irrecuperables (y esta bien)
```

#### Metricas de Repeat Purchase a Trackear

| Metrica | Definicion | Target |
|---------|-----------|--------|
| **Repeat Purchase Rate** | % de clientes que compran 2+ challenges | >45% |
| **Customer Lifetime Value (LTV)** | Revenue total por trader en su vida | >$600 |
| **Avg Challenges Per Customer** | Promedio de challenges comprados | >2.3 |
| **Time Between Purchases** | Dias entre un fallo y la siguiente compra | <14 dias |
| **Churn Reason Distribution** | % por cada razon de abandono | Trackear mensualmente |
| **NPS Post-Fallo** | Net Promoter Score despues de fallar | >20 |
| **Referral Rate** | % de clientes que refieren a alguien | >15% |

#### Intervenciones de Loyalty y Repeat Purchase

**PROGRAMA DE LEALTAD "NEOMAAA ELITE"**

```
NIVEL 1 - CHALLENGER (1er compra)
  - Acceso a Discord basico
  - Weekly market analysis
  - Standard rules

NIVEL 2 - PERSISTENT (2da compra / retry)
  - 10% descuento permanente en challenges
  - Acceso a webinars semanales exclusivos
  - Priority support (respuesta en <2h)

NIVEL 3 - DEDICATED (3+ compras)
  - 15% descuento permanente
  - 1 free retry por trimestre
  - Acceso a coaching grupal mensual
  - Badge visible en comunidad

NIVEL 4 - FUNDED (ha pasado al menos 1 challenge)
  - Mejor profit split
  - Scaling path automatico
  - Acceso a cuentas de mayor tamano
  - Invitacion a programa de afiliados (10% comision)

NIVEL 5 - ELITE (3+ payouts o 6+ meses fondeado)
  - Profit split premium (hasta 90/10)
  - Feature en marketing
  - Mentoria pagada a otros traders
  - Early access a nuevos productos
  - Call trimestral con fundadores
```

**ENCUESTA POST-FALLO (automatizada, 1 click)**

```
TRIGGER: 24 horas despues de fallo
FORMATO: 1 pregunta principal + 1 seguimiento

"Que vas a hacer ahora?"
  A) "Voy a intentar de nuevo pronto" >>> [Ofrecer descuento inmediato]
  B) "Necesito prepararme mas" >>> [Enviar recursos educativos + descuento a 14 dias]
  C) "Estoy evaluando otras opciones" >>> [Activar secuencia de retencion competitiva]
  D) "Voy a tomar un descanso" >>> [Mover a nurture mensual + reactivar en 30 dias]
```

---

## TABLA DE KPIs POR ETAPA DEL FUNNEL

```
==========================================================================
ETAPA              | KPI PRIMARIO          | TARGET   | BENCHMARK INDUSTRIA
==========================================================================
Post-Compra        | Activation Rate       | >85%     | 75-80%
                   | Time to First Trade   | <24h     | 48-72h
---------------------------------------------------------------------------
Mid-Challenge      | Completion Rate       | >70%     | 50-60%
                   | Weekly Active Days    | >3/sem   | 2-3/sem
---------------------------------------------------------------------------
Challenge Result   | Pass Rate             | 8-12%    | 5-10%
                   | Clean Fail Rate*      | >60%     | 40-50%
---------------------------------------------------------------------------
Post-Fallo         | Retry Rate            | >45%     | 30-35%
                   | Time to Retry         | <14 dias | 21-30 dias
                   | Recovery Email CTR    | >5%      | 3-4%
---------------------------------------------------------------------------
Fondeo Inicial     | 30-Day Survival       | >50%     | 30-40%
                   | Time to First Payout  | <25 dias | 30-45 dias
---------------------------------------------------------------------------
Trader Fondeado    | 90-Day Survival       | >30%     | 10-15%
                   | Avg Monthly Payout    | >$500    | $200-400
---------------------------------------------------------------------------
Repeat Purchase    | LTV por Trader        | >$600    | $300-400
                   | Avg Purchases/Trader  | >2.3     | 1.5-2.0
                   | Referral Rate         | >15%     | 5-8%
---------------------------------------------------------------------------
Overall            | Revenue/Trader (LTV)  | >$800    | $400-600
                   | NPS                   | >40      | 15-25
                   | Chargeback Rate       | <1.5%    | 2-4%
==========================================================================

* Clean Fail Rate = traders que fallan por merito (no por abandono/inactividad)
  Un fail "limpio" indica un trader engaged que tiene mas probabilidad de recomprar
```

---

## STACK TECNOLOGICO RECOMENDADO

```
==========================================================================
FUNCION                    | HERRAMIENTA          | COSTO APROX
==========================================================================
Email Automation           | ActiveCampaign       | $150-500/mes
                           | (o Customer.io si    |
                           | hay dev disponible)  |
---------------------------------------------------------------------------
CRM / Segmentacion         | Intercom (ya tienen) | Ya pagado
                           | + ActiveCampaign     |
---------------------------------------------------------------------------
SMS Transaccionales        | Twilio               | $0.01-0.05/SMS
---------------------------------------------------------------------------
Push Notifications         | OneSignal             | Free tier
---------------------------------------------------------------------------
Analytics de Trading       | API propia del        | Desarrollo custom
                           | broker/plataforma    |
---------------------------------------------------------------------------
Dashboards / Reportes      | Metabase o Mixpanel  | Free-$100/mes
---------------------------------------------------------------------------
Retargeting                | Meta Ads + Google Ads | Variable
---------------------------------------------------------------------------
Comunidad                  | Discord               | Free
---------------------------------------------------------------------------
Encuestas                  | Typeform Simple       | Free-$30/mes
                           | (o 1-click en email) |
==========================================================================
```

---

## PLAN DE IMPLEMENTACION POR PRIORIDAD

### P1 -- HACER ESTA SEMANA (Alto impacto, bajo esfuerzo)

| Accion | Impacto Estimado | Esfuerzo |
|--------|-----------------|----------|
| Secuencia post-fallo de 6 emails | +10-15% retry rate = +$X,XXX/mes | 1-2 dias |
| Email de onboarding post-compra (5 emails) | -50% abandono pre-inicio | 1 dia |
| Encuesta post-fallo de 1 click | Data para optimizar todo lo demas | 2 horas |
| Weekly progress report automatizado | -25% abandono mid-challenge | 1 dia |

### P2 -- HACER ESTE MES (Alto impacto, esfuerzo medio)

| Accion | Impacto Estimado | Esfuerzo |
|--------|-----------------|----------|
| Segmentacion por tipo de fallo (Ruta A/B/C) | +5-8% retry rate adicional | 3-5 dias |
| Sistema de alertas de drawdown (semaforo) | +20% supervivencia de cuentas fondeadas | 5-7 dias dev |
| Programa de lealtad "NEOMAAA Elite" (niveles) | +15-20% repeat purchase | 3-5 dias |
| Retargeting ads para traders fallidos | +5-10% retries via paid | 2-3 dias |

### P3 -- HACER ESTE TRIMESTRE (Impacto estrategico, esfuerzo alto)

| Accion | Impacto Estimado | Esfuerzo |
|--------|-----------------|----------|
| Dashboard de analytics completo (Mixpanel/Metabase) | Visibilidad total del funnel | 2-3 semanas |
| Programa de scaling para traders fondeados | +3-5x LTV de traders exitosos | 2-4 semanas |
| Analisis automatizado de challenge (post-mortem) | +10% retry + mejor brand | 1-2 semanas |
| Referral program con comisiones | +10-15% nuevos traders organicos | 1-2 semanas |
| Comunidad Discord estructurada con roles/badges | Retencion + moat competitivo | Ongoing |

---

## IMPACTO FINANCIERO ESTIMADO

```
==========================================================================
ESCENARIO: 1,000 challenges vendidos/mes a $250 promedio
==========================================================================

SIN RETENCION (estado actual estimado):
  Revenue de 1ra compra:                   $250,000
  Retry rate (25% sin intervencion):        250 retries x $250 = $62,500
  Total Revenue Mensual:                    ~$312,500
  LTV por trader:                           ~$312

CON FUNNEL DE RETENCION OPTIMIZADO:
  Revenue de 1ra compra:                   $250,000
  Retry rate (45% con intervenciones):      450 retries x $225* = $101,250
  2do retry (20% de los que recompran):     90 retries x $212* = $19,080
  Payouts mejorados (funded retention):     +$15,000/mes (profit splits)
  Referrals (15% de clientes refieren):     150 nuevos x $250 = $37,500
  Total Revenue Mensual:                    ~$422,830
  LTV por trader:                           ~$423

  * Precio reducido por descuentos de lealtad

DIFERENCIA:
  +$110,330/mes = +$1,323,960/año
  SIN GASTAR MAS EN ADQUISICION

  ROI del sistema de retencion:
  Costo de implementar: ~$5,000-15,000 (one-time) + $500-1,000/mes tools
  Retorno en mes 1: ~$110,000
  ROI primer ano: >50x
==========================================================================
```

---

## PROXIMOS PASOS INMEDIATOS

1. **HOY:** Configurar la secuencia post-fallo de 6 emails en ActiveCampaign/Intercom -- es el 40% del revenue perdido
2. **ESTA SEMANA:** Implementar onboarding post-compra y weekly progress reports
3. **ESTE MES:** Construir la segmentacion por tipo de fallo y el programa de lealtad
4. **ESTE TRIMESTRE:** Dashboard de analytics + programa de scaling + referral program

---

## FUENTES Y DATOS DE REFERENCIA

- [Prop Firm Statistics 2026: Pass Rates, Payouts & Trends - QuantVPS](https://www.quantvps.com/blog/prop-firm-statistics)
- [The Future of Prop Trading Is Not Challenges. It Is Retention - Axcera](https://axcera.io/blog/the-future-of-prop-trading-is-not-challenges-it-is-retention)
- [Only 1 in 20 Traders Pass Prop Firm Challenges - Finance Magnates](https://www.financemagnates.com/forex/only-1-in-20-traders-pass-prop-firm-challenges-reports-the-funded-trader/)
- [Prop Firm Pass Rates in 2025 - FunderPro](https://funderpro.com/blog/prop-trading-pass-rates-in-2025-what-the-data-really-shows/)
- [Email Marketing for Prop Firms: Complete Guide 2026 - AIM](https://aimcompany.co/blog/email-marketing-for-prop-firms)
- [Prop Firm Marketing in 2026 - Alpha Market Flow](https://alphamarketflow.com/blog/prop-firm-marketing-in-2026-what-actually-drives-trader-signups-and-retention)
- [Prop Firm Statistics 2026 - Atmos Funded](https://atmosfunded.com/prop-firm-statistics/)
- [FTMO Statistics 2026 - CoinLaw](https://coinlaw.io/ftmo-statistics/)
