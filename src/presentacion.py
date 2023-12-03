from art import text2art
from colorama import init, Fore, Back

def inicio():
    init()
    titulo = text2art("SQL Injection")
    print(Fore.RED + titulo + Fore.RESET)
    print(Fore.WHITE)
    print("\n\t\t" + Back.RED  + "Una herramienta para realizar SQL Injection" + Fore.RESET + Back.RESET + "\n")

if __name__ == "__main__":
    inicio()