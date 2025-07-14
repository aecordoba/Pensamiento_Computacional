# La profesora Mariana guarda las notas del parcial de Pensamiento Computacional en listas. Tiene una lista con 4 listas dentro:
# una con los nombres, otra con los apellidos, otra con los intentos y otra con las notas. Los intentos pueden ser 1 (si es la primera
# vez que rinde el parcial) o 2 (si está en el recuperatorio). Ejemplo: [[Mariana, Lucía, Laura, Melina], [Juarez,
# Lourengo, Maciel, Retamozo], [1, 1, 2, 1], [4, 8, 9, 6]]
# 
# Al momento de pasar las notas a una planilla para hacer análisis, se da cuenta que no es lo más eficiente, y decide pasarlo a una
# lista de diccionarios. Además, queremos agregar al diccionario un nuevo par clave-valor llamado promociona que indique si la
# persona promocionó la materia o no. Una persona promociona si la nota es mayor a 7.
# 
# Hacer una función que dada esta lista de listas, devuelva una lista de diccionarios, uno por estudiante. Considerar que no ocurren
# errores durante la ejecución.


list_to_convert =  [['Mariana', 'Lucía', 'Laura', 'Melina'], ['Juarez', 'Lourengo', 'Maciel', 'Retamozo'], [1, 1, 2, 1], [4, 8, 9, 6]]


def list_to_dict(total_list):
    keys = {0: 'nombre', 1: 'apellido', 2: 'intentos', 3: 'notas'}
    total_dict = []

    for i in range(len(total_list)):
       for j in range(len(total_list[i])):
            if i == 0:
                total_dict.append({})
            total_dict[j][keys[i]] = total_list[i][j]
            if i == 3:
                if total_list[i][j] > 7:
                    total_dict[j]['promociona'] = 'SI'
                else:
                    total_dict[j]['promociona'] = 'NO'

    return total_dict

print(list_to_dict(list_to_convert))
