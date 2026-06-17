def check_triangle(a, b, c):
    # Check if all sides are greater than 0
    if a <= 0 or b <= 0 or c <= 0:
        return False
        
    # Check the triangle rule: sum of two sides must be greater than the third
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False

# Testing the function
print(check_triangle(3, 4, 5))   # This will print True
print(check_triangle(1, 2, 3))   # This will print False
print(check_triangle(10, 2, 2))  # This will print False
print(check_triangle(0, 5, 5))   # This will print False