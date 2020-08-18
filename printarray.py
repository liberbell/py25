import numpy as np

x = np.arange(8)
print(x)

y = np.arange(16).reshape(4, 4)
print(y)

z = np.arange(36).reshape(3, 4, 3)
print(z)

print(np.arange(12100))
print(np.arange(12100).reshape(110, 110))

# np.set_printoptions(threshold = 110)
print(np.arange(121).reshape(11, 11))
print(np.arange(100).reshape(10, 10))

np.set_printoptions(threshold = 50)
print(np.arange(100).reshape(10, 10))