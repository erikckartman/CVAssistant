from unittest import result
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()

API_URL = "https://api.groq.com/openai/v1/chat/completions"
API_KEY = os.getenv("API_KEY")

def extract_text_from_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        
        for script in soup(["script", "style"]):
            script.extract()
        
        text = soup.get_text()
        return text
    
    except Exception as e:
        print(f"Error fetching URL: {e}")
        return ""

def analyze_cv(cv_text, job_text):
    prompt = f"""
You are an HR expert.

Analyze this CV and job description.

Return:
1. Match score (0-100)
2. Missing skills
3. Suggestions

CV:
{cv_text}

Job:
{job_text}
"""

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(API_URL, headers=headers, json=data)

    return response.json()["choices"][0]["message"]["content"]
    """result = response.json()
    print(result)
    return result"""