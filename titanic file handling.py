import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')

# Using numpy
ages = titanic['age'].fillna(titanic['age'].mean()).to_numpy()
mean_age = np.mean(ages)
max_age = np.max(ages)
min_age = np.min(ages)

print("Average Age:", mean_age)
print("Oldest Passenger:", max_age)
print("Youngest Passenger:", min_age)

# Using pandas
male_deaths = titanic[(titanic['sex'] == 'male') & (titanic['survived'] == 0)]
female_deaths = titanic[(titanic['sex'] == 'female') & (titanic['survived'] == 0)]

print("\nNumber of male deaths:", len(male_deaths))
print("Number of female deaths:", len(female_deaths))

# Using matplotlib
death_counts = titanic[titanic['survived'] == 0]['sex'].value_counts()

plt.bar(death_counts.index, death_counts.values)
plt.title("Number of Deaths by Gender (Titanic)")
plt.xlabel("Gender")
plt.ylabel("Number of Deaths")
plt.show()
