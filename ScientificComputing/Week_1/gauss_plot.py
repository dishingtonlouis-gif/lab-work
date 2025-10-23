import numpy as np
import matplotlib.pyplot as plt

mu = 5.0  # assign the value of mu
sigma_1 = 1.5  # assign the value of sigma
sigma_2 = 0.8

x = np.linspace(0,10,1000)  # make an array containing 1000 values evenly spaced from 0 to 10

# Now calculate the y values - do this step by step:
S1 = 1.0/(sigma_1 * np.sqrt(2.0 * np.pi))  # this is the first part of the expression
S2 = (x - mu)**2  # this is the numerator of the exponential factor, 
# without the overall negative sign
S3 = - S2 / (2.0 * sigma_1**2)  # this is the exponential factor
y_1 = S1 * np.exp(S3) # this is the final result

# Now calculate the y values - do this step by step:
S4 = 1.0/(sigma_2 * np.sqrt(2.0 * np.pi))  # this is the first part of the expression
S5 = (x - mu)**2  # this is the numerator of the exponential factor, 
# without the overall negative sign
S6 = - S5 / (2.0 * sigma_2**2)  # this is the exponential factor
y_2 = S4 * np.exp(S6) # this is the final result

# The following lines make a plot and save a copy.
plt.xlabel('x') # creates a label 'x' for the x-axis
plt.ylabel('y') # creates a label 'y' for the y-axis
plt.title('The Gaussian Function') # gives the plot a title
plt.plot(x,y_2)
plt.plot(x,y_1) # plot y versus x
plt.savefig('GaussPlot.png', dpi=600)  # save a copy of the plot
plt.show()