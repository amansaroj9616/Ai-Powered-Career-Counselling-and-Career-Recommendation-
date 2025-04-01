import os
import fitz  # PyMuPDF
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found. Check your .env file.")
genai.configure(api_key=api_key)

def get_gemini_response(input_text, pdf_content, prompt):
    """
    Generates AI response using the Gemini-Pro model.
    """
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([input_text, pdf_content, prompt])
    return response.text

def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from an uploaded PDF file.
    """
    if uploaded_file is not None:
        document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text_parts = [page.get_text() for page in document]
        return " ".join(text_parts)
    raise FileNotFoundError("No file uploaded")
