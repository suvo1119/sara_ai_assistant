import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ No GOOGLE_API_KEY found.")
    exit()

print(f"🔑 checking models for key: {api_key[:5]}...")
genai.configure(api_key=api_key)

try:
    print("Fetched models:")
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"- {m.name}")
except Exception as e:
    print(f"❌ Error fetching models: {e}")
