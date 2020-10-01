# -*- coding: utf-8 -*-
import numpy as np
from scipy. integrate import odeint
import matplotlib.pyplot as plt

k1 = 0.3
k2 = 0.5
h0 = 100
hk = 500
v0 = 0.1
F = 5
g = -9.8
m = 20
c = 0.045
p0 = 0.02
s = 10
betta = 5.6 * 10**(-5)

 # create function
def f(y, t):
	y1, y2 = y
	while y1 < hk:
	 return [y2, F - m*c*p0*(10**(-betta * y1))*s*y2**2]
	else:
	 return [y2, (m*g - k1*y2 - k2*y2**2) / m]


t = np.linspace(0, 100) # vector of time
y0 = [h0, v0] # start value
w = odeint(f, y0, t) # solve eq.
y1 = w[:,0]
y2 = w[:,1]
fig = plt.figure(facecolor='white')
plt.plot(t, y1, '-o', t, y2, '-o', linewidth=2)
plt.ylabel("N - Численность популяций")
plt.xlabel("t - время")
plt.grid(True)
plt.show() # display

