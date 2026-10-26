from dotenv import load_dotenv

# Carga las variables del archivo .env antes de ejecutar el menú
load_dotenv()
from src.modelos.menu.menu_main import MenuPrincipal
def main():
    menu = MenuPrincipal()
    menu.ejecutar_opcion()

if __name__=="__main__":
    main()