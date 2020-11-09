#Daniel Andrés Solís, Ingeniería Matemática UCM
import scipy.special
import numpy as np 
import matplotlib.pyplot as plt 
import math

#Introducción de los puntos
puntos1=[np.array([-1,1]),np.array([0,-1]),np.array([2,2]),np.array([3,2])]
                                                    
#Introducción de los tiempos
times1=[-1,0,2,3]   

#Calcula la timeline con precisión 0.01 (se puede cambiar)
def timeline(times):
    k=len(times)-1
    timeline=np.arange(times[0],times[k],0.01)
    return timeline

#Calcula los coeficientes l_i(t)
def l_i(times,i,t):
    j=0
    result=1
    k=len(times)-1  
    while j<=k:
        if j!=i:
            result=result*((t-times[j])/(times[i]-times[j]))
        else: #Para cuando i=j, lo dejamos todo igual y seguimos
            result=result
        j+=1
    return result

#Calcula la curva de Lagrange para t dado
def lagrange(puntos,times,t):
    k=len(times)-1
    result=0
    for i in range(0,k+1):
        result=result+puntos[i]*l_i(times,i,t)
    return result

#Dibuja la curva        
def dibujar(puntos,times):
    xdata,ydata=[],[]
    t=timeline(times)
    for i in range(len(t)):
        x=lagrange(puntos,times,t[i])[0]
        y=lagrange(puntos,times,t[i])[1]
        xdata.append(x)
        ydata.append(y)
    plt.plot(xdata,ydata)
    for i in [0,1,2,3]:
        plt.scatter(puntos[i][0],puntos[i][1])                                                                  
                                                                    