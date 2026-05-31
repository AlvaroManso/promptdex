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
        PromptCreate(
            title="Unit test generator with fixtures / Generador de tests unitarios con fixtures",
            category="Coding",
            tags=[*shared, "testing", "unit-tests", "fixtures", "tdd"],
            rating=5,
            body="""ES:
Dado este codigo y su comportamiento esperado, escribe tests unitarios con buena cobertura y fixtures/minimos mocks.
Entrega:
1) Lista de casos (happy path + bordes + errores)
2) Tests listos para ejecutar (elige el framework mas comun del repo)
3) Datos de ejemplo/fixtures reutilizables
4) Notas de diseno del test (que NO probar y por que)
Reglas: no inventes dependencias; si falta contexto, pregunta 2-3 cosas max y propone defaults.

Codigo:
{code}

Comportamiento esperado:
{requirements}

EN:
Given this code and expected behavior, write unit tests with good coverage and fixtures/minimal mocks.
Deliver:
1) Case list (happy path + edges + errors)
2) Tests ready to run (use the repo's most common framework)
3) Reusable sample data/fixtures
4) Test design notes (what NOT to test and why)
Rules: don't invent dependencies; if context is missing, ask 2–3 questions max and propose sane defaults.

Code:
{code}

Expected behavior:
{requirements}""",
        ),
        PromptCreate(
            title="Codebase orientation brief / Brief de orientacion del codebase",
            category="Productivity",
            tags=[*shared, "onboarding", "codebase", "architecture", "overview"],
            rating=4,
            body="""ES:
Explica este repositorio para una persona nueva en 10 minutos. Entrega:
1) Mapa mental: modulos principales y responsabilidades
2) Flujo end-to-end de la feature mas importante
3) Donde estan: config, DB, API, frontend, jobs, tests
4) Comandos tipicos (dev, test, lint, build)
5) 5 riesgos/zonas fragiles a vigilar
Reglas: cita rutas de archivos; si no encuentras algo, dilo.

Repo (notas / arbol / enlaces):
{repo_notes}

EN:
Explain this repository to a newcomer in 10 minutes. Deliver:
1) Mental map: main modules and responsibilities
2) End-to-end flow of the most important feature
3) Where to find: config, DB, API, frontend, jobs, tests
4) Typical commands (dev, test, lint, build)
5) 5 risks/brittle areas to watch
Rules: reference file paths; if you can't find something, say so.

Repo (notes / tree / links):
{repo_notes}""",
        ),
        PromptCreate(
            title="Commit message helper / Ayuda para mensaje de commit",
            category="Productivity",
            tags=[*shared, "git", "commit", "changelog", "communication"],
            rating=4,
            body="""ES:
Genera 5 opciones de mensaje de commit siguiendo Conventional Commits. Entrada: diff/resumen.
Entrega:
- 1 opcion concisa (ideal)
- 2 opciones mas descriptivas
- 2 opciones con alcance (scope) sugerido
Reglas: evita exagerar; si el cambio es breaking, indicalo claramente y explica el impacto en 1 linea.

Resumen o diff:
{diff}

EN:
Generate 5 Conventional Commits-style commit message options from this diff/summary.
Deliver:
- 1 concise ideal option
- 2 more descriptive options
- 2 options with suggested scope
Rules: don't oversell; if it's breaking, mark it clearly and explain impact in 1 line.

Summary or diff:
{diff}""",
        ),
        PromptCreate(
            title="Dependency risk audit / Auditoria de riesgos de dependencias",
            category="Architecture",
            tags=[*shared, "dependencies", "supply-chain", "risk", "maintenance"],
            rating=5,
            body="""ES:
Audita estas dependencias para un proyecto OSS. Entrega una tabla con:
- dependencia, proposito, criticidad, riesgo (bajo/medio/alto), senales (mantenimiento, licencias), alternativa posible
Luego:
1) 5 acciones de mitigacion (pinning, lockfile, vendoring, SBOM, etc.)
2) Politica propuesta para actualizar dependencias
Reglas: no inventes vulnerabilidades; si no tienes datos, marca como "desconocido" y sugiere como verificar.

Dependencias:
{dependencies}

EN:
Audit these dependencies for an OSS project. Provide a table with:
- dependency, purpose, criticality, risk (low/med/high), signals (maintenance, licensing), possible alternative
Then:
1) 5 mitigation actions (pinning, lockfile, vendoring, SBOM, etc.)
2) A proposed dependency update policy
Rules: don't invent vulnerabilities; if data is missing, mark "unknown" and suggest how to verify.

Dependencies:
{dependencies}""",
        ),
        PromptCreate(
            title="Prompt injection defense checklist / Checklist anti prompt injection",
            category="Architecture",
            tags=[*shared, "security", "prompt-injection", "llm", "guardrails"],
            rating=5,
            body="""ES:
Estoy construyendo una app que usa LLM con herramientas y contenido no confiable. Dame un checklist practico para reducir riesgo de prompt injection.
Incluye:
1) Modelado de amenazas (activos, atacantes, superficies)
2) Controles tecnicos (separacion de instrucciones/datos, allowlists, sanitizacion, sandboxing)
3) Controles de producto (UX, permisos, confirmaciones, logs)
4) Tests de ataque (10 ejemplos)
5) Red flags en prompts y en codigo
Reglas: asume que el contenido externo es malicioso por defecto; evita soluciones magicas.

Contexto de la app:
{app_context}

EN:
I'm building an LLM app with tools and untrusted content. Give me a practical checklist to reduce prompt injection risk.
Include:
1) Threat model (assets, attackers, surfaces)
2) Technical controls (instruction/data separation, allowlists, sanitization, sandboxing)
3) Product controls (UX, permissions, confirmations, logs)
4) Attack tests (10 examples)
5) Prompt and code red flags
Rules: assume external content is malicious by default; avoid magic solutions.

App context:
{app_context}""",
        ),
        PromptCreate(
            title="RAG retrieval plan / Plan de recuperacion para RAG",
            category="Architecture",
            tags=[*shared, "rag", "retrieval", "search", "evaluation"],
            rating=4,
            body="""ES:
Disena un plan de recuperacion (RAG) para este caso. Entrega:
1) Que indexar y como trocear (chunking)
2) Metadatos y filtros recomendados
3) Estrategia de ranking (BM25, embeddings, rerank) y por que
4) Esquema de prompt (instrucciones vs contexto)
5) Evaluacion: dataset, metricas, casos de fallo, guardrails
Reglas: prioriza simplicidad y privacidad; evita depender de servicios externos si no es necesario.

Caso de uso:
{use_case}

Contenido disponible:
{content}

EN:
Design a retrieval (RAG) plan for this use case. Deliver:
1) What to index and how to chunk
2) Recommended metadata and filters
3) Ranking strategy (BM25, embeddings, rerank) and why
4) Prompt frame (instructions vs context)
5) Evaluation: dataset, metrics, failure modes, guardrails
Rules: prioritize simplicity and privacy; avoid external services unless necessary.

Use case:
{use_case}

Available content:
{content}""",
        ),
        PromptCreate(
            title="Incident postmortem / Postmortem de incidente",
            category="Productivity",
            tags=[*shared, "incident", "postmortem", "root-cause", "ops"],
            rating=5,
            body="""ES:
Escribe un postmortem sin culpas para este incidente. Entrega:
1) Resumen ejecutivo (que paso, impacto, duracion)
2) Timeline con horas (UTC) y eventos clave
3) Causa raiz y factores contribuyentes (tecnicos y de proceso)
4) Que funciono / que no funciono
5) Acciones: mitigaciones ya hechas y tareas con owner + fecha objetivo
6) Lecciones y cambios sistemicos (no solo "tener mas cuidado")
Reglas: se preciso y accionable; evita datos sensibles.

Datos del incidente:
{incident_data}

EN:
Write a blameless postmortem for this incident. Deliver:
1) Executive summary (what happened, impact, duration)
2) Timeline with times (UTC) and key events
3) Root cause and contributing factors (technical + process)
4) What worked / what didn't
5) Action items: done mitigations and tasks with owner + target date
6) Learnings and systemic changes (not just "be careful")
Rules: be precise and actionable; avoid sensitive data.

Incident data:
{incident_data}""",
        ),
        PromptCreate(
            title="Feature flag rollout plan / Plan de despliegue con feature flags",
            category="Architecture",
            tags=[*shared, "release", "feature-flags", "rollout", "risk"],
            rating=4,
            body="""ES:
Ayudame a desplegar esta feature con el menor riesgo usando feature flags. Entrega:
1) Estrategia de flags (nombres, defaults, scopes)
2) Plan de rollout por fases (0% -> 1% -> 10% -> 100%)
3) Observabilidad: metricas, logs, alertas
4) Plan de rollback y condiciones para activarlo
5) Plan de comunicacion (interno + usuarios)
Reglas: asume que habra regresiones; prioriza pasos reversibles.

Feature:
{feature}

EN:
Help me roll out this feature with minimal risk using feature flags. Deliver:
1) Flag strategy (names, defaults, scopes)
2) Phased rollout plan (0% -> 1% -> 10% -> 100%)
3) Observability: metrics, logs, alerts
4) Rollback plan and triggers
5) Communication plan (internal + users)
Rules: assume regressions will happen; prioritize reversible steps.

Feature:
{feature}""",
        ),
        PromptCreate(
            title="Database migration safety plan / Plan de seguridad para migraciones",
            category="Coding",
            tags=[*shared, "database", "migrations", "backfill", "zero-downtime"],
            rating=5,
            body="""ES:
Revisa esta migracion y propone un plan seguro. Entrega:
1) Riesgos (locks, tiempo, data loss, compatibilidad)
2) Estrategia zero-downtime si aplica (expand/contract)
3) Backfill: pasos, batches, verificacion, reintentos
4) Plan de rollback (incluye como revertir datos)
5) Checklist de despliegue (staging -> prod)
Reglas: no ejecutes comandos destructivos; marca claramente lo irreversible.

Migracion:
{migration}

EN:
Review this migration and propose a safe plan. Deliver:
1) Risks (locks, time, data loss, compatibility)
2) Zero-downtime strategy if applicable (expand/contract)
3) Backfill: steps, batching, verification, retries
4) Rollback plan (including data rollback strategy)
5) Deployment checklist (staging -> prod)
Rules: don't run destructive commands; clearly flag irreversible steps.

Migration:
{migration}""",
        ),
        PromptCreate(
            title="CLI UX audit / Auditoria de UX para CLI",
            category="Design",
            tags=[*shared, "cli", "ux", "copy", "errors"],
            rating=4,
            body="""ES:
Audita esta CLI como si fuera un producto. Evalua:
- consistencia de comandos/flags, ayuda, ejemplos, mensajes de error, defaults seguros
Entrega:
1) 10 mejoras concretas (con ejemplo de texto)
2) Propuesta de ayuda `--help` y ejemplos (2-3 comandos)
3) Recomendaciones de errores (codes, sugerencias, hints)
Reglas: prioriza claridad y seguridad; evita output ruidoso por defecto.

Descripcion / output actual:
{cli}

EN:
Audit this CLI like a real product. Evaluate:
- command/flag consistency, help, examples, error messages, safe defaults
Deliver:
1) 10 concrete improvements (with copy examples)
2) Proposed `--help` and examples (2–3 commands)
3) Error recommendations (codes, suggestions, hints)
Rules: prioritize clarity and safety; avoid noisy output by default.

Current description / output:
{cli}""",
        ),
        PromptCreate(
            title="Prompt library lint / Linter de libreria de prompts",
            category="Prompts",
            tags=[*shared, "prompting", "library", "quality", "consistency"],
            rating=4,
            body="""ES:
Revisa esta libreria de prompts y detecta problemas de calidad/consistencia.
Entrega:
1) Duplicados y solapamientos
2) Titulo/categoria/tags inconsistentes
3) Placeholders faltantes o ambiguos
4) Riesgos de privacidad o datos sensibles
5) Recomendaciones de estandar (plantilla base)
Reglas: sugiere cambios minimos que mejoren reutilizacion.

Libreria:
{library}

EN:
Review this prompt library and detect quality/consistency issues.
Deliver:
1) Duplicates and overlaps
2) Inconsistent title/category/tags
3) Missing or ambiguous placeholders
4) Privacy risks or sensitive data patterns
5) Standardization recommendations (base template)
Rules: suggest minimal changes that improve reuse.

Library:
{library}""",
        ),
        PromptCreate(
            title="Agent tool policy / Politica de herramientas para agente",
            category="Agents",
            tags=[*shared, "agents", "tools", "policy", "safety"],
            rating=5,
            body="""ES:
Define una politica de herramientas para un agente autonomo en este entorno. Entrega:
1) Herramientas permitidas y prohibidas (con razones)
2) Reglas de confirmacion humana (high-risk actions)
3) Limites de datos (PII, secretos, logs)
4) Auditoria: que registrar y como
5) Manejo de errores y reintentos
Reglas: por defecto, minimo privilegio; explica tradeoffs.

Entorno / herramientas:
{environment}

EN:
Define a tool policy for an autonomous agent in this environment. Deliver:
1) Allowed and disallowed tools (with rationale)
2) Human confirmation rules (high-risk actions)
3) Data boundaries (PII, secrets, logs)
4) Auditing: what to log and how
5) Error handling and retries
Rules: default to least privilege; explain tradeoffs.

Environment / tools:
{environment}""",
        ),
        PromptCreate(
            title="Context budgeter / Presupuestador de contexto",
            category="Prompts",
            tags=[*shared, "prompting", "context", "summarization", "budget"],
            rating=4,
            body="""ES:
Tengo mucho contexto y una ventana limitada. Ayudame a empaquetarlo sin perder lo importante.
Entrega:
1) Objetivo y restricciones (resumen de 2-3 lineas)
2) Contexto minimo necesario (bullets)
3) Detalles opcionales (seccion separada)
4) Preguntas clave para cerrar huecos (max 5)
5) Prompt final listo para usar
Reglas: no incluyas datos privados; cita hechos y supuestos por separado.

Objetivo:
{goal}

Contexto bruto:
{context}

EN:
I have lots of context and a limited window. Help me package it without losing what matters.
Deliver:
1) Goal and constraints (2–3 lines)
2) Minimum necessary context (bullets)
3) Optional details (separate section)
4) Key questions to close gaps (max 5)
5) Final ready-to-use prompt
Rules: no private data; separate facts vs assumptions.

Goal:
{goal}

Raw context:
{context}""",
        ),
        PromptCreate(
            title="Stakeholder update note / Nota de update a stakeholders",
            category="Productivity",
            tags=[*shared, "communication", "status", "stakeholders", "writing"],
            rating=4,
            body="""ES:
Escribe una nota corta de estado para stakeholders no tecnicos. Entrega 2 versiones:
- Version corta (<= 6 lineas)
- Version larga (<= 15 lineas)
Incluye: progreso, riesgos, bloqueos, proximos pasos y si necesitas decision.
Reglas: evita jerga; usa fechas concretas.

Contexto:
{context}

EN:
Write a short status update for non-technical stakeholders. Provide 2 versions:
- Short (<= 6 lines)
- Long (<= 15 lines)
Include: progress, risks, blockers, next steps, and any decision needed.
Rules: avoid jargon; use concrete dates.

Context:
{context}""",
        ),
        PromptCreate(
            title="Experiment design (A/B) / Diseno de experimento (A/B)",
            category="Research",
            tags=[*shared, "experiment", "ab-test", "metrics", "product"],
            rating=5,
            body="""ES:
Disena un experimento A/B para esta hipotesis. Entrega:
1) Hipotesis y criterio de exito
2) Variable primaria y guardrails
3) Segmentacion y asignacion
4) Tamaño de muestra (estimacion) y duracion
5) Analisis (que test usar, efectos esperados)
6) Riesgos y como evitarlos (seasonality, peeking, novelty)
Reglas: si faltan numeros, pide los minimos y ofrece un rango razonable.

Hipotesis:
{hypothesis}

Contexto:
{context}

EN:
Design an A/B experiment for this hypothesis. Deliver:
1) Hypothesis and success criteria
2) Primary metric and guardrails
3) Segmentation and assignment
4) Sample size (estimate) and duration
5) Analysis plan (which test, expected effects)
6) Risks and how to avoid them (seasonality, peeking, novelty)
Rules: if numbers are missing, ask for the minimum and provide a reasonable range.

Hypothesis:
{hypothesis}

Context:
{context}""",
        ),
        PromptCreate(
            title="Error message audit table / Tabla de auditoria de mensajes de error",
            category="Design",
            tags=[*shared, "ux", "errors", "copy", "accessibility"],
            rating=4,
            body="""ES:
Mejora estos mensajes de error para que sean claros y accionables. Entrega una tabla con:
- original, problema, version mejorada, sugerencia al usuario, nivel (info/warn/error)
Reglas: no culpes al usuario; incluye pasos concretos; evita exponer datos sensibles.

Mensajes:
{messages}

EN:
Improve these error messages to be clear and actionable. Provide a table with:
- original, issue, improved version, user hint, level (info/warn/error)
Rules: don't blame the user; include concrete steps; avoid leaking sensitive data.

Messages:
{messages}""",
        ),
        PromptCreate(
            title="Regex builder / Constructor de regex",
            category="Coding",
            tags=[*shared, "regex", "text", "parsing", "examples"],
            rating=4,
            body="""ES:
Construye una expresion regular para este objetivo. Entrega:
1) regex final
2) explicacion paso a paso
3) 10 ejemplos que matchean
4) 10 ejemplos que NO matchean
5) opciones mas seguras (parseo alternativo) si regex es fragil
Reglas: evita backtracking catastrofico; si el lenguaje importa, pregunta por el motor (PCRE, RE2, etc.).

Objetivo:
{goal}

Ejemplos:
{examples}

EN:
Build a regex for this goal. Deliver:
1) final regex
2) step-by-step explanation
3) 10 matching examples
4) 10 non-matching examples
5) safer alternatives if regex is brittle
Rules: avoid catastrophic backtracking; ask which engine matters (PCRE, RE2, etc.).

Goal:
{goal}

Examples:
{examples}""",
        ),
        PromptCreate(
            title="Repo search plan / Plan de busqueda en el repo",
            category="Debugging",
            tags=[*shared, "debugging", "search", "ripgrep", "code-reading"],
            rating=4,
            body="""ES:
Necesito encontrar donde se implementa/comporta algo en este repo. Haz un plan de busqueda:
1) Palabras clave probables (sinonimos)
2) Comandos `rg` sugeridos (5-10) y por que
3) Archivos a revisar primero (rutas)
4) Como validar rapidamente hipotesis
Reglas: minimiza ruido; prioriza senales (tests, docs, routes, config).

Descripcion del problema:
{problem}

EN:
I need to find where something is implemented/behaves in this repo. Make a search plan:
1) Likely keywords (and synonyms)
2) Suggested `rg` commands (5–10) and why
3) Files to inspect first (paths)
4) How to quickly validate hypotheses
Rules: minimize noise; prioritize signals (tests, docs, routes, config).

Problem description:
{problem}""",
        ),
        PromptCreate(
            title="Roadmap prioritization matrix / Matriz de priorizacion de roadmap",
            category="Productivity",
            tags=[*shared, "product", "prioritization", "roadmap", "tradeoffs"],
            rating=5,
            body="""ES:
Ayudame a priorizar estas iniciativas. Entrega:
1) Criterios propuestos (impacto, esfuerzo, riesgo, urgencia, dependencia)
2) Matriz de priorizacion (RICE o similar) con scores y supuestos
3) Recomendacion: top 5 ahora, top 5 despues, y que NO hacer (por que)
4) Riesgos y mitigaciones
5) Preguntas para desbloquear incertidumbre (max 7)
Reglas: separa hechos vs supuestos; si faltan datos, estima rangos y marca la confianza.

Iniciativas:
{initiatives}

Contexto:
{context}

EN:
Help me prioritize these initiatives. Deliver:
1) Proposed criteria (impact, effort, risk, urgency, dependencies)
2) Prioritization matrix (RICE or similar) with scores and assumptions
3) Recommendation: top 5 now, top 5 next, and what NOT to do (and why)
4) Risks and mitigations
5) Questions to reduce uncertainty (max 7)
Rules: separate facts vs assumptions; if data is missing, estimate ranges and mark confidence.

Initiatives:
{initiatives}

Context:
{context}""",
        ),
        PromptCreate(
            title="PR description template / Plantilla de descripcion de PR",
            category="Productivity",
            tags=[*shared, "pr", "review", "communication", "templates"],
            rating=5,
            body="""ES:
Redacta una descripcion de PR lista para pegar. Incluye secciones:
- Contexto
- Cambios
- Como probar (pasos exactos)
- Riesgos / rollbacks
- Notas para reviewers (que mirar primero)
Reglas: se conciso; evita prometer cosas no verificadas; incluye comandos de verificacion.

Diff/resumen:
{diff}

EN:
Draft a ready-to-paste PR description. Include sections:
- Context
- Changes
- How to test (exact steps)
- Risks / rollbacks
- Notes for reviewers (what to look at first)
Rules: be concise; don't claim unverifiable things; include verification commands.

Diff/summary:
{diff}""",
        ),
        PromptCreate(
            title="Migration plan / Plan de migracion",
            category="Architecture",
            tags=[*shared, "migration", "rollout", "backward-compatibility", "risk"],
            rating=5,
            body="""ES:
Necesito migrar de {from} a {to}. Disena un plan con:
1) Objetivo y no-objetivos
2) Estrategia (big-bang vs fases) y justificacion
3) Cambios tecnicos por etapa (con checks de salida)
4) Compatibilidad hacia atras y plan de datos (si aplica)
5) Observabilidad: metricas/alertas para detectar problemas
6) Plan de rollback y criterios de abortar
7) Checklist de comunicacion (equipo, usuarios, soporte)
Entrega como tabla por fases.

Contexto:
{context}

EN:
I need to migrate from {from} to {to}. Design a plan with:
1) Goals and non-goals
2) Strategy (big-bang vs phased) and rationale
3) Technical changes per phase (with exit checks)
4) Backward compatibility and data plan (if relevant)
5) Observability: metrics/alerts to detect issues
6) Rollback plan and abort criteria
7) Communication checklist (team, users, support)
Deliver as a phased table.

Context:
{context}""",
        ),
        PromptCreate(
            title="Data model critique / Critica del modelo de datos",
            category="Architecture",
            tags=[*shared, "data-model", "schema", "constraints", "tradeoffs"],
            rating=5,
            body="""ES:
Evalua este modelo de datos. Devuelve:
1) Invariantes y reglas de negocio implicitas
2) Riesgos (nulos, duplicados, consistencia, cascadas)
3) Indices y constraints recomendados
4) Evolucion futura: como soportar nuevos casos sin romper
5) Consultas clave y como optimizarlas
Incluye preguntas para aclarar dominios ambiguos.

Esquema:
{schema}

EN:
Evaluate this data model. Return:
1) Invariants and implicit business rules
2) Risks (nulls, duplicates, consistency, cascades)
3) Recommended indexes and constraints
4) Future evolution: support new cases without breaking
5) Key queries and how to optimize them
Include questions to clarify ambiguous domain areas.

Schema:
{schema}""",
        ),
        PromptCreate(
            title="Performance profiling plan / Plan de profiling de rendimiento",
            category="Debugging",
            tags=[*shared, "performance", "profiling", "benchmark", "latency"],
            rating=5,
            body="""ES:
Quiero mejorar rendimiento sin adivinar. Propon un plan:
1) Metricas objetivo (p50/p95/p99, CPU, RAM, I/O) y como medir
2) Experimentos controlados (benchmarks reproducibles)
3) Hipotesis principales (max 5) y como falsarlas
4) Instrumentacion minima (logs, trazas, counters)
5) Plan de cambios por impacto/ riesgo
Devuelve comandos/herramientas sugeridas segun stack si lo conoces.

Stack y sintomas:
{details}

EN:
I want to improve performance without guessing. Propose a plan:
1) Target metrics (p50/p95/p99, CPU, RAM, I/O) and how to measure
2) Controlled experiments (reproducible benchmarks)
3) Main hypotheses (max 5) and how to falsify them
4) Minimal instrumentation (logs, traces, counters)
5) Change plan by impact/risk
Include suggested commands/tools based on the stack if known.

Stack and symptoms:
{details}""",
        ),
        PromptCreate(
            title="Minimal reproducible example / Ejemplo minimo reproducible",
            category="Debugging",
            tags=[*shared, "mre", "repro", "debugging", "triage"],
            rating=5,
            body="""ES:
Convierte este problema en un MRE (ejemplo minimo reproducible). Entrega:
1) Pasos exactos para reproducir
2) Codigo minimo (sin dependencias innecesarias)
3) Salida esperada vs actual
4) Hipotesis de causa raiz (2-3)
5) Experimentos pequenos para confirmar
Reglas: elimina ruido; si falta informacion, pregunta 3 preguntas max.

Descripcion:
{problem}

EN:
Turn this into an MRE (minimal reproducible example). Deliver:
1) Exact reproduction steps
2) Minimal code (no unnecessary deps)
3) Expected vs actual output
4) Root-cause hypotheses (2-3)
5) Small experiments to confirm
Rules: remove noise; if info is missing, ask at most 3 questions.

Description:
{problem}""",
        ),
        PromptCreate(
            title="SQL query review / Revision de consulta SQL",
            category="Coding",
            tags=[*shared, "sql", "performance", "indexes", "query-plan"],
            rating=4,
            body="""ES:
Revisa esta consulta SQL. Devuelve:
1) Que hace (en lenguaje simple)
2) Riesgos de rendimiento (joins, filtros, cardinalidad)
3) Indices sugeridos y por que
4) Reescrituras posibles (CTE, subqueries, agregaciones)
5) Como verificar: EXPLAIN/ANALYZE y metricas
Reglas: no asumas el motor; pregunta si es Postgres/MySQL/SQLite/etc.

SQL:
{sql}

EN:
Review this SQL query. Return:
1) What it does (plain language)
2) Performance risks (joins, filters, cardinality)
3) Suggested indexes and why
4) Possible rewrites (CTE, subqueries, aggregations)
5) How to verify: EXPLAIN/ANALYZE and metrics
Rules: don't assume the engine; ask if it's Postgres/MySQL/SQLite/etc.

SQL:
{sql}""",
        ),
        PromptCreate(
            title="Unit test plan / Plan de tests unitarios",
            category="Coding",
            tags=[*shared, "testing", "unit-tests", "coverage", "edge-cases"],
            rating=5,
            body="""ES:
Disena un plan de tests unitarios para esta funcion/modulo. Incluye:
1) Casos felices (min 3)
2) Bordes y errores (min 5)
3) Propiedades/invariantes (si aplica)
4) Mocks/fakes necesarios y como aislar I/O
5) Nombres de tests sugeridos y estructura AAA
Reglas: prioriza casos que puedan romper en produccion.

Codigo/descripcion:
{code}

EN:
Design a unit test plan for this function/module. Include:
1) Happy paths (at least 3)
2) Edge cases and errors (at least 5)
3) Properties/invariants (if applicable)
4) Required mocks/fakes and how to isolate I/O
5) Suggested test names and AAA structure
Rules: prioritize cases that can break in production.

Code/description:
{code}""",
        ),
        PromptCreate(
            title="Refactor safety checklist / Checklist de refactor seguro",
            category="Coding",
            tags=[*shared, "refactor", "safety", "tests", "regression"],
            rating=5,
            body="""ES:
Quiero refactorizar sin romper. Crea un checklist:
1) Preparacion (tests, tipos, linters, snapshots)
2) Estrategia (pasos pequenos, flags, compatibilidad)
3) Senales de riesgo (cambios en contratos, fechas, precision, i18n)
4) Validacion (pruebas, performance, observabilidad)
5) Plan de rollback
Devuelve una lista accionable y ordenada.

Contexto:
{context}

EN:
I want to refactor without breaking things. Create a checklist:
1) Preparation (tests, types, linters, snapshots)
2) Strategy (small steps, flags, compatibility)
3) Risk signals (contract changes, dates, precision, i18n)
4) Validation (tests, performance, observability)
5) Rollback plan
Return an actionable ordered list.

Context:
{context}""",
        ),
        PromptCreate(
            title="Docs from code / Documentacion desde el codigo",
            category="Productivity",
            tags=[*shared, "docs", "documentation", "readme", "developer-experience"],
            rating=4,
            body="""ES:
Genera documentacion a partir de este codigo. Entrega:
1) Resumen del proposito
2) Conceptos clave y terminos
3) Como ejecutar (comandos)
4) Ejemplos de uso
5) Errores comunes y troubleshooting
6) API/Interfaces (si aplica)
Reglas: no inventes; si falta algo, marca TODO.

Codigo:
{code}

EN:
Generate documentation from this code. Deliver:
1) Purpose summary
2) Key concepts and terms
3) How to run (commands)
4) Usage examples
5) Common errors and troubleshooting
6) API/Interfaces (if applicable)
Rules: don't make things up; if something is missing, mark TODOs.

Code:
{code}""",
        ),
        PromptCreate(
            title="Meeting prep + decision log / Preparacion de reunion + log de decisiones",
            category="Productivity",
            tags=[*shared, "meeting", "decisions", "notes", "alignment"],
            rating=4,
            body="""ES:
Prepara una reunion sobre este tema. Devuelve:
1) Objetivo de la reunion (1 frase)
2) Agenda (con tiempos)
3) Preguntas de alineamiento (max 8)
4) Decisiones a tomar (con criterios)
5) Plantilla para notas: decisiones, acciones, riesgos, pendientes
Reglas: enfoca; no mas de 30 minutos salvo que se justifique.

Tema:
{topic}

EN:
Prepare a meeting on this topic. Return:
1) Meeting goal (1 sentence)
2) Agenda (with timings)
3) Alignment questions (max 8)
4) Decisions to make (with criteria)
5) Notes template: decisions, actions, risks, open items
Rules: stay focused; keep it under 30 minutes unless justified.

Topic:
{topic}""",
        ),
        PromptCreate(
            title="Stakeholder status update / Update de estado para stakeholders",
            category="Productivity",
            tags=[*shared, "communication", "status", "stakeholders", "concise"],
            rating=4,
            body="""ES:
Escribe un update semanal para stakeholders. Incluye:
- Estado (verde/amarillo/rojo) y por que
- Logros de la semana
- Bloqueos y ayuda necesaria
- Riesgos (con mitigacion)
- Plan de la proxima semana
Estilo: max 12 lineas, sin jerga, con numeros si existen.

Notas:
{notes}

EN:
Write a weekly stakeholder update. Include:
- Status (green/yellow/red) and why
- Wins this week
- Blockers and help needed
- Risks (with mitigation)
- Plan for next week
Style: max 12 lines, no jargon, include numbers when available.

Notes:
{notes}""",
        ),
        PromptCreate(
            title="User interview script / Guion de entrevista a usuarios",
            category="Research",
            tags=[*shared, "user-research", "interviews", "product", "questions"],
            rating=5,
            body="""ES:
Disena un guion de entrevista (30-45 min) para entender este problema. Entrega:
1) Objetivo y supuestos a validar
2) Preguntas de contexto (5)
3) Preguntas profundas sobre el dolor (8-10)
4) Tareas/escenarios para que el usuario los cuente (3)
5) Señales de alerta (bias, leading questions) y como evitarlas
6) Plan de sintesis (temas, quotes, severidad, frecuencia)

Producto/tema:
{topic}

EN:
Design a 30-45 min interview script to understand this problem. Deliver:
1) Goal and assumptions to validate
2) Context questions (5)
3) Deep pain questions (8-10)
4) Tasks/scenarios for the user to narrate (3)
5) Red flags (bias, leading questions) and how to avoid them
6) Synthesis plan (themes, quotes, severity, frequency)

Product/topic:
{topic}""",
        ),
        PromptCreate(
            title="Competitive analysis table / Tabla de analisis competitivo",
            category="Research",
            tags=[*shared, "competitive-analysis", "market", "positioning", "table"],
            rating=4,
            body="""ES:
Crea un analisis competitivo en tabla. Columnas:
- Producto
- Segmento
- Propuesta de valor (1 frase)
- Puntos fuertes (3)
- Debilidades (3)
- Precio (si se conoce)
- Diferenciadores reales vs marketing
- Oportunidades para nosotros
Termina con 3 recomendaciones de posicionamiento.
Reglas: si no hay datos, marca "desconocido".

Lista de competidores:
{competitors}

Contexto de nuestro producto:
{our_product}

EN:
Create a competitive analysis table. Columns:
- Product
- Segment
- Value prop (1 sentence)
- Strengths (3)
- Weaknesses (3)
- Pricing (if known)
- Real differentiators vs marketing
- Opportunities for us
End with 3 positioning recommendations.
Rules: if data is missing, mark as "unknown".

Competitors:
{competitors}

Our product context:
{our_product}""",
        ),
        PromptCreate(
            title="A/B test design / Diseno de experimento A/B",
            category="Marketing",
            tags=[*shared, "ab-test", "experiment", "metrics", "hypothesis"],
            rating=4,
            body="""ES:
Disena un experimento A/B. Entrega:
1) Hipotesis (clara y falsable)
2) Variantes A y B (cambios concretos)
3) Metricas primarias y secundarias (con definiciones)
4) Segmentacion y criterios de exclusion
5) Tamaño de muestra aproximado (si no hay datos, asume rangos)
6) Riesgos (novelty effect, selection bias) y mitigaciones
Termina con un plan de decision: que resultado implica "lanzar".

Contexto:
{context}

EN:
Design an A/B experiment. Deliver:
1) Hypothesis (clear and falsifiable)
2) Variants A and B (concrete changes)
3) Primary and secondary metrics (with definitions)
4) Segmentation and exclusion criteria
5) Rough sample size (assume ranges if no data)
6) Risks (novelty effect, selection bias) and mitigations
End with a decision plan: what result means "ship".

Context:
{context}""",
        ),
        PromptCreate(
            title="Newsletter draft / Borrador de newsletter",
            category="Marketing",
            tags=[*shared, "newsletter", "copy", "content", "outline"],
            rating=4,
            body="""ES:
Escribe un borrador de newsletter para {audience}. Devuelve:
1) Asunto (5 opciones) + preheader
2) Intro breve (2-3 frases)
3) 3 secciones con titulo + bullets
4) CTA final (2 variantes)
Estilo: humano, claro, sin hype; evita promesas no verificables.

Tema y enlaces (opcionales):
{topic_and_links}

EN:
Write a newsletter draft for {audience}. Return:
1) Subject lines (5 options) + preheader
2) Short intro (2-3 sentences)
3) 3 sections with heading + bullets
4) Final CTA (2 variants)
Style: human, clear, no hype; avoid unverifiable promises.

Topic and links (optional):
{topic_and_links}""",
        ),
        PromptCreate(
            title="Accessibility audit checklist / Checklist de auditoria de accesibilidad",
            category="Design",
            tags=[*shared, "a11y", "accessibility", "wcag", "ui"],
            rating=5,
            body="""ES:
Audita esta UI para accesibilidad. Devuelve:
1) Problemas criticos (teclado, foco, contraste, labels)
2) Problemas moderados (estructura, headings, ARIA, estados)
3) Recomendaciones concretas con ejemplos
4) Checklist de QA manual (pasos)
Reglas: prioriza impacto; si falta HTML, pide el markup relevante.

Descripcion/UI:
{ui}

EN:
Audit this UI for accessibility. Return:
1) Critical issues (keyboard, focus, contrast, labels)
2) Moderate issues (structure, headings, ARIA, states)
3) Concrete recommendations with examples
4) Manual QA checklist (steps)
Rules: prioritize impact; if HTML is missing, ask for relevant markup.

UI/description:
{ui}""",
        ),
        PromptCreate(
            title="Localization style guide / Guia de estilo de localizacion",
            category="Design",
            tags=[*shared, "i18n", "localization", "copy", "style-guide"],
            rating=4,
            body="""ES:
Crea una guia de estilo de localizacion para esta app. Incluye:
1) Tono y voz (do/don't)
2) Terminos clave (glosario)
3) Reglas para fechas/horas/numeros/moneda
4) Mensajes de error (patrones y ejemplos)
5) Longitud maxima y truncado
6) Checklist antes de enviar traducciones

Contexto de la app:
{context}

EN:
Create a localization style guide for this app. Include:
1) Tone and voice (do/don't)
2) Key terms (glossary)
3) Rules for dates/times/numbers/currency
4) Error messages (patterns and examples)
5) Max length and truncation
6) Checklist before shipping translations

App context:
{context}""",
        ),
        PromptCreate(
            title="Prompt safety and privacy check / Chequeo de seguridad y privacidad del prompt",
            category="Prompts for ChatGPT",
            tags=[*shared, "prompting", "safety", "privacy", "redaction"],
            rating=5,
            body="""ES:
Revisa este prompt para seguridad y privacidad. Entrega:
1) Riesgos: datos personales, credenciales, secretos, informacion sensible
2) Preguntas para clarificar el contexto (max 5)
3) Version segura del prompt (con placeholders)
4) Reglas/guardrails para el modelo (lo que no debe hacer)
Reglas: no repitas secretos si aparecen; redacta y explica.

Prompt:
{prompt}

EN:
Review this prompt for safety and privacy. Deliver:
1) Risks: personal data, credentials, secrets, sensitive info
2) Clarifying questions (max 5)
3) Safer prompt rewrite (with placeholders)
4) Guardrails for the model (what it must not do)
Rules: do not repeat secrets if present; redact and explain.

Prompt:
{prompt}""",
        ),
        PromptCreate(
            title="Agent tool contract / Contrato de herramientas para un agente",
            category="Agents",
            tags=[*shared, "agents", "tools", "contracts", "interfaces"],
            rating=5,
            body="""ES:
Define el contrato de herramientas para un agente. Entrega:
1) Lista de herramientas (nombre, proposito)
2) Esquema de entradas/salidas (campos, tipos, ejemplos)
3) Politicas: permisos, limites, rate limits, datos prohibidos
4) Estrategia de errores (reintentos, fallback, mensajes)
5) Observabilidad (logs/eventos) y auditoria
Reglas: minimiza superficie; separa lectura vs escritura; evita herramientas peligrosas por defecto.

Caso de uso:
{use_case}

EN:
Define a tool contract for an agent. Deliver:
1) Tool list (name, purpose)
2) Input/output schema (fields, types, examples)
3) Policies: permissions, limits, rate limits, forbidden data
4) Error strategy (retries, fallbacks, messages)
5) Observability (logs/events) and auditing
Rules: minimize surface area; separate read vs write; avoid dangerous tools by default.

Use case:
{use_case}""",
        ),
        PromptCreate(
            title="LLM eval rubric / Rubrica de evaluacion de LLM",
            category="Research",
            tags=[*shared, "evals", "rubric", "quality", "testing"],
            rating=5,
            body="""ES:
Crea una rubrica para evaluar respuestas de un LLM en este caso. Incluye:
1) Criterios (correctitud, completitud, claridad, seguridad, accionabilidad)
2) Escala 1-5 por criterio con descriptores
3) Ejemplos de respuesta buena vs mala (breves)
4) Casos frontera y como puntuar
5) Checklist para evaluadores humanos
Devuelve tambien un formato JSON de puntuacion.

Caso de uso:
{use_case}

EN:
Create a rubric to evaluate LLM answers for this use case. Include:
1) Criteria (correctness, completeness, clarity, safety, actionability)
2) 1-5 scale per criterion with descriptors
3) Brief examples of good vs bad answers
4) Edge cases and scoring guidance
5) Checklist for human evaluators
Also return a JSON scoring format.

Use case:
{use_case}""",
        ),
        PromptCreate(
            title="Prompt library curator / Curador de libreria de prompts",
            category="Prompts for Codex",
            tags=[*shared, "prompt-library", "curation", "tags", "quality"],
            rating=4,
            body="""ES:
Actua como curador de una libreria de prompts. Para cada prompt, sugiere:
1) Titulo mejorado (bilingue si aplica)
2) Categoria
3) Tags (5-12) consistentes
4) Rating sugerido (1-5) y por que
5) Version mas corta (si se puede sin perder claridad)
Reglas: evita duplicados; estandariza placeholders; prioriza seguridad y privacidad.

Prompts:
{prompts}

EN:
Act as a prompt library curator. For each prompt, suggest:
1) Improved title (bilingual if applicable)
2) Category
3) Consistent tags (5-12)
4) Suggested rating (1-5) and why
5) Shorter version (if possible without losing clarity)
Rules: avoid duplicates; standardize placeholders; prioritize safety and privacy.

Prompts:
{prompts}""",
        ),
        PromptCreate(
            title="Prompt template normalizer / Normalizador de plantilla de prompt",
            category="Prompts for Codex",
            tags=[*shared, "prompting", "templates", "placeholders", "style", "consistency"],
            rating=5,
            body="""ES:
Normaliza este prompt para que sea reutilizable en una libreria publica. Entrega:
1) Version final (bilingue ES/EN si aplica)
2) Placeholders estandarizados (ej: {context}, {input}, {constraints})
3) Reglas claras (que hacer / que NO hacer)
4) Formato de salida exacto (lista, tabla, JSON, etc.)
5) Mini checklist de privacidad (datos a redactar)
Reglas: evita pedir chain-of-thought; pide pasos verificables.

Prompt original:
{prompt}

EN:
Normalize this prompt so it is reusable in a public library. Deliver:
1) Final version (bilingual ES/EN if applicable)
2) Standardized placeholders (e.g., {context}, {input}, {constraints})
3) Clear rules (do / do NOT)
4) Exact output format (bullets, table, JSON, etc.)
5) Mini privacy checklist (what to redact)
Rules: avoid asking for chain-of-thought; ask for verifiable steps.

Original prompt:
{prompt}""",
        ),
        PromptCreate(
            title="Prompt parameter audit / Auditoria de parametros del prompt",
            category="Prompts for Codex",
            tags=[*shared, "prompting", "inputs", "constraints", "quality", "debugging"],
            rating=4,
            body="""ES:
Audita este prompt como si fuera una funcion. Identifica:
1) Entradas necesarias vs opcionales (con tipos y ejemplo)
2) Suposiciones implicitas y como hacerlas explicitas
3) Restricciones que faltan (seguridad, formato, alcance)
4) Salida esperada (esquema) y criterios de exito
5) Test cases: 3 ejemplos de input y output esperado (breve)

Prompt:
{prompt}

EN:
Audit this prompt as if it were a function. Identify:
1) Required vs optional inputs (with types and examples)
2) Implicit assumptions and how to make them explicit
3) Missing constraints (safety, format, scope)
4) Expected output (schema) and success criteria
5) Test cases: 3 input examples and expected output (brief)

Prompt:
{prompt}""",
        ),
        PromptCreate(
            title="Structured brainstorming with constraints / Brainstorming estructurado con restricciones",
            category="Productivity",
            tags=[*shared, "brainstorming", "constraints", "ideas", "planning"],
            rating=4,
            body="""ES:
Genera ideas de calidad bajo restricciones. Sigue este formato:
1) Reformula el objetivo en 1 frase
2) Lista restricciones (duras vs blandas)
3) 10 ideas (cada una: titulo + 2 frases + por que encaja)
4) Top 3 recomendadas con tradeoffs
5) Primer experimento pequeno para validar cada una

Contexto:
{context}

Restricciones:
{constraints}

EN:
Generate high-quality ideas under constraints. Follow this format:
1) Restate the goal in 1 sentence
2) List constraints (hard vs soft)
3) 10 ideas (each: title + 2 sentences + why it fits)
4) Top 3 recommendations with tradeoffs
5) First small experiment to validate each

Context:
{context}

Constraints:
{constraints}""",
        ),
        PromptCreate(
            title="Decision matrix builder / Constructor de matriz de decision",
            category="Productivity",
            tags=[*shared, "decisions", "tradeoffs", "prioritization", "framework"],
            rating=5,
            body="""ES:
Crea una matriz de decision para elegir entre estas opciones. Entrega:
1) Criterios (5-9) con definicion y peso (0-5)
2) Tabla de puntuacion por opcion (0-5) con justificacion breve
3) Resultado total y recomendacion
4) Sensibilidad: que pasaria si el criterio #1 pesa menos?
5) Riesgos y plan de mitigacion para la opcion ganadora

Opciones:
{options}

Contexto:
{context}

EN:
Build a decision matrix to choose among these options. Deliver:
1) Criteria (5-9) with definition and weight (0-5)
2) Scoring table per option (0-5) with brief justification
3) Total result and recommendation
4) Sensitivity: what if criterion #1 matters less?
5) Risks and mitigation plan for the winning option

Options:
{options}

Context:
{context}""",
        ),
        PromptCreate(
            title="API error playbook / Playbook de errores API",
            category="Architecture",
            tags=[*shared, "api", "errors", "http", "contracts", "debugging"],
            rating=5,
            body="""ES:
Disena un playbook de errores para esta API. Incluye:
1) Taxonomia (validacion, auth, permisos, not-found, conflicto, rate-limit, server)
2) Mapeo a codigos HTTP y estructura JSON de error
3) Mensajes orientados a accion (para usuario y para dev)
4) Correlation/request id y como exponerlo
5) Ejemplos: 6 errores tipicos (request + response)
Reglas: no filtres detalles sensibles; evita mensajes ambiguos.

API/Contexto:
{context}

EN:
Design an API error playbook. Include:
1) Taxonomy (validation, auth, permissions, not-found, conflict, rate-limit, server)
2) Mapping to HTTP codes and JSON error shape
3) Actionable messages (for end users and for devs)
4) Correlation/request id and how to expose it
5) Examples: 6 typical errors (request + response)
Rules: do not leak sensitive details; avoid ambiguous messages.

API/Context:
{context}""",
        ),
        PromptCreate(
            title="Logging strategy for local apps / Estrategia de logging para apps locales",
            category="Architecture",
            tags=[*shared, "logging", "local-first", "privacy", "debugging", "ops"],
            rating=4,
            body="""ES:
Propone una estrategia de logging para una app local-first. Define:
1) Objetivos (debug, soporte, auditoria) y lo que NO se debe loggear
2) Niveles y convenciones (info/warn/error, eventos, contexto)
3) Campos recomendados (timestamp, request_id, modulo, accion)
4) Rotacion/retencion local y limites de tamano
5) Como permitir exportar logs de forma segura (redaccion)
Devuelve un ejemplo de 5 lineas de log.

Contexto:
{context}

EN:
Propose a logging strategy for a local-first app. Define:
1) Goals (debug, support, audit) and what must NOT be logged
2) Levels and conventions (info/warn/error, events, context)
3) Recommended fields (timestamp, request_id, module, action)
4) Local rotation/retention and size limits
5) How to safely export logs (redaction)
Return a 5-line log example.

Context:
{context}""",
        ),
        PromptCreate(
            title="Dependency diet review / Revision de dieta de dependencias",
            category="Architecture",
            tags=[*shared, "dependencies", "minimalism", "security", "maintenance"],
            rating=5,
            body="""ES:
Revisa estas dependencias con mentalidad dependency-light. Entrega:
1) Dependencias criticas vs prescindibles
2) Riesgos (supply chain, licencias, mantenimiento, tamano)
3) Alternativas: stdlib, small libs, o codigo propio (si es razonable)
4) Plan de reduccion en 3 pasos con verificacion
5) Reglas para futuras dependencias (criteria de aceptacion)

Dependencias/Contexto:
{context}

EN:
Review these dependencies with a dependency-light mindset. Deliver:
1) Critical vs optional dependencies
2) Risks (supply chain, licenses, maintenance, size)
3) Alternatives: stdlib, smaller libs, or custom code (when reasonable)
4) 3-step reduction plan with verification
5) Rules for future dependencies (acceptance criteria)

Dependencies/Context:
{context}""",
        ),
        PromptCreate(
            title="Offline-first sync design / Diseno de sincronizacion offline-first",
            category="Architecture",
            tags=[*shared, "offline-first", "sync", "conflicts", "data", "ux"],
            rating=5,
            body="""ES:
Disena una sincronizacion offline-first opcional. Incluye:
1) Modelo de datos y versionado
2) Estrategia de conflictos (last-write-wins, merge, CRDT, manual) y por que
3) Flujo UX para conflictos y estados (offline, syncing, error)
4) Seguridad: cifrado, autenticacion, y minimizacion de datos
5) Pruebas y simulaciones (latencia, duplicados, cortes)
Mantener la app util sin sync es un requisito.

Contexto:
{context}

EN:
Design an optional offline-first sync. Include:
1) Data model and versioning
2) Conflict strategy (LWW, merge, CRDT, manual) and why
3) UX flow for conflicts and states (offline, syncing, error)
4) Security: encryption, auth, and data minimization
5) Tests and simulations (latency, duplicates, disconnects)
The app must remain useful without sync.

Context:
{context}""",
        ),
        PromptCreate(
            title="Data anonymization plan / Plan de anonimization de datos",
            category="Research",
            tags=[*shared, "privacy", "anonymization", "redaction", "datasets", "risk"],
            rating=5,
            body="""ES:
Crea un plan de anonimization para este conjunto de datos. Entrega:
1) Campos sensibles (PII/PHI/secretos) y riesgos
2) Tecnicas (masking, hashing con salt, generalizacion, k-anon, supresion)
3) Reglas por campo (tabla) con ejemplos antes/despues
4) Validacion: como medir reidentificacion y utilidad
5) Politica de retencion y acceso (quien, cuanto tiempo, auditoria)
Reglas: asume entorno local; minimiza la exposicion.

Datos/Contexto:
{context}

EN:
Create an anonymization plan for this dataset. Deliver:
1) Sensitive fields (PII/PHI/secrets) and risks
2) Techniques (masking, salted hashing, generalization, k-anon, suppression)
3) Field-by-field rules (table) with before/after examples
4) Validation: how to measure re-identification risk and utility
5) Retention and access policy (who, how long, auditing)
Rules: assume a local environment; minimize exposure.

Data/Context:
{context}""",
        ),
        PromptCreate(
            title="Prompt red-team scenarios / Escenarios de red-team de prompts",
            category="Prompts for ChatGPT",
            tags=[*shared, "prompting", "red-team", "safety", "abuse", "testing"],
            rating=5,
            body="""ES:
Genera escenarios de red-team para estresar este prompt/sistema. Entrega:
1) 12 ataques (cada uno: objetivo, input, por que funciona)
2) Severidad y probabilidad (baja/media/alta)
3) Mitigacion: cambio minimo al prompt o guardrails
4) Tests automatizables: 5 casos con expected outcome
Reglas: no incluyas instrucciones ilegales ni contenido peligroso; usa ejemplos abstractos.

Prompt/Sistema:
{prompt}

EN:
Generate red-team scenarios to stress-test this prompt/system. Deliver:
1) 12 attacks (each: goal, input, why it works)
2) Severity and likelihood (low/medium/high)
3) Mitigation: minimal prompt/guardrail change
4) Automatable tests: 5 cases with expected outcome
Rules: do not include illegal instructions or dangerous content; use abstract examples.

Prompt/System:
{prompt}""",
        ),
        PromptCreate(
            title="Evaluation dataset spec / Especificacion de dataset de evaluacion",
            category="Research",
            tags=[*shared, "evals", "dataset", "metrics", "quality", "benchmark"],
            rating=4,
            body="""ES:
Especifica un dataset para evaluar este caso de uso. Incluye:
1) Objetivo y definicion de exito
2) Distribucion de casos (facil/medio/dificil; normales vs bordes)
3) Esquema de cada item (campos) y 3 ejemplos completos
4) Metricas (exactitud, cobertura, seguridad) y como calcular
5) Protocolo de evaluacion humana (instrucciones + rubric)
Reglas: evita datos reales; usa ejemplos sinteticos.

Caso de uso:
{use_case}

EN:
Specify a dataset to evaluate this use case. Include:
1) Goal and success definition
2) Case distribution (easy/medium/hard; normal vs edge)
3) Item schema (fields) and 3 full examples
4) Metrics (accuracy, coverage, safety) and how to compute
5) Human eval protocol (instructions + rubric)
Rules: avoid real data; use synthetic examples.

Use case:
{use_case}""",
        ),
        PromptCreate(
            title="Product roadmap slice / Rebanada de roadmap de producto",
            category="Productivity",
            tags=[*shared, "roadmap", "planning", "prioritization", "milestones"],
            rating=4,
            body="""ES:
Convierte estos objetivos en un slice de roadmap de 6-8 semanas. Entrega:
1) 3-5 outcomes medibles
2) Epics y alcance (in-scope/out-of-scope)
3) Hitos semanales con criterios de terminado
4) Riesgos, dependencias y mitigaciones
5) Lista de cosas que NO haremos (para proteger el foco)

Objetivos/Contexto:
{context}

EN:
Turn these goals into a 6-8 week roadmap slice. Deliver:
1) 3-5 measurable outcomes
2) Epics and scope (in-scope/out-of-scope)
3) Weekly milestones with definition of done
4) Risks, dependencies, and mitigations
5) Explicit list of what we will NOT do (to protect focus)

Goals/Context:
{context}""",
        ),
        PromptCreate(
            title="GitHub issue triage reply / Respuesta de triage en issue de GitHub",
            category="Productivity",
            tags=[*shared, "github", "triage", "support", "oss", "communication"],
            rating=4,
            body="""ES:
Redacta una respuesta de triage para este issue. Debe ser amable y accionable. Incluye:
1) Agradecimiento y confirmacion de entendimiento
2) Preguntas concretas (max 6) para reproducir/diagnosticar
3) Checklist de informacion (version, OS, pasos, logs, config)
4) Si procede: workaround temporal
5) Etiquetas sugeridas (bug, question, needs-repro, etc.)
Reglas: no pidas datos privados; sugiere redaccion.

Issue:
{issue}

EN:
Draft a triage reply for this issue. Keep it friendly and actionable. Include:
1) Thanks and understanding confirmation
2) Concrete questions (max 6) to reproduce/diagnose
3) Info checklist (version, OS, steps, logs, config)
4) If applicable: temporary workaround
5) Suggested labels (bug, question, needs-repro, etc.)
Rules: do not request private data; suggest redaction.

Issue:
{issue}""",
        ),
        PromptCreate(
            title="Contributor-friendly bug report form / Formulario de reporte de bug amigable",
            category="Productivity",
            tags=[*shared, "oss", "bugs", "templates", "github", "repro"],
            rating=5,
            body="""ES:
Crea una plantilla de bug report para un repo open-source. Entrega un template en Markdown con:
- Resumen
- Version/entorno
- Pasos para reproducir
- Resultado esperado vs actual
- Logs (con instrucciones para redactar secretos)
- Capturas (opcional)
- Contexto adicional
- Incluye un ejemplo completado con datos ficticios.

EN:
Create a bug report template for an open-source repo. Return a Markdown template with:
- Summary
- Version/environment
- Steps to reproduce
- Expected vs actual result
- Logs (with instructions to redact secrets)
- Screenshots (optional)
- Additional context
- Include a filled example with fictional data.""",
        ),
        PromptCreate(
            title="Design system component checklist / Checklist de componente de design system",
            category="Design",
            tags=[*shared, "design-system", "components", "a11y", "ux", "frontend"],
            rating=4,
            body="""ES:
Evalua este componente para un design system. Devuelve un checklist con:
1) Props/APIs (nombres, defaults, variantes)
2) Accesibilidad (roles, labels, teclado, focus, contrast)
3) Estados (loading, empty, error, disabled)
4) Responsive y theming
5) Performance (re-renders, virtualization si aplica)
6) Documentacion y ejemplos
Incluye 'bloqueantes' vs 'nice-to-have'.

Componente/Contexto:
{context}

EN:
Evaluate this component for a design system. Return a checklist covering:
1) Props/APIs (names, defaults, variants)
2) Accessibility (roles, labels, keyboard, focus, contrast)
3) States (loading, empty, error, disabled)
4) Responsive and theming
5) Performance (re-renders, virtualization if applicable)
6) Documentation and examples
Include 'blockers' vs 'nice-to-have'.

Component/Context:
{context}""",
        ),
        PromptCreate(
            title="Microcopy UX pass / Revision de microcopy UX",
            category="Design",
            tags=[*shared, "ux", "copy", "microcopy", "ui", "accessibility"],
            rating=4,
            body="""ES:
Mejora el microcopy de esta UI. Entrega:
1) Cambios propuestos (antes -> despues) por pantalla/elemento
2) Guia de tono (3-5 reglas)
3) Consistencia de terminos y etiquetas
4) Errores y vacios: mensajes de error, empty states, loading
5) Accesibilidad: claridad, longitud, lenguaje simple
Reglas: no inventes funciones que no existan; no uses promesas legales.

Texto/UI:
{context}

EN:
Improve the microcopy for this UI. Deliver:
1) Proposed changes (before -> after) per screen/element
2) Tone guide (3-5 rules)
3) Terminology consistency
4) Error/empty/loading messages
5) Accessibility: clarity, length, plain language
Rules: do not invent features that do not exist; avoid legal promises.

Text/UI:
{context}""",
        ),
        PromptCreate(
            title="Case study outline / Esquema de caso de exito",
            category="Marketing",
            tags=[*shared, "case-study", "storytelling", "marketing", "structure"],
            rating=4,
            body="""ES:
Crea el esquema de un caso de exito. Incluye:
1) Contexto del cliente (anonimo si es necesario)
2) Problema (con sintomas medibles)
3) Solucion (pasos, timeline)
4) Resultados (metricas; si faltan, placeholders)
5) Lecciones y recomendaciones
6) Citas (solo si se proporcionan; si no, sugiere donde conseguirlas)

Detalles:
{context}

EN:
Create an outline for a case study. Include:
1) Customer context (anonymous if needed)
2) Problem (with measurable symptoms)
3) Solution (steps, timeline)
4) Results (metrics; use placeholders if missing)
5) Lessons and recommendations
6) Quotes (only if provided; otherwise suggest how to gather them)

Details:
{context}""",
        ),
        PromptCreate(
            title="Explain like I'm new / Explica como si fuera nuevo",
            category="Coding",
            tags=[*shared, "teaching", "onboarding", "explain", "examples"],
            rating=5,
            body="""ES:
Explica este concepto/codigo como si yo fuera nuevo en el tema. Formato:
1) Idea central en 1 frase
2) Metafora simple (si ayuda)
3) Explicacion paso a paso con un ejemplo minimo
4) Errores comunes y como evitarlos
5) Mini ejercicio con solucion
Reglas: no asumas contexto no dado; define terminos.

Tema/Codigo:
{context}

EN:
Explain this concept/code as if I were new to it. Format:
1) Core idea in 1 sentence
2) Simple metaphor (if helpful)
3) Step-by-step explanation with a minimal example
4) Common mistakes and how to avoid them
5) Mini exercise with a solution
Rules: do not assume unstated context; define terms.

Topic/Code:
{context}""",
        ),
        PromptCreate(
            title="Agent workspace boundaries / Limites del workspace para un agente",
            category="Agents",
            tags=[*shared, "agents", "safety", "boundaries", "filesystem", "workflow"],
            rating=4,
            body="""ES:
Define limites claros para un agente que trabaja en un repo. Entrega:
1) Que puede leer/escribir (paths permitidos)
2) Acciones prohibidas por defecto (delete masivo, push, secrets)
3) Politica de aprobacion para operaciones riesgosas
4) Politica de datos: que no debe exfiltrar ni copiar
5) Checklist final antes de entregar cambios
Devuelve tambien un bloque YAML con estas reglas.

Contexto:
{context}

EN:
Define clear workspace boundaries for an agent working in a repo. Deliver:
1) What it can read/write (allowed paths)
2) Default-prohibited actions (mass deletes, pushes, secrets)
3) Approval policy for risky operations
4) Data policy: what it must not exfiltrate or copy
5) Final checklist before delivering changes
Also return a YAML block with these rules.

Context:
{context}""",
        ),
        PromptCreate(
            title="Supply-chain risk review / Revision de riesgo de supply-chain",
            category="Research",
            tags=[*shared, "security", "supply-chain", "dependencies", "risk", "oss"],
            rating=5,
            body="""ES:
Analiza riesgos de supply-chain para este proyecto. Entrega:
1) Superficies de riesgo (deps, build, CI, releases)
2) Controles recomendados (pinning, hashes, provenance, minimal perms)
3) Lista priorizada de acciones (P0/P1/P2) con esfuerzo estimado
4) Politica de actualizaciones (cadencia y criterios)
5) Checklist rapido para PRs de dependencias
Reglas: asume un repo publico; prioriza controles simples.

Proyecto/Contexto:
{context}

EN:
Analyze supply-chain risks for this project. Deliver:
1) Risk surfaces (deps, build, CI, releases)
2) Recommended controls (pinning, hashes, provenance, minimal perms)
3) Prioritized actions (P0/P1/P2) with rough effort
4) Update policy (cadence and criteria)
5) Quick checklist for dependency PRs
Rules: assume a public repo; prioritize simple controls.

Project/Context:
{context}""",
        ),
        PromptCreate(
            title="Git bisect guide / Guia de git bisect",
            category="Debugging",
            tags=[*shared, "git", "bisect", "debugging", "regression"],
            rating=5,
            body="""ES:
Ayudame a encontrar el commit que introdujo una regresion usando `git bisect`. Entrega:
1) Requisitos previos (rama, tests, limpieza del repo)
2) Comandos exactos para iniciar bisect (good/bad) y ejecutarlo con un test
3) Como definir un criterio automatico (script o comando) para marcar good/bad
4) Que hacer si el test es flaky o lento
5) Como terminar y volver a un estado limpio
6) Nota de seguridad: no reescribas historia si no lo pido

Contexto (comando de test, sintomas, rango de commits):
{context}

EN:
Help me find the commit that introduced a regression using `git bisect`. Deliver:
1) Preconditions (branch, tests, clean repo)
2) Exact commands to start bisect (good/bad) and drive it with a test
3) How to define an automatic criterion (script/command) to mark good/bad
4) What to do if the test is flaky or slow
5) How to finish and return to a clean state
6) Safety note: do not rewrite history unless asked

Context (test command, symptoms, commit range):
{context}""",
        ),
        PromptCreate(
            title="Minimal reproduction in a sandbox / Reproduccion minima en sandbox",
            category="Debugging",
            tags=[*shared, "debugging", "repro", "minimize", "isolation"],
            rating=5,
            body="""ES:
Convierte este bug en una reproduccion minima. Entrega:
1) Hipotesis sobre el componente minimo que falla
2) Pasos para aislar variables (config, datos, red, concurrencia)
3) Un repro en 1 archivo (si aplica) o un repo-esqueleto (estructura + comandos)
4) Inputs exactos y expected/actual
5) Criterio de exito: un test automatizado que falla de forma determinista
Reglas: evita datos sensibles; usa valores ficticios.

Bug/Contexto:
{context}

EN:
Turn this bug into a minimal reproduction. Deliver:
1) Hypothesis about the smallest failing component
2) Steps to isolate variables (config, data, network, concurrency)
3) A one-file repro (if applicable) or a skeleton repo (structure + commands)
4) Exact inputs and expected/actual output
5) Success criterion: a deterministic failing automated test
Rules: avoid sensitive data; use fictional values.

Bug/Context:
{context}""",
        ),
        PromptCreate(
            title="Dependency license check / Revision de licencias de dependencias",
            category="Research",
            tags=[*shared, "licenses", "oss", "compliance", "dependencies"],
            rating=4,
            body="""ES:
Revisa licencias de dependencias para este proyecto. Entrega:
1) Lista de dependencias y sus licencias (si falta info, marca como Unknown)
2) Riesgos tipicos por familia (permisivas, copyleft, network copyleft)
3) Acciones recomendadas (atribucion, NOTICE, reemplazos) priorizadas
4) Politica simple para PRs de dependencias (checks minimos)
Reglas: no asumas licencias sin fuente; propone como verificar.

Proyecto/Dependencias (lockfile, lista, etc.):
{context}

EN:
Review dependency licenses for this project. Deliver:
1) Dependency list and their licenses (mark Unknown if missing)
2) Typical risks by family (permissive, copyleft, network copyleft)
3) Recommended actions (attribution, NOTICE, replacements) prioritized
4) A simple policy for dependency PRs (minimum checks)
Rules: do not assume licenses without a source; propose how to verify.

Project/Dependencies (lockfile, list, etc.):
{context}""",
        ),
        PromptCreate(
            title="API pagination design / Diseno de paginacion de API",
            category="Architecture",
            tags=[*shared, "api", "pagination", "design", "contracts"],
            rating=5,
            body="""ES:
Disena paginacion para este endpoint. Incluye:
1) Estrategia recomendada (cursor vs offset) y por que
2) Contrato request/response (campos, ejemplos)
3) Ordenamiento estable, filtros y coherencia en presencia de inserts/updates
4) Errores y limites (max page size, rate limits)
5) Plan de migracion desde el esquema actual (si existe)

Contexto:
{context}

EN:
Design pagination for this endpoint. Include:
1) Recommended strategy (cursor vs offset) and why
2) Request/response contract (fields, examples)
3) Stable ordering, filters, and consistency under inserts/updates
4) Errors and limits (max page size, rate limits)
5) Migration plan from the current scheme (if any)

Context:
{context}""",
        ),
        PromptCreate(
            title="Data migration plan / Plan de migracion de datos",
            category="Architecture",
            tags=[*shared, "data", "migration", "backfill", "rollout"],
            rating=5,
            body="""ES:
Crea un plan de migracion de datos seguro. Entrega:
1) Objetivo y cambios de esquema
2) Estrategia (expand/contract) con fases y criterios de salida
3) Backfill (batching, idempotencia, reintentos) y como medir progreso
4) Compatibilidad hacia atras (lecturas/escrituras duales si aplica)
5) Rollback plan y senales de parada
6) Checklist de verificacion post-migracion

Contexto:
{context}

EN:
Create a safe data migration plan. Deliver:
1) Goal and schema changes
2) Strategy (expand/contract) with phases and exit criteria
3) Backfill (batching, idempotency, retries) and how to measure progress
4) Backward compatibility (dual reads/writes if applicable)
5) Rollback plan and stop signals
6) Post-migration verification checklist

Context:
{context}""",
        ),
        PromptCreate(
            title="Observability quickstart / Inicio rapido de observabilidad",
            category="Architecture",
            tags=[*shared, "observability", "logging", "metrics", "tracing"],
            rating=4,
            body="""ES:
Propone un inicio rapido de observabilidad para una app local-first. Entrega:
1) Eventos y metricas minimas (P0) con nombres sugeridos
2) Estructura de logs (campos obligatorios, niveles)
3) Trazas (si aplica): que spans y atributos capturar
4) Politica de privacidad: que NO registrar (PII, secretos)
5) Plan de rollout incremental y como validar que sirve

App/Contexto:
{context}

EN:
Propose an observability quickstart for a local-first app. Deliver:
1) Minimum events and metrics (P0) with suggested names
2) Log structure (required fields, levels)
3) Tracing (if applicable): which spans and attributes to capture
4) Privacy policy: what NOT to log (PII, secrets)
5) Incremental rollout plan and how to validate usefulness

App/Context:
{context}""",
        ),
        PromptCreate(
            title="UX usability test script / Guion de test de usabilidad",
            category="Design",
            tags=[*shared, "ux", "usability", "research", "script"],
            rating=5,
            body="""ES:
Escribe un guion de test de usabilidad de 30-45 min para este producto/flujo. Incluye:
1) Objetivo y criterios de exito
2) Screening rapido (si aplica)
3) Warm-up y preguntas de contexto
4) Tareas (con escenarios realistas) y probes
5) Preguntas de cierre (SUS o similares opcional)
6) Plan de notas: que observar y como codificar hallazgos
Reglas: evita pedir datos personales; usa ejemplos ficticios.

Producto/Flujo:
{context}

EN:
Write a 30–45 min usability test script for this product/flow. Include:
1) Goal and success criteria
2) Quick screening (if applicable)
3) Warm-up and background questions
4) Tasks (realistic scenarios) and probes
5) Wrap-up questions (SUS or similar optional)
6) Note-taking plan: what to observe and how to code findings
Rules: avoid collecting personal data; use fictional examples.

Product/Flow:
{context}""",
        ),
        PromptCreate(
            title="Design token audit / Auditoria de design tokens",
            category="Design",
            tags=[*shared, "design-system", "tokens", "accessibility", "consistency"],
            rating=4,
            body="""ES:
Audita nuestros design tokens. Entrega:
1) Inventario (color, tipografia, spacing, radius, shadow, motion)
2) Inconsistencias y duplicados (con regla para consolidar)
3) Accesibilidad (contraste) y tokens que faltan
4) Convencion de nombres propuesta y ejemplos
5) Plan de migracion incremental (sin romper UI)

Tokens/Contexto:
{context}

EN:
Audit our design tokens. Deliver:
1) Inventory (color, typography, spacing, radius, shadow, motion)
2) Inconsistencies and duplicates (with a consolidation rule)
3) Accessibility (contrast) and missing tokens
4) Proposed naming convention with examples
5) Incremental migration plan (avoid breaking UI)

Tokens/Context:
{context}""",
        ),
        PromptCreate(
            title="Changelog entry writer / Redactor de changelog",
            category="Productivity",
            tags=[*shared, "release", "changelog", "writing", "docs"],
            rating=4,
            body="""ES:
Escribe una entrada de changelog a partir de estos commits/notas. Devuelve:
1) Titulo de release (si aplica)
2) Secciones: Added/Changed/Fixed/Security
3) Texto orientado a usuario (no interno) y conciso
4) Notas de migracion (si hay breaking changes)
Reglas: no inventes features; si falta info, pide un dato puntual.

Commits/Notas:
{context}

EN:
Write a changelog entry from these commits/notes. Return:
1) Release title (if applicable)
2) Sections: Added/Changed/Fixed/Security
3) User-facing concise wording (avoid internal jargon)
4) Migration notes (if there are breaking changes)
Rules: do not invent features; if info is missing, ask for one specific detail.

Commits/Notes:
{context}""",
        ),
        PromptCreate(
            title="Release checklist / Checklist de release",
            category="Productivity",
            tags=[*shared, "release", "checklist", "qa", "ops"],
            rating=5,
            body="""ES:
Construye un checklist de release para este proyecto. Incluye:
1) Pre-release (tests, lint, versioning, docs)
2) Seguridad y privacidad (secrets scan, permisos)
3) Build/packaging y reproducibilidad
4) Deploy/publicacion (pasos, validaciones)
5) Post-release (monitorizacion, rollback readiness, notas)
Devuelve un checklist accionable en Markdown con casillas.

Proyecto/Contexto:
{context}

EN:
Build a release checklist for this project. Include:
1) Pre-release (tests, lint, versioning, docs)
2) Security and privacy (secrets scan, permissions)
3) Build/packaging and reproducibility
4) Deploy/publish (steps, validations)
5) Post-release (monitoring, rollback readiness, notes)
Return an actionable Markdown checklist with checkboxes.

Project/Context:
{context}""",
        ),
        PromptCreate(
            title="Job story generator / Generador de job stories",
            category="Marketing",
            tags=[*shared, "product", "research", "jtbd", "messaging"],
            rating=4,
            body="""ES:
Genera Job Stories (JTBD) a partir de este contexto. Entrega:
1) 5-8 job stories en formato: Cuando..., quiero..., para poder...
2) Segmentos/variantes (novato vs power user, etc.)
3) Senales de progreso (metricas o indicadores) por job
4) Preguntas para validar con usuarios (sin leading questions)

Contexto:
{context}

EN:
Generate Job Stories (JTBD) from this context. Deliver:
1) 5–8 job stories in the format: When..., I want..., so I can...
2) Segments/variants (novice vs power user, etc.)
3) Progress signals (metrics or indicators) per job
4) Questions to validate with users (avoid leading questions)

Context:
{context}""",
        ),
        PromptCreate(
            title="Pricing page messaging / Mensajes de pagina de precios",
            category="Marketing",
            tags=[*shared, "pricing", "copy", "positioning", "objections"],
            rating=4,
            body="""ES:
Escribe mensajes para una pagina de precios. Entrega:
1) Titular/subtitular para 3 planes
2) 6-10 bullets de valor (no features) por plan
3) Objeciones tipicas y como resolverlas con copy
4) FAQ (5-8) enfocadas en riesgo, privacidad y soporte
Reglas: no inventes claims medibles; usa placeholders si faltan datos.

Producto/Planes/Contexto:
{context}

EN:
Write messaging for a pricing page. Deliver:
1) Headline/subheadline for 3 plans
2) 6–10 value bullets (not just features) per plan
3) Common objections and how to address them with copy
4) FAQ (5–8) focused on risk, privacy, and support
Rules: do not invent measurable claims; use placeholders if data is missing.

Product/Plans/Context:
{context}""",
        ),
        PromptCreate(
            title="Content repurposing plan / Plan de reutilizacion de contenido",
            category="Marketing",
            tags=[*shared, "content", "repurpose", "distribution", "marketing"],
            rating=4,
            body="""ES:
Convierte esta pieza de contenido en un plan de reutilizacion multiplataforma. Entrega:
1) 5-10 atomizaciones (tweets, LinkedIn, newsletter, short video, etc.)
2) Angulos alternativos (beneficio, historia, datos, opinion)
3) Calendario de 2 semanas con cadencia
4) CTA sugeridas y metricas de exito por canal
Reglas: respeta tono; no inventes datos.

Contenido original:
{context}

EN:
Turn this content into a cross-platform repurposing plan. Deliver:
1) 5–10 atoms (tweets, LinkedIn, newsletter, short video, etc.)
2) Alternate angles (benefit, story, data, opinion)
3) Two-week calendar with cadence
4) Suggested CTAs and success metrics per channel
Rules: keep the tone; do not invent data.

Original content:
{context}""",
        ),
        PromptCreate(
            title="Academic paper reading grid / Plantilla de lectura de paper",
            category="Research",
            tags=[*shared, "research", "papers", "notes", "learning"],
            rating=4,
            body="""ES:
Ayudame a leer y resumir un paper con una plantilla. Devuelve:
1) Pregunta que responde y aportacion principal
2) Metodo/datos (dataset, setup, supuestos)
3) Resultados clave (con numeros si se proveen)
4) Limitaciones y amenazas a validez
5) Implicaciones practicas
6) Preguntas abiertas y proximos experimentos
7) Glosario de terminos (si hay jerga)
Reglas: cita solo lo que se proporciona; marca incertidumbre.

Paper/Notas:
{context}

EN:
Help me read and summarize a paper using a template. Return:
1) Research question and main contribution
2) Method/data (dataset, setup, assumptions)
3) Key results (include numbers if provided)
4) Limitations and threats to validity
5) Practical implications
6) Open questions and next experiments
7) Glossary (if jargon-heavy)
Rules: cite only what is provided; mark uncertainty.

Paper/Notes:
{context}""",
        ),
        PromptCreate(
            title="Source credibility rubric / Rubrica de credibilidad de fuentes",
            category="Research",
            tags=[*shared, "research", "sources", "credibility", "evaluation"],
            rating=5,
            body="""ES:
Crea una rubrica para evaluar la credibilidad de fuentes sobre este tema. Entrega:
1) Criterios (autoridad, evidencia, conflictos, actualidad, replicabilidad)
2) Puntuacion 0-2 por criterio (con definiciones claras)
3) Red flags comunes y como verificarlas
4) Plantilla para registrar fuentes (tabla)
5) Recomendacion de triangulacion (como corroborar)

Tema/Contexto:
{context}

EN:
Create a rubric to evaluate source credibility for this topic. Deliver:
1) Criteria (authority, evidence, conflicts, recency, replicability)
2) 0–2 scoring per criterion (clear definitions)
3) Common red flags and how to check them
4) A source-tracking template (table)
5) Triangulation recommendation (how to corroborate)

Topic/Context:
{context}""",
        ),
        PromptCreate(
            title="Agent tool-use policy / Politica de uso de herramientas para agentes",
            category="Agents",
            tags=[*shared, "agents", "tools", "policy", "safety", "approvals"],
            rating=5,
            body="""ES:
Define una politica de uso de herramientas para un agente. Incluye:
1) Lista de herramientas y propositos
2) Que requiere aprobacion (red, push, deletes, pagos, prod)
3) Reglas para manejo de errores (reintentos, backoff, rollback)
4) Politica de datos (PII, secretos, logs) y redaccion
5) Formato de auditoria: como registrar acciones y resultados
Devuelve una version corta (para prompt) y una larga (para docs).

Contexto:
{context}

EN:
Define a tool-use policy for an agent. Include:
1) Tool list and purposes
2) What requires approval (network, push, deletes, payments, prod)
3) Error-handling rules (retries, backoff, rollback)
4) Data policy (PII, secrets, logs) and redaction
5) Audit format: how to record actions and outcomes
Return a short version (for prompts) and a long version (for docs).

Context:
{context}""",
        ),
        PromptCreate(
            title="Codex test-first patch / Parche test-first para Codex",
            category="Prompts for Codex",
            tags=[*shared, "codex", "testing", "tdd", "regression", "patch"],
            rating=5,
            favorite=True,
            body="""ES:
Actua como Codex en modo test-first. Reglas:
1) Primero reproduce el bug o agrega un test que falle (minimo)
2) Luego implementa el fix mas pequeno posible
3) Asegura que el estilo del repo se mantiene (format/lint)
4) No toques codigo no relacionado
5) Termina con comandos ejecutados y resultados (tests/lint)
Formato de salida:
- Hipotesis
- Test (archivo + descripcion)
- Cambio minimo
- Verificacion (comandos + salida resumida)

Tarea/Contexto:
{context}

EN:
Act as Codex in test-first mode. Rules:
1) First reproduce the bug or add a minimal failing test
2) Then implement the smallest possible fix
3) Keep repo style (format/lint)
4) Do not touch unrelated code
5) Finish with executed commands and results (tests/lint)
Output format:
- Hypothesis
- Test (file + description)
- Minimal change
- Verification (commands + brief output)

Task/Context:
{context}""",
        ),
        PromptCreate(
            title="Claude concise redline / Redline conciso para Claude",
            category="Prompts for Claude",
            tags=[*shared, "claude", "editing", "redline", "clarity"],
            rating=4,
            body="""ES:
Haz un redline conciso de este texto. Devuelve:
1) Version revisada (sin explicaciones en medio)
2) Lista corta de cambios (max 8) con razon (claridad, tono, consistencia)
3) Preguntas abiertas (si falta info)
Reglas: mantén significado; evita inventar hechos.

Texto:
{context}

EN:
Do a concise redline of this text. Return:
1) Revised version (no inline explanations)
2) Short change list (max 8) with reason (clarity, tone, consistency)
3) Open questions (if info is missing)
Rules: preserve meaning; do not invent facts.

Text:
{context}""",
        ),
        PromptCreate(
            title="ChatGPT evaluation rubric / Rubrica de evaluacion ChatGPT",
            category="Prompts for ChatGPT",
            tags=[*shared, "chatgpt", "evaluation", "rubric", "quality"],
            rating=4,
            body="""ES:
Construye una rubrica para evaluar respuestas a este tipo de tarea. Entrega:
1) 6-10 criterios con definicion (exactitud, cobertura, accionabilidad, seguridad, claridad)
2) Puntuacion 1-5 por criterio con anclas
3) Ejemplos de una respuesta 1/5 vs 5/5 (breves)
4) Checklist final para el evaluador
Reglas: no pidas cadena de pensamiento; evalua outputs observables.

Tipo de tarea/Contexto:
{context}

EN:
Build a rubric to evaluate answers for this type of task. Deliver:
1) 6–10 criteria with definitions (accuracy, coverage, actionability, safety, clarity)
2) 1–5 scoring per criterion with anchors
3) Brief examples of a 1/5 vs 5/5 response
4) Final evaluator checklist
Rules: do not ask for chain-of-thought; evaluate observable outputs.

Task type/Context:
{context}""",
        ),
        PromptCreate(
            title="Prompt pack curation / Curacion de pack de prompts",
            category="Prompts",
            tags=[*shared, "prompts", "library", "curation", "taxonomy"],
            rating=5,
            body="""ES:
Cura un pack de prompts para un repositorio publico. Entrega:
1) Taxonomia propuesta (categorias + tags) y convenciones de nombres
2) Reglas de calidad (claridad, limites, formato de salida, ejemplos)
3) Checklist de seguridad/privacidad (sin PII, sin secretos, sin datos de cliente)
4) Proceso para evitar duplicados y mantener consistencia
5) Plan de mantenimiento (versionado, deprecaciones, notas de cambios)

Contexto del pack:
{context}

EN:
Curate a prompt pack for a public repository. Deliver:
1) Proposed taxonomy (categories + tags) and naming conventions
2) Quality rules (clarity, constraints, output format, examples)
3) Safety/privacy checklist (no PII, no secrets, no customer data)
4) Process to avoid duplicates and keep consistency
5) Maintenance plan (versioning, deprecations, changelog notes)

Pack context:
{context}""",
        ),
        PromptCreate(
            title="Minimal PR description / Descripcion minima de PR",
            category="Productivity",
            tags=[*shared, "productivity", "writing", "pull-request", "review"],
            rating=5,
            body="""ES:
Escribe una descripcion de PR lista para copiar/pegar. Incluye:
1) Contexto (1-2 frases)
2) Cambios principales (3-6 bullets)
3) Como probar (pasos exactos)
4) Riesgos/impacto (si aplica)
5) Capturas/ejemplos (si aplica)
Reglas: no inventes hechos; pregunta si falta info.

Datos:
{context}

EN:
Write a copy/paste-ready PR description. Include:
1) Context (1-2 sentences)
2) Key changes (3-6 bullets)
3) How to test (exact steps)
4) Risks/impact (if any)
5) Screenshots/examples (if relevant)
Rules: do not invent facts; ask if info is missing.

Inputs:
{context}""",
        ),
        PromptCreate(
            title="Codebase onboarding map (30 min) / Mapa de onboarding del codebase (30 min)",
            category="Architecture",
            tags=[*shared, "architecture", "onboarding", "codebase", "map"],
            rating=5,
            body="""ES:
Ayudame a onboardearme a este repositorio. Entrega:
1) Mapa de alto nivel (modulos y responsabilidades)
2) Flujos principales (de entrada a salida)
3) Puntos de extension (donde agregar features)
4) Riesgos (zonas fragiles, deuda tecnica)
5) 5 tareas pequenas para aprender (ordenadas)
Incluye rutas de archivos concretas cuando sea posible.

Repo/Contexto:
{context}

EN:
Help me onboard to this repository. Deliver:
1) High-level map (modules and responsibilities)
2) Key flows (input to output)
3) Extension points (where to add features)
4) Risks (fragile areas, tech debt)
5) Five small learning tasks (ordered)
Include concrete file paths when possible.

Repo/Context:
{context}""",
        ),
        PromptCreate(
            title="Log triage checklist / Checklist de triaje de logs",
            category="Debugging",
            tags=[*shared, "debugging", "logs", "triage", "observability"],
            rating=4,
            body="""ES:
Analiza estos logs y haz triaje. Devuelve:
1) Resumen del incidente (que paso, cuando, a quien afecta)
2) 3 hipotesis con evidencia (lineas/campos)
3) Siguientes pasos (ordenados, minimo-toque)
4) Que datos faltan (metricas, trazas, ids)
5) Recomendaciones de logging (campos utiles, nivel, redaccion de PII)
Reglas: no asumas PII; si aparece, redacta.

Logs/Contexto:
{context}

EN:
Triage these logs. Return:
1) Incident summary (what happened, when, who is affected)
2) Three hypotheses with evidence (lines/fields)
3) Next steps (ordered, minimal-touch)
4) Missing data (metrics, traces, ids)
5) Logging improvements (useful fields, level, PII redaction)
Rules: do not assume PII; if present, redact it.

Logs/Context:
{context}""",
        ),
        PromptCreate(
            title="SQL query review / Revision de consultas SQL",
            category="Coding",
            tags=[*shared, "coding", "sql", "performance", "review"],
            rating=5,
            body="""ES:
Revisa esta consulta SQL. Entrega:
1) Que hace (en lenguaje simple)
2) Posibles bugs (joins, nulls, duplicados)
3) Riesgos de performance (filtros, indices, cardinalidad)
4) Version mejorada (si aplica) con explicacion breve
5) Casos de prueba (3-5) con datos minimos
Reglas: no inventes esquema; pide columnas/tablas faltantes.

SQL/Contexto:
{context}

EN:
Review this SQL query. Deliver:
1) What it does (plain language)
2) Possible bugs (joins, nulls, duplicates)
3) Performance risks (filters, indexes, cardinality)
4) Improved version (if needed) with brief explanation
5) 3-5 test cases with minimal data
Rules: do not invent schema; ask for missing tables/columns.

SQL/Context:
{context}""",
        ),
        PromptCreate(
            title="Threat model lite / Threat model ligero",
            category="Architecture",
            tags=[*shared, "architecture", "security", "threat-model", "risks"],
            rating=5,
            body="""ES:
Haz un threat model ligero para este sistema/feature. Entrega:
1) Activos a proteger (datos, dinero, integridad)
2) Actores (usuarios, atacantes, insiders)
3) Superficies de ataque (endpoints, storage, auth, supply chain)
4) Top 10 amenazas (probabilidad x impacto) con mitigacion
5) Controles recomendados y que monitorear
Reglas: mantente practico; marca suposiciones.

Sistema/Contexto:
{context}

EN:
Create a lightweight threat model for this system/feature. Deliver:
1) Assets to protect (data, money, integrity)
2) Actors (users, attackers, insiders)
3) Attack surfaces (endpoints, storage, auth, supply chain)
4) Top 10 threats (likelihood x impact) with mitigation
5) Recommended controls and what to monitor
Rules: stay practical; label assumptions.

System/Context:
{context}""",
        ),
        PromptCreate(
            title="UI copy tone guide / Guia de tono para UI copy",
            category="Design",
            tags=[*shared, "design", "ux-writing", "tone", "microcopy"],
            rating=4,
            body="""ES:
Define una guia de tono para el texto de UI de este producto. Incluye:
1) Personalidad (3-5 adjetivos) y anti-personalidad
2) Do/Don't con ejemplos
3) Reglas para errores, confirmaciones y vacios (empty states)
4) Glosario de terminos (preferidos vs prohibidos)
5) Plantillas: boton, tooltip, error, banner, modal

Producto/Contexto:
{context}

EN:
Define a UI copy tone guide for this product. Include:
1) Personality (3-5 adjectives) and anti-personality
2) Do/Don't with examples
3) Rules for errors, confirmations, and empty states
4) Glossary (preferred vs forbidden terms)
5) Templates: button, tooltip, error, banner, modal

Product/Context:
{context}""",
        ),
        PromptCreate(
            title="User interview synthesis / Sintesis de entrevistas de usuario",
            category="Research",
            tags=[*shared, "research", "ux", "interviews", "synthesis"],
            rating=5,
            body="""ES:
Sintetiza estas notas de entrevistas. Devuelve:
1) 5-10 hallazgos (con evidencia: citas o notas)
2) Necesidades/JTBD y como se miden
3) Puntos de dolor y frecuencia
4) Oportunidades (quick wins vs apuestas grandes)
5) Preguntas pendientes para la proxima ronda
Reglas: no extrapoles mas alla de la evidencia.

Notas/Contexto:
{context}

EN:
Synthesize these interview notes. Return:
1) 5-10 findings (with evidence: quotes or notes)
2) Needs/JTBD and how to measure them
3) Pain points and frequency
4) Opportunities (quick wins vs big bets)
5) Open questions for the next round
Rules: do not extrapolate beyond the evidence.

Notes/Context:
{context}""",
        ),
        PromptCreate(
            title="A/B experiment plan / Plan de experimento A/B",
            category="Marketing",
            tags=[*shared, "marketing", "experiments", "ab-test", "metrics"],
            rating=5,
            body="""ES:
Disena un experimento A/B para esta hipotesis. Entrega:
1) Hipotesis y criterio de exito (metrica primaria + guardrails)
2) Variantes (A vs B) con cambios exactos
3) Segmentacion y supuestos
4) Duracion estimada y consideraciones de muestra (sin calculos exactos si faltan datos)
5) Plan de analisis (que mirar, como decidir)
6) Riesgos y como mitigarlos

Hipotesis/Contexto:
{context}

EN:
Design an A/B experiment for this hypothesis. Deliver:
1) Hypothesis and success criteria (primary metric + guardrails)
2) Variants (A vs B) with exact changes
3) Targeting and assumptions
4) Estimated duration and sample considerations (no exact math if data is missing)
5) Analysis plan (what to look at, decision rule)
6) Risks and mitigations

Hypothesis/Context:
{context}""",
        ),
        PromptCreate(
            title="Meeting agenda + decisions / Agenda + decisiones de reunion",
            category="Productivity",
            tags=[*shared, "productivity", "meetings", "decisions", "notes"],
            rating=4,
            body="""ES:
Prepara una agenda de reunion orientada a decisiones. Devuelve:
1) Objetivo (una frase)
2) Decisiones a tomar (max 3)
3) Agenda con tiempos (30-45 min por defecto)
4) Pre-reads y datos necesarios
5) Preguntas para desbloquear
6) Template de acta: decisiones, acciones, owner, fecha

Tema/Contexto:
{context}

EN:
Prepare a decision-oriented meeting agenda. Return:
1) Goal (one sentence)
2) Decisions to make (max 3)
3) Timed agenda (default 30-45 min)
4) Pre-reads and required data
5) Unblocking questions
6) Minutes template: decisions, actions, owner, due date

Topic/Context:
{context}""",
        ),
        PromptCreate(
            title="Agent sandbox constraints / Restricciones de sandbox para agentes",
            category="Agents",
            tags=[*shared, "agents", "safety", "sandbox", "permissions"],
            rating=5,
            body="""ES:
Define restricciones de sandbox para un agente que usa herramientas. Incluye:
1) Politica por defecto (deny/allow)
2) Archivos: lecturas/escrituras permitidas y prohibidas
3) Red: cuando se permite y como registrar dominios
4) Operaciones peligrosas: deletes masivos, push, prod, pagos
5) Registro (audit log) y redaccion de datos sensibles
Devuelve una version corta (para prompt) y una larga (para docs).

Contexto:
{context}

EN:
Define sandbox constraints for a tool-using agent. Include:
1) Default policy (deny/allow)
2) Filesystem: allowed/prohibited reads and writes
3) Network: when allowed and how to log domains
4) Dangerous ops: mass deletes, push, prod, payments
5) Audit log and sensitive-data redaction
Return a short version (for prompts) and a long version (for docs).

Context:
{context}""",
        ),
        PromptCreate(
            title="Tool-call plan / Plan de llamadas a herramientas",
            category="Agents",
            tags=[*shared, "agents", "tools", "planning", "verification"],
            rating=5,
            body="""ES:
Antes de usar herramientas, crea un plan de ejecucion minimo. Devuelve:
1) Objetivo y definicion de hecho (done)
2) Riesgos (seguridad/privacidad/coste) y mitigaciones
3) Lista de comandos/llamadas a herramientas (ordenadas) con proposito
4) Señales de exito/fallo por paso
5) Que no vas a hacer (out of scope)
Reglas: no ejecutes nada hasta que el plan sea aprobado.

Tarea/Contexto:
{context}

EN:
Before using tools, create a minimal execution plan. Return:
1) Goal and definition of done
2) Risks (security/privacy/cost) and mitigations
3) Ordered tool calls/commands with purpose
4) Success/failure signals per step
5) Explicit out-of-scope items
Rules: do not execute anything until the plan is approved.

Task/Context:
{context}""",
        ),
        PromptCreate(
            title="Claude JSON contract / Contrato JSON para Claude",
            category="Prompts for Claude",
            tags=[*shared, "claude", "json", "structure", "prompting"],
            rating=5,
            body="""ES:
Responde SOLO con JSON valido (sin markdown). Usa este esquema:
{
  \"summary\": \"...\",
  \"assumptions\": [\"...\"],
  \"steps\": [{\"name\": \"...\", \"details\": \"...\"}],
  \"risks\": [{\"risk\": \"...\", \"mitigation\": \"...\"}]
}
Reglas: no incluyas texto fuera del JSON; si falta informacion, ponla en assumptions.

Tarea/Contexto:
{context}

EN:
Reply with VALID JSON only (no markdown). Use this schema:
{
  \"summary\": \"...\",
  \"assumptions\": [\"...\"],
  \"steps\": [{\"name\": \"...\", \"details\": \"...\"}],
  \"risks\": [{\"risk\": \"...\", \"mitigation\": \"...\"}]
}
Rules: no text outside JSON; if info is missing, put it in assumptions.

Task/Context:
{context}""",
        ),
        PromptCreate(
            title="ChatGPT study plan / Plan de estudio ChatGPT",
            category="Prompts for ChatGPT",
            tags=[*shared, "chatgpt", "learning", "plan", "practice"],
            rating=4,
            body="""ES:
Actua como tutor. Construye un plan de estudio en 2 semanas. Incluye:
1) Objetivo medible
2) Modulos diarios (30-60 min) con recursos sugeridos (tipos, no links)
3) Ejercicios practicos y criterios de correccion
4) Mini-proyecto final con rubric
5) Como adaptar si tengo menos tiempo
Reglas: prioriza practica; pregunta por nivel inicial.

Tema/Contexto:
{context}

EN:
Act as a tutor. Build a 2-week study plan. Include:
1) Measurable goal
2) Daily modules (30-60 min) with suggested resource types (no links required)
3) Practice exercises with grading criteria
4) Final mini-project with rubric
5) How to adapt if I have less time
Rules: prioritize practice; ask about starting level.

Topic/Context:
{context}""",
        ),
        PromptCreate(
            title="Codex repo-safe refactor / Refactor seguro para Codex",
            category="Prompts for Codex",
            tags=[*shared, "codex", "refactor", "safety", "tests", "minimal-diff"],
            rating=5,
            favorite=True,
            body="""ES:
Actua como Codex y haz un refactor seguro con diff minimo. Reglas:
1) No cambies comportamiento (salvo bugfix solicitado)
2) Mantén commits pequenos (si aplica) y cambios localizados
3) Actualiza tests si es estrictamente necesario
4) Ejecuta lint/format/tests y reporta resultados
5) Si hay riesgo, propone alternativa mas simple
Salida:
- Intencion del refactor
- Plan de pasos
- Cambios realizados (archivos)
- Verificacion (comandos)

Tarea/Contexto:
{context}

EN:
Act as Codex and perform a repo-safe refactor with minimal diff. Rules:
1) Do not change behavior (except requested bugfix)
2) Keep changes small and localized
3) Update tests only if strictly necessary
4) Run lint/format/tests and report results
5) If risky, propose a simpler alternative
Output:
- Refactor intent
- Step plan
- Changes made (files)
- Verification (commands)

Task/Context:
{context}""",
        ),
        PromptCreate(
            title="Bug report template / Plantilla de reporte de bug",
            category="Debugging",
            tags=[*shared, "debugging", "bug-report", "template", "repro"],
            rating=5,
            body="""ES:
Convierte esta informacion en un reporte de bug accionable. Incluye:
1) Resumen (una frase)
2) Entorno (OS, version, flags)
3) Pasos para reproducir (numerados)
4) Resultado esperado vs actual
5) Impacto/severidad
6) Adjuntos (logs, capturas) y redaccion de PII
7) Sugerencia de causa raiz (si hay evidencia)
Reglas: si faltan datos, lista preguntas concretas.

Info/Contexto:
{context}

EN:
Turn this into an actionable bug report. Include:
1) Summary (one sentence)
2) Environment (OS, version, flags)
3) Steps to reproduce (numbered)
4) Expected vs actual
5) Impact/severity
6) Attachments (logs, screenshots) with PII redaction
7) Root-cause guess (only if evidence exists)
Rules: if data is missing, ask concrete questions.

Info/Context:
{context}""",
        ),
        PromptCreate(
            title="Architecture diagram narrator / Narrador de diagrama de arquitectura",
            category="Architecture",
            tags=[*shared, "architecture", "diagram", "documentation", "systems"],
            rating=4,
            body="""ES:
Describe este diagrama (o descripcion) como si fuera documentacion. Entrega:
1) Componentes y responsabilidades
2) Flujos principales (paso a paso)
3) Limites y contratos (APIs, eventos, schemas)
4) Fallos y degradacion (timeouts, retries, colas)
5) Observabilidad (logs, metricas, trazas) y SLOs sugeridos
Reglas: si no hay suficiente detalle, explicita supuestos.

Diagrama/Contexto:
{context}

EN:
Turn this diagram (or description) into documentation. Deliver:
1) Components and responsibilities
2) Key flows (step-by-step)
3) Boundaries and contracts (APIs, events, schemas)
4) Failure modes and degradation (timeouts, retries, queues)
5) Observability (logs, metrics, traces) and suggested SLOs
Rules: if detail is missing, label assumptions.

Diagram/Context:
{context}""",
        ),
        PromptCreate(
            title="Design critique scorecard / Scorecard de critica de diseno",
            category="Design",
            tags=[*shared, "design", "critique", "rubric", "usability"],
            rating=5,
            body="""ES:
Evalua este diseño con una rubrica. Incluye criterios:
- Jerarquia visual
- Legibilidad/contraste
- Consistencia de componentes
- Accesibilidad (teclado, focus, aria)
- Estados (loading, error, empty)
- Responsividad
Devuelve: puntuaciones 1-5 + recomendaciones concretas + quick wins.
Reglas: no inventes requisitos; pregunta por target y constraints.

Diseño/Contexto:
{context}

EN:
Evaluate this design with a rubric. Include criteria:
- Visual hierarchy
- Readability/contrast
- Component consistency
- Accessibility (keyboard, focus, aria)
- States (loading, error, empty)
- Responsiveness
Return: 1-5 scores + concrete recommendations + quick wins.
Rules: do not invent requirements; ask about audience and constraints.

Design/Context:
{context}""",
        ),
        PromptCreate(
            title="Competitive analysis matrix / Matriz de analisis competitivo",
            category="Research",
            tags=[*shared, "research", "marketing", "competitive", "positioning"],
            rating=4,
            body="""ES:
Construye una tabla de analisis competitivo. Columnas sugeridas:
- Producto
- Para quien
- Propuesta de valor
- Diferenciadores
- Debilidades
- Pricing (si se conoce)
- Evidencia (fuente/resumen)
Luego entrega: 3 oportunidades de posicionamiento + 3 riesgos.
Reglas: marca que es suposicion vs evidencia; no alucines features.

Contexto:
{context}

EN:
Build a competitive analysis table. Suggested columns:
- Product
- Target user
- Value proposition
- Differentiators
- Weaknesses
- Pricing (if known)
- Evidence (source/summary)
Then deliver: 3 positioning opportunities + 3 risks.
Rules: label assumptions vs evidence; do not hallucinate features.

Context:
{context}""",
        ),
        PromptCreate(
            title="Docs-as-code rewrite / Reescritura docs-as-code",
            category="Productivity",
            tags=[*shared, "productivity", "docs", "writing", "maintenance"],
            rating=4,
            body="""ES:
Reescribe esta documentacion para un repo (docs-as-code). Entrega:
1) Version revisada (estructura clara: que es, como usar, ejemplos, troubleshooting)
2) Lista de cambios (max 10) y por que
3) Secciones faltantes
4) Propuesta de tabla de contenidos
Reglas: no inventes comandos/flags; si faltan, pregunta.

Docs/Contexto:
{context}

EN:
Rewrite this documentation for a repo (docs-as-code). Deliver:
1) Revised version (clear structure: what it is, how to use, examples, troubleshooting)
2) Change list (max 10) and why
3) Missing sections
4) Proposed table of contents
Rules: do not invent commands/flags; ask if missing.

Docs/Context:
{context}""",
        ),
        PromptCreate(
            title="Triage to tasks / Triaje a tareas",
            category="Productivity",
            tags=[*shared, "productivity", "triage", "planning", "backlog"],
            rating=5,
            body="""ES:
Convierte este input (feedback/bugs/ideas) en tareas accionables. Devuelve:
1) Lista de items con titulo, descripcion, criterio de hecho, estimacion (S/M/L)
2) Priorizacion (impacto x esfuerzo) con razon
3) Dependencias y riesgos
4) Lo que queda fuera de alcance por ahora
Reglas: evita tareas vagas; cada item debe ser verificable.

Input/Contexto:
{context}

EN:
Turn this input (feedback/bugs/ideas) into actionable tasks. Return:
1) Items with title, description, definition of done, estimate (S/M/L)
2) Prioritization (impact x effort) with rationale
3) Dependencies and risks
4) Explicit out-of-scope for now
Rules: avoid vague tasks; every item must be verifiable.

Input/Context:
{context}""",
        ),
        PromptCreate(
            title="One-page PRD / PRD de una pagina",
            category="Productivity",
            tags=[*shared, "productivity", "prd", "writing", "product"],
            rating=5,
            body="""ES:
Escribe un PRD de 1 pagina para esta idea. Incluye:
- Problema y para quien
- Objetivos (3 max) y no-objetivos
- Alcance (MVP) y fases futuras
- Historias de usuario (5 max) con criterios de aceptacion
- Riesgos, dependencias, metricas (como sabremos que funciona)
Reglas: evita jergas; si faltan datos, enumera preguntas.

Idea/Contexto:
{context}

EN:
Write a one-page PRD for this idea. Include:
- Problem and target users
- Goals (max 3) and non-goals
- Scope (MVP) and future phases
- User stories (max 5) with acceptance criteria
- Risks, dependencies, metrics (how we’ll know it works)
Rules: avoid jargon; if data is missing, list questions.

Idea/Context:
{context}""",
        ),
        PromptCreate(
            title="Threat model lite / Modelo de amenazas ligero",
            category="Architecture",
            tags=[*shared, "architecture", "security", "threat-model", "privacy"],
            rating=5,
            body="""ES:
Haz un threat model ligero para este sistema. Devuelve:
1) Activos a proteger (datos, secretos, disponibilidad)
2) Superficies de ataque (entradas, integraciones, permisos)
3) 5 amenazas principales (STRIDE opcional) con impacto/probabilidad
4) Mitigaciones concretas y prioridad (P0/P1/P2)
5) Preguntas abiertas y supuestos
Reglas: no inventes componentes; etiqueta suposiciones vs evidencia.

Sistema/Contexto:
{context}

EN:
Do a lightweight threat model for this system. Return:
1) Assets to protect (data, secrets, availability)
2) Attack surfaces (inputs, integrations, permissions)
3) Top 5 threats (STRIDE optional) with impact/likelihood
4) Concrete mitigations and priority (P0/P1/P2)
5) Open questions and assumptions
Rules: don’t invent components; label assumptions vs evidence.

System/Context:
{context}""",
        ),
        PromptCreate(
            title="API contract from examples / Contrato API desde ejemplos",
            category="Architecture",
            tags=[*shared, "architecture", "api", "contract", "examples"],
            rating=4,
            body="""ES:
Dado este set de ejemplos de request/response, deriva un contrato API consistente:
- Endpoints, metodos, rutas
- Esquemas (campos, tipos, opcionales, enums)
- Codigos de estado y errores (formato estandar)
- Reglas de validacion y limites
- 3 ejemplos por endpoint (feliz + 2 errores)
Reglas: mantente fiel a los ejemplos; si hay conflicto, propon opciones.

Ejemplos:
{context}

EN:
Given these request/response examples, derive a consistent API contract:
- Endpoints, methods, routes
- Schemas (fields, types, optionality, enums)
- Status codes and errors (standard format)
- Validation rules and limits
- 3 examples per endpoint (happy + 2 error cases)
Rules: stay faithful to the examples; if conflicts exist, propose options.

Examples:
{context}""",
        ),
        PromptCreate(
            title="Log triage to hypotheses / Triaje de logs a hipotesis",
            category="Debugging",
            tags=[*shared, "debugging", "logs", "hypotheses", "triage"],
            rating=5,
            body="""ES:
Analiza estos logs y produce:
1) Resumen del fallo (1-2 frases)
2) Timeline de eventos (bullet list)
3) 3 hipotesis ordenadas por probabilidad con evidencia (lineas de log)
4) 5 checks o experimentos para confirmar/refutar (comandos si aplica)
5) Propuesta de fix minimo y prueba de regresion
Reglas: no asumas infraestructura; marca incertidumbre.

Logs/Contexto:
{context}

EN:
Analyze these logs and produce:
1) Failure summary (1-2 sentences)
2) Event timeline (bullets)
3) 3 hypotheses ordered by likelihood with evidence (log lines)
4) 5 checks/experiments to confirm/refute (commands if applicable)
5) Minimal fix proposal and a regression test idea
Rules: don’t assume infrastructure; mark uncertainty.

Logs/Context:
{context}""",
        ),
        PromptCreate(
            title="Unit test selection / Seleccion de pruebas unitarias",
            category="Coding",
            tags=[*shared, "coding", "tests", "unit-tests", "coverage"],
            rating=4,
            body="""ES:
Para este cambio, decide que pruebas unitarias agregar o actualizar. Devuelve:
- Riesgos principales del cambio (3 max)
- Casos de prueba propuestos (tabla: nombre, objetivo, inputs, asserts)
- Que NO probar (y por que)
- Estrategia para mocks/stubs (minimo necesario)
Reglas: prioriza tests deterministas y rapidos; evita over-mocking.

Cambio/Contexto:
{context}

EN:
For this change, decide which unit tests to add or update. Return:
- Main change risks (max 3)
- Proposed test cases (table: name, goal, inputs, asserts)
- What NOT to test (and why)
- Mock/stub strategy (minimum needed)
Rules: prioritize deterministic fast tests; avoid over-mocking.

Change/Context:
{context}""",
        ),
        PromptCreate(
            title="SQL query explainer / Explicador de consulta SQL",
            category="Coding",
            tags=[*shared, "coding", "sql", "performance", "explain"],
            rating=4,
            body="""ES:
Explica esta consulta SQL para una persona tecnica:
1) Que hace (alto nivel)
2) Tabla por tabla: joins, filtros, agregaciones
3) Posibles problemas (N+1, cardinalidad, indices, funciones no sargables)
4) 2 alternativas: (a) mas legible (b) mas eficiente
5) Si aplica: indices sugeridos y por que
Reglas: no inventes esquema; pide columnas faltantes.

SQL/Contexto:
{context}

EN:
Explain this SQL query for a technical reader:
1) What it does (high level)
2) Table by table: joins, filters, aggregations
3) Potential issues (cardinality, indexes, non-sargable functions)
4) Two alternatives: (a) more readable (b) more efficient
5) If applicable: suggested indexes and why
Rules: don’t invent schema; ask for missing columns.

SQL/Context:
{context}""",
        ),
        PromptCreate(
            title="Accessibility QA checklist / Checklist QA de accesibilidad",
            category="Design",
            tags=[*shared, "design", "a11y", "qa", "checklist"],
            rating=5,
            body="""ES:
Haz una revision de accesibilidad para esta UI. Devuelve:
- Problemas por severidad (P0/P1/P2) con evidencia
- Recomendacion concreta (texto exacto, aria-labels, roles, focus)
- Checks de teclado (tab order, focus visible, traps)
- Contraste y tamanos (si hay datos)
- Lista de pruebas manuales (10 max)
Reglas: no inventes colores/HTML; pide capturas o markup si falta.

UI/Contexto:
{context}

EN:
Do an accessibility review for this UI. Return:
- Issues by severity (P0/P1/P2) with evidence
- Concrete recommendations (exact copy, aria-labels, roles, focus)
- Keyboard checks (tab order, focus visible, traps)
- Contrast and sizing (if data provided)
- Manual test list (max 10)
Rules: don’t invent colors/HTML; ask for screenshots/markup if missing.

UI/Context:
{context}""",
        ),
        PromptCreate(
            title="Design token audit / Auditoria de design tokens",
            category="Design",
            tags=[*shared, "design", "design-system", "tokens", "consistency"],
            rating=4,
            body="""ES:
Audita estos estilos/components para detectar inconsistencias de tokens. Entrega:
1) Lista de tokens implicitos (espaciado, tipografia, color, radius)
2) Duplicados y valores cercanos (con propuesta de consolidacion)
3) Reglas de nomenclatura recomendadas
4) Plan de migracion por etapas (bajo riesgo)
Reglas: no inventes sistema; deriva de lo que veas.

Estilos/Contexto:
{context}

EN:
Audit these styles/components for token inconsistencies. Deliver:
1) Implicit tokens (spacing, typography, color, radius)
2) Duplicates and near-values (with consolidation proposal)
3) Recommended naming rules
4) Low-risk staged migration plan
Rules: don’t invent a system; derive from what you see.

Styles/Context:
{context}""",
        ),
        PromptCreate(
            title="Landing page outline / Esquema de landing page",
            category="Marketing",
            tags=[*shared, "marketing", "landing-page", "copywriting", "positioning"],
            rating=5,
            body="""ES:
Escribe un esquema de landing page para este producto. Devuelve:
- Headline + subheadline (3 variantes)
- Secciones (orden recomendado) con bullets de copy
- Propuesta de CTA (2 opciones) y objeciones que responde
- FAQs (6) enfocadas a conversion
- Lista de claims que requieren prueba/metricas
Reglas: no inventes certificaciones o clientes; mantenlo veraz.

Producto/Contexto:
{context}

EN:
Write a landing page outline for this product. Return:
- Headline + subheadline (3 variants)
- Sections (recommended order) with copy bullets
- CTA proposal (2 options) and objections they address
- FAQs (6) focused on conversion
- Claims that require proof/metrics
Rules: don’t invent certifications or customers; keep it truthful.

Product/Context:
{context}""",
        ),
        PromptCreate(
            title="SEO keyword clustering / Cluster de keywords SEO",
            category="Marketing",
            tags=[*shared, "marketing", "seo", "keywords", "research"],
            rating=4,
            body="""ES:
Agrupa estas keywords en clusters por intencion y tema. Entrega:
1) Tabla: cluster, keywords, intencion (informacional/comercial/transaccional), dificultad estimada (baja/media/alta)
2) Propuesta de paginas (slug + titulo) por cluster
3) Internal linking sugerido (hub/spoke)
4) Prioridad (impacto x esfuerzo) y por que
Reglas: si faltan datos, asume lo minimo y marca suposiciones.

Keywords/Contexto:
{context}

EN:
Cluster these keywords by intent and theme. Deliver:
1) Table: cluster, keywords, intent (informational/commercial/transactional), estimated difficulty (low/med/high)
2) Suggested pages (slug + title) per cluster
3) Suggested internal linking (hub/spoke)
4) Priority (impact x effort) and why
Rules: if data is missing, assume minimally and label assumptions.

Keywords/Context:
{context}""",
        ),
        PromptCreate(
            title="Competitive teardown / Desmontaje competitivo",
            category="Research",
            tags=[*shared, "research", "competitive", "teardown", "analysis"],
            rating=4,
            body="""ES:
Haz un teardown competitivo a partir de esta info (links, notas, capturas). Devuelve:
- Propuesta de valor y posicionamiento (en 1 frase)
- ICP/personas y jobs-to-be-done inferidos (marca inferencias)
- Features clave (tabla) y diferenciadores
- Pricing/packaging (si hay datos) y riesgos
- Oportunidades para nosotros (top 5) con hipotesis testables
Reglas: no inventes datos; cita lo observado vs inferido.

Info/Contexto:
{context}

EN:
Do a competitive teardown based on this info (links, notes, screenshots). Return:
- Value prop and positioning (1 sentence)
- Inferred ICP/personas and jobs-to-be-done (label inferences)
- Key features (table) and differentiators
- Pricing/packaging (if present) and risks
- Opportunities for us (top 5) with testable hypotheses
Rules: don’t invent data; separate observed vs inferred.

Info/Context:
{context}""",
        ),
        PromptCreate(
            title="Literature scan memo / Memo de escaneo bibliografico",
            category="Research",
            tags=[*shared, "research", "literature", "memo", "sources"],
            rating=4,
            body="""ES:
Con estas fuentes o notas, redacta un memo de investigacion:
1) Pregunta de investigacion y definiciones
2) Hallazgos principales (con citas a fuente)
3) Lo que NO sabemos aun (gaps)
4) Implicaciones practicas / decisiones que habilita
5) Proximos pasos (3) para validar
Reglas: no inventes citas; si no hay fuente, dilo.

Fuentes/Notas:
{context}

EN:
Using these sources or notes, write a research memo:
1) Research question and definitions
2) Key findings (with source citations)
3) What we still don’t know (gaps)
4) Practical implications / decisions it enables
5) Next steps (3) to validate
Rules: don’t invent citations; if a source isn’t provided, say so.

Sources/Notes:
{context}""",
        ),
        PromptCreate(
            title="Agent tool spec / Especificacion de herramientas del agente",
            category="Agents",
            tags=[*shared, "agents", "tools", "interfaces", "reliability"],
            rating=5,
            body="""ES:
Define el contrato de herramientas para un agente. Devuelve:
- Lista de herramientas (nombre, inputs, outputs, errores)
- Reglas de uso (cuando llamar, cuando NO llamar)
- Politicas de seguridad (redaccion de secretos, limites)
- Estrategia de retries/timeouts
- 5 casos de prueba (inputs -> outputs esperados)
Reglas: el contrato debe ser JSON-friendly y verificable.

Contexto:
{context}

EN:
Define a tool contract for an agent. Return:
- Tool list (name, inputs, outputs, errors)
- Usage rules (when to call, when NOT to call)
- Safety policies (secret redaction, limits)
- Retry/timeout strategy
- 5 test cases (inputs -> expected outputs)
Rules: contract must be JSON-friendly and verifiable.

Context:
{context}""",
        ),
        PromptCreate(
            title="Checkpointed execution plan / Plan de ejecucion con checkpoints",
            category="Agents",
            tags=[*shared, "agents", "planning", "checkpoints", "verification"],
            rating=4,
            body="""ES:
Convierte este objetivo en un plan de ejecucion con checkpoints. Incluye:
1) 5-8 pasos max, ordenados por dependencia
2) Para cada paso: criterio de exito verificable (comando o evidencia)
3) Riesgos y mitigaciones por paso
4) Que hacer si un paso falla (fallback)
Reglas: cada checkpoint debe poder verificarse sin suposiciones.

Objetivo/Contexto:
{context}

EN:
Turn this goal into an execution plan with checkpoints. Include:
1) 5-8 steps max, dependency-ordered
2) For each step: verifiable success criteria (command or evidence)
3) Risks and mitigations per step
4) What to do if a step fails (fallback)
Rules: each checkpoint must be verifiable without assumptions.

Goal/Context:
{context}""",
        ),
        PromptCreate(
            title="Tone & style adapter / Adaptador de tono y estilo",
            category="Prompts",
            tags=[*shared, "prompts", "writing", "tone", "style"],
            rating=4,
            body="""ES:
Reescribe este texto manteniendo el significado, pero adaptando el tono y estilo segun estas instrucciones. Devuelve:
1) Version reescrita
2) Lista breve de cambios (5 max)
Reglas: no cambies hechos, numeros o nombres propios; preserva estructura si se pide.

Instrucciones de tono:
{context}

Texto:
{text}

EN:
Rewrite this text preserving meaning, but adapting tone and style per instructions. Return:
1) Rewritten version
2) Brief change list (max 5)
Rules: do not change facts, numbers, or proper nouns; preserve structure if requested.

Tone instructions:
{context}

Text:
{text}""",
        ),
        PromptCreate(
            title="Prompt eval rubric / Rubrica de evaluacion de prompts",
            category="Prompts",
            tags=[*shared, "prompts", "evaluation", "rubric", "quality"],
            rating=4,
            body="""ES:
Crea una rubrica para evaluar este prompt. Devuelve:
- Criterios (claridad, contexto, restricciones, formato, seguridad, verificabilidad)
- Escala 1-5 por criterio con descripcion
- 3 fallos comunes y como detectarlos
- Version mejorada del prompt siguiendo la rubrica
Reglas: mantente general; evita afirmar \"mejores practicas actuales\" sin evidencia.

Prompt a evaluar:
{context}

EN:
Create a rubric to evaluate this prompt. Return:
- Criteria (clarity, context, constraints, format, safety, verifiability)
- 1-5 scale per criterion with descriptions
- 3 common failure modes and how to spot them
- Improved prompt version following the rubric
Rules: keep it general; avoid claiming “current best practices” without evidence.

Prompt to evaluate:
{context}""",
        ),
        PromptCreate(
            title="ChatGPT strict JSON output / Salida JSON estricta ChatGPT",
            category="Prompts for ChatGPT",
            tags=[*shared, "chatgpt", "json", "schema", "format"],
            rating=4,
            body="""ES:
Responde SOLO con JSON valido segun este esquema. No incluyas markdown ni texto extra.
Si falta informacion para completar un campo, usa null y agrega un array \"questions\" con lo que necesitas.

Esquema JSON:
{schema}

Tarea/Contexto:
{context}

EN:
Respond ONLY with valid JSON according to this schema. Do not include markdown or extra text.
If information is missing for a field, use null and add a \"questions\" array with what you need.

JSON schema:
{schema}

Task/Context:
{context}""",
        ),
        PromptCreate(
            title="Claude disagreement protocol / Protocolo de desacuerdo Claude",
            category="Prompts for Claude",
            tags=[*shared, "claude", "reasoning", "safety", "disagreement"],
            rating=4,
            body="""ES:
Si detectas que el usuario esta pidiendo algo incorrecto o peligroso, discrepa con claridad y educacion. Estructura:
1) Lo que entendiste (1 frase)
2) Por que puede estar mal/riesgoso (evidencia o principio)
3) Alternativa segura y util (pasos concretos)
4) Pregunta final para ajustar
Reglas: no humilles; no inventes politicas; se directo.

Solicitud/Contexto:
{context}

EN:
If you detect the user is asking for something incorrect or unsafe, disagree clearly and politely. Structure:
1) What you understood (1 sentence)
2) Why it may be wrong/risky (evidence or principle)
3) A safe, useful alternative (concrete steps)
4) A final question to adjust
Rules: don’t shame; don’t invent policies; be direct.

Request/Context:
{context}""",
        ),
        PromptCreate(
            title="Codex verification gate / Puerta de verificacion para Codex",
            category="Prompts for Codex",
            tags=[*shared, "codex", "verification", "tests", "ci"],
            rating=5,
            body="""ES:
Antes de decir \"listo\", ejecuta verificaciones adecuadas al repo. Devuelve:
- Comandos corridos y resultados
- Cambios realizados (archivos tocados)
- Riesgos restantes y como mitigarlos
Reglas: no afirmes que algo pasa si no lo ejecutaste; si no puedes ejecutar, explica por que.

Tarea/Contexto:
{context}

EN:
Before saying “done”, run repo-appropriate verification. Return:
- Commands run and results
- Changes made (touched files)
- Remaining risks and how to mitigate them
Rules: don’t claim something passes if you didn’t run it; if you can’t run, explain why.

Task/Context:
{context}""",
        ),
        PromptCreate(
            title="Meeting notes to decisions / Notas de reunion a decisiones",
            category="Productivity",
            tags=[*shared, "productivity", "meeting", "decisions", "alignment"],
            rating=4,
            body="""ES:
Convierte estas notas de reunion en un resumen accionable:
1) Decisiones tomadas (bullet)
2) Acciones con responsable y fecha (si existe)
3) Preguntas abiertas
4) Riesgos/bloqueos
5) Proximo sync recomendado (agenda breve)
Reglas: no inventes responsables ni fechas; si faltan, marca como TBD.

Notas:
{context}

EN:
Turn these meeting notes into an actionable summary:
1) Decisions made (bullets)
2) Action items with owner and date (if present)
3) Open questions
4) Risks/blockers
5) Recommended next sync (short agenda)
Rules: don’t invent owners or dates; if missing, mark TBD.

Notes:
{context}""",
        ),
        PromptCreate(
            title="PR review comment responder / Responder comentarios de PR",
            category="Coding",
            tags=[*shared, "coding", "review", "pr", "communication"],
            rating=4,
            body="""ES:
Ayudame a responder estos comentarios de una PR y a planificar cambios minimos:
1) Resumen del feedback (por tema)
2) Respuestas propuestas (amables, claras, con compromisos concretos)
3) Lista de cambios (archivo y riesgo) y orden sugerido
4) Si hay desacuerdo, propone una alternativa con trade-offs
Reglas: no prometas tiempos; no inventes decisiones; pregunta si falta contexto.

Comentarios:
{context}

EN:
Help me respond to these PR review comments and plan minimal changes:
1) Feedback summary (grouped by theme)
2) Proposed replies (polite, clear, with concrete commitments)
3) Change list (file and risk) with suggested order
4) If you disagree, propose an alternative with trade-offs
Rules: don't promise timelines; don't invent decisions; ask if context is missing.

Comments:
{context}""",
        ),
        PromptCreate(
            title="Changelog entry writer / Escritor de entrada de changelog",
            category="Productivity",
            tags=[*shared, "release", "changelog", "writing", "summary"],
            rating=4,
            body="""ES:
Escribe una entrada de changelog a partir de estos cambios. Devuelve:
- Titulo corto (<= 60 chars)
- 3-6 bullets orientados a usuario (no a implementacion)
- Nota de compatibilidad/ruptura si aplica
- Nota de migracion si aplica
Reglas: no inventes features; si hay incertidumbre, marca como "por confirmar".

Cambios:
{context}

EN:
Write a changelog entry from these changes. Return:
- Short title (<= 60 chars)
- 3-6 user-facing bullets (not implementation details)
- Compatibility/breaking note if applicable
- Migration note if applicable
Rules: don't invent features; if uncertain, mark "needs confirmation".

Changes:
{context}""",
        ),
        PromptCreate(
            title="README quickstart generator / Generador de quickstart README",
            category="Productivity",
            tags=[*shared, "docs", "readme", "quickstart", "onboarding"],
            rating=4,
            body="""ES:
Genera una seccion "Quickstart" para el README segun este repo. Incluye:
1) Requisitos
2) Instalacion
3) Comandos tipicos (dev/test/lint)
4) Ejemplo minimo de uso
5) Problemas comunes (2-3) y soluciones
Reglas: usa comandos reales encontrados en el repo; si no puedes verificarlos, pide confirmacion.

Contexto del repo:
{context}

EN:
Generate a README "Quickstart" section for this repo. Include:
1) Prereqs
2) Installation
3) Typical commands (dev/test/lint)
4) Minimal usage example
5) Common issues (2-3) and fixes
Rules: use commands you can find in the repo; if you can't verify, ask for confirmation.

Repo context:
{context}""",
        ),
        PromptCreate(
            title="API rate limit policy / Politica de rate limiting API",
            category="Architecture",
            tags=[*shared, "api", "architecture", "rate-limit", "security"],
            rating=5,
            body="""ES:
Disena una politica de rate limiting para esta API. Devuelve:
- Objetivos (seguridad, coste, UX)
- Limites propuestos (por usuario/IP/token/endpoint) con numeros iniciales
- Respuesta cuando se excede (codigo, headers, mensaje)
- Excepciones (admins, health checks) y riesgos
- Plan de rollout y observabilidad (metricas, alertas)
Reglas: asume que los numeros son un punto de partida y deben ajustarse con datos.

API/Contexto:
{context}

EN:
Design a rate limiting policy for this API. Return:
- Goals (security, cost, UX)
- Proposed limits (per user/IP/token/endpoint) with initial numbers
- Exceeded behavior (status code, headers, message)
- Exceptions (admins, health checks) and risks
- Rollout + observability plan (metrics, alerts)
Rules: treat numbers as starting points to tune with data.

API/Context:
{context}""",
        ),
        PromptCreate(
            title="Error budget policy draft / Borrador de politica de error budget",
            category="Architecture",
            tags=[*shared, "reliability", "sre", "error-budget", "slis"],
            rating=5,
            body="""ES:
Redacta una politica de error budget para este servicio. Incluye:
1) SLI(s) y como se miden
2) SLO(s) y ventana temporal
3) Como se calcula el budget y umbrales (verde/amarillo/rojo)
4) Acciones por estado (feature freeze, focus en fiabilidad, excepciones)
5) Gobernanza: quien decide excepciones y como se documentan
Reglas: mantenlo accionable; evita jerga innecesaria.

Servicio/Contexto:
{context}

EN:
Draft an error budget policy for this service. Include:
1) SLI(s) and how they're measured
2) SLO(s) and time window
3) Budget calculation + thresholds (green/yellow/red)
4) Actions per state (feature freeze, reliability focus, exceptions)
5) Governance: who approves exceptions and how they're documented
Rules: keep it actionable; avoid unnecessary jargon.

Service/Context:
{context}""",
        ),
        PromptCreate(
            title="Observability instrumentation plan / Plan de instrumentacion de observabilidad",
            category="Debugging",
            tags=[*shared, "observability", "logging", "metrics", "tracing"],
            rating=5,
            body="""ES:
Crea un plan para instrumentar este sistema para diagnosticar problemas. Devuelve:
- Metricas clave (latencia, errores, colas, recursos) con nombres sugeridos
- Logs: eventos, campos obligatorios, niveles, redaccion de PII
- Traces: spans principales y atributos
- Dashboards y alertas iniciales
- Estrategia de muestreo y coste
Reglas: no incluyas datos sensibles; propone campos anonimizados/hashes si hace falta.

Sistema/Contexto:
{context}

EN:
Create a plan to instrument this system for debugging. Return:
- Key metrics (latency, errors, queues, resources) with suggested names
- Logs: events, required fields, levels, PII redaction
- Traces: main spans and attributes
- Initial dashboards and alerts
- Sampling + cost strategy
Rules: avoid sensitive data; suggest anonymized fields/hashes when needed.

System/Context:
{context}""",
        ),
        PromptCreate(
            title="Test pyramid alignment / Alineacion con piramide de pruebas",
            category="Debugging",
            tags=[*shared, "testing", "quality", "strategy", "ci"],
            rating=4,
            body="""ES:
Evalua nuestra estrategia de pruebas con respecto a la piramide (unit/integration/e2e). Devuelve:
1) Diagnostico (donde estamos desbalanceados)
2) Riesgos (flakiness, coste, cobertura real)
3) 5 cambios concretos para mejorar (con prioridad)
4) Reglas practicas: que probar en cada nivel
Reglas: adapta recomendaciones al stack y restricciones del repo.

Repositorio/Contexto:
{context}

EN:
Evaluate our test strategy against the test pyramid (unit/integration/e2e). Return:
1) Diagnosis (where we're imbalanced)
2) Risks (flakiness, cost, true coverage)
3) 5 concrete improvements (prioritized)
4) Practical rules: what to test at each level
Rules: tailor recommendations to the repo's stack and constraints.

Repo/Context:
{context}""",
        ),
        PromptCreate(
            title="Deterministic output checklist / Checklist de salida determinista",
            category="Prompts",
            tags=[*shared, "prompts", "determinism", "format", "quality"],
            rating=4,
            body="""ES:
Convierte esta tarea en una salida lo mas determinista posible. Devuelve:
- Variables de entrada (con valores por defecto)
- Reglas de formato (titulos, listas, orden)
- Prohibiciones (lo que NO debe aparecer)
- Criterios de validacion (checks que el usuario puede hacer)
- Un ejemplo de salida con datos ficticios
Reglas: evita pedir "creatividad"; prioriza estructura y verificabilidad.

Tarea/Contexto:
{context}

EN:
Turn this task into the most deterministic output possible. Return:
- Input variables (with defaults)
- Formatting rules (headings, lists, ordering)
- Prohibitions (what must NOT appear)
- Validation criteria (checks the user can run)
- One sample output with dummy data
Rules: avoid asking for "creativity"; prioritize structure and verifiability.

Task/Context:
{context}""",
        ),
        PromptCreate(
            title="Model-agnostic prompt template / Plantilla de prompt agnostica",
            category="Prompts",
            tags=[*shared, "prompts", "template", "model-agnostic", "structure"],
            rating=4,
            body="""ES:
Escribe un prompt agnostico al modelo para esta tarea. Devuelve:
<objetivo>...</objetivo>
<contexto>...</contexto>
<restricciones>...</restricciones>
<salida>...</salida>
<criterios>...</criterios>
Incluye placeholders {variables} y un ejemplo corto de uso.
Reglas: no menciones modelos ni marcas; enfocate en instrucciones verificables.

Tarea/Contexto:
{context}

EN:
Write a model-agnostic prompt template for this task. Return:
<goal>...</goal>
<context>...</context>
<constraints>...</constraints>
<output>...</output>
<criteria>...</criteria>
Include {placeholders} and a short usage example.
Rules: do not mention models or brands; focus on verifiable instructions.

Task/Context:
{context}""",
        ),
        PromptCreate(
            title="Risk register builder / Constructor de registro de riesgos",
            category="Productivity",
            tags=[*shared, "risk", "planning", "mitigation", "project"],
            rating=4,
            body="""ES:
Crea un registro de riesgos para este proyecto. Devuelve una tabla con:
- Riesgo
- Probabilidad (baja/media/alta)
- Impacto (bajo/medio/alto)
- Senales tempranas
- Mitigacion preventiva
- Plan de contingencia
- Owner (si se conoce, si no "TBD")
Reglas: no inventes owners; manten 8-12 riesgos max.

Proyecto/Contexto:
{context}

EN:
Create a risk register for this project. Return a table with:
- Risk
- Likelihood (low/med/high)
- Impact (low/med/high)
- Early signals
- Preventive mitigation
- Contingency plan
- Owner (if known, else "TBD")
Rules: don't invent owners; keep to 8-12 risks max.

Project/Context:
{context}""",
        ),
        PromptCreate(
            title="Stakeholder update memo / Memo de estado a stakeholders",
            category="Productivity",
            tags=[*shared, "communication", "status", "stakeholders", "writing"],
            rating=4,
            body="""ES:
Redacta un update semanal para stakeholders. Secciones:
1) Resumen (3 bullets max)
2) Progreso (hechos concretos)
3) Bloqueos/riesgos (con mitigacion)
4) Proximos pasos (1-2 semanas)
5) Decisiones necesarias (si aplica)
Reglas: evita jerga tecnica; no inventes fechas/metricas.

Contexto:
{context}

EN:
Draft a weekly stakeholder update. Sections:
1) Summary (max 3 bullets)
2) Progress (concrete facts)
3) Blockers/risks (with mitigation)
4) Next steps (1-2 weeks)
5) Decisions needed (if any)
Rules: avoid technical jargon; don't invent dates/metrics.

Context:
{context}""",
        ),
        PromptCreate(
            title="UX microcopy for empty states / Microcopy UX para estados vacios",
            category="Design",
            tags=[*shared, "ux", "microcopy", "empty-state", "product"],
            rating=4,
            body="""ES:
Escribe microcopy para estos estados vacios y errores. Para cada estado devuelve:
- Titulo (<= 40 chars)
- Mensaje (1-2 frases)
- CTA principal y secundario
- Nota de accesibilidad (si aplica)
Reglas: tono humano; no culpes al usuario; evita promesas legales.

Estados:
{context}

EN:
Write microcopy for these empty and error states. For each state return:
- Title (<= 40 chars)
- Message (1-2 sentences)
- Primary and secondary CTA
- Accessibility note (if relevant)
Rules: human tone; don't blame the user; avoid legal promises.

States:
{context}""",
        ),
        PromptCreate(
            title="Figma handoff checklist / Checklist de handoff de Figma",
            category="Design",
            tags=[*shared, "design", "figma", "handoff", "frontend"],
            rating=4,
            body="""ES:
Crea un checklist de handoff de Figma a implementacion. Incluye:
- Tokens (colores, tipografia, espaciado)
- Estados (hover/focus/disabled/loading/empty/error)
- Responsive/breakpoints
- Accesibilidad (contraste, focus, labels)
- Assets (iconos, ilustraciones) y formatos
- Analitica/eventos (si aplica)
Reglas: que sea accionable para devs; max 20 items.

Pantalla/Contexto:
{context}

EN:
Create a Figma-to-implementation handoff checklist. Include:
- Tokens (colors, type, spacing)
- States (hover/focus/disabled/loading/empty/error)
- Responsive/breakpoints
- Accessibility (contrast, focus, labels)
- Assets (icons, illustrations) and formats
- Analytics/events (if applicable)
Rules: make it actionable for devs; max 20 items.

Screen/Context:
{context}""",
        ),
        PromptCreate(
            title="Competitive positioning statement / Declaracion de posicionamiento competitivo",
            category="Marketing",
            tags=[*shared, "marketing", "positioning", "competitive", "strategy"],
            rating=4,
            body="""ES:
Escribe un posicionamiento claro usando este formato:
- Para (audiencia)
- Que necesita (problema)
- Nuestro producto (categoria)
- Ofrece (beneficio clave)
- A diferencia de (alternativas)
- Porque (pruebas)
Luego genera 3 variantes mas cortas (tweet, tagline, H1).
Reglas: no inventes pruebas; marca [necesita dato] donde falte evidencia.

Contexto:
{context}

EN:
Write a clear positioning statement using:
- For (audience)
- Who needs (problem)
- Our product (category)
- Provides (key benefit)
- Unlike (alternatives)
- Because (proof)
Then generate 3 shorter variants (tweet, tagline, H1).
Rules: don't invent proof; mark [needs data] when evidence is missing.

Context:
{context}""",
        ),
        PromptCreate(
            title="Content brief for blog post / Brief de contenido para post",
            category="Marketing",
            tags=[*shared, "content", "marketing", "seo", "writing"],
            rating=4,
            body="""ES:
Crea un brief SEO para un post de blog. Devuelve:
- Publico objetivo y nivel
- Intencion de busqueda
- Outline H2/H3
- Puntos clave y ejemplos
- FAQ (5)
- Call to action
- Palabras clave secundarias (10)
Reglas: no inventes datos; si necesitas fuentes, pide cuales usar.

Tema/Contexto:
{context}

EN:
Create an SEO content brief for a blog post. Return:
- Target audience and level
- Search intent
- H2/H3 outline
- Key points and examples
- FAQ (5)
- Call to action
- Secondary keywords (10)
Rules: don't invent data; if you need sources, ask which to use.

Topic/Context:
{context}""",
        ),
        PromptCreate(
            title="Customer interview guide / Guia de entrevista a clientes",
            category="Research",
            tags=[*shared, "research", "interviews", "product", "discovery"],
            rating=5,
            body="""ES:
Genera una guia de entrevista para entender el problema del usuario. Devuelve:
- Objetivo (1-2 frases)
- Preguntas (10-12) abiertas, ordenadas por fase (contexto, comportamiento, dolor, alternativas)
- 3 preguntas de profundizacion ("por que", "cuentame mas")
- Red flags de sesgo (cosas a evitar)
- Plantilla de notas (secciones)
Reglas: no pidas datos personales; no hagas preguntas que sugieran la respuesta.

Producto/Contexto:
{context}

EN:
Generate an interview guide to understand the user's problem. Return:
- Goal (1-2 sentences)
- Questions (10-12) open-ended, ordered by phase (context, behavior, pain, alternatives)
- 3 follow-up probes ("why", "tell me more")
- Bias red flags (things to avoid)
- Notes template (sections)
Rules: don't ask for personal data; avoid leading questions.

Product/Context:
{context}""",
        ),
        PromptCreate(
            title="Research question to search queries / Pregunta de investigacion a queries",
            category="Research",
            tags=[*shared, "research", "search", "queries", "literature"],
            rating=4,
            body="""ES:
Convierte esta pregunta de investigacion en un set de queries de busqueda. Devuelve:
- 10 queries (Google/Scholar) con sinonimos y operadores
- 5 terminos excluidos (NOT) para filtrar ruido
- 3 estrategias de ampliacion (snowballing, citas, autores)
- Criterios de inclusion/exclusion
Reglas: evita terminos de marca si no son esenciales; prioriza reproducibilidad.

Pregunta:
{context}

EN:
Turn this research question into a set of search queries. Return:
- 10 queries (Google/Scholar) with synonyms and operators
- 5 excluded terms (NOT) to filter noise
- 3 expansion strategies (snowballing, citations, authors)
- Inclusion/exclusion criteria
Rules: avoid brand terms unless essential; prioritize reproducibility.

Question:
{context}""",
        ),
        PromptCreate(
            title="Agent termination criteria / Criterios de parada del agente",
            category="Agents",
            tags=[*shared, "agents", "guardrails", "stopping", "quality"],
            rating=4,
            body="""ES:
Define criterios claros para que un agente se detenga o pida ayuda. Devuelve:
- Condiciones de "done" (verificables)
- Condiciones de "blocked" (que informacion falta)
- Presupuesto (tiempo/iteraciones) y cuando abortar
- Checks antes de terminar (tests, lint, sanity)
- Mensaje final estandar (resumen + riesgos + siguientes pasos)
Reglas: evita bucles infinitos; exige evidencia antes de afirmar exito.

Tarea/Contexto:
{context}

EN:
Define clear criteria for an agent to stop or ask for help. Return:
- "Done" conditions (verifiable)
- "Blocked" conditions (what info is missing)
- Budget (time/iterations) and when to abort
- Pre-finish checks (tests, lint, sanity)
- Standard final message (summary + risks + next steps)
Rules: avoid infinite loops; require evidence before claiming success.

Task/Context:
{context}""",
        ),
        PromptCreate(
            title="Prompt red-teaming / Red-teaming de prompt",
            category="Prompts",
            tags=[*shared, "prompts", "safety", "evaluation", "adversarial"],
            rating=5,
            body="""ES:
Haz red-teaming de este prompt: encuentra ambiguedades, fallos previsibles y vectores de abuso. Devuelve:
1) 8 ataques/edge-cases (input malicioso o confuso)
2) Para cada uno: por que falla, severidad y mitigacion (cambio minimo al prompt)
3) Version endurecida del prompt
Reglas: no generes contenido ilegal; enfocate en mejorar instrucciones y limites.

Prompt:
{context}

EN:
Red-team this prompt: find ambiguities, likely failure modes, and abuse vectors. Return:
1) 8 attacks/edge-cases (malicious or confusing inputs)
2) For each: why it fails, severity, and mitigation (minimal prompt change)
3) Hardened prompt version
Rules: do not generate illegal content; focus on strengthening instructions and boundaries.

Prompt:
{context}""",
        ),
        PromptCreate(
            title="ChatGPT tool-use decision tree / Arbol de decision de uso de tools ChatGPT",
            category="Prompts for ChatGPT",
            tags=[*shared, "chatgpt", "tools", "decision", "workflow"],
            rating=4,
            body="""ES:
Crea un arbol de decision para decidir si usar herramientas externas o responder sin ellas. Devuelve:
- 6-10 reglas tipo "si/entonces" (verificables)
- Ejemplos de cuando SI usar tool (con justificacion)
- Ejemplos de cuando NO usar tool
- Formato de respuesta cuando se usa tool (pasos + resultado)
Reglas: se conservador con datos cambiantes; si hay riesgo de estar desactualizado, recomienda verificar.

Tarea/Contexto:
{context}

EN:
Create a decision tree for when to use external tools vs answer directly. Return:
- 6-10 "if/then" rules (verifiable)
- Examples of when to use a tool (with justification)
- Examples of when NOT to use a tool
- Response format when a tool is used (steps + result)
Rules: be conservative with time-sensitive facts; if there's a risk of being outdated, recommend verification.

Task/Context:
{context}""",
        ),
    ]
