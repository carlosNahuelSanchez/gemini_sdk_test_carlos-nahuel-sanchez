import os
from dotenv import load_dotenv
from google import genai

# Cargar variables de entorno desde el archivo .env (si existe)
load_dotenv()

api_key = os.getenv("API_KEY")

# Inicializar el cliente con la API key tomada desde el .env
client = genai.Client(api_key=api_key)

response = client.models.generate_content_stream(
    model="gemini-2.5-flash",
    contents="Porque recomiendas aprender Python como primer lenguaje de programación?"   
)

for chunk in response:
    if chunk.text:
        print(chunk.text, end="", flush=True)