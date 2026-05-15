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
    ]
