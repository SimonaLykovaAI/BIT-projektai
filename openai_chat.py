import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

# 1️⃣ Įkeliame .env failą
load_dotenv(dotenv_path=find_dotenv(), override=True)

# 2️⃣ Paimame GitHub tokeną iš .env
token = os.getenv("GITHUB_TOKEN")
if not token:
    raise RuntimeError("Neradau GITHUB_TOKEN. Patikrink .env failą!")

# 3️⃣ Nustatome modelio adresą ir pavadinimą
endpoint = "https://models.inference.ai.azure.com"
model = "gpt-4.1-nano"

# 4️⃣ Sukuriame OpenAI klientą
client = OpenAI(base_url=endpoint, api_key=token)

# 5️⃣ Sukuriame paprastą užklausą
response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ],
    temperature=1.0,
    top_p=1.0
)

# 6️⃣ Atspausdiname atsakymą
print(response.choices[0].message.content)