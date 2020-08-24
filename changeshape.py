import numpy as np

tech_companies = np.array([("IBM", "Apple.inc", "Intel", "Dell", "Microsoft"),
                           ("New York", "California", "California", "Texas", "Washinton")])

print(tech_companies)
print(tech_companies.shape)
print(tech_companies.ravel())
print(tech_companies.T)
print(tech_companies.T.ravel())

print(tech_companies.shape)

print(tech_companies.reshape(2, 5))
print(np.arange(18).reshape(3, 6))

companies = np.array(["IBM", "Apple", "Intel", "Sony", "Microsoft", "HP", "Hitachi", "Panasonic"])
print(companies)

print(companies.reshape(-1, 4))
print(companies.reshape(4, -1))