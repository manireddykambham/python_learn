x=10
print("Outside function, x is:", x)
def my_function():
    global x # Declare x as global to modify it so after function call it will be 20
    x = 20
    print("Inside function, x is:", x)
print("Before calling function, x is:", x)
my_function()
print("After calling function, x is:", x)