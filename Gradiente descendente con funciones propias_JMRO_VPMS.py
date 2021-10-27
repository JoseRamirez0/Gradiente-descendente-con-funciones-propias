"""
Created on Fri Oct 22 23:06:10 2021

@author: José Manuel Ramírez Olivera.
         Viviana Paloma Muñoz Sánchez.

"""

import numpy as np

x=[0,0,0]
A=[[4,-1,1],[-1,4,-2],[1,-2,4]]        
b=[12,-1,5]        

def transponer(A):
    T=[]        
    for i in range (len(A)):
        aux=[]
        for j in range(len(A)):
            aux.append(A[j][i])
        T.append(aux)
    return T    

def resta(A,B):
     C=[]
     for i in range(len(A)):
         if isinstance(A[0],list):
             aux=[]
             for j in range(len(A[0])):
                 aux.append(A[i][j]+B[i][j])
             C.append(aux)
         else:
             C.append(A[i]+B[i])
     return C

def mult1(A,b):
    C=[]
    for i in range (len(A)):
        for j in range (len(b)):
            x=0
            for k in range(len(A[0])):
                x=x+A[i][k]*b[k]
        C.append(x)  
    return C

def mult2(A,n):
    B=[]
    for i in range (len(A)):
        aux=[]
        if isinstance(A[0],list):
            for j in range (len(A[i])):
                x=A[i][j]
                aux.append(n*x)
            B.append(aux)
        else:
            B.append(n*A[i])
    return B

def Gradiente(x_sol,A,b,umbral,it_max):
    e1=mult1(transponer(A),mult1(A,x_sol))
    e2=mult1(transponer(A),b)
    for i in range (it_max):
        x_sol=resta(x_sol,mult2(resta(mult2(e1,2),mult2(e2,2)),k))
        print(i,x_sol)
        btent=mult1(A,x_sol)
        error= np.sum(np.abs(resta(btent,b)))
        if error < umbral:
            return x_sol
        
def printn(A):
    for i in range (len(A)):
        print(A[i])
                

k=0.001
u=0.0001
it_max=5

Gradiente(x,A,b,u,it_max)
print("b:",mult1(A,x))