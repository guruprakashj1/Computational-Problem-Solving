# 13- Infinite Loops
# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# This program demonstrates various aspects of infinite loops in Python

import time

# 1. Basic infinite loop with a break condition
print("1. Basic infinite loop with a break condition:")
count = 0
while True:
    print(count, end=" ")
    count += 1
    if count >= 5:
        break
print("\nLoop ended\n")

# 2. Infinite loop with user input for exit
print("2. Infinite loop with user input for exit:")
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input.lower() == 'quit':
        break
    print(f"You entered: {user_input}")
print("Loop ended\n")

# 3. Infinite loop with a flag variable
print("3. Infinite loop with a flag variable:")
is_running = True
count = 0
while is_running:
    print(count, end=" ")
    count += 1
    if count >= 5:
        is_running = False
print("\nLoop ended\n")

# 4. Simulating a simple game loop
print("4. Simulating a simple game loop:")
game_running = True
player_health = 100
turns = 0

while game_running:
    print(f"Turn {turns + 1}: Player health: {player_health}")
    player_health -= 10
    turns += 1
    
    if player_health <= 0:
        print("Game Over!")
        game_running = False
    
    if turns >= 5:
        print("Exiting game loop for demonstration")
        break

    # Simulate game processing time
    time.sleep(0.5)
print()

# 5. Infinite loop with exception handling
print("5. Infinite loop with exception handling:")
while True:
    try:
        x = int(input("Enter a number (non-integer to exit): "))
        print(f"You entered: {x}")
    except ValueError:
        print("Invalid input. Exiting loop.")
        break
print()

# 6. Demonstrating the danger of unintentional infinite loops
print("6. Demonstrating the danger of unintentional infinite loops:")
print("Uncomment the following code to see an unintentional infinite loop:")
# i = 0
# while i < 5:
#     print(i)
#     # Oops! Forgot to increment i
print("This loop would run forever because 'i' is never incremented.")
print()

# 7. Using an infinite loop for a simple menu system
print("7. Using an infinite loop for a simple menu system:")
while True:
    print("\nMenu:")
    print("1. Say Hello")
    print("2. Say Goodbye")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    
    if choice == '1':
        print("Hello!")
    elif choice == '2':
        print("Goodbye!")
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

print("\nProgram ended.")

# This program covers various aspects of infinite loops in Python,
# demonstrating their uses, control mechanisms, and potential pitfalls.
