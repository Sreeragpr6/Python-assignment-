# Factorial Calculator

# Iterative method
def factorial_iterative(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Recursive method
def factorial_recursive(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Select method
print("Choose method to calculate factorial:")
print("1. Iterative")
print("2. Recursive")

choice = input("Enter choice (1/2): ")

try:
    number = int(input("Enter a non-negative integer: "))
except ValueError:
    print("Invalid input! Please enter a non-negative integer.")
else:
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    elif choice == '1':
        print(f"The factorial of {number} is {factorial_iterative(number)}")
    elif choice == '2':
        print(f"The factorial of {number} is {factorial_recursive(number)}")
    else:
        print("Invalid choice! Please select 1 or 2.")
