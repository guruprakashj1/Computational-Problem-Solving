# The Minion Game - Solution and Explanation

## Problem Description

Kevin and Stuart want to play "The Minion Game" with the following rules:

1. Both players are given the same string, S.
2. Both players have to make substrings using the letters of the string S.
3. Stuart has to make words starting with consonants.
4. Kevin has to make words starting with vowels.
5. The game ends when both players have made all possible substrings.

**Scoring:** A player gets +1 point for each occurrence of the substring in the string S.

## Solution

Here's a Python solution to the problem:

```python
def minion_game(string):
    vowels = 'AEIOU'
    stuart_score = 0
    kevin_score = 0
    length = len(string)

    for i in range(length):
        if string[i] in vowels:
            kevin_score += length - i
        else:
            stuart_score += length - i

    if stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    elif kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")

# Example usage
minion_game("BANANA")
```

## Explanation

1. We define a function `minion_game` that takes the input string as an argument.

2. We initialize variables:
   - `vowels`: a string containing all vowels
   - `stuart_score` and `kevin_score`: to keep track of each player's score
   - `length`: the length of the input string

3. We iterate through each character in the string using its index:
   
   ```python
   for i in range(length):
   ```

4. For each character, we check if it's a vowel:
   
   ```python
   if string[i] in vowels:
   ```

5. If it's a vowel, Kevin gets points. The number of points is equal to the number of substrings starting with this character, which is `length - i`.

6. If it's not a vowel (i.e., a consonant), Stuart gets points in the same way.

7. After iterating through all characters, we compare the scores and print the result.

## Why This Solution Works

- This solution is efficient because it counts all possible substrings in a single pass through the string.
- For each character, we're essentially counting how many substrings start with that character, which is equal to the number of characters from that position to the end of the string.
- By doing this for all characters and separating vowels and consonants, we get the correct score for both players without explicitly generating all substrings.

## Time Complexity

The time complexity of this solution is O(n), where n is the length of the input string. We only iterate through the string once, making it an efficient solution even for very long strings.

## Space Complexity

The space complexity is O(1) because we only use a fixed amount of additional space regardless of the input size.

To use this solution, simply call the `minion_game` function with your input string. For example:

```python
minion_game("BANANA")
```

This will output the winner and their score, or "Draw" if it's a tie.
