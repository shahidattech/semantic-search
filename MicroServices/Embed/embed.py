import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer
import torch
import faiss
import numpy as np

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()
    doc.close()
    return text

pdf_path = "Ency-Newton.pdf"
text_from_pdf = extract_text_from_pdf(pdf_path)

# Split
sentences = text_from_pdf.split('\n')  # Split text into sentences
print("sen", sentences[:10])
device='cuda' if torch.cuda.is_available() else 'cpu'
model = SentenceTransformer('all-MiniLM-L6-v2', device=device)
print(model.get_sentence_embedding_dimension())
embeddings = model.encode(sentences, convert_to_numpy=True)
# Normalize the vectors for cosine similarity
embeddings /= np.linalg.norm(embeddings, axis=1, keepdims=True)

index = faiss.IndexFlatIP(embeddings.shape[1])  # Inner Product (cosine similarity)

index.add(embeddings)
faiss.write_index(index, "faiss_index")

sample_query = 'English physicist'
query_embedding = model.encode([sample_query], convert_to_numpy=True)[0]

query_embedding /= np.linalg.norm(query_embedding) 

k = 2  # Number of nearest neighbors to retrieve

# Perform a similarity search
loaded_index = faiss.read_index("faiss_index")
distances, indices = loaded_index.search(np.expand_dims(query_embedding, axis=0), k)
print("distances, indices", distances, indices[0])
print("Query=", sample_query)
print("\nNearest Neighbors:")
print([sentences[i] for i in indices[0]])










