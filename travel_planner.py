import os
import sys
from dotenv import load_dotenv
import google.generativeai as genai

# 🔹 Įkeliame API raktą iš .env failo
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# 🔹 Sukuriame funkciją kelionės planui sugeneruoti
def plan_trip(destination, days):
    """Sugeneruoja kelionės planą su Gemini AI"""
    prompt = (
        f"Sukurk {days}-dienų kelionės planą į {destination}. "
        "Įtrauk lankytinas vietas, vietinį maistą, poilsio ir kultūros rekomendacijas."
    )

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

# 🔹 Pagrindinė dalis
if __name__ == "__main__":
    if len(sys.argv) >= 3:
        dest = sys.argv[1]
        days = int(sys.argv[2])
    else:
        dest = input("Kur keliaujam? ")
        days = int(input("Kiek dienų? "))

    print("\n--- Kelionės planas ---\n")
    itinerary = plan_trip(dest, days)
    print(itinerary)