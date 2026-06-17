import random
import matplotlib.pyplot as plt

random_values = [random.randint(1, 100) for _ in range(30)]
indices = list(range(1, 31))

plt.bar(indices, random_values, color='b')
plt.xlabel('Index Number')
plt.ylabel('Random Values')
plt.title('Values')
plt.grid(True)
plt.show()