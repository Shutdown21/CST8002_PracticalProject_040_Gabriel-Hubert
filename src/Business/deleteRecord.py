from Presentation.ui import selectRow

def deleteRecord(records):
    print("Author: Gabriel Hubert")
    try:
        row = selectRow() - 1
        if 0 <= row < len(records):
            deleted_record = records.pop(row)
            print(f"Record deleted successfully: {deleted_record}\n")
        else:
            print("Invalid row selection: Out of range\n")
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")
