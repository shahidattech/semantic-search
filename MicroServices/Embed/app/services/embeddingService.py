from sentence_transformers import SentenceTransformer
import torch
import faiss
import numpy as np
import os
import logging
import argparse
from app.services.pdfExtractionService import extract_text_from_pdf

def create_embedding_pdf(user_id: str, tenant_id:str, skill_id:int, pdf_path):
    try:
        text_from_pdf = extract_text_from_pdf(pdf_path)
        sentences = text_from_pdf.split('\n')  # Split text into sentences
        device='cuda' if torch.cuda.is_available() else 'cpu'
        model = SentenceTransformer('all-MiniLM-L6-v2', device=device)
        print(model.get_sentence_embedding_dimension())
        embeddings = model.encode(sentences, convert_to_numpy=True)
        # Normalize the vectors for cosine similarity
        embeddings /= np.linalg.norm(embeddings, axis=1, keepdims=True)
        index = faiss.IndexFlatIP(embeddings.shape[1])  # Inner Product (cosine similarity)
        index.add(embeddings)
        FOLDER_BASE = os.getenv("FOLDER_BASE", "") if os.getenv("FOLDER_BASE", "") else "/"
        EMBED_BASE = os.getenv("EMBED_BASE", "") if os.getenv("EMBED_BASE", "") else "/"
        INDEX_BASE = f"{FOLDER_BASE}/{EMBED_BASE}/{str(tenant_id)}/{str(user_id)}/"
        if not os.path.exists(INDEX_BASE):
            os.makedirs(INDEX_BASE)
        faiss.write_index(index,  f"{INDEX_BASE}/index-{str(skill_id)}")
    except Exception as Err:
        logging.error("Error in Embedding ::create_embedding_pdf ====" + str(Err))
        raise Err

if __name__ == "__main__":
    parser = argparse.ArgumentParser("skill_id")
    parser.add_argument("skill_id", help="skill_id", type=str)
    args = parser.parse_args()
    print("args", args)
    # create_embedding_pdf()

