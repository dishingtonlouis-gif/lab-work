import numpy as np
import matplotlib.pyplot as plt

voltage = np.array([1.00,2.00,3.00,4.00,5.00,6.00])#arrays of data
current = np.array([9.80,20.3,30.2,39.8,50.1,60.2])#arrays of data
dy = 0.025 * current

x_mean = np.sum(voltage)/6 #mean calculation
y_mean = np.sum(current)/6 #mean calculation
xsquare_mean = np.sum(voltage**2)/6 #mean calculation
xy_mean = np.sum(voltage*current)/6 #mean calculation

m = (xy_mean - (x_mean * y_mean)) / (xsquare_mean - (x_mean * x_mean)) #subbing in the means to calculate
#the values of m and c in order to plot the best line on the graph

c = (y_mean * xsquare_mean - (xy_mean * x_mean)) / (xsquare_mean - (x_mean * x_mean)) #subbing in the means to calculate
#the values of m and c in order to plot the best line on the graph

deviationsquare = (m * voltage + c - current)**2 #calculation of the deviation in order to find goodness of fit on following line
g = np.sum(deviationsquare)

plt.xlabel('voltage') #plotting all the data in the graph
plt.ylabel('current')
plt.title('current in terms of voltage')
plt.errorbar(voltage,current,yerr=dy, fmt='rx') #using the percentage uncertainty value
# given in our current data values shown as a vertical  line in the y axis 
#dy = current times the uncertainty percentage on line 6

bestline = voltage * m + c
plt.plot(voltage, bestline)

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
