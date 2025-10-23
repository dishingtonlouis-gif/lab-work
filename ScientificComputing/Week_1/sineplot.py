import numpy as np
import matplotlib.pyplot as plt

xvals = np.genfromtxt("data_input.txt",dtype='float',skip_header=0) 
# reads data from data_input.txt into a numpy array called xvals

yvals = np.sin(xvals) # calculates sine of the data

outputdata = np.zeros((len(xvals),2))  
# This line creates a 2-d array and fills it with the value 0.0
outputdata[:,0]= xvals  # Copy our x values into the first column of outputdata
outputdata[:,1]= yvals  # Copy our y values into the second column of outputdata


plt.xlabel('x') # creates a label 'x' for the x-axis
plt.ylabel('y') # creates a label 'y' for the y-axis
plt.title('y = sin(x)') # gives the plot a title
plt.plot(xvals,yvals,'b.-') # Create plot
plt.savefig('sineplot_fig.png', dpi=600) # Save the plot to a file called 
# sineplot_fig.png
plt.show() # Show the plot

np.savetxt('sineplot_output.txt', outputdata, delimiter=',',fmt='%1.4e')  
# Write the contents of outputdata into a file called sineplot_output.txt 
# with x and y values separated by a comma
