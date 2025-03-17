import sqlite3

DB_FILE = "database.db"

def createRecord(csduid, csd, period, indicatorSummaryDescription, unitOfMeasure, originalValue, use_database=True):
    """
    Create a new record and add it to the database.

    Args:
        csduid (str): The CSDUID of the record.
        csd (str): The CSD of the record.
        period (str): The period of the record.
        indicatorSummaryDescription (str): The indicator summary description of the record.
        unitOfMeasure (str): The unit of measure of the record.
        originalValue (str): The original value of the record.
        use_database (bool): If True, saves the record to the database.

    Returns:
        None
    """
    try:
        if use_database:
            # Connect to the database
            connection = sqlite3.connect(DB_FILE)
            cursor = connection.cursor()

            # Insert the new record into the database
            cursor.execute("""
                INSERT INTO records (csduid, csd, period, indicatorSummaryDescription, unitOfMeasure, originalValue)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (csduid, csd, period, indicatorSummaryDescription, unitOfMeasure, originalValue))

            # Commit the transaction and close the connection
            connection.commit()
            connection.close()

            print("Record successfully added to the database.")
        else:
            print("Error: The 'use_database' flag is set to False, so no database operation was performed.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")