import numpy as np

angles = np.array([6.0, 12.0, 18.0, 24.0, 36.0])  # our list of incident angles in degrees
n_r = 1.54   # define the refractive index of the glass
n_i = 1.0 # define the refractive index of air

angles = angles * np.pi/180

sin_angles = np.sin(angles)

sin_r = (sin_angles)/n_r

sin_r = np.arcsin(sin_r)

r = sin_r/(np.pi/180)
print(r)