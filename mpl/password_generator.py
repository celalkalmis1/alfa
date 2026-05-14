import random

N = 12

characters = ["a","b","d","e","f","g","i","j","1","2","3","4","X","Y","Z","$",".","#"]
password = ""
for i in range(N):
    password += random.choice(characters)

print(password)