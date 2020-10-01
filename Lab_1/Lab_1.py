# -*- coding: utf-8 -*-
import numpy as np
from scipy. integrate import odeint
import matplotlib.pyplot as plt

r1 = 2
r2 = 2
K1 = 200
K2 = 200
alpha12 = float(input('Введите значение alpha12: '))
alpha21 = float(input('Введите значение alpha21: '))


 # create function
def f(y, t):
	y1, y2 = y
	return [r1 * y1 * (K1 - y1 - alpha12 * y2) / K1, r2 * y2 * (K2 - y2 - alpha21 * y1) / K2]

t = np.linspace( 0, 10) # vector of time
y0 = [100, 100] # start value
w = odeint(f, y0, t) # solve eq.
y1 = w[:,0]
y2 = w[:,1]
fig = plt.figure(facecolor='white')
plt.plot(t, y1, '-o', t, y2, '-o', linewidth=2)
plt.ylabel("N - Численность популяций")
plt.xlabel("t - время")
plt.grid(True)
plt.show() # display
