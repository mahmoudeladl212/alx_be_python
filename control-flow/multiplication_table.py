# multiplication_table.py
# Generates a multiplication table for a given number from 1 to 10

# Get user input
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print the multiplication table
print(f"Multiplication table for {number}:")
for i in range(1, 11):  # Loops from 1 to 10
    product = number * i
    print(f"{number} * {i} = {product}")