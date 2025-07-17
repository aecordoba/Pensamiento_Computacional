# Se está diseñando una montaña rusa para el Parque de la Costa. Se quiere que sea la mejor de LATAM. La misma tiene una
# parte en donde hay una serie de bucles con distintos radios.
#
# Se tienen dos opciones:
# 1.El bucle más grande tiene 22 metros de radio y los bucles siguientes van disminuyendo su radio de a 2 metros hasta
# llegar a 0 y seguir su recorrido de forma recta.
# 2. El bucle más grande tiene 30 metros de radio y los bucles siguientes van disminuyendo su radio de a 5 metros hasta
# llegar a 0 y seguir su recorrido de forma recta.
#
# Queremos ver en un gráfico la fuerza centrípeta que van a sufrir nuestros pasajeros a través de cada secuencia de bucles,
# sabiendo que el máximo de masa es de 300kg por carrito (viajan dos personas), la velocidad es de 27.78 m/s, y el radio va a ir
# variando como mencionamos arriba.
#
# El cálculo de la fuerza centrípeta (en unidad Newton [N]) es: Fc = ( m . v^2 ) / r
# Donde m es la masa, v es la velocidad y r es el radio.
#
# Graficar en una línea continua el valor de la Fuerza Centrípeta (Fc) respecto de los radios de cada opción, de forma creciente (de
# 2 a 22 y de 5 a 30). Incluir título, nombres de ejes y label (leyenda) con el valor de la masa y la velocidad.


import matplotlib.pyplot as plt
import numpy as np

masa = 300
velocidad = 27.78

radio1 = np.linspace(2, 22, 2)
radio2 = np.linspace(5, 30, 5)
fig, ax = plt.subplots(figsize=(7, 5), layout='constrained')
ax.plot(radio1, masa * velocidad ** 2 / radio1, label='opción 1')
ax.plot(radio2, masa * velocidad ** 2 / radio2, label='opción 2')
ax.set_title('Parque de la Costa')
ax.text(22, 80000, 'masa = {}kg\nvelocidad = {}m/s'.format(masa, velocidad))
ax.set_xlabel('radio (m)')
ax.set_ylabel('Fc (N)')
ax.legend()
