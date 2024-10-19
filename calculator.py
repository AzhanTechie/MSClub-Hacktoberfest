# calculator.py
# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract b from a
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide a by b
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# Function to calculate the modulus (remainder)
def modulus(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a % b

# Function to calculate the exponentiation (a raised to the power of b)
def power(a, b):
    return a ** b

# Function to display the available operations
def display_operations():
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Exponentiation")

# Function to get valid input from the user for numbers
def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

# Main function to run the calculator
def calculator():
    display_operations()
    
    # Get the operation choice from the user
    while True:
        try:
            choice = int(input("Enter the number corresponding to the operation: "))
            if choice < 1 or choice > 6:
                print("Invalid choice, please select between 1 and 6.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
    
    # Get the two numbers from the user
    num1 = get_number_input("Enter the first number: ")
    num2 = get_number_input("Enter the second number: ")

    # Perform the calculation based on user choice
    if choice == 1:
        result = add(num1, num2)
    elif choice == 2:
        result = subtract(num1, num2)
    elif choice == 3:
        result = multiply(num1, num2)
    elif choice == 4:
        result = divide(num1, num2)
    elif choice == 5:
        result = modulus(num1, num2)
    elif choice == 6:
        result = power(num1, num2)
    
    print(f"The result is: {result}")

# Main entry point
if __name__ == "__main__":
    print("Basic Calculator is ready!")
    calculator()

