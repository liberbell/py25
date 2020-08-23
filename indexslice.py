import numpy as np

x = np.arange(10) ** 3
print(x)

print(x[3])
print(x[-4])
print(x[1:8])
print(x[3:-3])
print(x[:8])
print(x[ : 10 : 2])
print(x[::-1])

companies = ([["Capcon", "Microsoft", "IBM", "Spotify", "Filipkart"],
             [1938, 1975, 1911, 2006, 2007],
             [489000, 1310000, 380000, 3000, 30000]])

print(companies)
# companies[0:2, 2:4]
# print(companies[0])
# print(companies[0, 2])