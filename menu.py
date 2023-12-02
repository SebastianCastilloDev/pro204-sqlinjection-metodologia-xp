from colorama import init, Fore, Back
import sys

def menu_de_opciones():
    print(Fore.LIGHTBLUE_EX + "Lista de opciones.\nSeleccione un ataque de la lista:\n")
    lista = [
        ["UNION attack  : Recuperar datos ocultos","https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data"],
        ["UNION attack  : Saltar inicio de sesión","https://portswigger.net/web-security/sql-injection/lab-login-bypass"],
        ["UNION attack  : Consultar tipo y version de base de datos en Oracle","https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-oracle"],
        ["UNION attack  : Consultar tipo y version de base de datos en MySQL y SQL Server","https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-mysql-microsoft"],
        ["UNION attack  : Listar el contenido de la base de datos","https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-non-oracle"],
        ["UNION attack  : Recuperar datos a partir de otras tablas","https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-data-from-other-tables"],
        ["UNION attack  : Recuperar múltiples valores en una sola columna","https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-multiple-values-in-single-column"],
        ["Blind SQL     : Buscar respuestas condicionales","https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses"],
        ["Blind SQL     : Buscar errores condicionales","https://portswigger.net/web-security/sql-injection/blind/lab-conditional-errors"],
        ["Blind SQL     : Inyección SQL con retraso de tiempo","https://portswigger.net/web-security/sql-injection/blind/lab-time-delays-info-retrieval"],
    ]
    
    for i in range(len(lista)):
        print(f"{str(i+1)}. {lista[i][0]}")
    
    print("\nIngrese la opción seleccionada: ", end="")
    opcion = int(input())
    try:
        lista[opcion-1][1]
    except IndexError:
        print("\n" + Fore.RED + "❌ " + "Ha habido un error")
        print(Fore.WHITE + "Terminando la ejecución del programa...")
        sys.exit(-1)
    
    print("\n" + Fore.GREEN + "✔️ " + Fore.BLUE +"Ingrese a la siguiente URL (ctrl + click):\n")
    print(Fore.GREEN + lista[opcion-1][1])
    print(Fore.BLUE + "\nY genere un nuevo laboratorio")
    
    return opcion



if __name__ == "__main__":
    menu_de_opciones()