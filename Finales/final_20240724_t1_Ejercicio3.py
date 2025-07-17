# El detective privado Mike Ehrmantraut tiene asignada una lista de personas sospechosas a las cuales debe vigilar. Para ello, le
# pide a sus empleados de confianza que cada uno siga a uno de los sospechosos. Al final de la semana, los empleados le mandan
# un archivo CSV que se llama como el sospechoso, y contiene información de cada día, hora y duración de tiempo (en minutos) de
# los momentos en los cuales los perdieron de vista.
#
# Ejemplo: El archivo "jimmy_mcgill.csv" contiene la siguiente información:
# 4_10_2002;10:45;45
# 4_10_2002;22:45;23
# 5_10_2002;09:05;o7
# 5_10_2002;09:05;4E
#
# Cada semana, Mike toma todos los archivos, y arma un diccionario, donde las claves son los nombres de las personas, y los
# valores, la cantidad total de tiempo que se lo perdió de vista (en minutos). Ejemplo: {"jimmy_mcgill":345,
# "kim_wexler":20, ...etc}. Escribir una función que reciba la lista de los nombres de los sospechosos (en formato
# snake_case), y devuelva el diccionario pedido.
#
# Considerar:
# - Tal vez algún archivo de sospechoso no existe. En ese caso, se debe imprimir un mensaje descriptivo del error.
# - Al ser una tarea manual, podría pasar que los empleados de Mike ingresen mal los minutos. En ese caso, se debe ignorar
# la línea en cuestión e imprimir un mensaje descriptivo para avisarle.

def procesar_sospechosos(sospechosos):
    sin_vigilancia = {}
    for sospechoso in sospechosos:
        tiempo = 0
        try:
            archivo = open(sospechoso + '.csv', 'r')
            incidentes = archivo.readlines()
            for incidente in incidentes:
                componentes = incidente.split(';')
                try:
                    tiempo += int(componentes[2])
                except:
                    print('Error en archivo {}, fecha: {} hora: {}.'.format(
                        sospechoso, componentes[0], componentes[1]))
                    sin_vigilancia[sospechoso] = tiempo
        except FileNotFoundError:
            print('El archivo {} no existe.'.format(sospechoso))
    return sin_vigilancia


sospechosos = ['juan_valdez', 'segundo_peralta', 'romualdo_farias']
print(procesar_sospechosos(sospechosos))
