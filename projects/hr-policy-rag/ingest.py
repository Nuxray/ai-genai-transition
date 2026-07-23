from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import sys
sys.path.append('../..')

# Load the policy document
loader = TextLoader(r"D:\Trainning\ai-genai-transition\projects\hr-policy-rag/data/hr_policy.txt")
documents = loader.load()

# Chunk it
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100,
    separators=["\n\n", "\n1", "\n2", "\n3", "\n4", "\n5", "\n6", "\n7", "\n8", "\n9", "\n", " "]
)

chunks = text_splitter.split_documents(documents)
print(f"Split into {len(chunks)} chunks")

# Embed + store (free, local, no API key needed)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"
)
vectorstore.persist()
print("Vector store built and saved to ./chroma_db")