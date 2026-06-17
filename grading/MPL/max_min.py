my_numbers = [45, 12, 89, 33, 7, 64, 91, 22, 53, 18, 76, 5]

print("My List:", my_numbers)

max_value = my_numbers[0]
min_value = my_numbers[0]

for num in my_numbers:
    if num > max_value:
        max_value = num  
        
    if num < min_value:
        min_value = num  

# Display the final results
print("Maximum Value:", max_value)
print("Minimum Value:", min_value)