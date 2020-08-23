import numpy as np

x = np.arange(10)**3
print(x)

for i in x:
    print(i)

companies = np.array([["Capcon", "Microsoft", "IBM", "Spotify", "Filipkart"],
             [1938, 1975, 1911, 2006, 2007],
             [489000, 1310000, 380000, 3000, 30000]])

i = 0
for row in companies:
    print("Row", i, ": ", row)
    i += 1

print(companies.flatten())

for data in companies.flatten(order = "F"):
    print(data)

num = np.arange(16).reshape(4, 4)
print(num)