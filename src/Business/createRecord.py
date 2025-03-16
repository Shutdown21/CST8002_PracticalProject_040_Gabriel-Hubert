from Model.record import Record
import sqlite3

DB_FILE = "database.db"

def createRecord(csduid, csd, period, indicatorSummaryDescription, unitOfMeasure, originalValue, records, use_database=False):
    """
    Create a new record and add it to the records list.

    Args:
        csduid (str): The CSDUID of the record.
        csd (str): The CSD of the record.
        period (str): The period of the record.
        indicatorSummaryDescription (str): The indicator summary description of the record.
        unitOfMeasure (str): The unit of measure of the record.
        originalValue (str): The original value of the record.
        records (list): The list of records to which the new record will be added.

    Returns:
        list: The updated list of records with the new record added.
    """
    if use_database:
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO records (csduid, csd, period, indicatorSummaryDescription, unitOfMeasure, originalValue)
            VALUES (?, ?, ?, ?, ?, ?) """, (csduid, csd, period, indicatorSummaryDescription, unitOfMeasure, originalValue))

        connection.commit()
        connection.close()
        print("Record successfully added to the database.")

    else:
        new_record = Record(csduid, csd, period, indicatorSummaryDescription, unitOfMeasure, originalValue)
        records.append(new_record)
        print("Record successfully added to the in-memory list.")
        return records
