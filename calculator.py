def add(x,y):
    return x + y 
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    if y == 0:
        return "Error! Duivision by zero."
    return x / y
def power(x,y):
    return x ** y

print("===SIMPLE CALCULATOR===")
print("Choose the operation: ")
print("1. Addition (+) ")
print("2. Subtration (-) ")
print("3. Multiplication (*) ")
print("4. Division (/) ")
print("5. Exponent (^) ")

oprtr = input("Enter your choice(1, 2, 3, 4, 5): ")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if oprtr == '1':
    result = add(a,b)
elif oprtr == '2':
    result = subtract(a,b)
elif oprtr == '3':
    result = multiply(a,b)
elif oprtr == '4':
    result = divide(a,b)
elif oprtr == '5':
    result = a ** b
else:
    result = "Invalid Operator."
print("Result = ", result)
