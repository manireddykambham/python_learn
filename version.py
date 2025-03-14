import sys

print("Python version:", sys.version)
if 5>2:
    print("5 is greater than 2")

x = 5
y = 10
if x < y:
    print("x is less than y")

X=2
y="hello"
z='world'
a=1.0
print("X is", X," and x is ", x)
print(type(X), type(x), type(y), type(z), type(a))

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
print(myvar, my_var, _my_var, myVar, MYVAR, myvar2)
fruits = ["apple", "banana", "cherry"]#if added more in list it will thorw error
x, y, z = fruits
print(x)
print(y)
print(z)
