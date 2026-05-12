numbers = range(10)

for i in numbers:
    current = numbers[i]
    if current == 0:
        previous = 0
    else:
        previous = current -1
    print(f"{current} + {previous} = {current + previous}")
