import numpy as np
import matplotlib.pyplot as plt

data_1 = np.array([90,83,90,90,90])
data_2 = np.array([69,69,69,69,69])

standard_error = 3#standard error value in cm
mean_1 = np.mean(data_1)#first mean value
mean_2 = np.mean(data_2) #second mean value

std_1 = np.std(data_1)
std_2 = np.std(data_2)

print(mean_1)
print(mean_2)
print(std_1)
print(std_2)