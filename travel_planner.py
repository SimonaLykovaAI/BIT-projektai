import os
import sys
from dotenv import load_dotenv
from google import genai

# Įkraunam API raktus iš .env failo
load_dotenv()

# Gauk API raktą
api_key = os.getenv("GOOGLE_API_KEY")

# Inicijuojam Gemini klientą
client = genai.Client(api_key=api_key)

def plan_trip(destination, days):
    """Sugeneruoja kelionės planą su Gemini AI"""
    prompt = f"Sukurk {days}-dienų kelionės planą į {destination}. " \
             f"Įtrauk lankytinas vietas, vietinį maistą, poilsio ir kultūros rekomendacijas."

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text

# Pagrindinė dalis
if __name__ == "__main__":
    if len(sys.argv) >= 3:
        dest = sys.argv[1]
        days = int(sys.argv[2])
    else:
        dest = input("Kur keliaujam? ")
        days = int(input("Kiek dienų? "))

    print("\n=== Kelionės planas ===\n")
    itinerary = plan_trip(dest, days)
    print(itinerary)