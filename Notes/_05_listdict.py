from collections import defaultdict

# Step 1: Create a list of words
words = ["apple", "banana", "apple", "cherry", "banana", "apple", "date"]

# Step 2: Count the frequency of each word and store it in a dictionary
word_frequency = defaultdict(int)

for word in words:
    word_frequency[word] += 1

# Step 3: Sort the dictionary by frequency in descending order
sorted_words = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)

# Step 4: Print the sorted words
for word, frequency in sorted_words:
    print(f"{word}: {frequency}")
