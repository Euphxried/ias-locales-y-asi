from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

class ModeloGoogle:
    def __init__(self):
        load_dotenv()
        self.modelo=ChatGoogleGenerativeAI(model="gemini-1.5-flash-002",temperature=0.2)

    def generar_respuesta(self,prompt):
        respuesta=self.modelo.invoke(prompt)
        return respuesta.text

        