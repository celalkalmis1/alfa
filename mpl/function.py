def cm2feet(cm):
    inc = int(cm / 2.54)
    feet = int(inc / 30.48)
    return f"{feet} feet {inc} inches"


print(cm2feet(150))
print(cm2feet(190))
print(cm2feet(175))
