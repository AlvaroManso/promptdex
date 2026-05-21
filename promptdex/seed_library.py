from __future__ import annotations

from promptdex.schemas import PromptCreate

LIBRARY_VERSION_TAG = "library-2026-05"


def builtin_prompt_library() -> list[PromptCreate]:
    shared = [LIBRARY_VERSION_TAG, "es", "en"]
    return [
        PromptCreate(
            title="Codex task spec / Especificacion para Codex",
            category="Prompts for Codex",
            tags=[*shared, "codex", "coding", "spec"],
            rating=5,
            favorite=True,
            body="""ES:
Actua como mi senior founding engineer. Antes de tocar codigo, resume el objetivo, inspecciona el repositorio y convierte esta tarea en cambios pequenos y verificables. Implementa solo lo necesario, respeta el estilo existente, no reviertas cambios ajenos y termina con pruebas ejecutadas, estado de git y siguientes mejoras.

EN:
Act as my senior founding engineer. Before touching code, summarize the goal, inspect the repository, and turn this task into small verifiable changes. Implement only what is needed, respect the existing style, do not revert other people's changes, and finish with executed checks, git status, and next improvements.""",
        ),
        PromptCreate(
            title="Bug reproduction loop / Bucle de reproduccion de bug",
            category="Debugging",
            tags=[*shared, "debugging", "repro", "tests"],
            rating=5,
            body="""ES:
Diagnostica este bug con disciplina: reproduce el fallo, reduce el caso, formula 2-3 hipotesis, instrumenta lo minimo, arregla la causa raiz y agrega una prueba de regresion. No propongas cambios hasta tener evidencia.

EN:
Diagnose this bug with discipline: reproduce the failure, minimize the case, form 2-3 hypotheses, instrument only what is needed, fix the root cause, and add a regression test. Do not propose changes until you have evidence.""",
        ),
        PromptCreate(
            title="Architecture decision record / ADR de arquitectura",
            category="Architecture",
            tags=[*shared, "architecture", "adr", "tradeoffs"],
            rating=5,
            body="""ES:
Escribe un ADR breve para esta decision. Incluye contexto, fuerzas en tension, opciones consideradas, decision, consecuencias, riesgos y senales para reconsiderarla. Se claro sobre lo que queda fuera de alcance.

EN:
Write a concise ADR for this decision. Include context, competing forces, options considered, decision, consequences, risks, and signals that should trigger reconsideration. Be explicit about what is out of scope.""",
        ),
        PromptCreate(
            title="Prompt upgrade for reasoning models / Mejora para modelos de razonamiento",
            category="Prompts for ChatGPT",
            tags=[*shared, "chatgpt", "reasoning", "prompting"],
            rating=5,
            favorite=True,
            body="""ES:
Reescribe este prompt para un modelo de razonamiento moderno. Hazlo directo, con objetivo claro, contexto suficiente, restricciones, formato de salida y criterios de exito. Evita pedir cadena de pensamiento; pide una respuesta verificable y concisa.

EN:
Rewrite this prompt for a modern reasoning model. Make it direct, with a clear goal, enough context, constraints, output format, and success criteria. Avoid asking for chain-of-thought; request a verifiable and concise answer.""",
        ),
        PromptCreate(
            title="Claude XML task frame / Marco XML para Claude",
            category="Prompts for Claude",
            tags=[*shared, "claude", "xml", "prompting"],
            rating=5,
            body="""ES:
Usa esta estructura para una tarea compleja:
<contexto>...</contexto>
<objetivo>...</objetivo>
<restricciones>...</restricciones>
<ejemplos>...</ejemplos>
<salida>Define el formato exacto.</salida>
Primero verifica ambiguedades criticas; despues responde.

EN:
Use this structure for a complex task:
<context>...</context>
<goal>...</goal>
<constraints>...</constraints>
<examples>...</examples>
<output>Define the exact format.</output>
First check for critical ambiguity; then answer.""",
        ),
        PromptCreate(
            title="Code review severity pass / Revision de codigo por severidad",
            category="Coding",
            tags=[*shared, "review", "quality", "codex"],
            rating=5,
            body="""ES:
Revisa este diff como reviewer senior. Prioriza bugs, regresiones, seguridad, datos y pruebas faltantes. Devuelve hallazgos ordenados por severidad con archivo/linea, por que importa y el cambio minimo recomendado. Si no hay hallazgos, dilo claramente.

EN:
Review this diff as a senior reviewer. Prioritize bugs, regressions, security, data issues, and missing tests. Return findings by severity with file/line, why it matters, and the minimal recommended change. If there are no findings, say so clearly.""",
        ),
        PromptCreate(
            title="Design critique / Critica de diseno",
            category="Design",
            tags=[*shared, "ui", "ux", "design"],
            rating=4,
            body="""ES:
Critica esta interfaz para un producto real. Evalua jerarquia, densidad, accesibilidad, estados vacios/error, responsive, copy y flujos frecuentes. Propone 5 mejoras concretas, ordenadas por impacto.

EN:
Critique this interface for a real product. Evaluate hierarchy, density, accessibility, empty/error states, responsiveness, copy, and frequent workflows. Propose 5 concrete improvements ordered by impact.""",
        ),
        PromptCreate(
            title="Landing page copy / Copy de landing",
            category="Marketing",
            tags=[*shared, "marketing", "copy", "landing"],
            rating=4,
            body="""ES:
Escribe copy para una landing. Audiencia: [audiencia]. Producto: [producto]. Diferenciador: [diferenciador]. Devuelve H1, subtitulo, 3 beneficios, prueba social, CTA principal/secundario y objeciones frecuentes con respuestas.

EN:
Write landing page copy. Audience: [audience]. Product: [product]. Differentiator: [differentiator]. Return H1, subtitle, 3 benefits, social proof, primary/secondary CTA, and common objections with responses.""",
        ),
        PromptCreate(
            title="Research synthesis / Sintesis de investigacion",
            category="Research",
            tags=[*shared, "research", "synthesis", "sources"],
            rating=5,
            body="""ES:
Sintetiza esta investigacion. Separa hechos, inferencias y opiniones. Incluye una tabla con fuente, fecha, afirmacion clave, confianza y contradicciones. Termina con preguntas abiertas y proximos pasos.

EN:
Synthesize this research. Separate facts, inferences, and opinions. Include a table with source, date, key claim, confidence, and contradictions. End with open questions and next steps.""",
        ),
        PromptCreate(
            title="Agent handoff brief / Brief para agentes",
            category="Agents",
            tags=[*shared, "agents", "handoff", "workflow"],
            rating=5,
            body="""ES:
Prepara un brief para un agente autonomo. Incluye mision, contexto, limites, herramientas permitidas, criterios de exito, riesgos, comandos de verificacion y formato de reporte final. Hazlo accionable y sin ambiguedad.

EN:
Prepare a brief for an autonomous agent. Include mission, context, boundaries, allowed tools, success criteria, risks, verification commands, and final report format. Make it actionable and unambiguous.""",
        ),
        PromptCreate(
            title="Meeting to execution plan / Reunion a plan de ejecucion",
            category="Productivity",
            tags=[*shared, "productivity", "planning", "meeting"],
            rating=4,
            body="""ES:
Convierte estas notas de reunion en un plan. Extrae decisiones, responsables, tareas, dependencias, fechas, riesgos y preguntas abiertas. Marca cualquier accion sin owner como bloqueada.

EN:
Turn these meeting notes into a plan. Extract decisions, owners, tasks, dependencies, dates, risks, and open questions. Mark any action without an owner as blocked.""",
        ),
        PromptCreate(
            title="SQL query helper / Ayudante SQL",
            category="Coding",
            tags=[*shared, "sql", "data", "debugging"],
            rating=4,
            body="""ES:
Ayudame con esta consulta SQL. Primero explica el objetivo en una frase, luego propone la consulta, indices utiles, casos borde y como validarla con 3 filas de ejemplo. Evita optimizaciones prematuras.

EN:
Help me with this SQL query. First explain the goal in one sentence, then propose the query, useful indexes, edge cases, and how to validate it with 3 example rows. Avoid premature optimization.""",
        ),
        PromptCreate(
            title="API contract design / Diseno de contrato API",
            category="Architecture",
            tags=[*shared, "api", "backend", "contracts"],
            rating=5,
            body="""ES:
Disena este contrato API local. Define recursos, endpoints, esquemas request/response, errores, paginacion si aplica, idempotencia, validaciones y pruebas de contrato. Mantenerlo simple es un requisito.

EN:
Design this local API contract. Define resources, endpoints, request/response schemas, errors, pagination if applicable, idempotency, validations, and contract tests. Keeping it simple is a requirement.""",
        ),
        PromptCreate(
            title="Test plan from requirements / Plan de pruebas desde requisitos",
            category="Debugging",
            tags=[*shared, "qa", "tests", "requirements"],
            rating=5,
            body="""ES:
Crea un plan de pruebas desde estos requisitos. Incluye happy path, errores, bordes, persistencia, accesibilidad si hay UI, y una matriz requisito -> prueba. Prioriza pruebas que detectarian regresiones reales.

EN:
Create a test plan from these requirements. Include happy path, errors, edge cases, persistence, accessibility if there is UI, and a requirement -> test matrix. Prioritize tests that would catch real regressions.""",
        ),
        PromptCreate(
            title="Refactor without behavior change / Refactor sin cambiar comportamiento",
            category="Coding",
            tags=[*shared, "refactor", "tests", "codex"],
            rating=5,
            body="""ES:
Refactoriza este codigo sin cambiar comportamiento. Primero identifica responsabilidades mezcladas y riesgos. Propone pasos pequenos, cada uno con prueba o verificacion. Manten nombres claros y evita abstracciones que no eliminen complejidad real.

EN:
Refactor this code without changing behavior. First identify mixed responsibilities and risks. Propose small steps, each with a test or verification. Keep names clear and avoid abstractions that do not remove real complexity.""",
        ),
        PromptCreate(
            title="Competitive positioning / Posicionamiento competitivo",
            category="Marketing",
            tags=[*shared, "positioning", "strategy", "marketing"],
            rating=4,
            body="""ES:
Ayudame a posicionar este producto. Compara alternativas, jobs-to-be-done, usuarios ideales, mensaje principal, razones para creer y riesgos de percepcion. Devuelve una tabla y un pitch de 30 segundos.

EN:
Help me position this product. Compare alternatives, jobs-to-be-done, ideal users, main message, reasons to believe, and perception risks. Return a table and a 30-second pitch.""",
        ),
        PromptCreate(
            title="Long context extraction / Extraccion con contexto largo",
            category="Research",
            tags=[*shared, "long-context", "extraction", "claude"],
            rating=5,
            body="""ES:
Extrae informacion de este documento largo. Usa solo el contenido proporcionado, cita secciones o frases cortas, marca lo no encontrado como 'no consta' y devuelve JSON valido con los campos solicitados.

EN:
Extract information from this long document. Use only the provided content, cite sections or short phrases, mark missing information as 'not found', and return valid JSON with the requested fields.""",
        ),
        PromptCreate(
            title="Personal knowledge distiller / Destilador de conocimiento",
            category="Productivity",
            tags=[*shared, "notes", "knowledge", "summary"],
            rating=4,
            body="""ES:
Convierte estas notas dispersas en conocimiento reutilizable. Crea resumen, principios, decisiones, snippets accionables, etiquetas y recordatorios. Manten lo importante; elimina relleno.

EN:
Turn these scattered notes into reusable knowledge. Create a summary, principles, decisions, actionable snippets, tags, and reminders. Preserve what matters; remove filler.""",
        ),
        PromptCreate(
            title="Frontend implementation brief / Brief de frontend",
            category="Design",
            tags=[*shared, "frontend", "ui", "implementation"],
            rating=5,
            body="""ES:
Implementa esta UI con criterio de producto. Define estados completos, responsive, accesibilidad, microinteracciones y datos de ejemplo. Evita landing generica: construye la experiencia usable desde la primera pantalla.

EN:
Implement this UI with product judgment. Define complete states, responsiveness, accessibility, microinteractions, and sample data. Avoid a generic landing page: build the usable experience on the first screen.""",
        ),
        PromptCreate(
            title="Risk register / Registro de riesgos",
            category="Architecture",
            tags=[*shared, "risk", "planning", "systems"],
            rating=4,
            body="""ES:
Crea un registro de riesgos para este proyecto. Para cada riesgo incluye probabilidad, impacto, senales tempranas, mitigacion, owner y decision requerida. Separa riesgos tecnicos, producto y operacion.

EN:
Create a risk register for this project. For each risk include probability, impact, early warning signs, mitigation, owner, and required decision. Separate technical, product, and operational risks.""",
        ),
        PromptCreate(
            title="Codex PR finishing pass / Cierre de PR con Codex",
            category="Prompts for Codex",
            tags=[*shared, "codex", "git", "release"],
            rating=5,
            body="""ES:
Prepara este trabajo para cerrar. Revisa diff, ejecuta pruebas relevantes, actualiza README si aplica, resume cambios, riesgos restantes, comandos ejecutados, estado de git y commit sugerido. No hagas push.

EN:
Prepare this work for completion. Review the diff, run relevant checks, update README if needed, summarize changes, remaining risks, commands run, git status, and suggested commit. Do not push.""",
        ),
        PromptCreate(
            title="ChatGPT structured answer / Respuesta estructurada ChatGPT",
            category="Prompts for ChatGPT",
            tags=[*shared, "chatgpt", "structured-output", "analysis"],
            rating=4,
            body="""ES:
Responde con esta estructura: conclusion breve, supuestos, pasos recomendados, riesgos, y ejemplo. Si falta informacion critica, haz maximo 3 preguntas; si puedes avanzar con supuestos razonables, hazlo y declaralos.

EN:
Answer with this structure: brief conclusion, assumptions, recommended steps, risks, and example. If critical information is missing, ask at most 3 questions; if you can proceed with reasonable assumptions, do so and state them.""",
        ),
        PromptCreate(
            title="Performance investigation plan / Plan de investigacion de rendimiento",
            category="Debugging",
            tags=[*shared, "performance", "profiling", "observability"],
            rating=5,
            body="""ES:
Ayudame a investigar un problema de rendimiento. Primero define el sintoma medible (latencia, CPU, memoria, I/O) y el objetivo. Luego propone:
1) Hipotesis (max 5) ordenadas por probabilidad/impacto
2) Instrumentacion minima (logs, metrics, traces) para confirmar/refutar cada hipotesis
3) Experimentos reproducibles y como evitar sesgos
4) Cambio minimo para corregir la causa raiz
5) Prueba/alerta de regresion y como monitorear despues
Devuelve una lista accionable con comandos sugeridos y criterios de exito.

EN:
Help me investigate a performance issue. First define the measurable symptom (latency, CPU, memory, I/O) and the goal. Then propose:
1) Hypotheses (max 5) ordered by probability/impact
2) Minimal instrumentation (logs, metrics, traces) to confirm/refute each hypothesis
3) Reproducible experiments and how to avoid bias
4) Minimal change to fix the root cause
5) Regression test/alert and post-fix monitoring plan
Return an actionable checklist with suggested commands and success criteria.""",
        ),
        PromptCreate(
            title="Security threat model / Modelo de amenazas",
            category="Architecture",
            tags=[*shared, "security", "threat-model", "risk"],
            rating=5,
            body="""ES:
Haz un threat model para este sistema/feature. Define activos, limites de confianza, actores, vectores de ataque y supuestos. Luego produce:
- Tabla STRIDE (amenaza, impacto, probabilidad, mitigacion, owner)
- Controles minimos recomendados (auth, autorizacion, validacion, logging, rate limits)
- Lista de "no hacer" (antipatrones)
No inventes requisitos: si falta info, pregunta maximo 3 cosas y continua con supuestos claramente marcados.

EN:
Do a threat model for this system/feature. Define assets, trust boundaries, actors, attack vectors, and assumptions. Then produce:
- STRIDE table (threat, impact, likelihood, mitigation, owner)
- Minimal recommended controls (auth, authorization, validation, logging, rate limits)
- "Do not do" list (anti-patterns)
Do not invent requirements: if key info is missing, ask at most 3 questions and proceed with clearly labeled assumptions.""",
        ),
        PromptCreate(
            title="PRD one-pager / PRD de una pagina",
            category="Productivity",
            tags=[*shared, "product", "requirements", "writing"],
            rating=4,
            body="""ES:
Convierte esta idea en un PRD de una pagina. Incluye: problema, usuario objetivo, objetivos medibles, no-objetivos, alcance (MVP), UX a alto nivel, requisitos funcionales, requisitos no funcionales, riesgos, dependencia y como se medira el exito. Mantenerlo corto es requisito.

EN:
Turn this idea into a one-page PRD. Include: problem, target user, measurable goals, non-goals, scope (MVP), high-level UX, functional requirements, non-functional requirements, risks, dependencies, and how success will be measured. Keeping it short is a requirement.""",
        ),
        PromptCreate(
            title="User story mapping / Mapa de historias de usuario",
            category="Productivity",
            tags=[*shared, "product", "user-stories", "prioritization"],
            rating=4,
            body="""ES:
Crea un user story map para este producto/feature. Define: actividades del usuario, pasos (journey), historias por paso, prioridades (MVP / despues), criterios de aceptacion y riesgos. Devuelve una tabla y una lista de entregables por iteracion.

EN:
Create a user story map for this product/feature. Define: user activities, journey steps, stories per step, priorities (MVP / later), acceptance criteria, and risks. Return a table plus a deliverables list per iteration.""",
        ),
        PromptCreate(
            title="UX copy tone guide / Guia de tono para UX copy",
            category="Design",
            tags=[*shared, "ux-writing", "copy", "tone"],
            rating=4,
            body="""ES:
Define una guia de tono para este producto. Incluye: personalidad, palabras a usar/evitar, ejemplos de microcopy (errores, vacio, confirmaciones), longitud objetivo, y reglas para mensajes de error (accionable, sin culpar, con siguiente paso). Devuelve ejemplos listos para pegar.

EN:
Define a tone guide for this product. Include: personality, words to use/avoid, microcopy examples (errors, empty states, confirmations), target length, and error-message rules (actionable, no blame, clear next step). Return copy-ready examples.""",
        ),
        PromptCreate(
            title="Email campaign outline / Esquema de campana de email",
            category="Marketing",
            tags=[*shared, "email", "campaign", "copy"],
            rating=4,
            body="""ES:
Disena una campana de email de 3-5 correos para este producto. Define segmento, propuesta de valor, objetivo por email, asunto (3 opciones), estructura, CTA, y como medir resultados. Evita promesas exageradas; se especifico.

EN:
Design a 3-5 email campaign for this product. Define segment, value proposition, goal per email, subject lines (3 options), structure, CTA, and how to measure results. Avoid hype; be specific.""",
        ),
        PromptCreate(
            title="SEO content brief / Brief de contenido SEO",
            category="Marketing",
            tags=[*shared, "seo", "content", "research"],
            rating=4,
            body="""ES:
Crea un brief SEO para un articulo. Incluye: keyword principal, intent, keywords secundarias, estructura H1/H2, preguntas a responder, ejemplos, contraejemplos, y criterios de calidad. Si faltan datos, pide maximo 3 aclaraciones y continua con supuestos.

EN:
Create an SEO content brief for an article. Include: primary keyword, intent, secondary keywords, H1/H2 outline, questions to answer, examples, counterexamples, and quality criteria. If key data is missing, ask at most 3 clarifying questions and proceed with assumptions.""",
        ),
        PromptCreate(
            title="Data model sanity check / Revision de modelo de datos",
            category="Architecture",
            tags=[*shared, "data-model", "database", "consistency"],
            rating=5,
            body="""ES:
Revisa este modelo de datos. Busca: invariantes, normalizacion vs pragmatismo, claves/indices, relaciones, borrado/retencion, migraciones, y consultas mas comunes. Devuelve:
1) Lista de riesgos (con severidad)
2) Cambios minimos recomendados
3) Pruebas de integridad a agregar

EN:
Review this data model. Check: invariants, normalization vs pragmatism, keys/indexes, relationships, deletion/retention, migrations, and common queries. Return:
1) Risk list (with severity)
2) Minimal recommended changes
3) Integrity tests to add""",
        ),
        PromptCreate(
            title="Agent tool contract / Contrato de herramienta para agente",
            category="Agents",
            tags=[*shared, "agents", "tools", "contracts"],
            rating=5,
            body="""ES:
Define un contrato para una herramienta que usara un agente. Incluye: nombre, proposito, entradas (schema), salidas (schema), errores, idempotencia, limites (tiempo/tamano), permisos, y ejemplos. Termina con casos borde y pruebas sugeridas.

EN:
Define a contract for a tool an agent will use. Include: name, purpose, inputs (schema), outputs (schema), errors, idempotency, limits (time/size), permissions, and examples. End with edge cases and suggested tests.""",
        ),
        PromptCreate(
            title="Prompt evaluation rubric / Rubrica de evaluacion de prompts",
            category="Prompts for ChatGPT",
            tags=[*shared, "prompting", "evaluation", "quality"],
            rating=5,
            body="""ES:
Evalua este prompt con una rubrica. Puntua 1-5: claridad del objetivo, contexto, restricciones, formato de salida, criterios de exito, testabilidad, seguridad/privacidad, y esfuerzo del usuario. Devuelve:
- Tabla (criterio, puntuacion, por que, mejora concreta)
- Version mejorada del prompt (sin pedir cadena de pensamiento)

EN:
Evaluate this prompt with a rubric. Score 1-5: goal clarity, context, constraints, output format, success criteria, testability, safety/privacy, and user effort. Return:
- Table (criterion, score, why, concrete improvement)
- Improved prompt version (without requesting chain-of-thought)""",
        ),
        PromptCreate(
            title="Codex TDD feature builder / Constructor de feature TDD con Codex",
            category="Prompts for Codex",
            tags=[*shared, "codex", "tdd", "tests"],
            rating=5,
            favorite=True,
            body="""ES:
Implementa esta feature con enfoque TDD. Primero escribe/actualiza pruebas (unit/integration) que fallen por la razon correcta. Luego implementa el minimo para pasar. Itera hasta cubrir bordes. Mantente dentro del repo; no agregues dependencias sin necesidad. Termina con comandos exactos ejecutados y estado de git.

EN:
Implement this feature using TDD. First write/update unit/integration tests that fail for the right reason. Then implement the minimum to pass. Iterate until edges are covered. Stay within the repo; do not add dependencies unless necessary. Finish with exact commands executed and git status.""",
        ),
        PromptCreate(
            title="Claude structured extraction to JSON / Extraccion estructurada a JSON para Claude",
            category="Prompts for Claude",
            tags=[*shared, "claude", "extraction", "json"],
            rating=5,
            body="""ES:
Extrae la informacion solicitada y devuelve SOLO JSON valido (sin markdown). Reglas:
- Usa solo el texto proporcionado
- Si un campo no aparece, usa null o \"no consta\" (segun se pida)
- Incluye un campo \"evidence\" con citas cortas (max 20 palabras) por cada item importante
Si hay ambiguedad critica, pregunta maximo 3 cosas.

EN:
Extract the requested information and return ONLY valid JSON (no markdown). Rules:
- Use only the provided text
- If a field is missing, use null or \"not found\" (as requested)
- Include an \"evidence\" field with short quotes (max 20 words) for key items
If there is critical ambiguity, ask at most 3 questions.""",
        ),
        PromptCreate(
            title="ChatGPT quick decision memo / Memo rapido de decision para ChatGPT",
            category="Prompts for ChatGPT",
            tags=[*shared, "chatgpt", "decision", "tradeoffs"],
            rating=4,
            body="""ES:
Ayudame a tomar esta decision. Devuelve: recomendacion, 2 alternativas, criterios, tradeoffs, riesgos, y plan de reversibilidad. Si faltan datos, declara supuestos y pide maximo 3 preguntas al final.

EN:
Help me make this decision. Return: recommendation, 2 alternatives, criteria, tradeoffs, risks, and reversibility plan. If data is missing, state assumptions and ask at most 3 questions at the end.""",
        ),
        PromptCreate(
            title="Git commit message helper / Ayudante de mensajes de commit",
            category="Productivity",
            tags=[*shared, "git", "commits", "writing"],
            rating=4,
            body="""ES:
Genera un mensaje de commit claro. Entradas: resumen del cambio, impacto, riesgos. Salida:
- 3 opciones (conventional commits si aplica)
- Una opcion recomendada
- Cuerpo opcional con bullets (que cambio, por que, como verificar)

EN:
Generate a clear commit message. Inputs: change summary, impact, risks. Output:
- 3 options (Conventional Commits if applicable)
- One recommended option
- Optional body bullets (what changed, why, how to verify)""",
        ),
        PromptCreate(
            title="Incident status update / Actualizacion de estado de incidente",
            category="Productivity",
            tags=[*shared, "incident", "oncall", "communication"],
            rating=4,
            body="""ES:
Redacta una actualizacion de incidente para stakeholders. Incluye: resumen, impacto, alcance, linea temporal breve, mitigacion aplicada, estado actual, siguientes pasos, riesgos, y ETA si existe (o explica por que no). Mantenerlo honesto es requisito.

EN:
Write an incident update for stakeholders. Include: summary, impact, scope, short timeline, mitigation applied, current status, next steps, risks, and ETA if known (or explain why not). Being honest is a requirement.""",
        ),
        PromptCreate(
            title="Customer interview script / Guion de entrevista a usuarios",
            category="Research",
            tags=[*shared, "research", "interviews", "product"],
            rating=4,
            body="""ES:
Crea un guion de entrevista de 30 minutos para este problema. Incluye: objetivos, preguntas abiertas, probes, preguntas de comportamiento pasado, y como evitar sesgos. Termina con una plantilla para capturar notas (quotes, dolor, soluciones actuales).

EN:
Create a 30-minute customer interview script for this problem. Include: goals, open-ended questions, probes, past-behavior questions, and how to avoid bias. End with a note-taking template (quotes, pain, current solutions).""",
        ),
        PromptCreate(
            title="Competitive teardown / Analisis competitivo profundo",
            category="Research",
            tags=[*shared, "competition", "analysis", "marketing"],
            rating=4,
            body="""ES:
Haz un analisis competitivo profundo. Compara 3-5 alternativas en: publico objetivo, propuesta de valor, pricing (si se conoce), UX, integraciones, barreras de cambio y riesgos. Devuelve una tabla y 3 apuestas estrategicas.

EN:
Do a competitive teardown. Compare 3-5 alternatives on: target audience, value proposition, pricing (if known), UX, integrations, switching costs, and risks. Return a table plus 3 strategic bets.""",
        ),
        PromptCreate(
            title="API error taxonomy / Taxonomia de errores API",
            category="Architecture",
            tags=[*shared, "api", "errors", "contracts"],
            rating=5,
            body="""ES:
Define una taxonomia de errores para esta API. Incluye: codigos, estructura JSON, mensajes para usuario vs logs, trazabilidad (request_id), y reglas de mapeo desde excepciones internas. Devuelve ejemplos de 5 errores comunes y como probarlos.

EN:
Define an error taxonomy for this API. Include: codes, JSON structure, user-facing vs log messages, traceability (request_id), and mapping rules from internal exceptions. Return examples for 5 common errors and how to test them.""",
        ),
        PromptCreate(
            title="Documentation from code / Documentacion desde codigo",
            category="Coding",
            tags=[*shared, "docs", "maintenance", "readme"],
            rating=4,
            body="""ES:
Genera documentacion a partir de este codigo. Produce: descripcion, como ejecutarlo, configuracion, ejemplos, y errores comunes. No inventes flags ni endpoints: si no estan en el codigo, marca como \"no consta\" o pide una aclaracion.

EN:
Generate documentation from this code. Produce: overview, how to run it, configuration, examples, and common errors. Do not invent flags or endpoints: if they are not in the code, mark as \"not found\" or ask for clarification.""",
        ),
        PromptCreate(
            title="Architecture diagram spec / Especificacion de diagrama de arquitectura",
            category="Architecture",
            tags=[*shared, "architecture", "diagram", "documentation"],
            rating=4,
            body="""ES:
Convierte esta arquitectura en una especificacion de diagrama (texto). Incluye: componentes, limites de confianza, flujos principales, dependencias externas, y datos persistidos. Devuelve:
1) Lista de nodos (id, nombre, tipo)
2) Lista de aristas (origen, destino, tipo de flujo, datos)
3) Un diagrama Mermaid (flowchart o sequence) si es posible
No inventes servicios: si falta info, declara supuestos.

EN:
Turn this architecture into a diagram specification (text). Include: components, trust boundaries, main flows, external dependencies, and persisted data. Return:
1) Node list (id, name, type)
2) Edge list (source, target, flow type, data)
3) A Mermaid diagram (flowchart or sequence) if possible
Do not invent services: if info is missing, state assumptions.""",
        ),
        PromptCreate(
            title="Minimal repro request / Pedido de repro minimo",
            category="Debugging",
            tags=[*shared, "debugging", "repro", "triage"],
            rating=5,
            body="""ES:
Necesito un ejemplo minimo reproducible. Devuelve:
- Pasos exactos (1..N)
- Versiones (OS, lenguaje, framework, dependencias)
- Entrada minima (datos/sample) y salida actual
- Salida esperada (criterio de exito)
- Logs/stacktrace completos (sin recortar)
- Si es posible: repo minimo o snippet autocontenido

EN:
I need a minimal reproducible example. Provide:
- Exact steps (1..N)
- Versions (OS, language, framework, dependencies)
- Minimal input (data/sample) and current output
- Expected output (success criteria)
- Full logs/stacktrace (no trimming)
- If possible: a tiny repo or self-contained snippet""",
        ),
        PromptCreate(
            title="Root-cause analysis writeup / Informe de causa raiz",
            category="Productivity",
            tags=[*shared, "incident", "rca", "postmortem"],
            rating=4,
            body="""ES:
Escribe un RCA breve (1-2 paginas). Incluye: resumen, impacto, linea temporal, causa raiz, factores contribuyentes,
por que no se detecto antes, que funciono, que no, acciones (dueno + fecha), y medidas preventivas. Evita culpas.

EN:
Write a concise RCA (1-2 pages). Include: summary, impact, timeline, root cause, contributing factors, why it wasn't
detected earlier, what worked, what didn't, actions (owner + due date), and preventative measures. No blame.""",
        ),
        PromptCreate(
            title="Database migration checklist / Checklist de migracion de base de datos",
            category="Architecture",
            tags=[*shared, "database", "migrations", "rollout"],
            rating=5,
            body="""ES:
Planifica esta migracion de base de datos. Devuelve:
1) Cambios de esquema (DDL) y compatibilidad hacia atras
2) Plan de despliegue en fases (expand/contract si aplica)
3) Backfill: estrategia, limites, monitorizacion, tiempos
4) Indices/locks: riesgos y mitigaciones
5) Plan de rollback y verificacion post-deploy

EN:
Plan this database migration. Return:
1) Schema changes (DDL) and backwards compatibility
2) Phased rollout plan (expand/contract if applicable)
3) Backfill: strategy, limits, monitoring, timing
4) Index/lock risks and mitigations
5) Rollback plan and post-deploy verification""",
        ),
        PromptCreate(
            title="API pagination + filtering design / Diseno de paginacion + filtros API",
            category="Architecture",
            tags=[*shared, "api", "pagination", "filters"],
            rating=5,
            body="""ES:
Disena paginacion y filtros para este endpoint. Incluye: cursor vs offset (y por que), orden estable,
parametros de filtro (tipos + validacion), limites, ejemplos de requests/responses, y como evitar inconsistencias
cuando cambian los datos. Propone tests (unidad + integracion).

EN:
Design pagination and filters for this endpoint. Include: cursor vs offset (and why), stable ordering,
filter parameters (types + validation), limits, request/response examples, and how to avoid inconsistencies
as data changes. Propose tests (unit + integration).""",
        ),
        PromptCreate(
            title="Async bug triage (Python) / Triage de bug async (Python)",
            category="Debugging",
            tags=[*shared, "python", "async", "debugging"],
            rating=4,
            body="""ES:
Diagnostica este bug async en Python. Pide primero: version de Python, event loop, framework, y un snippet minimo.
Luego: identifica condiciones de carrera, cancelaciones, timeouts, tareas colgadas, y puntos de await peligrosos.
Propone instrumentacion (logs, traces) y un fix minimo con prueba.

EN:
Diagnose this async Python bug. First ask for: Python version, event loop, framework, and a minimal snippet.
Then: identify races, cancellations, timeouts, stuck tasks, and risky await points. Propose instrumentation
(logs, traces) and a minimal fix with a test.""",
        ),
        PromptCreate(
            title="Test data strategy / Estrategia de datos de tests",
            category="Coding",
            tags=[*shared, "testing", "fixtures", "data"],
            rating=4,
            body="""ES:
Define una estrategia de datos de test para este proyecto. Incluye: fixtures vs factories, datos minimos,
datos realistas (sin PII), seeds deterministas, limpieza, paralelismo, y como evitar tests fragiles. Devuelve
una guia corta y 3 ejemplos.

EN:
Define a test data strategy for this project. Include: fixtures vs factories, minimal data, realistic data
(no PII), deterministic seeds, cleanup, parallelism, and how to avoid brittle tests. Return a short guide
and 3 examples.""",
        ),
        PromptCreate(
            title="Prompt injection test cases / Casos de prueba de prompt injection",
            category="Architecture",
            tags=[*shared, "security", "prompt-injection", "testing"],
            rating=5,
            body="""ES:
Genera casos de prueba de prompt injection para esta app (inputs no confiables). Devuelve:
- 10 ataques directos (\"ignora instrucciones\", exfiltracion, abuso de tools)
- 10 ataques indirectos (texto embebido en docs/URLs)
- Que debe pasar (bloquear, degradar, requerir confirmacion humana)
- Criterios de logging y alertas (sin capturar secretos)

EN:
Generate prompt-injection test cases for this app (untrusted inputs). Return:
- 10 direct attacks (\"ignore instructions\", exfiltration, tool abuse)
- 10 indirect attacks (instructions embedded in docs/URLs)
- Expected behavior (block, degrade, require human confirmation)
- Logging/alerting criteria (without capturing secrets)""",
        ),
        PromptCreate(
            title="Agent tool schema spec / Especificacion de herramienta para agente",
            category="Agents",
            tags=[*shared, "agents", "tools", "schema"],
            rating=5,
            body="""ES:
Define una herramienta (tool) para un agente. Devuelve:
1) Nombre y proposito (1 frase)
2) Contrato de entrada (campos, tipos, validaciones)
3) Contrato de salida (campos, tipos, errores)
4) Ejemplos (2 inputs + 2 outputs)
5) Limites y guardrails (rate limits, timeouts, PII)

EN:
Define an agent tool. Return:
1) Name and purpose (1 sentence)
2) Input contract (fields, types, validations)
3) Output contract (fields, types, errors)
4) Examples (2 inputs + 2 outputs)
5) Limits and guardrails (rate limits, timeouts, PII)""",
        ),
        PromptCreate(
            title="Agent runbook + guardrails / Runbook + guardrails de agente",
            category="Agents",
            tags=[*shared, "agents", "safety", "operations"],
            rating=4,
            body="""ES:
Escribe un runbook para operar este agente en produccion. Incluye: modos de fallo comunes, limites de herramientas,
politica de reintentos, observabilidad (logs/metrics/traces), criterios de parada (circuit breaker), y checklist de
privacidad (minimizacion de datos). Termina con un playbook de incidentes.

EN:
Write a runbook to operate this agent in production. Include: common failure modes, tool limits, retry policy,
observability (logs/metrics/traces), stop criteria (circuit breaker), and a privacy checklist (data minimization).
End with an incident playbook.""",
        ),
        PromptCreate(
            title="Docs changelog entry / Entrada de changelog de docs",
            category="Productivity",
            tags=[*shared, "docs", "changelog", "writing"],
            rating=4,
            body="""ES:
Redacta una entrada de changelog para este cambio. Devuelve: titulo, bullets (que cambia, a quien afecta),
breaking changes (si aplica), y como verificar. Tono: claro y conciso, sin marketing.

EN:
Draft a changelog entry for this change. Return: title, bullets (what changed, who is impacted),
breaking changes (if any), and how to verify. Tone: clear and concise, no marketing.""",
        ),
        PromptCreate(
            title="Design system tokens / Tokens de sistema de diseno",
            category="Design",
            tags=[*shared, "design-system", "tokens", "naming"],
            rating=4,
            body="""ES:
Define tokens de diseno para este producto. Incluye: colores (semantic vs primitive), tipografia, espaciado,
radio, sombras, y z-index. Propone convencion de nombres, ejemplos, y reglas de versionado para evitar roturas.

EN:
Define design tokens for this product. Include: colors (semantic vs primitive), typography, spacing, radius,
shadows, and z-index. Propose a naming convention, examples, and versioning rules to avoid breaking changes.""",
        ),
        PromptCreate(
            title="Accessibility audit checklist / Checklist de accesibilidad",
            category="Design",
            tags=[*shared, "a11y", "ux", "audit"],
            rating=4,
            body="""ES:
Haz una auditoria rapida de accesibilidad para esta UI. Devuelve una lista accionable que cubra: navegacion por
teclado, focus visible, contrastes, labels/aria, headings, mensajes de error, y estados vacios. Incluye ejemplos
de cambios concretos (HTML/CSS) cuando sea posible.

EN:
Do a quick accessibility audit for this UI. Return an actionable list covering: keyboard navigation, visible focus,
contrast, labels/aria, headings, error messages, and empty states. Include concrete change examples (HTML/CSS)
when possible.""",
        ),
        PromptCreate(
            title="Landing page hero variants / Variantes de hero para landing",
            category="Marketing",
            tags=[*shared, "marketing", "copy", "landing"],
            rating=4,
            body="""ES:
Genera 5 variantes de hero para esta landing. Cada variante: titular (<= 10 palabras), subtitulo (<= 20),
3 bullets de valor, y CTA. Ajusta el tono a: {tono}. Evita claims no verificables.

EN:
Generate 5 hero variants for this landing page. Each variant: headline (<= 10 words), subheadline (<= 20),
3 value bullets, and a CTA. Match the tone: {tone}. Avoid unverifiable claims.""",
        ),
        PromptCreate(
            title="Pricing FAQ generator / Generador de FAQ de precios",
            category="Marketing",
            tags=[*shared, "pricing", "faq", "copy"],
            rating=4,
            body="""ES:
Crea una FAQ de precios para este producto. Devuelve 12 preguntas + respuestas cortas. Incluye: limites de plan,
facturacion, cancelacion, seguridad, soporte, y comparacion entre planes. Mantente honesto: si falta info,
marca supuestos o deja la respuesta como \"por definir\".

EN:
Create a pricing FAQ for this product. Return 12 Q&As with short answers. Include: plan limits, billing,
cancellation, security, support, and plan comparison. Be honest: if info is missing, state assumptions
or mark as \"TBD\".""",
        ),
        PromptCreate(
            title="SEO keyword clustering / Clusterizacion de keywords SEO",
            category="Marketing",
            tags=[*shared, "seo", "keywords", "content"],
            rating=4,
            body="""ES:
Agrupa estas keywords en clusters por intencion de busqueda. Devuelve: cluster name, keywords, pagina objetivo,
angulo de contenido, y prioridad (alto/medio/bajo). Sugiere 3 titulos por cluster.

EN:
Cluster these keywords by search intent. Return: cluster name, keywords, target page, content angle,
and priority (high/medium/low). Suggest 3 titles per cluster.""",
        ),
        PromptCreate(
            title="Research search plan / Plan de busqueda de investigacion",
            category="Research",
            tags=[*shared, "research", "search", "sources"],
            rating=4,
            body="""ES:
Convierte esta pregunta en un plan de busqueda. Devuelve: subpreguntas, terminos de busqueda, fuentes primarias
vs secundarias, criterios de calidad, sesgos posibles, y un formato para tomar notas con citas.

EN:
Turn this question into a research search plan. Return: sub-questions, search terms, primary vs secondary sources,
quality criteria, potential biases, and a note-taking format with citations.""",
        ),
        PromptCreate(
            title="Synthesis with citations / Sintesis con citas",
            category="Research",
            tags=[*shared, "research", "synthesis", "citations"],
            rating=5,
            body="""ES:
Sintetiza estos documentos. Devuelve: resumen ejecutivo, hallazgos clave, puntos de desacuerdo, lagunas,
y recomendaciones. Para cada hallazgo, incluye 1-2 citas cortas (<= 20 palabras) con referencia al documento.
No inventes fuentes.

EN:
Synthesize these documents. Return: executive summary, key findings, disagreements, gaps, and recommendations.
For each finding, include 1-2 short quotes (<= 20 words) with a document reference. Do not invent sources.""",
        ),
        PromptCreate(
            title="Codex PR reviewer checklist / Checklist de revision de PR con Codex",
            category="Prompts for Codex",
            tags=[*shared, "codex", "review", "pr"],
            rating=4,
            body="""ES:
Actua como reviewer senior. Revisa este PR y devuelve:
1) Riesgos (bugs, datos, seguridad, rendimiento)
2) Cobertura de pruebas (que falta y como testear)
3) API/UX: compatibilidad y edge cases
4) Lista de comentarios accionables (los 5 mas importantes primero)
Si algo es incierto, pide maximo 3 aclaraciones.

EN:
Act as a senior reviewer. Review this PR and return:
1) Risks (bugs, data, security, performance)
2) Test coverage (what's missing and how to test)
3) API/UX: compatibility and edge cases
4) Actionable comments (top 5 first)
If something is uncertain, ask at most 3 clarifying questions.""",
        ),
        PromptCreate(
            title="ChatGPT interviewer roleplay / Roleplay de entrevistador con ChatGPT",
            category="Prompts for ChatGPT",
            tags=[*shared, "chatgpt", "roleplay", "interview"],
            rating=4,
            body="""ES:
Actua como entrevistador para este rol: {rol}. Haz 6 preguntas: 2 de fundamentos, 2 de experiencia, 1 de sistema,
1 de debugging. Espera mi respuesta tras cada pregunta. Al final, evalua con una rubrica (claridad, rigor,
tradeoffs, comunicacion) y sugiere mejoras concretas.

EN:
Act as an interviewer for this role: {role}. Ask 6 questions: 2 fundamentals, 2 experience, 1 system design,
1 debugging. Wait for my answer after each question. At the end, grade with a rubric (clarity, rigor,
tradeoffs, communication) and suggest concrete improvements.""",
        ),
        PromptCreate(
            title="Claude long-doc summary with quotes / Resumen de doc largo con citas (Claude)",
            category="Prompts for Claude",
            tags=[*shared, "claude", "summarization", "quotes"],
            rating=4,
            body="""ES:
Resume este documento largo sin perder precision. Formato de salida:
1) Resumen ejecutivo (<= 8 bullets)
2) Terminos/definiciones
3) Riesgos y preguntas abiertas
4) Acciones recomendadas
Incluye 1-2 citas cortas por seccion (<= 20 palabras) para anclar los puntos. Si falta contexto, pregunta 1-3 cosas.

EN:
Summarize this long document without losing precision. Output format:
1) Executive summary (<= 8 bullets)
2) Terms/definitions
3) Risks and open questions
4) Recommended actions
Include 1-2 short quotes per section (<= 20 words) to ground the points. If context is missing, ask 1-3 questions.""",
        ),
        PromptCreate(
            title="GitHub issue to patch plan / Issue de GitHub a plan de patch",
            category="Coding",
            tags=[*shared, "github", "issue", "plan", "patch"],
            rating=4,
            body="""ES:
Convierte este issue en un plan de implementacion pequeno. Devuelve:
1) Resumen del problema y criterio de exito
2) Cambios propuestos (archivos probables y por que)
3) Riesgos/edge cases
4) Plan de pruebas (unit/integration/manual)
5) Mensaje de commit sugerido
Si falta informacion, pregunta maximo 3 cosas.

EN:
Turn this issue into a small implementation plan. Return:
1) Problem summary and success criteria
2) Proposed changes (likely files and why)
3) Risks/edge cases
4) Test plan (unit/integration/manual)
5) Suggested commit message
If info is missing, ask at most 3 questions.""",
        ),
        PromptCreate(
            title="Spec to OpenAPI skeleton / De spec a esqueleto OpenAPI",
            category="Architecture",
            tags=[*shared, "api", "openapi", "contract"],
            rating=4,
            body="""ES:
Dado este spec informal de una API, genera un esqueleto OpenAPI (YAML) con: paths, metodos, request/response
schemas, codigos de error, y ejemplos minimos. Si hay ambiguedades, anotalas como TODOs.

EN:
Given this informal API spec, generate an OpenAPI (YAML) skeleton with: paths, methods, request/response schemas,
error codes, and minimal examples. If there are ambiguities, note them as TODOs.""",
        ),
        PromptCreate(
            title="Python packaging triage / Triage de packaging Python",
            category="Debugging",
            tags=[*shared, "python", "packaging", "uv", "pip"],
            rating=4,
            body="""ES:
Tengo este error de packaging/instalacion. Diagnosticalo por fases:
1) Hipotesis probables (3 max)
2) Comandos para inspeccionar entorno (python -V, pip/uv, paths)
3) Fixes ordenados por seguridad (no destructivo primero)
4) Como verificar que quedo resuelto
No asumas que puedo borrar todo; prioriza cambios reversibles.

EN:
I have this packaging/install error. Diagnose it in phases:
1) Likely hypotheses (max 3)
2) Commands to inspect the environment (python -V, pip/uv, paths)
3) Fixes ordered by safety (non-destructive first)
4) How to verify it's resolved
Do not assume I can nuke everything; prioritize reversible changes.""",
        ),
        PromptCreate(
            title="TypeScript error explainer / Explicador de error TypeScript",
            category="Coding",
            tags=[*shared, "typescript", "errors", "explain"],
            rating=4,
            body="""ES:
Explica este error de TypeScript como si yo fuera un dev mid. Devuelve:
1) Que significa en lenguaje simple
2) La causa raiz mas probable
3) 2-3 fixes (con pros/contras)
4) Un ejemplo minimo que lo reproduzca
Mantente en lo verificable; no inventes tipos que no se ven.

EN:
Explain this TypeScript error as if I were a mid-level dev. Return:
1) Plain-language meaning
2) Most likely root cause
3) 2-3 fixes (with pros/cons)
4) A minimal example that reproduces it
Stick to what is observable; do not invent types you can't see.""",
        ),
        PromptCreate(
            title="CI failure log summary / Resumen de logs de CI",
            category="Debugging",
            tags=[*shared, "ci", "logs", "triage"],
            rating=4,
            body="""ES:
Resume este log de CI. Devuelve:
1) Fallo principal (1 frase)
2) 3-5 pistas clave (con lineas/palabras relevantes)
3) Causa probable vs alternativas
4) Siguiente accion concreta (comando local o cambio sugerido)
No ocultes incertidumbre: marca lo que es suposicion.

EN:
Summarize this CI log. Return:
1) Primary failure (1 sentence)
2) 3-5 key clues (with relevant lines/keywords)
3) Likely cause vs alternatives
4) Next concrete action (local command or suggested change)
Do not hide uncertainty: label assumptions.""",
        ),
        PromptCreate(
            title="Database index advisor / Asesor de indices",
            category="Architecture",
            tags=[*shared, "database", "performance", "indexes"],
            rating=4,
            body="""ES:
Dada esta query lenta y el esquema (tablas + columnas), sugiere indices. Devuelve:
1) Indices propuestos (por tabla) con justificacion
2) Riesgos (write amplification, size, lock)
3) Como validar (EXPLAIN/ANALYZE) y metricas a mirar
Si faltan datos, lista exactamente que necesitas.

EN:
Given this slow query and schema (tables + columns), suggest indexes. Return:
1) Proposed indexes (per table) with justification
2) Risks (write amplification, size, lock)
3) How to validate (EXPLAIN/ANALYZE) and what metrics to watch
If data is missing, list exactly what you need.""",
        ),
        PromptCreate(
            title="Release notes from commits / Notas de version desde commits",
            category="Productivity",
            tags=[*shared, "release", "changelog", "writing"],
            rating=4,
            body="""ES:
Genera notas de version basadas en estos commits. Separa en: Added, Changed, Fixed, Deprecated, Removed, Security.
Usa lenguaje orientado a usuario final. Marca posibles breaking changes y su migracion. Mantente fiel al texto: no
inventes features.

EN:
Generate release notes from these commits. Split into: Added, Changed, Fixed, Deprecated, Removed, Security.
Use end-user language. Flag potential breaking changes and migration guidance. Stay faithful to the text: do not
invent features.""",
        ),
        PromptCreate(
            title="Support reply template (no PII) / Respuesta de soporte (sin PII)",
            category="Productivity",
            tags=[*shared, "support", "writing", "tone"],
            rating=4,
            body="""ES:
Escribe una respuesta de soporte para este ticket. Reglas: no incluyas datos personales, no inventes politicas,
y pide solo la informacion minima. Devuelve 3 versiones (breve, estandar, muy empatica) y un checklist interno
de seguimiento.

EN:
Write a support reply for this ticket. Rules: do not include personal data, do not invent policies, and ask only
for the minimum needed info. Return 3 versions (brief, standard, very empathetic) and an internal follow-up
checklist.""",
        ),
        PromptCreate(
            title="Prompt library de-dup audit / Auditoria de duplicados de prompts",
            category="Prompts",
            tags=[*shared, "library", "dedup", "quality"],
            rating=4,
            body="""ES:
Analiza esta lista de prompts y detecta duplicados o solapes fuertes. Devuelve:
1) Grupos de prompts similares (con puntuacion 0-1 de similitud)
2) Recomendacion: fusionar, renombrar, o mantener (con razon)
3) Tags/categorias sugeridas para mejorar el orden

EN:
Analyze this prompt list and detect duplicates or strong overlaps. Return:
1) Groups of similar prompts (with a 0-1 similarity score)
2) Recommendation: merge, rename, or keep (with rationale)
3) Suggested tags/categories to improve organization.""",
        ),
        PromptCreate(
            title="Agent safety guardrails / Guardrails de seguridad para agentes",
            category="Agents",
            tags=[*shared, "agents", "safety", "guardrails"],
            rating=5,
            body="""ES:
Define guardrails para un agente que ejecuta tareas en un repo. Incluye:
- Limites (que nunca hacer)
- Politicas de datos (no PII, no secretos, no exfiltracion)
- Reglas de comandos (evitar deletes recursivos, pedir confirmacion)
- Formato de logs/auditoria
- Criterios para parar y pedir ayuda humana

EN:
Define guardrails for an agent that executes tasks in a repo. Include:
- Limits (what it must never do)
- Data policies (no PII, no secrets, no exfiltration)
- Command rules (avoid recursive deletes, ask for confirmation)
- Logging/audit format
- Criteria to stop and ask for human help.""",
        ),
        PromptCreate(
            title="Tool-use fallback plan / Plan de fallback si faltan herramientas",
            category="Agents",
            tags=[*shared, "tools", "fallback", "planning"],
            rating=4,
            body="""ES:
Para esta tarea, crea un plan A/B/C:
Plan A: con todas las herramientas disponibles
Plan B: sin acceso a red
Plan C: solo lectura (sin escribir archivos)
Para cada plan, lista pasos, limitaciones y como validar resultados.

EN:
For this task, create an A/B/C plan:
Plan A: with all tools available
Plan B: with no network access
Plan C: read-only (no file writes)
For each plan, list steps, limitations, and how to validate results.""",
        ),
        PromptCreate(
            title="System prompt critique / Critica de system prompt",
            category="Prompts",
            tags=[*shared, "prompting", "system", "review"],
            rating=4,
            body="""ES:
Revisa este system prompt. Identifica ambiguedades, conflictos, requisitos imposibles y gaps de seguridad.
Propone una version mejorada con: objetivo claro, limites, formato de salida, y politicas de datos. Mantiene el
tono y la intencion original.

EN:
Review this system prompt. Identify ambiguities, conflicts, impossible requirements, and safety gaps.
Propose an improved version with: clear goal, limits, output format, and data policies. Preserve the original
tone and intent.""",
        ),
        PromptCreate(
            title="Docs writing checklist / Checklist de escritura de docs",
            category="Productivity",
            tags=[*shared, "docs", "writing", "clarity"],
            rating=4,
            body="""ES:
Estoy escribiendo docs tecnicas. Dame un checklist de calidad: objetivos, audiencia, prerequisitos, ejemplos,
errores comunes, troubleshooting, enlaces, y mantenimiento. Luego aplica el checklist a este borrador y sugiere
mejoras concretas (sin reescribir todo).

EN:
I'm writing technical docs. Give me a quality checklist: goals, audience, prerequisites, examples,
common pitfalls, troubleshooting, links, and maintenance. Then apply the checklist to this draft and suggest
concrete improvements (without rewriting everything).""",
        ),
        PromptCreate(
            title="Design token naming scheme / Esquema de nombres para design tokens",
            category="Design",
            tags=[*shared, "design", "tokens", "naming"],
            rating=4,
            body="""ES:
Propone un esquema de nombres para design tokens (color, typography, spacing, radius, shadow). Reglas:
consistente, escalable, sin acoplarse a implementacion. Devuelve ejemplos y guidelines de migracion desde nombres
ad-hoc.

EN:
Propose a naming scheme for design tokens (color, typography, spacing, radius, shadow). Rules:
consistent, scalable, not tied to implementation details. Return examples and migration guidelines from
ad-hoc names.""",
        ),
        PromptCreate(
            title="Accessible alt text generator / Generador de alt text accesible",
            category="Design",
            tags=[*shared, "accessibility", "alt-text", "a11y"],
            rating=4,
            body="""ES:
Escribe alt text accesible para estas imagenes. Devuelve 2 versiones por imagen:
1) Alt corto (<= 125 caracteres)
2) Descripcion extendida (para longdesc o notas)
Evita redundancias como \"imagen de\" y respeta el contexto de la pagina.

EN:
Write accessible alt text for these images. Return 2 versions per image:
1) Short alt (<= 125 characters)
2) Extended description (for longdesc or notes)
Avoid redundancy like \"image of\" and respect the page context.""",
        ),
        PromptCreate(
            title="Meeting minutes to tasks / Acta de reunion a tareas",
            category="Productivity",
            tags=[*shared, "meetings", "action-items", "planning"],
            rating=4,
            body="""ES:
Convierte estas notas de reunion en tareas accionables. Devuelve:
- Decisiones
- Acciones (owner, deadline, dependencia)
- Riesgos y follow-ups
- Preguntas abiertas
Mantente fiel al texto; no inventes compromisos.

EN:
Turn these meeting notes into actionable tasks. Return:
- Decisions
- Actions (owner, deadline, dependency)
- Risks and follow-ups
- Open questions
Stay faithful to the text; do not invent commitments.""",
        ),
        PromptCreate(
            title="Research claim checker / Verificador de claims con fuentes",
            category="Research",
            tags=[*shared, "research", "fact-check", "citations"],
            rating=5,
            body="""ES:
Evalua estas afirmaciones. Para cada una: clasifica (hecho/inferencia/opinion), que evidencia hace falta,
y como verificaria con fuentes primarias. Si hay una fuente dada, cita exactamente que parte la soporta o no.

EN:
Evaluate these claims. For each: classify (fact/inference/opinion), what evidence is needed,
and how you would verify using primary sources. If sources are provided, cite exactly what supports (or doesn't)
each claim.""",
        ),
        PromptCreate(
            title="Codebase onboarding map / Mapa de onboarding del codebase",
            category="Architecture",
            tags=[*shared, "onboarding", "codebase", "architecture"],
            rating=4,
            body="""ES:
Ayudame a onboardear en este repo. Con el arbol de carpetas y 2-3 archivos clave, crea un mapa:
1) Modulos principales y responsabilidades
2) Flujos end-to-end (request -> response, build -> deploy)
3) \"Where to change X\" (3 ejemplos)
4) Checklist para correr, testear y debugear

EN:
Help me onboard to this repo. Using the folder tree and 2-3 key files, create a map:
1) Main modules and responsibilities
2) End-to-end flows (request -> response, build -> deploy)
3) \"Where to change X\" (3 examples)
4) Checklist to run, test, and debug.""",
        ),
        PromptCreate(
            title="Claude strict JSON extraction / Extraccion JSON estricta (Claude)",
            category="Prompts for Claude",
            tags=[*shared, "claude", "json", "extraction"],
            rating=4,
            body="""ES:
Extrae los datos a JSON estricto segun este schema. Reglas:
- Solo JSON valido, sin texto extra
- Si falta un campo, usa null
- Si no se puede inferir, agrega un array \"unknowns\" con preguntas
Schema:
{schema}
Texto:
{text}

EN:
Extract data into strict JSON per this schema. Rules:
- Output valid JSON only, no extra text
- If a field is missing, use null
- If it can't be inferred, add an \"unknowns\" array with questions
Schema:
{schema}
Text:
{text}""",
        ),
        PromptCreate(
            title="Codex safe refactor checklist / Checklist de refactor seguro (Codex)",
            category="Prompts for Codex",
            tags=[*shared, "codex", "refactor", "safety"],
            rating=5,
            body="""ES:
Quiero refactorizar sin cambiar comportamiento. Sigue este checklist:
1) Define invariantes observables (tests, outputs, contratos)
2) Haz cambios pequenos y mecanicos
3) Ejecuta checks y tests tras cada paso
4) Evita cambios de estilo no relacionados
5) Si algo falla, reduce el diff y aisla la causa
Devuelve el plan y los comandos de verificacion.

EN:
I want to refactor without changing behavior. Follow this checklist:
1) Define observable invariants (tests, outputs, contracts)
2) Make small, mechanical changes
3) Run checks and tests after each step
4) Avoid unrelated style changes
5) If something fails, shrink the diff and isolate the cause
Return the plan and verification commands.""",
        ),
        PromptCreate(
            title="PR description generator / Generador de descripcion de PR",
            category="Productivity",
            tags=[*shared, "pr", "github", "writing", "communication"],
            rating=4,
            body="""ES:
Escribe la descripcion de este PR para que sea facil de revisar. Incluye:
- Contexto y objetivo
- Cambios principales (bullet points)
- Riesgos y mitigaciones
- Como probar (comandos)
- Screenshots/recordings si aplica
- Notas de rollout / backwards-compat

Inputs:
Repo: {repo}
Issue/link: {link}
Resumen de cambios: {changes}

EN:
Write a PR description that is easy to review. Include:
- Context and goal
- Key changes (bullets)
- Risks and mitigations
- How to test (commands)
- Screenshots/recordings if applicable
- Rollout/backwards-compat notes

Inputs:
Repo: {repo}
Issue/link: {link}
Change summary: {changes}""",
        ),
        PromptCreate(
            title="Dependency upgrade plan / Plan de actualizacion de dependencias",
            category="Debugging",
            tags=[*shared, "deps", "upgrade", "risk", "tests"],
            rating=4,
            body="""ES:
Quiero actualizar dependencias con bajo riesgo. Dado este proyecto y su lockfile, propon:
1) Orden de actualizacion (segun riesgo/impacto)
2) Cambios de compatibilidad probables
3) Checklist de verificacion (lint, tests, build, smoke)
4) Plan de rollback
5) PRs pequenos sugeridos (1-3)

Contexto del proyecto:
{context}

EN:
I want to upgrade dependencies with low risk. Given this project and its lockfile, propose:
1) Upgrade order (by risk/impact)
2) Likely breaking changes
3) Verification checklist (lint, tests, build, smoke)
4) Rollback plan
5) Suggested small PR slices (1-3)

Project context:
{context}""",
        ),
        PromptCreate(
            title="Observability checklist / Checklist de observabilidad",
            category="Architecture",
            tags=[*shared, "observability", "logging", "metrics", "tracing"],
            rating=5,
            body="""ES:
Ayudame a hacer este servicio observable. Para cada endpoint/flujo, sugiere:
- Logs (campos estructurados, niveles, ejemplos)
- Metricas (SLIs/SLOs sugeridos)
- Trazas (spans, atributos, propagacion)
- Alertas (umbral + accion)
- Dashboards (widgets clave)
Reglas: no incluyas PII, tokens, secretos, ni payloads completos; sugiere redaccion/mascaras.

Servicio/flujo:
{service}

EN:
Help me make this service observable. For each endpoint/flow, suggest:
- Logs (structured fields, levels, examples)
- Metrics (suggested SLIs/SLOs)
- Traces (spans, attributes, propagation)
- Alerts (threshold + action)
- Dashboards (key widgets)
Rules: do not include PII, tokens, secrets, or full payloads; suggest redaction/masking.

Service/flow:
{service}""",
        ),
        PromptCreate(
            title="Caching strategy / Estrategia de caching",
            category="Architecture",
            tags=[*shared, "cache", "performance", "architecture"],
            rating=4,
            body="""ES:
Disena una estrategia de caching para este sistema. Incluye:
1) Que cachear (y que NO cachear)
2) Key design (incluye versionado)
3) TTLs e invalidacion (eventos)
4) Consistencia vs latencia (tradeoffs)
5) Observabilidad (metricas de hit/miss, staleness)
6) Riesgos (cache stampede, thundering herd) y mitigacion

Contexto:
{context}

EN:
Design a caching strategy for this system. Include:
1) What to cache (and what NOT to cache)
2) Cache key design (including versioning)
3) TTLs and invalidation (events)
4) Consistency vs latency tradeoffs
5) Observability (hit/miss, staleness metrics)
6) Risks (stampede/thundering herd) and mitigations

Context:
{context}""",
        ),
        PromptCreate(
            title="API rate limiting design / Diseno de rate limiting API",
            category="Architecture",
            tags=[*shared, "api", "rate-limit", "abuse", "security"],
            rating=4,
            body="""ES:
Disena rate limiting para esta API. Necesito:
- Limites por actor (IP, user, token) y por endpoint
- Respuesta estandar (status, headers, body)
- Estrategia para bursts (leaky bucket/token bucket)
- Manejo de retries y backoff (recomendaciones al cliente)
- Exenciones (admins, webhooks) con auditoria
- Plan de tests (incluye casos de abuso)

API:
{api}

EN:
Design rate limiting for this API. I need:
- Limits per actor (IP, user, token) and per endpoint
- Standard response (status, headers, body)
- Burst strategy (leaky bucket/token bucket)
- Retry/backoff guidance for clients
- Exemptions (admins, webhooks) with audit trail
- Test plan (including abuse cases)

API:
{api}""",
        ),
        PromptCreate(
            title="Error message rewrite / Reescritura de mensajes de error",
            category="Design",
            tags=[*shared, "ux", "errors", "copy", "accessibility"],
            rating=4,
            body="""ES:
Reescribe estos mensajes de error para que sean claros, accionables y amables.
Para cada error devuelve:
- Mensaje corto (UI)
- Detalle opcional (expandible)
- Accion sugerida
- Si es error del sistema vs del usuario
Reglas: no culpes al usuario, evita jerga tecnica, no expongas datos sensibles, incluye variantes para lector de pantalla si aplica.

Errores:
{errors}

EN:
Rewrite these error messages to be clear, actionable, and kind.
For each error return:
- Short UI message
- Optional details (expandable)
- Suggested action
- Whether it's user-caused vs system-caused
Rules: don't blame the user, avoid jargon, don't expose sensitive data, include screen-reader-friendly variants when applicable.

Errors:
{errors}""",
        ),
        PromptCreate(
            title="UX microcopy A/B variants / Variantes A/B de microcopy UX",
            category="Design",
            tags=[*shared, "ux", "microcopy", "ab-test", "writing"],
            rating=4,
            body="""ES:
Genera 10 variantes de microcopy para este UI. Para cada variante:
- Texto (max {max_chars} caracteres)
- Tono (ej: directo, calido, tecnico)
- Hipotesis de impacto (que mejora y por que)
Tambien sugiere 2 metricas y un plan A/B simple.

Contexto UI:
{context}

EN:
Generate 10 microcopy variants for this UI. For each variant:
- Text (max {max_chars} characters)
- Tone (e.g., direct, warm, technical)
- Impact hypothesis (what it improves and why)
Also suggest 2 metrics and a simple A/B plan.

UI context:
{context}""",
        ),
        PromptCreate(
            title="Pair programming loop / Bucle de pair programming",
            category="Prompts",
            tags=[*shared, "pairing", "coding", "workflow"],
            rating=4,
            body="""ES:
Vamos a programar en pareja. Reglas del flujo:
1) Yo te doy objetivo + constraints
2) Tu propones 2 opciones (A/B) y eliges una con razon
3) Escribes un plan de 3-6 pasos
4) Implementas en incrementos pequenos con checkpoints
5) Tras cada checkpoint, me pides confirmacion o inputs faltantes
6) Terminas con verificacion y resumen

Objetivo:
{goal}
Constraints:
{constraints}

EN:
Let's pair program. Workflow rules:
1) I give you a goal + constraints
2) You propose 2 options (A/B) and choose one with rationale
3) You write a 3-6 step plan
4) You implement in small increments with checkpoints
5) After each checkpoint, ask for confirmation or missing inputs
6) Finish with verification and a summary

Goal:
{goal}
Constraints:
{constraints}""",
        ),
        PromptCreate(
            title="LLM eval set builder / Constructor de set de evaluacion LLM",
            category="Research",
            tags=[*shared, "evals", "llm", "quality", "testing"],
            rating=5,
            body="""ES:
Quiero construir un set de evaluacion para esta tarea de LLM. Crea:
1) 20-50 casos de prueba variados (incluye edge cases)
2) Criterios de exito (rubrica con puntuacion)
3) Casos adversariales / seguridad (sin PII)
4) Un formato JSONL sugerido para almacenar inputs/expected
5) Como muestrear y evitar sobreajuste

Tarea:
{task}

EN:
I want to build an evaluation set for this LLM task. Create:
1) 20-50 diverse test cases (including edge cases)
2) Success criteria (scored rubric)
3) Adversarial / safety cases (no PII)
4) A suggested JSONL format for inputs/expected
5) Sampling guidance to avoid overfitting

Task:
{task}""",
        ),
        PromptCreate(
            title="RAG chunking + retrieval plan / Plan de chunking + retrieval (RAG)",
            category="Architecture",
            tags=[*shared, "rag", "search", "retrieval", "architecture"],
            rating=4,
            body="""ES:
Disena una estrategia RAG para este corpus. Incluye:
- Tipos de documentos y estructura (headers, tablas, codigo)
- Chunking (tamano, solapamiento, reglas por tipo)
- Metadata (source, section, timestamps, permisos)
- Indexing y recuperacion (BM25 vs embeddings, rerank)
- Prompt de respuesta (citas a fuentes internas)
- Plan de evaluacion (precision, coverage, hallucinations)
Reglas: no inventes contenido; si falta informacion, pregunta.

Corpus:
{corpus}

EN:
Design a RAG strategy for this corpus. Include:
- Document types and structure (headers, tables, code)
- Chunking (size, overlap, per-type rules)
- Metadata (source, section, timestamps, permissions)
- Indexing/retrieval (BM25 vs embeddings, rerank)
- Answer prompt (with citations to internal sources)
- Evaluation plan (precision, coverage, hallucinations)
Rules: do not fabricate content; ask questions when info is missing.

Corpus:
{corpus}""",
        ),
        PromptCreate(
            title="Data privacy review / Revision de privacidad de datos",
            category="Architecture",
            tags=[*shared, "privacy", "security", "data", "compliance"],
            rating=5,
            body="""ES:
Haz una revision de privacidad de este flujo de datos. Devuelve:
1) Datos recolectados (clasificalos: PII, sensibles, no sensibles)
2) Finalidad y minimizacion (que se puede eliminar/anonimizar)
3) Retencion y borrado
4) Accesos y permisos (principio de minimo privilegio)
5) Riesgos (reidentificacion, leak, prompt injection) y mitigaciones
6) Checklist de implementacion
Reglas: no pidas datos reales; usa ejemplos ficticios.

Flujo:
{flow}

EN:
Do a privacy review of this data flow. Return:
1) Data collected (classify: PII, sensitive, non-sensitive)
2) Purpose and minimization (what can be removed/anonymized)
3) Retention and deletion
4) Access controls (least privilege)
5) Risks (reidentification, leaks, prompt injection) and mitigations
6) Implementation checklist
Rules: don't ask for real data; use fictitious examples.

Flow:
{flow}""",
        ),
        PromptCreate(
            title="Meeting agenda builder / Generador de agenda de reunion",
            category="Productivity",
            tags=[*shared, "meeting", "agenda", "facilitation"],
            rating=4,
            body="""ES:
Crea una agenda de 30/45/60 minutos para esta reunion. Incluye:
- Objetivo (1 frase)
- Decisiones a tomar (max 3)
- Bloques con tiempos y owner
- Pre-reads
- Resultado esperado (artefactos/tareas)
- Preguntas para desbloquear

Tema:
{topic}
Participantes:
{attendees}

EN:
Create a 30/45/60-minute agenda for this meeting. Include:
- Goal (1 sentence)
- Decisions to make (max 3)
- Timed blocks with owner
- Pre-reads
- Expected outputs (artifacts/tasks)
- Questions to unblock progress

Topic:
{topic}
Attendees:
{attendees}""",
        ),
        PromptCreate(
            title="Roadmap prioritization (RICE) / Priorizacion de roadmap (RICE)",
            category="Productivity",
            tags=[*shared, "roadmap", "prioritization", "rice", "strategy"],
            rating=4,
            body="""ES:
Priorizemos este backlog usando RICE (Reach, Impact, Confidence, Effort).
1) Propone una escala concreta para cada factor
2) Rellena una tabla con R, I, C, E y score
3) Explica los top 5 y por que
4) Marca items con baja confianza y sugiere que datos faltan
5) Sugiere el siguiente experimento para subir la confianza

Backlog:
{backlog}

EN:
Let's prioritize this backlog using RICE (Reach, Impact, Confidence, Effort).
1) Propose a concrete scale for each factor
2) Fill a table with R, I, C, E and the score
3) Explain the top 5 and why
4) Flag low-confidence items and what data is missing
5) Suggest the next experiment to increase confidence

Backlog:
{backlog}""",
        ),
        PromptCreate(
            title="Customer persona generator / Generador de personas",
            category="Marketing",
            tags=[*shared, "marketing", "personas", "positioning"],
            rating=4,
            body="""ES:
Genera 3 personas para este producto. Para cada una incluye:
- Contexto y objetivo
- Trigger de compra
- Objeciones
- Jobs-to-be-done
- Mensajes clave (3)
- Canales de adquisicion probables
Reglas: no inventes datos sensibles; usa supuestos explicitamente marcados.

Producto:
{product}

EN:
Generate 3 customer personas for this product. For each include:
- Context and goal
- Purchase trigger
- Objections
- Jobs-to-be-done
- Key messages (3)
- Likely acquisition channels
Rules: don't invent sensitive details; clearly mark assumptions.

Product:
{product}""",
        ),
        PromptCreate(
            title="Product announcement post / Post de anuncio de producto",
            category="Marketing",
            tags=[*shared, "launch", "copy", "marketing", "social"],
            rating=4,
            body="""ES:
Escribe un post de anuncio para {channel} (ej: X, LinkedIn, blog). Incluye:
- Hook en la primera linea
- Problema -> solucion -> beneficio
- 3 bullets con features
- CTA claro
- 3 variantes de tono (neutral, entusiasta, tecnico)
Reglas: no hagas claims no verificables; si falta una metrica, deja un placeholder.

Inputs:
Producto: {product}
Audiencia: {audience}
Features: {features}

EN:
Write a product announcement post for {channel} (e.g., X, LinkedIn, blog). Include:
- First-line hook
- Problem -> solution -> benefit
- 3 feature bullets
- Clear CTA
- 3 tone variants (neutral, excited, technical)
Rules: avoid unverifiable claims; if a metric is missing, use a placeholder.

Inputs:
Product: {product}
Audience: {audience}
Features: {features}""",
        ),
        PromptCreate(
            title="Claude tool-use planner / Planificador de tool-use (Claude)",
            category="Prompts for Claude",
            tags=[*shared, "claude", "tools", "planning", "agents"],
            rating=4,
            body="""ES:
Eres un agente que puede usar herramientas. Antes de actuar:
1) Lista objetivos y criterios de exito
2) Enumera herramientas disponibles y que aporta cada una
3) Propone un plan con pasos pequenos y puntos de verificacion
4) Si falta informacion, pregunta antes de ejecutar acciones irreversibles
5) Al final, entrega resumen + siguientes pasos

Tarea:
{task}

EN:
You are an agent that can use tools. Before acting:
1) List goals and success criteria
2) Enumerate available tools and what each provides
3) Propose a plan with small steps and verification checkpoints
4) If info is missing, ask before irreversible actions
5) At the end, deliver a summary + next steps

Task:
{task}""",
        ),
        PromptCreate(
            title="Codex repo cleanup task / Tarea de limpieza de repo (Codex)",
            category="Prompts for Codex",
            tags=[*shared, "codex", "cleanup", "maintenance", "repo"],
            rating=4,
            body="""ES:
Limpia este repo sin cambios funcionales. Reglas:
- No cambies comportamiento
- No toques dependencias salvo que sea necesario
- Cambios pequenos y faciles de revisar
Checklist:
1) Elimina codigo muerto y archivos obsoletos (si se confirma)
2) Ordena imports / formatea segun el formatter del repo
3) Arregla warnings triviales del linter
4) Actualiza docs menores (si estan desincronizadas)
5) Ejecuta checks y tests y reporta resultados
Devuelve el diff planificado antes de aplicar cambios grandes.

EN:
Clean up this repo with no functional changes. Rules:
- Don't change behavior
- Don't touch dependencies unless necessary
- Keep changes small and reviewable
Checklist:
1) Remove dead code/obsolete files (when confirmed)
2) Sort imports / format with the repo formatter
3) Fix trivial linter warnings
4) Update small docs if out of sync
5) Run checks/tests and report results
Return a planned diff before applying large changes.""",
        ),
        PromptCreate(
            title="System prompt red-team / Red-team de system prompt",
            category="Prompts",
            tags=[*shared, "security", "prompting", "redteam"],
            rating=5,
            body="""ES:
Quiero hacer red-team de este system prompt. Genera:
1) 15 ataques (jailbreaks, inyeccion, data exfiltration) en distintos estilos
2) Para cada ataque: objetivo, por que podria funcionar, severidad
3) Mejoras al prompt para mitigarlo (sin hacerlo demasiado largo)
4) Un set minimo de tests automatizables
Reglas: no incluyas datos reales, secretos, ni instrucciones ilegales; enfocate en seguridad defensiva.

System prompt:
{prompt}

EN:
I want to red-team this system prompt. Generate:
1) 15 attacks (jailbreaks, injection, data exfiltration) in different styles
2) For each: goal, why it might work, severity
3) Prompt improvements to mitigate (without making it too long)
4) A minimal set of automatable tests
Rules: no real data, no secrets, no illegal instructions; focus on defensive security.

System prompt:
{prompt}""",
        ),
        PromptCreate(
            title="Incident postmortem template / Plantilla de postmortem",
            category="Productivity",
            tags=[*shared, "incident", "postmortem", "reliability"],
            rating=4,
            body="""ES:
Rellena un postmortem sin culpas para este incidente. Estructura:
- Resumen (1 parrafo)
- Impacto (quien, cuanto, cuanto tiempo)
- Timeline (timestamps)
- Causa raiz (5 whys)
- Que funciono / que no
- Acciones (owner, prioridad, fecha)
- Deteccion y alertas (que faltaba)
Reglas: no incluyas datos personales; anonimiza nombres.

Incidente:
{incident}

EN:
Fill a blameless postmortem for this incident. Structure:
- Summary (1 paragraph)
- Impact (who, how much, for how long)
- Timeline (timestamps)
- Root cause (5 whys)
- What went well / what didn't
- Action items (owner, priority, due date)
- Detection/alerts (what was missing)
Rules: no personal data; anonymize names.

Incident:
{incident}""",
        ),
        PromptCreate(
            title="Codex test-first bugfix / Bugfix test-first (Codex)",
            category="Prompts for Codex",
            tags=[*shared, "codex", "tdd", "bugfix", "tests"],
            rating=5,
            body="""ES:
Arregla este bug con enfoque test-first:
1) Escribe un test que falle (repro minimo)
2) Ejecuta tests para confirmar el fallo
3) Implementa el fix mas pequeno que pase
4) Refactoriza si hace falta
5) Ejecuta lint/format/tests y reporta output
Reglas: no cambies APIs publicas salvo que lo justifiques; prioriza causa raiz.

Bug:
{bug}

EN:
Fix this bug with a test-first approach:
1) Write a failing test (minimal repro)
2) Run tests to confirm failure
3) Implement the smallest fix that passes
4) Refactor if needed
5) Run lint/format/tests and report output
Rules: don't change public APIs unless justified; prioritize root cause.

Bug:
{bug}""",
        ),
        PromptCreate(
            title="Code review with risk matrix / Code review con matriz de riesgo",
            category="Coding",
            tags=[*shared, "code-review", "risk", "quality", "checklist"],
            rating=5,
            body="""ES:
Haz una revision de codigo con foco en riesgos. Entrega:
1) Resumen de cambios (3-6 bullets)
2) Matriz de riesgo: (Severidad x Probabilidad) para cada hallazgo
3) Hallazgos por categoria: Correctitud, Seguridad, Rendimiento, DX, Mantenibilidad
4) Recomendaciones concretas con snippets cortos (si aplica)
5) Preguntas de aclaracion (si faltan requisitos)
Reglas: no inventes contexto; cita lineas/archivos cuando se proporcionen.

Codigo / diff:
{diff}

EN:
Do a code review focused on risk. Provide:
1) Change summary (3–6 bullets)
2) Risk matrix: (Severity x Likelihood) per finding
3) Findings by category: Correctness, Security, Performance, DX, Maintainability
4) Concrete recommendations with short snippets (if applicable)
5) Clarifying questions (if requirements are missing)
Rules: don't invent context; reference lines/files when provided.

Code / diff:
{diff}""",
        ),
        PromptCreate(
            title="Minimal reproducible example builder / Constructor de ejemplo minimo reproducible",
            category="Debugging",
            tags=[*shared, "debugging", "mre", "repro", "triage"],
            rating=5,
            body="""ES:
Ayudame a crear un ejemplo minimo reproducible (MRE) para este bug. Proceso:
1) Reescribe el bug como: entrada -> pasos -> salida observada -> salida esperada
2) Identifica dependencias y elimina todo lo no esencial
3) Propone el MRE en un unico archivo (o el minimo numero posible)
4) Incluye comandos para ejecutar y verificar
5) Enumera 3 hipotesis de causa raiz y como confirmarlas con logs/asserts
Reglas: no incluyas datos reales; usa placeholders.

Descripcion del bug:
{bug}

Contexto (opcional):
{context}

EN:
Help me build a minimal reproducible example (MRE) for this bug. Process:
1) Rewrite as: input -> steps -> observed output -> expected output
2) Identify dependencies and remove anything non-essential
3) Propose the MRE as a single file (or the minimum possible)
4) Include commands to run and verify
5) List 3 root-cause hypotheses and how to confirm with logs/asserts
Rules: no real data; use placeholders.

Bug description:
{bug}

Context (optional):
{context}""",
        ),
        PromptCreate(
            title="API pagination design / Diseno de paginacion API",
            category="Architecture",
            tags=[*shared, "api", "pagination", "design", "backend"],
            rating=4,
            body="""ES:
Disena paginacion para este endpoint. Entrega:
- Opcion A: offset/limit (pros/contras, limites)
- Opcion B: cursor-based (formato de cursor, orden estable, consistencia)
- Contrato API: request/response JSON + ejemplos
- Consideraciones: filtros, sorting, total counts, caching, rate limits
- Estrategia de migracion si ya existe un esquema previo
Reglas: prioriza simplicidad y compatibilidad hacia atras.

Endpoint:
{endpoint}

Modelo de datos (opcional):
{schema}

EN:
Design pagination for this endpoint. Provide:
- Option A: offset/limit (pros/cons, limits)
- Option B: cursor-based (cursor format, stable ordering, consistency)
- API contract: request/response JSON + examples
- Considerations: filters, sorting, total counts, caching, rate limits
- Migration strategy if an older scheme exists
Rules: prioritize simplicity and backward compatibility.

Endpoint:
{endpoint}

Data model (optional):
{schema}""",
        ),
        PromptCreate(
            title="Database migration safety plan / Plan seguro de migraciones de BD",
            category="Architecture",
            tags=[*shared, "database", "migrations", "reliability", "rollback"],
            rating=5,
            body="""ES:
Propone un plan seguro para esta migracion de base de datos. Incluye:
1) Cambios de esquema (DDL) y su impacto
2) Plan en fases (expand/contract) si hay cambios breaking
3) Backfill: estrategia, batches, idempotencia, reintentos
4) Rollout: flags, despliegue, compatibilidad de versiones
5) Rollback: que se puede revertir y que no
6) Verificaciones: queries de salud y validaciones de datos
Reglas: evita downtime cuando sea posible; explica tradeoffs.

Migracion:
{migration}

Stack (opcional):
{stack}

EN:
Propose a safe plan for this database migration. Include:
1) Schema changes (DDL) and impact
2) Phased plan (expand/contract) for breaking changes
3) Backfill: strategy, batching, idempotency, retries
4) Rollout: flags, deployment, version compatibility
5) Rollback: what can/can't be reverted
6) Verification: health queries and data validations
Rules: avoid downtime when possible; explain tradeoffs.

Migration:
{migration}

Stack (optional):
{stack}""",
        ),
        PromptCreate(
            title="UI accessibility audit / Auditoria de accesibilidad UI",
            category="Design",
            tags=[*shared, "a11y", "accessibility", "ux", "design"],
            rating=5,
            body="""ES:
Audita la accesibilidad de esta UI y propone mejoras. Entrega:
1) Problemas detectados (prioridad Alta/Media/Baja)
2) Recomendaciones: texto alternativo, labels, foco, contraste, semantica
3) Checklist de pruebas manuales (teclado, screen reader)
4) Cambios sugeridos en HTML/CSS (snippets cortos)
Reglas: asume WCAG como referencia general, pero no cites numeros exactos si no se proveen.

UI (descripcion, markup o captura):
{ui}

EN:
Audit this UI for accessibility and propose improvements. Provide:
1) Issues found (High/Medium/Low priority)
2) Recommendations: alt text, labels, focus, contrast, semantics
3) Manual testing checklist (keyboard, screen reader)
4) Suggested HTML/CSS changes (short snippets)
Rules: use WCAG as general guidance, but don't cite exact clause numbers unless provided.

UI (description, markup, or screenshot):
{ui}""",
        ),
        PromptCreate(
            title="Design critique rubric / Rubrica de critica de diseno",
            category="Design",
            tags=[*shared, "design", "critique", "ui", "rubric"],
            rating=4,
            body="""ES:
Critica este diseno usando una rubrica consistente. Evalua (0-5) y justifica:
- Claridad (jerarquia, escaneabilidad)
- Consistencia (espaciados, tipografia, patrones)
- Accion (CTA, affordances)
- Accesibilidad (contraste, foco, texto)
- Confianza (errores, estados vacios, feedback)
Termina con: 3 quick wins y 2 apuestas grandes.

Diseno:
{design}

EN:
Critique this design using a consistent rubric. Score (0–5) and justify:
- Clarity (hierarchy, scannability)
- Consistency (spacing, typography, patterns)
- Action (CTA, affordances)
- Accessibility (contrast, focus, text)
- Trust (errors, empty states, feedback)
End with: 3 quick wins and 2 big bets.

Design:
{design}""",
        ),
        PromptCreate(
            title="Landing page value prop / Propuesta de valor para landing",
            category="Marketing",
            tags=[*shared, "marketing", "copy", "landing", "positioning"],
            rating=5,
            body="""ES:
Escribe copy para una landing page con enfoque en conversion. Entrega:
1) 5 opciones de titular + subtitulo
2) Seccion \"Como funciona\" (3 pasos)
3) Beneficios (no features) en bullets
4) Objeciones comunes + respuestas (FAQ)
5) 2 CTAs con microcopy
Tono:
{tone}

Producto:
{product}

Audiencia:
{audience}

EN:
Write landing page copy focused on conversion. Provide:
1) 5 headline + subheadline options
2) \"How it works\" section (3 steps)
3) Benefits (not features) as bullets
4) Common objections + answers (FAQ)
5) 2 CTAs with microcopy
Tone:
{tone}

Product:
{product}

Audience:
{audience}""",
        ),
        PromptCreate(
            title="SEO brief generator / Generador de brief SEO",
            category="Marketing",
            tags=[*shared, "seo", "content", "marketing", "brief"],
            rating=4,
            body="""ES:
Genera un brief SEO para este tema. Incluye:
- Intento de busqueda y audiencia
- Outline con H2/H3
- Lista de preguntas (People Also Ask style) sin inventar datos
- Tono, longitud objetivo y estructura de introduccion
- \"Do / Don't\" (claims, compliance, estilo)
- 10 keywords relacionadas (sin volumen; solo semantica)
Reglas: no inventes estadisticas; marca claramente lo que requiera fuentes.

Tema:
{topic}

EN:
Generate an SEO brief for this topic. Include:
- Search intent and audience
- Outline with H2/H3
- Question list (People Also Ask style) without making up facts
- Tone, target length, and intro structure
- Do/Don't (claims, compliance, style)
- 10 related keywords (no volume; semantic only)
Rules: don't invent statistics; clearly mark anything that needs sources.

Topic:
{topic}""",
        ),
        PromptCreate(
            title="Weekly execution plan / Plan semanal de ejecucion",
            category="Productivity",
            tags=[*shared, "planning", "weekly", "prioritization", "execution"],
            rating=4,
            body="""ES:
Convierte estos objetivos en un plan semanal ejecutable. Entrega:
1) 3 prioridades maximas (con razon)
2) Backlog ordenado (Must/Should/Could)
3) Plan dia a dia (bloques de 60-120 min)
4) Riesgos y mitigaciones
5) Definicion de \"done\" y checkpoints
Reglas: asume capacidad realista; incluye tiempo para imprevistos.

Objetivos:
{goals}

Restricciones (opcional):
{constraints}

EN:
Turn these goals into an executable weekly plan. Provide:
1) Top 3 priorities (with rationale)
2) Ordered backlog (Must/Should/Could)
3) Day-by-day plan (60–120 min blocks)
4) Risks and mitigations
5) Definition of done and checkpoints
Rules: assume realistic capacity; include buffer time.

Goals:
{goals}

Constraints (optional):
{constraints}""",
        ),
        PromptCreate(
            title="Decision log entry (ADR) / Entrada de log de decision (ADR)",
            category="Architecture",
            tags=[*shared, "adr", "decision", "architecture", "docs"],
            rating=5,
            body="""ES:
Escribe una ADR corta para esta decision. Formato:
- Contexto
- Decision
- Alternativas consideradas (pros/contras)
- Consecuencias (positivas/negativas)
- Migracion / rollout (si aplica)
- Como se medira el exito
Reglas: se concreto; evita jerga; no inventes requisitos.

Decision:
{decision}

Opciones:
{options}

EN:
Write a short ADR for this decision. Format:
- Context
- Decision
- Alternatives considered (pros/cons)
- Consequences (positive/negative)
- Migration / rollout (if applicable)
- How success will be measured
Rules: be concrete; avoid jargon; don't invent requirements.

Decision:
{decision}

Options:
{options}""",
        ),
        PromptCreate(
            title="Literature review synthesis / Sintesis de revision bibliografica",
            category="Research",
            tags=[*shared, "research", "literature", "synthesis", "notes"],
            rating=4,
            body="""ES:
Sintetiza estas notas/papers en una revision bibliografica clara. Entrega:
1) Resumen ejecutivo (5 bullets)
2) Taxonomia de ideas (agrupa por tema)
3) Consensos vs desacuerdos
4) Limitaciones y sesgos
5) Preguntas abiertas y proximos experimentos
Reglas: no atribuyas claims si no hay fuente; marca citas como [autor, anio] si se provee.

Material:
{material}

EN:
Synthesize these notes/papers into a clear literature review. Provide:
1) Executive summary (5 bullets)
2) Idea taxonomy (group by theme)
3) Consensus vs disagreements
4) Limitations and biases
5) Open questions and next experiments
Rules: don't attribute claims without a source; mark citations as [author, year] when provided.

Material:
{material}""",
        ),
        PromptCreate(
            title="Experiment design (A/B test) / Diseno de experimento (A/B)",
            category="Research",
            tags=[*shared, "experiment", "ab-test", "metrics", "product"],
            rating=5,
            body="""ES:
Disena un experimento A/B para esta hipotesis. Incluye:
- Hipotesis clara (si/entonces/porque)
- Variable primaria y metricas secundarias (con definicion)
- Poblacion, segmentacion y criterios de exclusion
- Duracion estimada y riesgos (peeking, sesgos)
- Instrumentacion: eventos y propiedades
- Criterios de parada y decision
Reglas: no inventes numeros; deja placeholders si faltan supuestos.

Hipotesis:
{hypothesis}

Contexto:
{context}

EN:
Design an A/B test for this hypothesis. Include:
- Clear hypothesis (if/then/because)
- Primary metric and secondary metrics (with definitions)
- Population, segmentation, and exclusion criteria
- Estimated duration and risks (peeking, biases)
- Instrumentation: events and properties
- Stop criteria and decision rule
Rules: don't make up numbers; use placeholders when assumptions are missing.

Hypothesis:
{hypothesis}

Context:
{context}""",
        ),
        PromptCreate(
            title="Agent sandbox safety prompt / Prompt de seguridad para agente",
            category="Agents",
            tags=[*shared, "agents", "safety", "privacy", "tool-use"],
            rating=5,
            body="""ES:
Eres un agente que puede usar herramientas. Politica de seguridad:
- No pegues secretos (tokens, keys, cookies). Si aparecen, redáctalos.
- No ejecutes acciones destructivas sin confirmacion explicita.
- Minimiza acceso a datos: lee solo lo necesario.
- Prefiere cambios pequenos y reversibles.
Antes de cada accion con herramientas: explica proposito, riesgo, y como verificar.
Al final: lista de comandos ejecutados + cambios aplicados.

Tarea:
{task}

EN:
You are a tool-using agent. Safety policy:
- Never paste secrets (tokens, keys, cookies). If they appear, redact them.
- Don't run destructive actions without explicit confirmation.
- Minimize data access: read only what's needed.
- Prefer small, reversible changes.
Before each tool action: explain purpose, risk, and how to verify.
At the end: list commands run + changes applied.

Task:
{task}""",
        ),
        PromptCreate(
            title="Tool-use trace reporter / Reporte de trazas de tool-use",
            category="Agents",
            tags=[*shared, "agents", "tools", "trace", "observability"],
            rating=4,
            body="""ES:
Quiero registrar un trace de tu uso de herramientas para esta tarea. Tras cada paso, añade:
- Accion (tool, comando)
- Entrada (parametros resumidos)
- Salida (resumen + errores)
- Decision: por que el siguiente paso
- Evidencia: como sabes que vas bien
Mantente conciso; no repitas logs largos; enlaza archivos si aplica.

Tarea:
{task}

EN:
I want a trace of your tool usage for this task. After each step, add:
- Action (tool, command)
- Input (summarized parameters)
- Output (summary + errors)
- Decision: why the next step
- Evidence: how you know you're on track
Be concise; don't paste long logs; link files when applicable.

Task:
{task}""",
        ),
        PromptCreate(
            title="ChatGPT brainstorming facilitator / Facilitador de brainstorming (ChatGPT)",
            category="Prompts for ChatGPT",
            tags=[*shared, "chatgpt", "brainstorming", "ideation", "facilitation"],
            rating=4,
            body="""ES:
Actua como facilitador de brainstorming. Objetivo: generar opciones sin perder foco. Reglas:
1) Empieza con 5 preguntas para acotar
2) Genera 12 ideas agrupadas por 3 enfoques distintos
3) Para cada idea: impacto, esfuerzo, riesgos
4) Elige 3 y propon un mini-plan (primeros 3 pasos)
5) Termina con un resumen de decision y siguientes preguntas

Tema:
{topic}

EN:
Act as a brainstorming facilitator. Goal: generate options without losing focus. Rules:
1) Start with 5 scoping questions
2) Generate 12 ideas grouped into 3 distinct approaches
3) For each idea: impact, effort, risks
4) Pick 3 and propose a mini-plan (first 3 steps)
5) End with a decision summary and next questions

Topic:
{topic}""",
        ),
        PromptCreate(
            title="Claude writing style adapter / Adaptador de estilo de escritura (Claude)",
            category="Prompts for Claude",
            tags=[*shared, "claude", "writing", "style", "editing"],
            rating=4,
            body="""ES:
Reescribe este texto manteniendo el significado, pero adaptando estilo y claridad. Entrega:
1) Version final (lista para pegar)
2) Cambios clave (3-6 bullets)
3) Opciones alternativas para el primer parrafo (3 variantes)
Reglas: no agregues hechos nuevos; preserva numeros y nombres propios.

Estilo objetivo:
{style}

Texto:
{text}

EN:
Rewrite this text to keep the meaning but improve style and clarity. Provide:
1) Final version (ready to paste)
2) Key changes (3–6 bullets)
3) Alternative options for the first paragraph (3 variants)
Rules: don't add new facts; preserve numbers and proper nouns.

Target style:
{style}

Text:
{text}""",
        ),
        PromptCreate(
            title="Codex PR fix-up / Fix-up de PR (Codex)",
            category="Prompts for Codex",
            tags=[*shared, "codex", "pr", "review", "polish"],
            rating=5,
            body="""ES:
Mejora este PR para que sea facil de revisar. Checklist:
1) Divide commits si hay cambios no relacionados (sin reescribir historia si ya esta compartida)
2) Reduce ruido: formateo solo donde toque, elimina cambios accidentales
3) Asegura nombres claros y mensajes de error utiles
4) Actualiza tests y docs si estan afectados
5) Entrega una descripcion de PR: contexto, cambios, como probar, riesgos
Al final: comandos recomendados para verificar.

PR / diff:
{diff}

EN:
Improve this PR to make it easy to review. Checklist:
1) Split commits if there are unrelated changes (don't rewrite history if already shared)
2) Reduce noise: format only touched areas, remove accidental changes
3) Ensure clear naming and helpful error messages
4) Update tests and docs if impacted
5) Produce a PR description: context, changes, how to test, risks
At the end: recommended verification commands.

PR / diff:
{diff}""",
        ),
        PromptCreate(
            title="Prompt pack curator / Curador de packs de prompts",
            category="Prompts",
            tags=[*shared, "prompting", "library", "curation", "quality"],
            rating=5,
            body="""ES:
Ayudame a curar un pack de prompts para un equipo. Entrada: lista de prompts y el publico objetivo.
Entrega:
1) Taxonomia (categorias y subcategorias)
2) Duplicados/solapamientos (que quitar o fusionar)
3) Estandares de calidad: formato, placeholders, guardrails, longitud
4) 10 prompts recomendados \"core\" y por que
5) Guia rapida de uso (cuando usar cada categoria)
Reglas: no incluyas datos privados; prioriza prompts reutilizables.

Publico objetivo:
{audience}

Prompts:
{prompts}

EN:
Help me curate a prompt pack for a team. Input: a prompt list and the target audience.
Provide:
1) Taxonomy (categories and subcategories)
2) Duplicates/overlaps (what to remove or merge)
3) Quality standards: format, placeholders, guardrails, length
4) 10 recommended core prompts and why
5) Quick usage guide (when to use each category)
Rules: no private data; prioritize reusable prompts.

Target audience:
{audience}

Prompts:
{prompts}""",
        ),
        PromptCreate(
            title="PII redaction plan / Plan de redaccion de PII",
            category="Research",
            tags=[*shared, "privacy", "pii", "redaction", "compliance"],
            rating=5,
            body="""ES:
Necesito anonimizar/redactar datos personales (PII) de este material. Entrega:
1) Tipos de PII presentes (nombres, emails, IDs, ubicaciones, etc.)
2) Estrategia de redaccion: reemplazos consistentes, hashing, seudonimos
3) Reglas para conservar utilidad (fechas relativas, rangos, categorias)
4) Ejemplos de antes/despues con placeholders (no datos reales)
5) Checklist de verificacion y errores comunes
Reglas: no reconstruyas identidades; si hay dudas, redáctalo.

Material:
{material}

EN:
I need to anonymize/redact personal data (PII) from this material. Provide:
1) Types of PII present (names, emails, IDs, locations, etc.)
2) Redaction strategy: consistent replacements, hashing, pseudonyms
3) Rules to preserve utility (relative dates, ranges, categories)
4) Before/after examples using placeholders (no real data)
5) Verification checklist and common mistakes
Rules: never try to re-identify people; when in doubt, redact.

Material:
{material}""",
        ),
        PromptCreate(
            title="Incident runbook quickstart / Quickstart de runbook de incidentes",
            category="Productivity",
            tags=[*shared, "incident", "runbook", "ops", "reliability"],
            rating=4,
            body="""ES:
Crea un runbook practico para este tipo de incidente. Incluye:
- Senales / sintomas
- Diagnostico rapido (5-10 checks con comandos genericos)
- Mitigaciones seguras (ordenadas por menor riesgo)
- Escalado y comunicacion (plantillas cortas)
- Post-incidente: datos a capturar y acciones
Reglas: no incluyas credenciales ni comandos destructivos por defecto; marca lo peligroso.

Tipo de incidente:
{incident_type}

Sistema (opcional):
{system}

EN:
Create a practical runbook for this incident type. Include:
- Signals / symptoms
- Quick diagnosis (5–10 checks with generic commands)
- Safe mitigations (ordered by lowest risk first)
- Escalation and comms (short templates)
- Post-incident: data to capture and action items
Rules: no credentials and no destructive commands by default; clearly flag risky steps.

Incident type:
{incident_type}

System (optional):
{system}""",
        ),
    ]
