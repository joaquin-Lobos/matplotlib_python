#!/usr/bin/env python
'''
Matplotlib [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes
import matplotlib.gridspec as gridspec
import mplcursors  # [Opcional cursores]


def ej1():
    # Line Plot
    # Se desea graficar tres funciones en una misma figura
    # en tres gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de x:
    x = list(range(-10, 11, 1))

    # Realizar tres gráficos que representen
    # y1 = x^2 (X al cuadrado)
    # y2 = x^3 (X al cubo)
    # y3 = x^4 (X a la cuarta)
    # Utilizar comprension de listas para generar
    # y1, y2 e y3 basado en los valores de x

    y1 = [i**2 for i in x]
    y2 = [i**3 for i in x]
    y3 = [i**4 for i in x]

    gs = gridspec.GridSpec(3, 1)
    fig = plt.figure()
    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[1, 0])
    ax3 = fig.add_subplot(gs[2, 0])

    ax1.plot(x, y1, c='darkred', marker='^', ms=5, label='y=x**2')
    ax1.legend()
    ax1.grid()

    ax2.plot(x, y2, c='green', marker='x', ms=5, label='y=x**3')
    ax2.legend()
    ax2.grid()
    
    ax3.plot(x, y3, c='darkblue', marker='o', ms=5, label='y=x**4')
    ax3.legend()
    ax3.grid()

    plt.plot()
    plt.show()
    # Esos tres gráficos deben estar colocados
    # en la diposición de 3 filas y 1 columna:
    # ------
    # graf1
    # ------
    # graf2
    # ------
    # graf3
    # ------
    # Utilizar add_subplot para lograr este efecto
    # de "3 filas" "1 columna" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un color distinto
    # a su elección


def ej2():
    # Scatter Plot
    # Se desea graficar dos funciones en una misma figura
    # en dos gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de x:
    x = np.arange(0, 4*np.pi, 0.1)


    y1 = np.sin(x)
    y2 = np.cos(x)

    gs = gridspec.GridSpec(1, 2)
    fig = plt.figure()
    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1])
    
    ax1.plot(x, y1, c='darkred', marker='^', ms=5, label='y=x**2')
    ax1.legend()
    ax1.grid()
    ax1.set_facecolor('whitesmoke')
    ax2.plot(x, y2, c='green', marker='x', ms=5, label='y=x**3')
    ax2.legend()
    ax2.grid()
    ax2.set_facecolor('whitesmoke')
    plt.plot()
    plt.show()
    # Realizar dos gráficos que representen
    # y1 = sin(x)
    # y2 = cos(x)
    # Utilizar los métodos de Numpy para calcular
    # "y1" y "y2" basado en los valores de x

    # Esos dos gráficos deben estar colocados
    # en la diposición de 1 fila y 2 columnas:
    # ------
    #  graf1 | graf2
    # ------
    # Utilizar add_subplot para lograr este efecto
    # de "1 fila" "2 columnas" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un mark distinto
    # a su elección.


def ej3():
    # Bar Plot
    # Generar un gráfico de barras simple a partir
    # de la siguiente información:

    lenguajes = ['Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp']
    performance = [10, 8, 6, 4, 2, 1]


    fig = plt.figure()
    ax1 = fig.add_subplot()
    fig.suptitle('Performance De Los Lenguajes', fontsize=16)
    ax1.bar(lenguajes, performance, label='perfomance')
    ax1.set_facecolor('whitesmoke')
    ax1.grid(c = 'darkgrey', ls = 'dotted')
    ax1.legend()
    plt.show()
    # Realizar un gráfico de barras en donde se pueda ver el uso
    # de cada lenguaje, se debe utilizar los labels "lenguajes"
    # como valor del eje X

    # Se debe colocar título al gráfico.
    # Se debe cambiar la grilla y el fondo a su elección.


def ej4():
    # Pie Plot
    # Se desea realizar un gráfico de torta con la siguiente
    # información acerca del % de uso de lenguajes en nuevos
    # programadores
    uso_lenguajes = {'Python': 29.9, 'Javascript': 19.1,
                     'Go': 16.2, 'Java': 10.5, 'C++': 10.2,
                     'C#': 8.2, 'C': 5.9
                     }

    fig = plt.figure()
    ax1 = fig.add_subplot()
    fig.suptitle('Uso De Lenguajes En Nuevos Programadores', fontsize = 12)
    
    ax1.pie(uso_lenguajes.values(), 
          colors = ['green', 'darkgreen', 'lightblue', 'red', 'orange', 'brown' , 'pink'],
          labels = uso_lenguajes.keys(), autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')       
    plt.show()

    # El gráfico debe tener usar como label las keys del diccionario,
    # debe usar como datos los values del diccionario
    # Se desea resaltar (explode) el dato de Python
    # Se desea mostrar en el gráfico los porcentajes de c/u
    # Se debe colocar un título al gráfico


def ej5():
    # Uso de múltiples líneas en un mismo gráfico (axes)
    # En el siguiente ejemplo generaremos una señal senoidal
    # haciendo uso solamente de comprension de listas
    step = 0.1
    sample_size = 100
    signal = [{'X': i*step, 'Y': math.sin(i*step)} for i in range(sample_size)]

    # Se generó una lista de diccionarios con dos columnas "X" e "Y"
    # que corresponden a los valores de nuestra señal senoidal.
    # Se pide usar comprensión de listas para generar las dos listas
    # por separado de los valoresde "X" e "Y" para poder utilizar
    # el line plot y observar la señal

    signal_x = [signals['X'] for signals in signal]
    signal_y = [signals['Y'] for signals in signal]

    # plot(signal_x, signal_y)

    fig = plt.figure()
    ax = fig.add_subplot()
    fig.suptitle('Señal Senoidal')

    ax.plot(signal_x, signal_y, c = 'darkred', label = 'Señal Senoidal')
    ax.grid(c = 'darkgrey', ls = 'dotted')
    ax.set_facecolor('whitesmoke')
    ax.legend()
    plt.show()

    # Ahora que han visto la señal senoidal en su gráfico, se desea
    # que generen otras dos listas de "X" e "Y" pero filtradas por
    # el valor de "Y". Solamente se debe completar la lista
    # con aquellos valores de "Y" cuyo valor absoluto (abs)
    # supere 0.7

    filter_signal = [x for x in signal if abs(x['Y']) > 0.7]
    filter_signal_x = [signal['X'] for signal in filter_signal]
    filter_signal_y = [signal['Y'] for signal in filter_signal]

    fig = plt.figure()
    ax = fig.add_subplot()
    fig.suptitle('Señales Senoidales Filtradas')

    ax.plot(signal_x, signal_y, c = 'green', label = 'Señal Senoidal')
    ax.scatter(filter_signal_x, filter_signal_y, label = 'Señales Filtradas')
    ax.grid(c = 'darkgrey', ls = 'dotted')
    ax.set_facecolor('whitesmoke')
    ax.legend()

    plt.show()

    # Graficar juntas ambos conjuntos de listas y observar
    # el resultado. Graficar filter como scatter plot

    # plot(signal_x, signal_y)
    # scatter(filter_signal_x, filter_signal_y)

    # Pueden ver el concepto y la utilidad de
    # realizar un gráfico encima de otro para filtrar datos?


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    # ej1()
    # ej2()
    # ej3()
    # ej4()
    # ej5()
