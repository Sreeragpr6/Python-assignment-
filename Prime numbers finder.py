# Prime Number Finder

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Get range from user
try:
    start_range = int(input("Enter the start of the range: "))
    end_range = int(input("Enter the end of the range: "))
except ValueError:
    print("Invalid input! Please enter integer values.")
else:
    if start_range > end_range:
        print("The start of the range must be less than or equal to the end.")
    else:
        primes = find_primes_in_range(start_range, end_range)
        print(f"Prime numbers between {start_range} and {end_range} are: {primes}")
