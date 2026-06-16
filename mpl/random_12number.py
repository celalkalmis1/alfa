import random

# Step 1: Create an empty list to store the random numbers
random_numbers = []

# Step 2: Use a loop to generate exactly 12 random integers
# In this example, the numbers will be between 1 and 100 (inclusive)
for _ in range(12):
    number = random.randint(1, 100)
    random_numbers.append(number)

# Step 3: Print the generated list to see the numbers
print("Generated List:", random_numbers)

# Step 4: Calculate the maximum and minimum values using built-in functions
max_value = max(random_numbers)
min_value = min(random_numbers)

# Step 5: Display the results
print("Maximum Value:", max_value)
print("Minimum Value:", min_value)