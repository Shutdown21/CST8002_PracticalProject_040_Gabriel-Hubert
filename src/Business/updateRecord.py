from Presentation.ui import selectRow, getUpdateRecordInput
import sqlite3

DB_FILE = "database.db"

def updateRecord(records, use_database=False):
    """
    Update a record in the records list. Prompts the user to select a row and enter new values for the record fields.

    Args:
        records (list): The list of records to be updated.
    """
    print("Author: Gabriel Hubert")
    try:
        row = selectRow() - 1  # Convert to zero-based index
        
        if use_database:
            connection = sqlite3.connect(DB_FILE)
            cursor = connection.cursor()

            # Fetch the ID from the database
            cursor.execute("SELECT id, csduid, csd, period, indicatorSummaryDescription, unitOfMeasure, originalValue FROM records LIMIT 1 OFFSET ?", (row,))
            result = cursor.fetchone()

            if result:
                record_id, *current_values = result
                new_values = getUpdateRecordInput(current_values)  # Get user input for updates
                
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
            if 0 <= row < len(records):
                record = records[row]
                new_values = getUpdateRecordInput(record)

                # Update the record's attributes
                record.csduid, record.csd, record.period, record.indicatorSummaryDescription, record.unitOfMeasure, record.originalValue = new_values

                print("Record updated successfully.\n")
            else:
                print("Invalid row selection: Out of range\n")

    except ValueError:
        print("Invalid input. Please enter a valid number.\n")