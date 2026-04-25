from crewai import Agent, Task, Crew, LLM


OLLAMA_BASE_URL = "http://localhost:11434/v1"
MODEL = "llama3:latest"

llm = LLM(
    model=MODEL,
    provider="openai",
    base_url=OLLAMA_BASE_URL,
    api_key="ollama",
    temperature=0.7,
)

# Definir agentes
designer = Agent(
    role="Game Designer",
    goal="Diseñar mecánicas divertidas para un juego tycoon de tatuajes",
    backstory="Experto en simuladores tipo Game Dev Tycoon y gestión",
    llm=llm,
)

programmer = Agent(
    role="Godot Developer",
    goal="Escribir código en GDScript limpio y funcional",
    backstory="Especialista en desarrollo de juegos en Godot",
    llm=llm,
)

# Crear tareas (diseño -> implementación)
design_task = Task(
    description=(
        "Diseña un sistema básico de clientes para Tattoo Tycoon. "
        "Incluye: tipos de cliente, atributos, cola/espera, satisfacción, presupuesto, rareza de estilos, y eventos."
    ),
    expected_output="Una especificación clara en viñetas (sin código).",
    agent=designer,
)

code_task = Task(
    description=(
        "Con la especificación anterior, escribe un ejemplo mínimo pero funcional en GDScript "
        "para Godot 4: clase `Customer`, generador/Spawner, y un bucle simple de atención con satisfacción."
    ),
    expected_output="Código GDScript para Godot 4, listo para pegar en el editor.",
    agent=programmer,
    context=[design_task],
)

# Crew
crew = Crew(
    agents=[designer, programmer],
    tasks=[design_task, code_task],
    verbose=False,
)

# Ejecutar
result = crew.kickoff()

print("\n" + "=" * 80)
print("DISEÑO (especificación)")
print("=" * 80)
print(result.tasks_output[0].raw if len(result.tasks_output) > 0 else "(sin salida)")

print("\n" + "=" * 80)
print("IMPLEMENTACIÓN (GDScript)")
print("=" * 80)
print(result.tasks_output[1].raw if len(result.tasks_output) > 1 else "(sin salida)")
