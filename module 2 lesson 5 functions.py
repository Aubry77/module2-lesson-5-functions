"""This program demonstrates the use of functions in Python."""


# Define functions for each arithmetic operation
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero"
    return num1 / num2

# Main program loop
while True:
    print("Choose an operation: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == "5":
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print(f"Result: {add(num1, num2)}")
    elif choice == "2":
        print(f"Result: {subtract(num1, num2)}")
    elif choice == "3":
        print(f"Result: {multiply(num1, num2)}")
    elif choice == "4":
        print(f"Result: {divide(num1, num2)}")
    else:
        print("Invalid choice")

    """Shopping List Program
    """

# Initialize empty shopping list
shopping_list = []

# Define functions for shopping list operations
def add_item():
    item = input("Enter item to add: ")
    shopping_list.append(item)

def remove_item():
    item = input("Enter item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
    else:
        print("Item not found in list")

def print_list():
    print("Shopping List:")
    for i, item in enumerate(shopping_list, start=1):
        print(f"{i}. {item}")

# Main program loop
while True:
    print("Choose an option: ")
    print("1. Add item")
    print("2. Remove item")
    print("3. Print list")
    print("4. Quit")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == "4":
        break

    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        print_list()
    else:
        print("Invalid choice")
