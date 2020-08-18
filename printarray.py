import numpy as np

x = np.arange(8)
print(x)

y = np.arange(16).reshape(4, 4)
print(y)

z = np.arange(36).reshape(3, 4, 3)
print(z)

print(np.arange(12100))
print(np.arange(12100).reshape(110, 110))

np.set_printoptions(threshold = np.nan)
print(np.arange(12100).reshape(110, 110))