#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#numerical integration of the optimal control equation
#Euler explicit integration scheme


import numpy as np
import matplotlib.pyplot as plt
import time 
import pickle
from tqdm import tqdm

import os

# Get the directory of the current script (the .py file you're running)
script_dir = os.path.dirname(os.path.abspath(__file__))

# Change the working directory to the script's directory
os.chdir(script_dir)



def V(x,t):
    return -np.cos(x)



def phi(x):
    return 0

s=0.1 #s=dt/dx**2
dx=0.01 #space discretization step

dt=s*dx**2 #time discretization step

D=1 #rotational diffusion constant
tf=10 #total time
X=np.pi #domain of definition is [-X,X]
t_steps=int(tf/dt)
x_steps=int(2*X/dx)




x=np.linspace(-X,X,x_steps)
t=np.linspace(tf,0,t_steps+1)

I=np.zeros((t_steps+1,x_steps))
R=np.zeros((t_steps+1,x_steps))



t_ends=[]
t_end=0
boundaries=[]

for i in range(x_steps):
        I[0,i]=phi(x[i])
        
        
for j in tqdm(range(t_steps)):
    boundary=[] #boundary of the moving boundary problem as a function of time
    
    for i in range(0,x_steps-1):
        I[j+1,i]=I[j,i]+V(x[i],t[j])*dt+dt*D*(I[j,i+1]+I[j,i-1]-2*I[j,i])/(dx**2)
    
    I[j+1,-1]=I[j,-1]+V(x[-1],t[j])*dt+dt*D*(I[j,0]+I[j,-2]-2*I[j,-1])/(dx**2)
    
    
    for i in range(x_steps):
        
        #check for the condition that defines the moving boundary
        if I[j+1,i]>=I[j,int(x_steps/2)]+1:
            I[j+1,i]=I[j,int(x_steps/2)]+1
            R[j+1,i]=1
    for i in range(1,x_steps-1):
        if R[j+1,i]==1:
            if R[j+1,i+1]==0 or R[j+1,i-1]==0:
                boundary.append(x[i])
    boundaries.append(boundary)


#saving data (boundary location) to file  


fp=open("boundary_p_"+str(dx)+".txt",'w')
fm=open("boundary_m_"+str(dx)+".txt",'w')
tp=[]
tm=[]
bp=[]
bm=[]


for j in range(0,t_steps):
    for b in boundaries[j]:
        if b>0:
            fp.write(str(t[j])+'\t'+str(b)+'\n')
            tp.append(t[j])
            bp.append(b)
        if b<0:
            fm.write(str(t[j])+'\t'+str(b)+'\n')
            tm.append(t[j])
            bm.append(b)
            
                

plt.plot(tm,bm)
plt.plot(tp,bp)


