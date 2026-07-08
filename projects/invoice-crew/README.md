# Finance Invoice Processing Crew

Multi-agent CrewAI system that extracts, validates, and routes invoice data.
Built with CrewAI + Ollama (local LLM) for zero-cost prototyping.

## Status: In progress (Week 3-4)

## Setup
poetry install
poetry config virtualenvs.in-project true
poetry init --name invoice-crew --python "^3.11" -n
poetry add crewai crewai-tools
poetry run python agent_test.py
