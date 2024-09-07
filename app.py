from flask import Flask, render_template, request, jsonify
import os
import google.generativeai as genai
from dotenv import load_dotenv
import PyPDF2
from docx import Document
import io

# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)

def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(file):
    doc = Document(file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'resume' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['resume']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file:
        # Read the file content based on its type
        file_extension = os.path.splitext(file.filename)[1].lower()
        
        if file_extension == '.pdf':
            resume_content = extract_text_from_pdf(file)
        elif file_extension in ['.doc', '.docx']:
            resume_content = extract_text_from_docx(file)
        else:
            return jsonify({"error": "Unsupported file type"}), 400
        
        # Analyze the resume using Gemini
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f'''Analyze the following resume for a data science role and provide insights.
        Make sure to rate the quality of projects , relevant workex , skills and notable achievments.
        Give it a resume score out of 100.
        Give insights on how to improve the resume
        :\n\n{resume_content}'''
        
        response = model.generate_content(prompt)
        
        # Render the results template with the full analysis
        return render_template('results.html', analysis=response.text)

if __name__ == '__main__':
    app.run(debug=True)
