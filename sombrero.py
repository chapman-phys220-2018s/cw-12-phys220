#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
#Daniel Chang
#2260161
#Chang254@mail.chapman.edu
#Myranda Hoggatt
#2285495
#hogga102@mail.chapman.edu
#Devon Ball
#2313078
#dball@chapman.edu
#PHYS220 Spring 2018
#CW12
###

import numpy as np
import matplotlib.pyplot as plt

def runge4(x0,y0,F,N):
    dt = .001
    x = np.zeros(N)
    x[0] = x0
    y = np.zeros(N)
    y[0] = y0
    for i in range(1,N):
        t += 0
        tmid = t - (dt/2)
        tforw = t + dt
        xk1 = dt*(y[i-1])
        yk1 = dt*(-.25*y[i-1]+x[i-1]-(x[i-1]**3)+F*np.cos(t))
        xmid = x[i-1] + xk1/2
        ymid = y[i-1] + yk1/2
        xk2 = dt*(ymid)
        yk2 = dt*(-.25*ymid[i-1]+xmid[i-1]-(xmid[i-1]**3)+F*np.cos(tmid))
        xmid = x[i-1] + xk2/2
        ymid = y[i-1] + yk2/2
        xk3 = dt*(ymid)
        yk3 = dt*(-.25*ymid[i-1]+xmid[i-1]-(xmid[i-1]**3)+F*np.cos(tmid))
        xforw = x[i-1] + xk3
        yforw = y[i-1] + yk3
        xk4 = dt*(yforw)
        yk4 = dt*(-.25*yforw[i-1]+xforw[i-1]-(xforw[i-1]**3)+F*np.cos(tforw))
        x[i] = x[i-1] + (xk1 + 2*xk2 + 2*xk3 +xk4)/6
        y[i] = y[i-1] + (yk1 + 2*yk2 + 2*yk3 +yk4)/6
    return (x,y)

def plot_sombrero():
    plt.figure(figsize=(10,10))
    plt.title("Sombrero Plot")
    plt.xlabel("x")
    plt.ylabel("v")
    x = np.linspace(-1.5,1.5,10000)
    v = (x**4/2)-(x**2/2)
    plt.plot(x,v)