import numpy as np
import matplotlib.pyplot as plt

##################################################################################
#ALIEN 1

jump_height_a1 = np.array([91,82.7,90.2,91.4,90.5])#alien 1 jump heights with no mass
jump_height_a1_with_mass = np.array([62.5,45.5,39.5,32.5,28])#alien 1 jump heights with added 5g each time
inverse_mass_a1 = 1/(np.array([5,10,15,20,25]))#added mass for each jump, inverse for the a linear graph
standard_dev1 = np.sqrt(0.5**2 + (np.std(jump_height_a1))**2)#standard deviation of the original 5 jumps, used for the uncertainty error bars
ori_jump_height_mean = np.mean(jump_height_a1)
#print(standard_dev1)

x_mean1 = np.sum(inverse_mass_a1)/6 #mean calculation of the inverse mass
y_mean1 = np.sum(jump_height_a1_with_mass)/6 #mean calculation of added mass jump heights
xsquare_mean1 = np.sum(inverse_mass_a1**2)/6 #mean calculation of the inverted mass squared
xy_mean1 = np.sum(jump_height_a1_with_mass*inverse_mass_a1)/6 #mean calculation of the sum of the 2 axis

m1 = (xy_mean1 - (x_mean1 * y_mean1)) / (xsquare_mean1 - (x_mean1 * x_mean1)) #subbing in the means to calculate
#the value of m, the gradiant of the best line on the graph
c1 = (y_mean1 * xsquare_mean1 - (xy_mean1 * x_mean1)) / (xsquare_mean1 - (x_mean1 * x_mean1)) #subbing in the means to calculate
#the value of c, the intersection with the y axis, for the best line on the graph

#g1 = np.sum(deviationsquare)

#here we need to calculate the chi X^2 value. should be around ~10 i think

plt.xlabel('inverse mass') #plotting all the data in the graph
plt.ylabel('jump height')
plt.title('jump height in terms of inverse mass')
best_line1 = inverse_mass_a1 * m1 + c1 #equation for the best line fit using the values found of m and c
plt.plot(inverse_mass_a1, best_line1, 'b--') #plotting the best line with the calculated values of m and c

dy1 = (standard_dev1*100)/jump_height_a1_with_mass #calculating the uncertainty for each indiviudal point
plt.errorbar(inverse_mass_a1,jump_height_a1_with_mass,yerr=dy1, fmt='rx')
#plotting the data points with their corresponding error bars
deviation = ((m1 * inverse_mass_a1) + (c1 - jump_height_a1_with_mass)) #calculation of the deviation in order to find goodness of fit on following line
chi_square = np.sum((deviation/dy1)**2)

print(np.std(jump_height_a1))
print(standard_dev1)
print(dy1)
#print(g1)
print(m1)
print(c1)
print(chi_square)
'''
###############################################################################
#ALIEN 2

jump_height_a2 = np.array([68.4,69.4,69.8,69.5,68.5])#alien 1 jump heights with no mass
jump_height_a2_with_mass = np.array([48,36,32,29,22])#alien 1 jump heights with added 5g each time
inverse_mass_a2 = 1/(np.array([5,10,15,20,25]))#added mass for each jump, inverse for the a linear graph
standard_dev2 = np.std(jump_height_a2)#standard deviation of the original 5 jumps, used for the uncertainty error bars

x_mean2 = np.sum(inverse_mass_a2)/6 #mean calculation of the inverse mass
y_mean2 = np.sum(jump_height_a2_with_mass)/6 #mean calculation of added mass jump heights
xsquare_mean2 = np.sum(inverse_mass_a2**2)/6 #mean calculation of the inverted mass squared
xy_mean2 = np.sum(jump_height_a2_with_mass*inverse_mass_a2)/6 #mean calculation of the sum of the 2 axis

m2 = (xy_mean2 - (x_mean2 * y_mean2)) / (xsquare_mean2 - (x_mean2 * x_mean2)) #subbing in the means to calculate
#the value of m, the gradiant of the best line on the graph
c2 = (y_mean2 * xsquare_mean2 - (xy_mean2 * x_mean2)) / (xsquare_mean2 - (x_mean2 * x_mean2)) #subbing in the means to calculate
#the value of c, the intersection with the y axis, for the best line on the graph

deviationsquare2 = (m2 * inverse_mass_a2 + c2 - jump_height_a2_with_mass**2) #calculation of the deviation in order to find goodness of fit on following line
g2 = np.sum(deviationsquare2)

#here we need to calculate the chi X^2 value. should be around ~10 i think

plt.xlabel('inverse mass') #plotting all the data in the graph
plt.ylabel('jump height')
plt.title('jump height in terms of inverse mass')
best_line2 = inverse_mass_a2 * m2 + c2 #equation for the best line fit using the values found of m and c
plt.plot(inverse_mass_a2, best_line2, 'y--') #plotting the best line with the calculated values of m and c

dy2 = (standard_dev2*100)/jump_height_a2_with_mass #calculating the uncertainty for each indiviudal point
plt.errorbar(inverse_mass_a2,jump_height_a2_with_mass,yerr=dy2, fmt='gx')
#plotting the data points with their corresponding error bars

print('the standard deviation is',standard_dev1)
print('the calculated spring constant is the gradiant of the best line plot :', m1)
print('the mean of the original jump heights is',ori_jump_height_mean)
'''
'''
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
#print(dy)'''