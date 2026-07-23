from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaLLM
import json

# --- Setup ---
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
llm = OllamaLLM(model="llama3.1:8b")

CONFIDENT_THRESHOLD = 1.0
BORDERLINE_THRESHOLD = 1.2

SYSTEM_PROMPT_TEMPLATE = """You are an HR policy assistant. You answer employee questions strictly based on the policy excerpts provided below. You do not use any outside knowledge about HR policy, labor law, or common company practices.

Policy excerpts (retrieved as most relevant to the question):
{context}

Rules:
- Answer only using information explicitly present in the excerpts above.
- If the excerpts do not actually answer the question, set "grounded" to false and set "answer" to EXACTLY this text and nothing else: "This isn't covered in the policy document provided. Please check with HR directly."
- When grounded is false, do not include any other information, partial answers, or related policy details in the answer field — even if the excerpts contain other relevant-sounding content.
- Do not combine unrelated excerpts to construct an answer to something not directly addressed.
- When you do answer (grounded: true), briefly note which excerpt you drew from.
- Keep answers concise and factual.

Return your output as JSON:
{{"answer": "", "grounded": true}}

Employee question:
{question}
"""

def answer_question(question: str):
    results = vectorstore.similarity_search_with_score(question, k=3)
    best_score = results[0][1]

    print(f"\n=== {question} ===")
    print(f"Best retrieval distance: {best_score:.4f}")

    # --- Refuse BEFORE calling the LLM if nothing relevant was retrieved ---
    if best_score > BORDERLINE_THRESHOLD:
        print("-> No relevant match. Skipping LLM call.")
        return {"answer": "This isn't covered in the policy document provided. Please check with HR directly.", "grounded": False}

    context = "\n\n".join([doc.page_content for doc, score in results])
    prompt = SYSTEM_PROMPT_TEMPLATE.format(context=context, question=question)

    raw_response = llm.invoke(prompt)
    print(f"-> LLM raw response:\n{raw_response}")
    return raw_response


questions = [
   # "How many paid leave days do I get per year?",
   # "What's the company policy on remote work?",
    "Can I carry forward my sick leave to next year?"
    #"My father is a Member of Parliament — can I work for your company?",
   # "My friends are asking about company stock status and whether they should buy it?"
]

for q in questions:
    answer_question(q)