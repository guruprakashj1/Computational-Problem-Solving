# Problem 20: Find the longest word in a sentence using a for loop and if statement

"""
Explanation: This problem uses a for loop to iterate through words and an if statement to compare lengths.
Logic: Split the sentence into words and keep track of the longest word encountered.
Algorithm:
1. Input a sentence
2. Split the sentence into words
3. Initialize longest_word to an empty string
4. For each word in the list of words:
   a. If length of word > length of longest_word, update longest_word
5. Print the longest word
"""

sentence = input("Enter a sentence: ")
words = sentence.split()
longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print(f"The longest word is: {longest_word}")
