import random
import matplotlib.pyplot as plt

random_values= [random.randint(1,10) for _ in range(12)]
months = list(range(1, 13))

plt.bar(months, random_values , color='red', edgecolor='black')

plt.xlabel('Values')
plt.ylabel('Months')
plt.title('the random values')

plt.xticks(months)

plt.grid(True, axis='x', linestyle='--',alpha=0.7)

plt.show()