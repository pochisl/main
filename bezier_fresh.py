#Daniel Andrés Solís, Ingeniería Matemática UCM
import scipy.special
import numpy as np 
import matplotlib.pyplot as plt 
import math
#Introducimos los puntos y el intervalo (0,1), se puede dividir en más/menos trozos
puntos=[np.array([0,0]),np.array([1,1]),np.array([2,1]),np.array([2,0])]
t=np.arange(0.0,1.0,0.01)

#Cálculo del coeficiente B
def B(k,i,t):
    return scipy.special.binom(k,i)*(t**i)*(1-t)**(k-i)

#Cálculo de la curva
def bezier(arraylist,t):
    alfa=0
    k=len(arraylist)-1
    i=0
    for p in arraylist:
        alfa=alfa+B(k,i,t)*p
        i=i+1
    return alfa

#Dibujo. Para dibujar, poner en la consola "dibujar()"
def dibujar():
    xdata,ydata=[],[]
    for i in range(100):
        x=bezier(puntos,t[i])[0]
        y=bezier(puntos,t[i])[1]
        xdata.append(x)
        ydata.append(y)
    plt.plot(xdata,ydata)
    for i in [0,1,2,3]:
        plt.scatter(puntos[i][0],puntos[i][1])
    
        
    
    

