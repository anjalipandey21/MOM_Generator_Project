from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
from datetime import datetime
from dotenv import load_dotenv

# ✅ Load environment variables from .env file
load_dotenv()

# ✅ Get Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ✅ Gemini 2.0 Flash model endpoint
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

# ✅ Initialize FastAPI app
app = FastAPI()

# ✅ Setup CORS to allow frontend interaction
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Define request schema
class RAGInput(BaseModel):
    text: str

# ✅ Main endpoint
@app.post("/generate-mom")
async def generate_mom(rag_input: RAGInput):
    try:
        print(f"[{datetime.now()}] Received RAG Input:")
        print(rag_input.text)
        print("-" * 50)

        # ✅ Polished prompt with formatting instructions
        prompt = f"""
You are a highly professional executive assistant specializing in generating clear, formal, and structured Minutes of Meeting (MOM) documents.

Given the following raw notes from a meeting, generate a polished and attractive MOM with these sections:

- Meeting Title (Create if missing)
- Date (Assume today's date if missing)
- Meeting Participants
- Agenda Topics
- Detailed Discussion Points
- Key Decisions Made
- Action Items and Responsible Owners
- Next Meeting Date (State "To be decided" if missing)

Formatting Requirements:
- Use bold section headings.
- Use bullet points for lists.
- Professional tone and structure.
- Reasonable assumptions if missing details.

Raw Meeting Notes:
\"\"\"
{rag_input.text}
\"\"\"
"""

        # ✅ Build API request
        payload = {
            "contents": [
                {
                    "parts": [{"text": prompt}]
                }
            ]
        }

        response = requests.post(GEMINI_API_URL, json=payload)
        response.raise_for_status()
        gemini_response = response.json()

        mom_output = gemini_response["candidates"][0]["content"]["parts"][0]["text"]

        print(f"[{datetime.now()}] Generated MOM:")
        print(mom_output)
        print("=" * 80)

        return {"mom": mom_output}

    except Exception as e:
        print(f"[{datetime.now()}] Error: {e}")
        return {"mom": None, "error": str(e)}
