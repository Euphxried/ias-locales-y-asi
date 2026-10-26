from langchain_ollama import ChatOllama
class Prompt01:
    def __init__(self):
        self.modelo=ChatOllama(model="qwen2.5:3b",temperature=0.8)

    def generar_respuesta(self,prompt):
        respuesta=self.modelo.invoke("hola como andas? yo ando buen buggy")
        return respuesta.text