import numpy as np
import matplotlib.pyplot as plt


t = np.linspace(0,1,100)
m = 0.00841
g = 9.81
h = 0.875
l = 0.018
u = 4.15

k = 0
k = 2*((h*m*g)/l**2)
print(k)

Es = (1/2)*k*t**2

s = u*t - 0.5*g*t**2
v = u - g*t

Eg = m*g*s
Ek = (1/2)*m*v**2

plt.xlabel('x') # creates a label 'x' for the x-axis
plt.ylabel('y') # creates a label 'y' for the y-axis
plt.title('Gravity potential & kinetic energy against time') # gives the plot a title
plt.plot(t,Eg) # plot y versus x
plt.plot(t,Ek)
plt.savefig('xsquared_fig')
plt.show()