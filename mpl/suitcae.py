def how_many_banknotes(height):
    thicness = 0.11 
    number_of_banknotes = round (height / thicness)
    return number_of_banknotes

height_of_column = 1000 #mm
print(how_many_banknotes(height_of_column)) 

def value_of_column(height, denomination):
    return how_many_banknotes(height)*denomination

print(value_of_column(1000 , 1))


#31.03.2026
