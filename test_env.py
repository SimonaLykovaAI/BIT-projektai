from dotenv import load_dotenv
import os

# Įkraunam .env failą
load_dotenv()

# Paimam raktus
github_key = os.getenv("GITHUB_TOKEN")
gemini_key = os.getenv("GEMINI_API_KEY")

# Patikrinam, ar jie gauti
print("GitHub raktas:", "OK" if github_key else "NERASTAS")
print("Gemini raktas:", "OK" if gemini_key else "NERASTAS")