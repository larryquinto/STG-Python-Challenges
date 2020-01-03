# Function for nth Fibonacci number with user input

n = (int(input("Enter A Whole Number Greater Than Zero For The Fibonacci Sequence, Please.  Then, Press Enter: ")))

def fibonacci(n):
    if n <= 0:
        print("Sorry!  Please enter a number greater than zero.")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(n))