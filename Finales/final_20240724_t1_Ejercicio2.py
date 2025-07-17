# Se cuenta con un archivo csv con las lecturas de profundidad del Rio de la Plata. Implementar una función
# que reciba la ruta al archivo y el tipo de marea y retorne el promedio de profundidad.
# Tener en cuenta que el archivo tiene encabezado y no hay que procesarlo. Puede que algunas profundidades no sean
# numéricas, en ese caso se saltea y se imprime por pantalla un mensaje descriptivo con la fecha, la hora y la
# profundidad.

def profundidad_promedio(ruta_archivo, marea):
    acum = 0.0
    cont = 0
    try:
        archivo = open(ruta_archivo, 'r')
        profundidades = archivo.readlines()
        for index in range(1, len(profundidades)):
            muestra = profundidades[index].rstrip().split(',')
            if muestra[5] == marea:
                try:
                    acum += float(muestra[4])
                    cont += 1
                except:
                    print('Error en archivo: Fecha: {} Hora: {} Profundidad: {}.'.format(
                        muestra[0], muestra[1], muestra[4]))
    except FileNotFoundError:
        print('Error en la ruta del archivo.')
    return acum / cont


print('Profundidad promedio:', profundidad_promedio('profundidad.csv', 'alta'))
