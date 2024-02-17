import sys
from os import system

def borrar_pantalla():
    if sys.platform == "linux" or sys.platform == "darwin":
        system("clear")
    else:
        system("cls")

def pausar_pantalla():
    if sys.platform == "linux" or sys.platform == "darwin":
        input('Enter para continuar....')
    else:
        system("pause")