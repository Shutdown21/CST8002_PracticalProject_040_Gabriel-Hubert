from Business.createRecord import createRecord

def userInterface():
    """
    Display the user interface menu and get the user's choice.

    Returns:
        str: The user's choice as a string.
    """
    print("Please select an option:")
    print("1. Load CSV")
    print("2. Save CSV")
    print("3. Select all records")
    print("4. Select a single record")
    print("5. Add a new record") 
    print("6. Update a record")    
    print("7. Delete a record")
    print("8. Search records")
    print("9. Exit")   
    choice = input("Enter your choice: ")
    return choice
                
def selectRow():
    """
    Prompt the user to select a row by entering a number.

    Returns:
        int: The selected row number.
    """
    while True:
        try:
            row = int(input("Please select a row: "))
            return row  # Return the integer value
        except ValueError:
             print("Invalid input. Please enter a valid number.\n")

def newRecord():
    """
    Prompt the user to enter details for a new record and add it to the records list.

    Args:
        records (list): The list of records to which the new record will be added.
    """
    csduid = input("Enter the CSDUID: ")
    csd = input("Enter the CSD: ")
    period = input("Enter the Period: ")
    indicatorSummaryDescription = input("Enter the Indicator Summary Description: ")
    unitOfMeasure = input("Enter the Unit of Measure: ")
    originalValue = input("Enter the Original Value: ")
    createRecord(csduid, csd, period, indicatorSummaryDescription, unitOfMeasure, originalValue)
    print("Record added successfully.")

def getUpdateRecordInput(current_values):
    """
    Prompt the user to enter new values for the fields of a record. Leave blank to keep the current value.

    Args:
        current_values (tuple): The current values of the record fields.

    Returns:
        tuple: The updated values for the record fields.
    """
    print(f"Editing Record: {current_values}")
    print("Leave blank to keep the current value.")
    
    # Prompt for new values, defaulting to current ones if left blank
    new_csduid = input(f"New CSDUID (Current: {current_values[0]}): ") or current_values[0]
    new_csd = input(f"New CSD (Current: {current_values[1]}): ") or current_values[1]
    new_period = input(f"New Period (Current: {current_values[2]}): ") or current_values[2]
    new_indicator = input(f"New Indicator Summary Description (Current: {current_values[3]}): ") or current_values[3]
    new_unit = input(f"New Unit of Measure (Current: {current_values[4]}): ") or current_values[4]
    new_original_value = input(f"New Original Value (Current: {current_values[5]}): ") or current_values[5]
    
    return new_csduid, new_csd, new_period, new_indicator, new_unit, new_original_value