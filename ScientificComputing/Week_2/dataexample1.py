import numpy as np  

measurements = [32.2, 34.5, 34.3, 33.7, 35.1, 33.5, 34.6, 34.7, 34.6, 33.9]  # this is our list of measurements
measurements_np = np.array(measurements)

measurements_np = (measurements_np + 5)**2


print(measurements)
print(measurements_np)