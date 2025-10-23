import numpy as np
import matplotlib.pyplot as plt

jump_height = np.array([62.0,44.0,40.0,33.0,28.0])#arrays of data
inverse_mass = 1/(np.array([5,10,15,20,25]))#arrays of data
dy = jump_height * 0.023

x_mean = np.sum(inverse_mass)/6 #mean calculation
y_mean = np.sum(jump_height)/6 #mean calculation
xsquare_mean = np.sum(inverse_mass**2)/6 #mean calculation
xy_mean = np.sum(jump_height*inverse_mass)/6 #mean calculation

m = (xy_mean - (x_mean * y_mean)) / (xsquare_mean - (x_mean * x_mean)) #subbing in the means to calculate
#the values of m and c in order to plot the best line on the graph

c = (y_mean * xsquare_mean - (xy_mean * x_mean)) / (xsquare_mean - (x_mean * x_mean)) #subbing in the means to calculate
#the values of m and c in order to plot the best line on the graph

deviationsquare = (m * inverse_mass + c - jump_height)**2 #calculation of the deviation in order to find goodness of fit on following line
g = np.sum(deviationsquare)

plt.xlabel('inverse mass') #plotting all the data in the graph
plt.ylabel('jump height')
plt.title('jump height in terms of inverse mass')
plt.errorbar(inverse_mass,jump_height,yerr=dy, fmt='rx') #using the percentage uncertainty value
# given in our current data values shown as a vertical  line in the y axis 
#dy = current times the uncertainty percentage on line 6

best_line = inverse_mass * m + c
plt.plot(inverse_mass, best_line, 'b--')

#printing all our data
print(x_mean)
print(y_mean)
print(xsquare_mean)
print(xy_mean)
print()
print(m)
print(c)
print()
print(g)
