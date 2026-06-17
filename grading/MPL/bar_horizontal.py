import random
import matplotlib.pyplot as plt

random_values = [random.randint(1, 100) for _ in range(30)]
indices = list(range(1, 31))

plt.barh(indices, random_values, color='b')
plt.xlabel('Random Values')
plt.ylabel('Index Number')
plt.title('Values')
plt.grid(True)
plt.show()