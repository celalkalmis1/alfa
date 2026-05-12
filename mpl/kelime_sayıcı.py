text = "Python is a good language. C# is also a good language."

lenght = len(text)

counter = 0
for x in text:

    if(x == "a"):
        counter +=1


print(f"The number of letter a is: {counter}")