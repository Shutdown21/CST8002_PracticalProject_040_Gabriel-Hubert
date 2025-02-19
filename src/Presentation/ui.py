from Business.createRecord import createRecord

def userInterface():
    print("Please select an option:")
    print("1. Load CSV")
    print("2. Save CSV")
    print("3. Select all records")
    print("4. Select a single record")
    print("5. Add a new record")
    print("6. Exit")
    choice = input("Enter your choice: ")
    return choice
                
def selectRow():
    while True:
        try:
            row = int(input("Please select a row: "))
            return row  # Return the integer value
        except ValueError:
             print("Invalid input. Please enter a valid number.\n")

def newRecord(records):
    csduid = input("Enter the CSDUID: ")
    csd = input("Enter the CSD: ")
    period = input("Enter the Period: ")
    indicatorSummaryDescription = input("Enter the Indicator Summary Description: ")
    unitOfMeasure = input("Enter the Unit of Measure: ")
    originalValue = input("Enter the Original Value: ")
    createRecord(csduid, csd, period, indicatorSummaryDescription, unitOfMeasure, originalValue, records)
    print("Record added successfully.")
