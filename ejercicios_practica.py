#!/usr/bin/env python
'''
Matplotlib [Python]
Ejercicios de práctica
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
    # Se desea graficar los valores de X e Y en un gráfico de línea

    # Función que se desea graficar:
    # y1 = x**2

    x = list(range(-10, 11, 1))
    # Estamos aprovechando el concepto de comprension de listas
    # para generar los valores que toma "Y" por cada valor de "X"
    y = [i**2 for i in x]
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot(x, y, c='darkred', marker='^', ms=10, label='y=x**2')
    fig.suptitle('"Y" en función de "X"')
    ax.legend()
    ax.grid()

    plt.plot()
    plt.show()
    # Crear una "figura" y crear un "ax" con add_subplot
    # Graficar el "line plot" de "Y" en función de "X"
    # Colocar la leyenda y el label con el nombre de la función
    # Darle color a la línea a su elección
    



def ej2():
    # Line Plot
    # Se desea graficar varias funciones en un mismmo gráfico (axe)

    # Las funciones que se desean implementar y graficar son:
    # y1 = x**2
    # y2 = x**3

    # Su implementación es la siguiente:
    x = list(np.linspace(-4, 4, 20))
    # Estamos aprovechando el concepto de comprension de listas
    # para generar los valores que toma "Y" por cada valor de "X"
    y1 = [i**2 for i in x]
    y2 = [i**3 for i in x]

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot(x, y1, c='darkred', marker='^', ms=10, label='y=x**2')
    ax.plot(x, y2, c='green', marker='x', ms=10, label='y=x**3')
    ax.legend()
    ax.grid()

    plt.plot()
    plt.show()
    # Realizar un gráfico que representen las dos funciones
    # Para ello se debe llamar dos veces a "plot" con el mismo "ax"

    # Se debe colocar en la leyenda la función que representa
    # cada función

    # Cada función dibujarla con un color distinto
    # a su elección


def ej3():
    # Scatter Plot
    # Se desea graficar la función tanh para el siguiente
    # intervalor de valores de "X"
    x = np.arange(-np.pi, np.pi, 0.1)

    # Función a implementar
    # y = tanh(x) --> tangente hiperbólica

    # Implementacion
    y = np.tanh(x)
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.scatter(x, y, c='darkgreen', marker='^', label='y=x**2')
    ax.legend()
    ax.grid()

    plt.show()

    # Graficar la función utilizando "scatter"

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Elegir un marker a elección


def ej4():
    # Figura con múltiples gráficos
    # Line Plot
    # Se desea graficar cuatro funciones en una misma figura
    # en cuatros gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de "X":
    x = np.linspace(-10, 10, 40)

    # Realizar tres gráficos que representen
    # y1 = x^2 (X al cuadrado)
    # y2 = x^3 (X al cubo)
    # y3 = x^4 (X a la cuarta)
    # y4 = raiz_cuadrada(X)

    # Implementación:
    y1 = x**2
    y2 = x**3
    y3 = x**4
    y4 = np.sqrt(x)


    gs = gridspec.GridSpec(2, 2)
    fig = plt.figure()
    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1])
    ax3 = fig.add_subplot(gs[1, 0])
    ax4 = fig.add_subplot(gs[1, 1])

    ax1.plot(x, y1, c='darkred', marker='^', ms=5, label='y=x**2')
    ax1.legend()
    ax1.grid()
    ax1.grid(c = 'darkgrey',)
    ax1.set_facecolor('whitesmoke')

    ax2.plot(x, y2, c='green', marker='x', ms=5, label='y=x**3')
    ax2.legend()
    ax2.grid()
    ax2.grid(c = 'darkgrey')
    ax2.set_facecolor('whitesmoke')

    ax3.plot(x, y3, c='darkblue', marker='o', ms=5, label='y=x**4')
    ax3.legend()
    ax3.grid()
    ax3.grid(c = 'darkgrey')
    ax3.set_facecolor('whitesmoke')

    ax4.plot(x, y4, c='orange', marker='*', ms=5, label='y= raiz cuadrada de x')
    ax4.legend()
    ax4.grid()
    ax4.set_facecolor('whitesmoke')
    ax4.grid(c = 'darkgrey')

    plt.plot()
    plt.show()
    # Esos tres gráficos deben estar colocados
    # en la diposición de 3 filas y 1 columna:
    # ------
    #  graf1 | graf2
    # ------
    #  graf3 | graf4
    # Utilizar add_subplot para lograr este efecto
    # de "2 filas" "2 columna" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un color distinto
    # a su elección

    # Colocar una grilla a elección


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    # ej1()
    # ej2()
    # ej3()
    # ej4()
