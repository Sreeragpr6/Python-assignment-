# Palindrome Checker

def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
    # Check if the cleaned string is the same forwards and backwards
    return cleaned_string == cleaned_string[::-1]

# Get input from user
user_input = input("Enter a string to check if it's a palindrome: ")

# Check and display result
if is_palindrome(user_input):
    print("The entered string is a palindrome!")
else:
    print("The entered string is not a palindrome.")
