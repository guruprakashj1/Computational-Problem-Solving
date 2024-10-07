# Movie List Operations

This Python script demonstrates various operations on a list of favorite movies.

## Instructions

1. Create a list of your favorite movies
2. Add a new movie to the end of the list
3. Insert a movie at the beginning of the list
4. Remove a movie from the list
5. Print the movie at index 2
6. Create a new list with the first three movies
7. Create a list of the lengths of each movie title using list comprehension
8. Sort the list of movies alphabetically
9. Reverse the order of the list

## Solution

```python
# 1. Create a list of your favorite movies
movies = ["The Shawshank Redemption", "Inception", "Pulp Fiction", "The Dark Knight", "Forrest Gump"]

# 2. Add a new movie to the end of the list
movies.append("The Matrix")

# 3. Insert a movie at the beginning of the list
movies.insert(0, "Goodfellas")

# 4. Remove a movie from the list
movies.remove("Forrest Gump")

# 5. Print the movie at index 2
print("Movie at index 2:", movies[2])

# 6. Create a new list with the first three movies
first_three = movies[:3]

# 7. Create a list of the lengths of each movie title using list comprehension
title_lengths = [len(title) for title in movies]

# 8. Sort the list of movies alphabetically
movies.sort()

# 9. Reverse the order of the list
movies.reverse()

# Print the final list of movies
print("Final list of movies:", movies)

# Print the list of first three movies
print("First three movies:", first_three)

# Print the list of title lengths
print("Title lengths:", title_lengths)
```

## Output

The script will produce output similar to this:

```
Movie at index 2: Inception
Final list of movies: ['The Shawshank Redemption', 'The Matrix', 'The Dark Knight', 'Pulp Fiction', 'Inception', 'Goodfellas']
First three movies: ['Goodfellas', 'The Shawshank Redemption', 'Inception']
Title lengths: [25, 9, 16, 12, 9, 9]
```

Note: The exact output may vary depending on the initial list of movies and any modifications made to the script.
