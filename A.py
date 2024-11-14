# Q.1 Write a Python program to sort the words in a sentence in alphabetical order.

# Function to sort words in a sentence alphabetically (ignoring case)
def sort_sentence(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Sort words alphabetically, ignoring case
    words.sort(key=str.lower)
    # Join sorted words into a sentence
    sorted_sentence = " ".join(words)
    return sorted_sentence

# Accept a sentence from the user
sentence = input("Enter a sentence: ")

# Sort the words in the sentence
sorted_sentence = sort_sentence(sentence)
print("Sorted sentence:", sorted_sentence)


Output:
Enter a sentence: The quick brown fox jumps over the lazy dog
Sorted sentence: brown dog fox jumps lazy over quick the The
