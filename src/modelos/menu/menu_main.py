import os
from src.modelos.modelo_google import ModeloGoogle
from src.modelos.modelo_groq import ModeloGroq
from src.modelos.prompt_01 import Prompt01
from src.modelos.prompt_02 import Prompt02

class MenuPrincipal():
    def __init__(self):
        self.opcion = 0

    def pausa():
        input("Presiona enter para volver al menú")

    def mostrar_menu(self):
        print("=== Menú Principal ===")
        print("1. Modelo Google API KEY")
        print("2. Modelo Groq API KEY")
        print("3. Modelo Local")
        print("4. Promp básico")
        print("5. Prompt avanzado")
        print("0. Salir\n")

    def ejecutar_opcion(self):
        while True:
            self.mostrar_menu()
            self.opcion = input("Seleccione una opción: ")

            if self.opcion == "1":
                modelo_google = ModeloGoogle()
                prompt = input("\nIngrese su prompt: ")
                respuesta = modelo_google.generar_respuesta(prompt)
                os.system("cls")
                print("Respuesta del modelo Google:\n")
                print("-"*30)
                print(respuesta)
                print("-"*30)
                print("")

            elif self.opcion == "2":
                modelo_groq = ModeloGroq()
                prompt = input("\nIngrese su prompt: ")
                respuesta = modelo_groq.generar_respuesta(prompt)
                os.system("cls")
                print("Respuesta del modelo Groq:\n")
                print("-"*30)
                print(respuesta)
                print("-"*30)
                print("")

            elif self.opcion == "3":
                from src.modelos.modelo_local import ModeloLocal
                modelo_local = ModeloLocal()
                prompt = input("\nIngrese su prompt: ")
                respuesta = modelo_local.generar_respuesta(prompt)
                os.system("cls")
                print("Respuesta del modelo Local:\n")
                print("-"*30)
                print(respuesta)
                print("-"*30)
                print("")

            elif self.opcion == "4":
                prompt01 = Prompt01()
                respuesta = prompt01.generar_respuesta("hola como andas? yo ando buen buggy")
                os.system("cls")
                print("Respuesta del prompt básico:\n")
                print("-"*30)
                print(respuesta)
                print("-"*30)
                print("")

            elif self.opcion == "5":
                prompt02 = Prompt02()
                respuesta = prompt02.generar_respuestas()
                os.system("cls")
                print("Respuesta del prompt avanzado:\n")
                print("-"*30)
                print(respuesta)
                print("-"*30)
                print("")

            elif self.opcion == "0":
                print("Saliendo del programa...")
                break 

            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")