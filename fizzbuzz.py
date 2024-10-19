# fizzbuzz.py
# Function to check divisibility by 3 and 5
def check_fizzbuzz(i):
    if i % 3 == 0 and i % 5 == 0:
        return "FizzBuzz"
    elif i % 3 == 0:
        return "Fizz"
    elif i % 5 == 0:
        return "Buzz"
    else:
        return str(i)

# Function to print the result of each number
def print_result(result):
    print(result)

# Function to perform the FizzBuzz logic
def fizzbuzz(n):
    for i in range(1, n + 1):
        result = check_fizzbuzz(i)
        print_result(result)

# Main function to execute the program
if __name__ == "__main__":
    fizzbuzz(20)

