from flask import Flask, request, jsonify, session
from flask_cors import CORS
import sqlite3
import os
from flask_session import Session  # ✅ Add this
from similarity import extract_text_from_pdf, calculate_similarity, generate_similarity_report


app = Flask(__name__)
app.secret_key = 'your_secret_key_here'


CORS(app, supports_credentials=True)  # ✅ Allow frontend to send cookies

HARDCODED_USERNAME = "admin"
HARDCODED_PASSWORD = "password"

def get_db_connection():
    conn = sqlite3.connect("plagiarism.db")
    conn.row_factory = sqlite3.Row
    return conn

def check_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']

    if username == HARDCODED_USERNAME and password == HARDCODED_PASSWORD:
        session['logged_in'] = True
        session['username'] = username
        return jsonify({"success": True, "message": "Login successful"}), 200
    elif check_user(username, password):
        session['logged_in'] = True
        session['username'] = username
        return jsonify({"success": True, "message": "Login successful"}), 200
    else:
        return jsonify({"success": False, "message": "Invalid credentials"}), 401

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure the upload folder exists

@app.route("/upload", methods=["POST"])
def upload_files():
    uploaded_files = request.files.getlist("files")
    file_names = []
    extracted_texts = []

    for file in uploaded_files:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        file_names.append(file.filename)

        text = extract_text_from_pdf(file_path)
        extracted_texts.append(text)

    # Calculate similarity
    similarity_matrix = calculate_similarity(extracted_texts)

    # Generate report
    return generate_similarity_report(file_names, similarity_matrix)


@app.route('/logout')
def logout():
    session.clear()
    return jsonify({"message": "Logged out successfully"}), 200

if __name__ == '__main__':
    if not os.path.exists("uploads"):
        os.makedirs("uploads")
    app.run(debug=True)
