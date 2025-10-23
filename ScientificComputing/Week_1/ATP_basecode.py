import numpy as np  
import matplotlib.pyplot as plt


a = 9.8 # acceleration due to gravity in m/s^2
s = 0.55 # alien starting height in m 

t = np.sqrt(2 * s / a)  # define the equation for t

plt.xlabel('x')
plt.ylabel('y')
plt.plot(x,y)
plt.show()





#print ("Time to fall to ground = ", t, "s") 
# prints the text string "Time to fall to ground = ", 
# then the value of t, then the text string "s"