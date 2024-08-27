# 12- While Loops
# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# This program demonstrates various aspects of while loops in Python

# 1. Basic while loop
print("1. Basic while loop:")
count = 0
while count < 5:
    print(count, end=" ")
    count += 1  # Increment count to avoid infinite loop
print("\n")

# 2. While loop with user input
print("2. While loop with user input:")
user_input = ""
while user_input != "quit":
    user_input = input("Enter a word (or 'quit' to exit): ")
    print(f"You entered: {user_input}")
print("Loop ended\n")

# 3. While loop with break statement
print("3. While loop with break statement:")
number = 0
while True:
    print(number, end=" ")
    number += 1
    if number >= 5:
        break  # Exit the loop when number reaches 5
print("\nLoop ended with break\n")

# 4. While loop with continue statement
print("4. While loop with continue statement:")
number = 0
while number < 5:
    number += 1
    if number == 3:
        continue  # Skip the rest of the loop body for number 3
    print(number, end=" ")
print("\nLoop ended\n")

# 5. While-else construction
print("5. While-else construction:")
count = 0
while count < 3:
    print(count, end=" ")
    count += 1
else:
    print("\nLoop completed normally")
print()

# 6. Nested while loops
print("6. Nested while loops:")
i = 1
while i <= 3:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i += 1
print()

# 7. Using while loop for input validation
print("7. Input validation with while loop:")
while True:
    try:
        age = int(input("Enter your age: "))
        if 0 <= age <= 120:
            print(f"Your age is {age}")
            break
        else:
            print("Please enter a valid age between 0 and 120")
    except ValueError:
        print("Please enter a valid integer")
print()

# 8. Using while loop to implement a simple menu
print("8. Simple menu with while loop:")
menu_active = True
while menu_active:
    print("\nMenu:")
    print("1. Say Hello")
    print("2. Say Goodbye")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    if choice == "1":
        print("Hello!")
    elif choice == "2":
        print("Goodbye!")
    elif choice == "3":
        print("Exiting...")
        menu_active = False
    else:
        print("Invalid choice. Please try again.")

# This program covers various aspects of while loops in Python,
# demonstrating their versatility and common use cases.
