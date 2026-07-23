from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)

# question1 = ["Can I carry forward my sick leave to next year?","Is there a limit to the number of vacation days I can take in a year?","Are there any restrictions on taking leave during peak business periods?","Can I take unpaid leave if I have exhausted my paid leave?","What is the process for requesting a leave of absence for personal reasons?","Are there any specific guidelines for taking maternity or paternity leave?","Can I take leave for attending a family member's wedding or funeral?","Is there a policy regarding taking leave for volunteering or community service activities?","What is the procedure for requesting a sabbatical or extended leave of absence?"]
questions = ["How many paid leave days do I get per year?",
"What's the company policy on remote work?",
"Can I carry forward my sick leave to next year?",
"My father is a Member of Parliament — can I work for your company? ",
"My friends are asking about company stock status and whether they should buy it?"]



CONFIDENT_THRESHOLD = 1.0
BORDERLINE_THRESHOLD = 1.2

for question in questions:
    print(f"\n=== Question: {question} ===")
    results = vectorstore.similarity_search_with_score(question, k=3)
    best_score = results[0][1]
    
    if best_score > BORDERLINE_THRESHOLD:
        print(f"NO RELEVANT MATCH (best distance {best_score:.4f}) — would refuse to answer.")
    elif best_score > CONFIDENT_THRESHOLD:
        print(f"BORDERLINE MATCH (best distance {best_score:.4f}) — flag as uncertain.")
    else:
        print(f"CONFIDENT MATCH (best distance {best_score:.4f})")
    
    for i, (doc, score) in enumerate(results):
        print(f"  Chunk {i+1} | distance: {score:.4f}")
        print(f"  {doc.page_content[:150]}...")

# SIMILARITY_THRESHOLD = 0.6


# for question in question1:
#     print(f"Question: {question}\n")
#     results = vectorstore.similarity_search_with_score(question, k=3)

#     for i, (doc, score) in enumerate(results):
#         print(f"--- Chunk {i+1} | distance score: {score:.4f} ---")
#         print(doc.page_content[:200], "...\n")
        
# results = vectorstore.similarity_search(question, k=1)

# print(f"Question: {question}\n")
# for i, doc in enumerate(results):
#     print(f"--- Retrieved chunk {i+1} ---")
#     print(doc.page_content)
#     print()