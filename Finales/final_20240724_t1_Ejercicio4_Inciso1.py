# Una empresa tiene el siguiente diccionario de información de empleados, y se pide crear un DataFrame como se ve en la imagen.
#   apellido    nombre  año_ingreso salario_al_ingreso
# 0 Perez       Malena  2008        700000
# 1 Sanchez     Sergio  2015        450000
# 2 Gomez       Carla   2023        300000
# 3 Quilpe      Jose    2022        600000
#
# Para el dataframe creado, se quiere calcular cuáles son los empleados peor pagos de la empresa al día de hoy, para ofrecerles un aumento. Ninguna
# persona entró todavía en el 2024, y sabemos que todos tienen 2 hijos y una pareja.
# - Sabemos que cada año que estuvo en la empresa, se le dió un 0.5 de aumento de sueldo. Crear una columna en el dataFrame al final
# llamada salario_actual, donde cada valor se calcula como la cantidad de años que lleva en la empresa, multiplicado por el aumento por año
# y el salario al momento del ingreso.
# - El INDEC mide la capacidad de una persona de satisfacer sus necesidades alimentarias y esenciales con la Canasta Básica Total. A junio del 2024,
# el valor de una Canasta Básica Total para una familia de 4 es de 851.351. Aquellas familias que cobren menos de ese monto, se las considera por
# debajo de la línea de la pobreza. En un nuevo dataframe, copia del original, quedarse con los empleados que están por debajo de la línea de la
# pobreza, y en una columna llamada salario_nuevo, cuatriplicarles a todos el sueldo.

import pandas as pd

# Ver https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
pd.options.mode.copy_on_write = True

año_actual = 2024
canasta_basica_total = 851351
data = {
    'apellido': ['Perez', 'Sanchez', 'Gomez', 'Quilpe'],
    'nombre': ['Malena', 'Sergio', 'Carla', 'Jose'],
    'año_ingreso': [2008, 2015, 2023, 2022],
    'salario_al_ingreso': [700000, 450000, 300000, 600000]
}


empleados = pd.DataFrame(data)
empleados['salario_actual'] = (
    (año_actual - empleados['año_ingreso']) * 0.5 + 1) * empleados['salario_al_ingreso']
print('Empleados con salario actual:\n{}'.format(empleados))

ingresos_cbt = empleados[empleados['salario_actual'] < canasta_basica_total]
ingresos_cbt['salario_nuevo'] = ingresos_cbt['salario_actual'] * 4
print('Empleados por debajo de la canasta básica total:\n{}'.format(ingresos_cbt))
