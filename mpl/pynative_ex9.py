sentence = "Learning Python is fun"

vowels = "aeiou"

count = 0

for char in sentence.lower():
    if char in vowels:
        count += 1

print(f"Number of vowels: {count}")