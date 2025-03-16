from Presentation.ui import selectRow
import sqlite3

DB_FILE = "database.db"

def deleteRecord(records, use_database=False):
    """
    Delete a record from the records list. Prompts the user to select a row to delete.

    Args:
        records (list): The list of records from which a record will be deleted.
    """
    print("Author: Gabriel Hubert")
    try:
        row = selectRow() - 1  # Convert to zero-based index
        
        if use_database:
            connection = sqlite3.connect(DB_FILE)
            cursor = connection.cursor()

            # Fetch the ID from the database
            cursor.execute("SELECT id FROM records LIMIT 1 OFFSET ?", (row,))
            result = cursor.fetchone()

            if result:
                record_id = result[0]
                cursor.execute("DELETE FROM records WHERE id = ?", (record_id,))
                connection.commit()
                print(f"Record with ID {record_id} deleted successfully from the database.\n")
            else:
                print("Invalid row selection: No record found at that position.\n")

            connection.close()

        else:
            if 0 <= row < len(records):
                deleted_record = records.pop(row)
                print(f"Record deleted successfully: {deleted_record}\n")
            else:
                print("Invalid row selection: Out of range\n")

    except ValueError:
        print("Invalid input. Please enter a valid number.\n")
