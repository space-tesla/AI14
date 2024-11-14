# Q.1 Write a Python program to sort the words in a sentence in alphabetical order.

def sort_sentence(sentence):
    words = sentence.split()
    words.sort(key=str.lower)
    sorted_sentence = " ".join(words)
    return sorted_sentence
sentence = input("Enter a sentence: ")

sorted_sentence = sort_sentence(sentence)
print("Sorted sentence:", sorted_sentence)


#Output:
#Enter a sentence: The quick brown fox jumps over the lazy dog
#Sorted sentence: brown dog fox jumps lazy over quick the The
