# Word Frequency Counter

def count_word_frequency(text):
    # Convert text to lowercase and split into words
    words = text.lower().split()
    frequency = {}

    # Count each word
    for word in words:
        # Remove punctuation from each word
        word = ''.join(char for char in word if char.isalnum())
        if word:
            frequency[word] = frequency.get(word, 0) + 1
    
    return frequency

# Get text input from the user
text_input = input("Enter a text to count word frequencies: ")

# Count and display word frequencies
word_frequencies = count_word_frequency(text_input)
print("Word frequencies:")
for word, count in word_frequencies.items():
    print(f"{word}: {count}")
