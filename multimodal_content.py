import os
from dotenv import load_dotenv
from google import genai

# Cargar variables de entorno desde el archivo .env (si existe)
load_dotenv()

api_key = os.getenv("API_KEY")

# Inicializar el cliente con la API key tomada desde el .env
client = genai.Client(api_key=api_key)

# Generamos la descripción con una pregunta específica
response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=[
        {
            "role": "user",
            "parts": [
                {"text": "Describe lo que ves en la imagen en español."},
                {"inline_data": {
                    "mime_type": "image/jpg",  
                    "data": open("C:/Users/IPF-2025/Desktop/google-api/galope-del-caballo.jpg", "rb").read()
                }}
            ]
        }
    ]
)

print(response.text)
