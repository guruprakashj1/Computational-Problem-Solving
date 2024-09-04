# Problem 19: Count the number of vowels and consonants in a string using a for loop and if-elif statements

"""
Explanation: This problem uses a for loop with if-elif statements to categorize characters.
Logic: Check if each character is a vowel or consonant and update counters accordingly.
Algorithm:
1. Input a string
2. Initialize vowel_count and consonant_count to 0
3. For each character in the string:
   a. If character is a vowel, increment vowel_count
   b. Else if character is a consonant, increment consonant_count
4. Print the counts
"""

text = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for char in text:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print(f"Number of vowels: {vowel_count}")
print(f"Number of consonants: {consonant_count}")
