from Presentation.ui import selectRow

def deleteRecord(records):
    """
    Delete a record from the records list. Prompts the user to select a row to delete.

    Args:
        records (list): The list of records from which a record will be deleted.
    """
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
