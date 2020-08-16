import numpy as np

array_one = np.array([0, 1, 3, 5, 7, 9])
print(array_one)

num = [11, 22, 33, 44, 55, 66, 77]
array_two = np.array(num)
print(array_two)

array_of_zeroes = np.zeros((2, 3))
print(array_of_zeroes)

array_of_ones = np.ones((3, 2))
print(array_of_ones)

array_of_ones = np.ones((3, 2), dtype=np.int32)
print(array_of_ones)

array_empty = np.empty((3, 2))
print(array_empty)

array_eye = np.eye(4)
print(array_eye)

array_of_evens = np.arange(2, 24, 2)
print(array_of_evens)

array_of_floats = np.arange(1, 3, 0.3)
print(array_of_floats)

array_2D = np.array([(3, 4, 6), (2, 1, 6)])
print(array_2D)
print(array_2D.shape)