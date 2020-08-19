import numpy as np

p = np.array([9, 8, 7])
q = np.array([3, 2, 4])
print(p + q)
print(p - q)

print("p * q = ", p * q)
print("p / q = ", p / q)
print("p % q = ", p % q)

print(p % 2)
print(p > 8)
print(p < 9)

x = np.array([[2, 1], [1, 3]])
y = np.array([[3, 2], [4, 2]])
print("x: \n", x)
print("y: \n", y)

print(x + y)
print(x - y)
print(x * y)

print(x.dot(y))
print(np.dot(x, y))