import sqlite3
from Presentation.ui import selectRow, getUpdateRecordInput

DB_FILE = "database.db"

def updateRecord(use_database=True):
    """
    Update a record in the database. Prompts the user to select a row and enter new values for the record fields.

    Args:
        use_database (bool): If True, updates the record in the database.
    """
    print("Author: Gabriel Hubert")
    try:
        row = selectRow() - 1  # Convert to zero-based index
        
        if use_database:
            # Connect to the database
            connection = sqlite3.connect(DB_FILE)
            cursor = connection.cursor()

            # Fetch the ID and current values of the record to update
            cursor.execute("SELECT id, csduid, csd, period, indicatorSummaryDescription, unitOfMeasure, originalValue FROM records LIMIT 1 OFFSET ?", (row,))
            result = cursor.fetchone()

            if result:
                record_id, *current_values = result
                new_values = getUpdateRecordInput(current_values)  # Get new values from the user
                
                # Update the record in the database
                cursor.execute("""
                    UPDATE records
                    SET csduid = ?, csd = ?, period = ?, indicatorSummaryDescription = ?, unitOfMeasure = ?, originalValue = ?
                    WHERE id = ?
                """, (*new_values, record_id))

                connection.commit()
                print(f"Record with ID {record_id} updated successfully in the database.\n")

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
