import numpy as np  

a = 9.8 # acceleration due to gravity in m/s^2
s = 0.645 # alien starting height in m 

t = np.sqrt(2 * s / a) # define the equation for t

v = s / t #define the equation for velocity

print ("Time to fall to ground = ", t, "s") 
# prints the text string "Time to fall to ground = ", 
# then the value of t, then the text string "s"
print("The velocity of the alien is = ", v, "m/s")
# prints the text string "The velocity of the alien is
# prints the value of v then the units associated