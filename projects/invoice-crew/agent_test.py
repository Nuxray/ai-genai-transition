from crewai import Agent, Task, Crew, LLM

# Point CrewAI at your local Ollama model
llm = LLM(
    model="ollama/llama3.1:8b",
    base_url="http://localhost:11434"
)

extractor = Agent(
    role="Invoice Data Extractor",
    goal="Extract structured fields from invoice text",
    backstory="An expert in parsing financial documents accurately.",
    llm=llm,
    verbose=True
)

extract_task = Task(
    description=(
        "Extract the following fields from this invoice text as JSON: "
        "vendor_name, invoice_number, amount, due_date.\n\n"
        "Invoice text: 'Invoice #INV-2091 from Acme Supplies Ltd, "
        "amount due $4,250.00, payable by 2026-08-15.'"
    ),
    expected_output="A JSON object with vendor_name, invoice_number, amount, due_date",
    agent=extractor
)

crew = Crew(agents=[extractor], tasks=[extract_task], verbose=True)
result = crew.kickoff()
print(result)