import numpy as np

circle_radii = np.array([145, 120, 90, 60, 45, 30])

circle_diameters = 2 * circle_radii
print(circle_diameters)

circle_areas = np.pi * circle_radii ** 2
print(circle_areas)