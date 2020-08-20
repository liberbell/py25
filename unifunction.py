import numpy as np

circle_radii = np.array([145, 120, 90, 60, 45, 30])

circle_diameters = 2 * circle_radii
print(circle_diameters)

circle_areas = np.pi * circle_radii ** 2
print(circle_areas)

angles_degrees = np.array([0, 30, 60, 90, 120, 150, 180])

angles_radians = angles_degrees * np.pi / 180
print(angles_radians)

print("Sine values: ")
print(np.sin(angles_radians))

print("Cosine values: ")
print(np.cos(angles_radians))