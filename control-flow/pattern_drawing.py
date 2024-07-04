# Prompt the user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
i = 0

# Use a while loop to iterate through each row
while i < size:
    # Initialize column counter
    j = 0
    # Use a while loop to print asterisks for each column in the row
    while j < size:
        print("*", end="")
        j += 1
    # Print a newline character after each row
    print()
    i += 1