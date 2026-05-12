def add(a, b):
    return a + b

def multi(a, b):
    return a * b

def devide(a, b):
    if b == 0:
        print("You can't devide by 0")
    else:
        return a/b
    
def triangle(a, b):
    return (a*b)/2

def rectangle(a, b):
    return a*b

def trapez(a, b ,h):
    return ((a+b)*h)/2

def new_rectangle(a,b,c,d):
    return ((c*d)-(((a*b)/2)*4))

a= 2
b= 2
c= 6
d= 12
h= 5
print(f"{a} + {b} = {add(a,b)}")

print(f"{a} * {b} = {multi(a,b)}")

print(f"{a} / {b} = {devide(a,b)}")

print(f"Volume of the triangle = {triangle(a,b)}")

print(f"Volume of the rectangle = {rectangle(a,b)}")

print(f"Volume of the trapez = {trapez(a,b,h)}")

print(f"Volume of the new_rectangle  = {new_rectangle(a,b,c,d)}")


#31.03.2026