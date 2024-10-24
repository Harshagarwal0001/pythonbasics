print("hello")
# Addition of two integers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = num1 + num2
print("The sum of", num1, "and", num2, "is:", result)
# Subtraction of two integers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = num1 - num2
print("The difference between", num1, "and", num2, "is:", result)
# Division of two integers
num1 = int(input("Enter the numerator: "))
num2 = int(input("Enter the denominator: "))

# Check to avoid division by zero
if num2 != 0:
    result = num1 / num2
    print(num1, "divided by", num2, "is:", result)
else:
    print("Division by zero is not allowed.")
# Multiplication of two integers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = num1 * num2
print("The product of", num1, "and", num2, "is:", result)


a = int(input("num1 = "))
b = int(input("num2 = "))
print("sum =",a+b)
print("subtract =",a-b)
print("multiple =",a*b)
print("divide =",a/b)

# Check if a number is even or odd
num = int(input("Enter an integer: "))

if num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")
