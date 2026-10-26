import os
from src.modelos.modelo_google import ModeloGoogle
from src.modelos.modelo_groq import ModeloGroq

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

            elif self.opcion == "0":
                print("Saliendo del programa...")
                break 

            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")