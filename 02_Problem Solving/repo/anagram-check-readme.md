# Check if the given string is Anagram or NOT

This README file provides a step-by-step procedure to determine whether two given strings are anagrams of each other.

## Problem Statement

Given two strings, determine if they are anagrams of each other.

## Definition

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Step-by-Step Procedure

1. Start with the two given strings, let's call them s1 and s2.

2. If the lengths of s1 and s2 are different, they are NOT anagrams. End the procedure.

3. Convert both strings to lowercase to make the comparison case-insensitive.

4. Remove any non-alphabetic characters and spaces from both strings (optional, depending on requirements).

5. Create a frequency counter (e.g., a hash map or an array) for characters in s1.

6. For each character in s1:
   a. Increment its count in the frequency counter.

7. For each character in s2:
   a. If the character is not in the frequency counter or its count is already 0, the strings are NOT anagrams. End the procedure.
   b. Decrement its count in the frequency counter.

8. If you've processed all characters in s2 without ending the procedure, the strings ARE anagrams.

9. Report the result: either "ANAGRAM" or "NOT ANAGRAM"

## Explanation

- This method checks if two strings have exactly the same characters with the same frequencies.
- Converting to lowercase and removing non-alphabetic characters ensures that "Listen" and "Silent!" are recognized as anagrams.
- The frequency counter keeps track of character occurrences, ensuring each character is used exactly once.

## Examples

1. Let's say the given strings are "listen" and "silent":
   - Both have length 6, continue
   - After lowercase and cleaning: "listen" and "silent"
   - Frequency counter for "listen": {l:1, i:1, s:1, t:1, e:1, n:1}
   - Check "silent" against the counter:
     All characters match and counts reduce to 0
   - "listen" and "silent" are ANAGRAMS

2. If the given strings are "hello" and "world":
   - Both have length 5, continue
   - After lowercase and cleaning: "hello" and "world"
   - Frequency counter for "hello": {h:1, e:1, l:2, o:1}
   - Check "world" against the counter:
     'w' not found in counter, so they are NOT ANAGRAMS

3. If the given strings are "Debit Card" and "Bad Credit":
   - Lengths differ (10 vs 9), but we'll clean them first
   - After lowercase and cleaning: "debitcard" and "badcredit"
   - Both have length 9, continue
   - Frequency counter for "debitcard": {d:2, e:1, b:1, i:1, t:1, c:1, a:1, r:1}
   - Check "badcredit" against the counter:
     All characters match and counts reduce to 0
   - "Debit Card" and "Bad Credit" are ANAGRAMS

This procedure works for any pair of strings.

## Note

- The decision to ignore spaces and punctuation or to consider them significant can vary based on the specific requirements of the problem.
- For very long strings, consider the time and space complexity of your chosen method.
- In some programming languages, you might need to handle Unicode characters specially.
- This method assumes single-byte characters. For languages with multi-byte characters, you might need to adjust the approach.
