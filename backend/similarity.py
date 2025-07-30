import fitz  # PyMuPDF for extracting text from PDFs
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from flask import jsonify

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text("text") + "\n"
    return text.strip()

def calculate_similarity(texts):
    """Calculates pairwise similarity between multiple documents."""
    vectorizer = TfidfVectorizer().fit_transform(texts)
    similarity_matrix = (vectorizer * vectorizer.T).toarray()
    return similarity_matrix

def generate_similarity_report(file_names, similarity_matrix):
    """Creates a JSON similarity report for all files."""
    report = []
    num_files = len(file_names)
    
    for i in range(num_files):
        for j in range(i + 1, num_files):  # Compare each file with others
            report.append({
                "File 1": file_names[i],
                "File 2": file_names[j],
                "Similarity Score": round(similarity_matrix[i][j], 2)
            })
    
    return jsonify({"similarity_report": report})




