import os

def generar_summary(archivos):
    for archivo in archivos:
        nombre_archivo = os.path.join("/home/sebastiarch/coding/metodologias_de_software/sql_injection_suite/src", archivo)
        with open(nombre_archivo, "r", encoding="utf-8") as archivo_lectura:
            contenido = archivo_lectura.read()
            with open("summary.txt", "a", encoding="utf-8") as archivo_summary:
                archivo_summary.write(f"# {archivo}\n\n{contenido}\n\n")


def main():
    archivos = [
        "buscar_errores_condicionales.py",
        "buscar_respuestas_condicionales.py",
        "consultar_version_mysql_sqlserver.py",
        "consultar_version_oracle.py",
        "listar_contenido_bbdd.py",
        "main.py",
        "menu.py",
        "presentacion.py",
        "recuperar_datos_de_otras_tablas.py",
        "recuperar_datos_ocultos.py",
        "recuperar_multiples_valores_en_una_sola_columna.py",
        "retraso_tiempo.py",
        "saltar_inicio_sesion.py"
    ]

    generar_summary(archivos)
    print("Summary generado en 'summary.txt'.")

if __name__ == "__main__":
    main()