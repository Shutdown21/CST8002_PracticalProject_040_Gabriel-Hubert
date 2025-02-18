def userInterface():
    print("Please select an option:")
    print("1. Load CSV")
    print("2. Save CSV")
    print("3. Select all records")
    print("4. Select a single record")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice
                
def selectRow():
    while True:
        try:
            row = int(input("Please select a row: "))
            return row  # Return the integer value
        except ValueError:
             print("Invalid input. Please enter a valid number.")