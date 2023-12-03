import re
import os

def generar_tabla_contenidos():
    ruta_script = os.path.dirname(os.path.abspath(__file__))
    ruta_readme = os.path.join(ruta_script, "README.md")

    with open(ruta_readme, 'r', encoding='utf-8') as file:
        content = file.read()

    pattern = re.compile(r'^(#{1,3})\s+(.+?)(?:\s+#|$)', re.MULTILINE)
    headings = pattern.findall(content)

    if headings:
        print("Tabla de Contenidos:")
        for level, title in headings:
            indent = '  ' * (len(level) - 1)
            link = '-'.join(title.lower().split())
            print(f"{indent}- [{title}](#{link})")

if __name__ == "__main__":
    generar_tabla_contenidos()