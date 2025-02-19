from Presentation.ui import selectRow, getUpdateRecordInput

def updateRecord(records):
    print("Author: Gabriel Hubert")
    try:
        row = selectRow() - 1 
        if 0 <= row < len(records):
            record = records[row]
            new_values = getUpdateRecordInput(record)

            # Update the record
            record.csduid, record.csd, record.period, record.indicatorSummaryDescription, record.unitOfMeasure, record.originalValue = new_values
            
            print("Record updated successfully.\n")
        else:
            print("Invalid row selection: Out of range\n")
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")