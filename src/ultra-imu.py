import numpy as np

DEG2RAD = np.pi/180
RAD2DEG = 180/np.pi

imu_x_tilt = 37.7  # Relative to horizontal
imu_y_tilt = 80.1  

ultra_x = 3.1
ultra_y = 5.2

dist_x = ultra_x * np.cos(imu_x_tilt * DEG2RAD)
dist_y = ultra_y * np.cos(imu_y_tilt * DEG2RAD)
