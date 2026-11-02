from langchain_ollama import ChatOllama

class ModeloSinMemoria:
    def __init__(self):
        self.modelo = ChatOllama(model="qwen2.5:3b",
                                temperature=0.1)

    def generar_respuesta(self):
        respuesta1 = self.modelo.invoke("Mi nombre es Axel Chávez")
        print("Respuesta de la primera pregunta:\n")
        print(respuesta1.text)
        print("-"*30)
        respuesta2 = self.modelo.invoke("Cuál es mi nombre?")
        print("Respuesta de la segunda pregunta:\n")
        print(respuesta2.text)
        print("-"*30)