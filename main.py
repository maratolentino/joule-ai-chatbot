import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google import genai
from google.genai import types

app = FastAPI(title="Joule AI - Conversational Assistant")

# CORS setup para makakonekta ang inyong HTML interface
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ang API key ay kinukuha mula sa environment variable, HINDI direktang isinusulat dito.
# Gumawa ng ".env" file (o i-set ang env var sa terminal) na may laman na:
#   GEMINI_API_KEY=your_actual_key_here
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise RuntimeError("Missing GEMINI_API_KEY environment variable. Set it before running the server.")
client = genai.Client(api_key=GEMINI_API_KEY)

class ChatInput(BaseModel):
    message: str

JOULE_GUARDRAIL = """
You are Joule AI, an expert household energy-saving assistant for Filipino families. 
Your strict rule is to answer questions ONLY if they are related to electricity, electrical appliances, household power consumption, energy efficiency, solar panels, electricity bills (like Meralco), or electrical safety.

CRITICAL POLICY:
If the user asks about anything unrelated to electricity (e.g., cooking recipes, history, programming, math, pop culture, creative writing, or general chat), you must strictly but politely decline to answer. Respond in Taglish or Filipino.

Example Response for invalid queries:
"Paumanhin, ngunit ang Joule AI ay idinisenyo lamang upang sumagot sa mga usapin at tanong na may kinalaman sa kuryente at pagtitipid ng enerhiya."
"""

@app.post("/api/chat")
async def chat_with_joule(input_data: ChatInput):
    try:
        # Tawagin ang Gemini 1.5 Flash (Libre at may Guardrails)
        response = client.models.generate_content(
            model='gemini-flash-latest',
            contents=input_data.message,
            config=types.GenerateContentConfig(
                system_instruction=JOULE_GUARDRAIL,
                temperature=0.2,
            )
        )
        return {"response": response.text}
    except Exception as e:
        # I-print ang buong error sa Render logs para makita natin ang totoong dahilan
        print(f"ERROR sa /api/chat: {type(e).__name__}: {e}")
        error_text = str(e).lower()
        if "resource_exhausted" in error_text or "429" in error_text or "quota" in error_text:
            raise HTTPException(status_code=429, detail="Rate limit ng Gemini API ang naabot. Sandaling maghintay bago magtanong ulit.")
        raise HTTPException(status_code=500, detail=str(e))
