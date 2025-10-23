import numpy as np

measurements = np.array([99.6 ,90.6, 94.6, 87.6 ,91.6])  # make numpy array of the set of measured values

MeanVal = np.mean(measurements)  #calculate mean value of this set
StDev = np.std(measurements)  # calculate the standard deviation of this set
StDevM = np.sqrt(1/(len(measurements)-1))*StDev

print("mean = ", MeanVal)  # print out the mean.
print("standard deviation = ", StDev)  # print out the standard deviation.calc
print(StDevM)