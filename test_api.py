import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Test API key
api_key = os.getenv('GOOGLE_API_KEY')
print(f"API Key found: {'Yes' if api_key else 'No'}")

try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("Hello!")
    print("API Test successful!")
    print("Response:", response.text)
except Exception as e:
    print(f"API Error: {str(e)}") 
