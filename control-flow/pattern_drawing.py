# pattern_drawing.py
# Draws a square pattern of asterisks using nested loops

# Get user input
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Draw the pattern using while and for loops
while row < size:
    # Print asterisks in the current row
    for col in range(size):
        print("*", end="")
    
    # Move to the next line after completing a row
    print()
    
    # Increment row counter
    row += 1