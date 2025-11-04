# Google AI Studio – naudojimas šiame projekte

## Paskirtis
Šis dokumentas aprašo, kaip projektas naudoja *Google AI Studio (Gemini API)* sugeneruoti kelionės planą pagal nurodytą miestą ir dienų skaičių.

## Failų struktūra
- .env – aplinkos kintamieji su API raktais:
  - GOOGLE_API_KEY – Google AI Studio raktas
  - (pas mane taip pat yra GITHUB_TOKEN ir GEMINI_API_KEY, bet projektui užtenka GOOGLE_API_KEY)
- travel_planner.py – pagrindinis skriptas, kviečiantis Gemini modelį.
- my-models.yml – (nebūtina paleidimui) – AI Toolkit/Gemini nustatymai, jei naudosi per įrankį.

## Bibliotekos
Naudojamos Python bibliotekos:
```bash
pip install -U google-generativeai python-dotenv