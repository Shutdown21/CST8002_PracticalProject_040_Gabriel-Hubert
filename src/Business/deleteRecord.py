import sqlite3
from Presentation.ui import selectRow

DB_FILE = "database.db"

def deleteRecord(use_database=True):
    """
    Delete a record from the database. Prompts the user to select a row to delete.

    Args:
        use_database (bool): If True, deletes the record from the database.
    """
    print("Author: Gabriel Hubert")
    try:
        row = selectRow() - 1  # Convert to zero-based index

        if use_database:
            # Connect to the database
            connection = sqlite3.connect(DB_FILE)
            cursor = connection.cursor()

            # Fetch the ID from the database for the selected row
            cursor.execute("SELECT id FROM records LIMIT 1 OFFSET ?", (row,))
            result = cursor.fetchone()

            if result:
                record_id = result[0]

                # Delete the record from the database
                cursor.execute("DELETE FROM records WHERE id = ?", (record_id,))
                connection.commit()

                print(f"Record with ID {record_id} deleted successfully from the database.\n")
            else:
                print("Invalid row selection: No record found at that position.\n")

            connection.close()

        else:
            print("Error: The 'use_database' flag is set to False, so no database operation was performed.")

    except ValueError:
        print("Invalid input. Please enter a valid number.\n")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
