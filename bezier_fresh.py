#Daniel Andrés Solís, Ingeniería Matemática UCM
import scipy.special
import numpy as np 
import matplotlib.pyplot as plt 
import math


#Introducimos los puntos y el intervalo (0,1), se puede dividir en más/menos trozos
puntos1=[np.array([0,0]),np.array([1,1]),np.array([2,1]),np.array([2,0])]
puntos2=[np.array([0,0]),np.array([0.5,0.5]),np.array([1,0.75]),np.array([1.375,0.75])]
puntos3=[np.array([1.375,0.75]),np.array([1.5625,0.75]),np.array([1.71875,0.6875]),np.array([1.828125,0.5625])]
puntos4=[np.array([1.828125,0.5625]),np.array([1.9375,0.6875]),np.array([2,0.25]),np.array([2,0])]
#puntos1: original #puntos2,3,4: trozos de curva original
t=np.arange(0.0,1.0,0.01)

#Cálculo del coeficiente B
def B(k,i,t):
    return scipy.special.binom(k,i)*(t**i)*(1-t)**(k-i)

#Cálculo de la curva en el punto t
def bezier(arraylist,t):
    alfa=0
    k=len(arraylist)-1
    i=0
    for p in arraylist:
        alfa=alfa+B(k,i,t)*p
        i=i+1
    return alfa

#Cálculo de la derivada de la curva (atención, ha de estar definida t en [0,1])
def dtbezier(arraylist,t):
    alfa=0
    k=len(arraylist)-1
    print(k)
    for i in range(0,k):
        alfa=alfa+(arraylist[i+1]-arraylist[i])*B(k-1,i,t)
        print(alfa)
    return k*alfa

#Dibujo. Para dibujar, poner en la consola "dibujar()"
def dibujar(puntos):
    xdata,ydata=[],[]
    for i in range(100):
        x=bezier(puntos,t[i])[0]
        y=bezier(puntos,t[i])[1]
        xdata.append(x)
        ydata.append(y)
    plt.plot(xdata,ydata)
    for i in [0,1,2,3]:
        plt.scatter(puntos[i][0],puntos[i][1])

#NOTA: los dibujos a veces pueden salir en escala distinta.
#Con Windows PowerShell o con PyCharm suelen salir bien. 

       
        
    
    

