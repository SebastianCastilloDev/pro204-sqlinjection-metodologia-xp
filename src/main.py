import presentacion
import menu

import buscar_errores_condicionales
import buscar_respuestas_condicionales
import consultar_version_mysql_sqlserver
import consultar_version_oracle
import listar_contenido_bbdd
import recuperar_datos_de_otras_tablas
import recuperar_datos_ocultos
import recuperar_multiples_valores_en_una_sola_columna
import retraso_tiempo
import saltar_inicio_sesion

presentacion.inicio()

opcion = menu.menu_de_opciones()
opcion -= 1

if opcion == 0:
    recuperar_datos_ocultos.main()
elif opcion == 1:
    saltar_inicio_sesion.main()
elif opcion == 2:
    consultar_version_oracle.main()
elif opcion == 3:
    consultar_version_mysql_sqlserver.main()
elif opcion == 4:
    listar_contenido_bbdd.main()
elif opcion == 5:
    recuperar_datos_de_otras_tablas.main()
elif opcion == 6:
    recuperar_multiples_valores_en_una_sola_columna.main()
elif opcion == 7:
    buscar_respuestas_condicionales.main()
elif opcion == 8:
    buscar_errores_condicionales.main()
elif opcion == 9:
    retraso_tiempo.main()
