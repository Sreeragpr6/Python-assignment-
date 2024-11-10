# Fibonacci Sequence Generator

def generate_fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Get the number of terms from the user
try:
    num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
    if num_terms <= 0:
        print("Please enter a positive integer.")
    else:
        fibonacci_sequence = generate_fibonacci(num_terms)
        print(f"Fibonacci sequence with {num_terms} terms: {fibonacci_sequence}")
except ValueError:
    print("Invalid input! Please enter a positive integer.")
