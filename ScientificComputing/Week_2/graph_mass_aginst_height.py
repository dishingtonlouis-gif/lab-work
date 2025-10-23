import numpy as np
import matplotlib.pyplot as plt


data = np.genfromtxt("AlienMHData.csv",dtype='float',delimiter=',',skip_header=0)
mass = np.array([8,11,14,17,20,23,26,29,32])
g = 9.81
l0 = 6.1
l1 = 4.2
k = 409.41

height = (k/(2*mass*g))*((l0-l1)**2)+l1


x_1 = data[:,0]#defining x as mass
y_1 = data[:,1]#defining y as height
x_2 = mass
y_2 = height

plt.xlabel('mass')#name of x
plt.ylabel('heights')# name of y
plt.title("Height against mass")#title of the graph
plt.plot(x_1,y_1,'b--', label="measured data")#plotting x against y
plt.plot(x_2,y_2,'g--', label="measured data")
#'b-- = dashed blue line