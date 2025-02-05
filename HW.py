# Import the math module to use the sqrt function
import math

# Define a function to calculate the square root
def calculate_square_root(number):
    return math.sqrt(number)

# Get user input
number = float(input("Please enter a number to find its square root: "))

# Calculate the square root
square_root = calculate_square_root(number)

# Display the result
print(f"The square root of {number} is {square_root}")
