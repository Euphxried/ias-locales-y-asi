from langchain_ollama import ChatOllama
from langchain_core.messages import (SystemMessage,HumanMessage)
class ModeloConMemoria:
    def __init__(self):
        self.modelo = ChatOllama(model="qwen2.5:3b",
                                temperature=0.1)
        self.historial = [
            SystemMessage(
            content="Eres un asistente que responde en español."
        )]
    def generar_respuesta(self):
        while True:
            pregunta = input("\nUsuario: ")
            if pregunta.lower() == "salir":
                break
            self.historial.append(HumanMessage(content=pregunta))
            respuesta = self.modelo.invoke(self.historial)
            print("IA:", respuesta.content)
            self.historial.append(respuesta)