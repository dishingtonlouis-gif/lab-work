import numpy as np
import matplotlib.pyplot as plt

angle_data = np.array([0,20,40,60,80,100,120,140,160,180]) # x axis
angle_data = np.deg2rad(angle_data)
angle_data = np.cos(2*angle_data)
intensity_data = np.array([1.86,1.63,1.13,0.52,0.16,0.00,0.57,1.11,1.56,1.71]) # y axis
uncertainty = 0.05
plt.xlabel('incident angle')
plt.ylabel('intensity')
plt.title('intensity in terms of the angle')
plt.errorbar(angle_data, intensity_data, yerr = 0.05, fmt='rx')


########################################################
#calculating best line
 
x_mean = np.sum(angle_data)/10 #mean calculation
y_mean = np.sum(intensity_data)/10 #mean calculation
xsquare_mean = np.sum(angle_data**2)/10 #mean calculation
xy_mean = np.sum(intensity_data*angle_data)/10 #mean calculation

m = (xy_mean - (x_mean * y_mean)) / (xsquare_mean - (x_mean * x_mean)) #subbing in the means to calculate
#the values of m and c in order to plot the best line on the graph

c = (y_mean * xsquare_mean - (xy_mean * x_mean)) / (xsquare_mean - (x_mean * x_mean)) #subbing in the means to calculate
#the values of m and c in order to plot the best line on the graph

bestline = m * angle_data + c

#print(m)
#print(c)

plt.plot(angle_data,bestline)

###########################################################
# uncertainties on m and c

slope_uncertainty = (1/10) * 1 / (np.mean(angle_data**2) - np.mean(angle_data)**2) * 0.05**2
intersect_uncertainty = (1/10) * np.mean(angle_data**2) / (np.mean(angle_data**2) - np.mean(angle_data)**2) * 0.05**2

#print(slope_uncertainty)
#print(intersect_uncertainty)

print(m, '+ or -', np.sqrt(slope_uncertainty))
print(c, '+ or -', np.sqrt(intersect_uncertainty))

chi = np.sum(((m * angle_data + c - intensity_data)/0.05)**2)
print(chi)

uncertainty = [0.0.125] * 10

data = np.array([angle_data, intensity_data, uncertainty])

np.savetxt('data.txt', data ,delimiter = ',')