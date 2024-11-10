# Unique Character Finder

def find_unique_characters(s):
    # Convert to lowercase and use a set to find unique characters
    unique_chars = set(s.lower())
    # Filter out non-alphabet characters
    unique_chars = {char for char in unique_chars if char.isalpha()}
    return unique_chars

# Get input from the user
user_input = input("Enter a string to find unique characters: ")

# Find and display unique characters
unique_characters = find_unique_characters(user_input)
print("Unique characters in the string:")
print(" ".join(sorted(unique_characters)))
