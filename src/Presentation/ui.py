from Business.createRecord import createRecord

def userInterface():
    print("Please select an option:")
    print("1. Load CSV")
    print("2. Save CSV")
    print("3. Select all records")
    print("4. Select a single record")
    print("5. Add a new record") 
    print("6. Update a record")       
    print("7. Exit")
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

def getUpdateRecordInput(record):
    print(f"Editing Record: {record}")
    print("Leave blank to keep the current value.")
    new_csduid = input(f"New CSDUID (Current: {record.csduid}): ") or record.csduid
    new_csd = input(f"New CSD (Current: {record.csd}): ") or record.csd
    new_period = input(f"New Period (Current: {record.period}): ") or record.period
    new_indicator = input(f"New Indicator Summary Description (Current: {record.indicatorSummaryDescription}): ") or record.indicatorSummaryDescription
    new_unit = input(f"New Unit of Measure (Current: {record.unitOfMeasure}): ") or record.unitOfMeasure
    new_original_value = input(f"New Original Value (Current: {record.originalValue}): ") or record.originalValue
    
    return new_csduid, new_csd, new_period, new_indicator, new_unit, new_original_value