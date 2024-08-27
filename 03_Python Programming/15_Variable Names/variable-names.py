# 2-Variable-Names-Example.py

# Good variable naming practices

# 1. Use lowercase with underscores for variable names (snake_case)
user_name = "Alice"
total_score = 95

# 2. Use descriptive names
current_temperature = 25.5  # Better than 'temp' or 't'
is_logged_in = True  # Better than 'flag' or 'status'

# 3. Use plural names for collections
fruits = ["apple", "banana", "cherry"]
user_ages = [25, 30, 35, 28]

# 4. Use verb phrases for function names
def calculate_area(length, width):
    return length * width

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# 5. Use UPPERCASE for constants
PI = 3.14159
MAX_ATTEMPTS = 3

# 6. Use CamelCase for class names
class UserAccount:
    def __init__(self, username, email):
        self.username = username
        self.email = email

# 7. Use a single leading underscore for non-public methods or attributes
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self._mileage = 0  # Internal use

    def _update_mileage(self, miles):
        self._mileage += miles

# 8. Use double leading underscores for name mangling in classes
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

# 9. Avoid single-letter names except for very short loops or mathematical expressions
for i in range(5):  # 'i' is acceptable here
    print(i)

# 10. Use intention-revealing names
is_ready_to_submit = all([form_completed, terms_accepted, captcha_passed])

# 11. Avoid redundant information in names
# Bad: list_of_users = ["Alice", "Bob", "Charlie"]
# Good:
users = ["Alice", "Bob", "Charlie"]

# Example usage
print(f"User: {user_name}, Score: {total_score}")
print(f"Current temperature: {current_temperature}°C")
print(f"Fruits available: {', '.join(fruits)}")
print(f"Area of rectangle: {calculate_area(5, 3)}")
print(f"Is 17 prime? {is_prime(17)}")

user = UserAccount("alice_wonder", "alice@example.com")
print(f"User created: {user.username}")

my_car = Car("Toyota", "Corolla")
my_car._update_mileage(100)  # Note: accessing a non-public method

my_account = BankAccount(1000)
my_account.deposit(500)
# print(my_account.__balance)  # This would raise an AttributeError due to name mangling

print(f"Ready to submit: {is_ready_to_submit}")
