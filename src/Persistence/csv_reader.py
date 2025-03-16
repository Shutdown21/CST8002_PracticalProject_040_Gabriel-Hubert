import csv
import uuid
from Model.record import Record  # Import the Record class from record.py
from Presentation.ui import selectRow
import sqlite3

DB_FILE = "database.db"
file_path = "src/dailyvehiclesdownload.csv"  # CSV file location

def loadRecords(use_database=True):
    """
    Load records from a CSV file.

    Returns:
        list: A list of Record objects loaded from the CSV file.
    """
    records = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)

            # Connect to database if using database storage
            connection = None
            cursor = None
            if use_database:
                connection = sqlite3.connect(DB_FILE)
                cursor = connection.cursor()

                # Create table if not exists
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS records (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        csduid TEXT,
                        csd TEXT,
                        period TEXT,
                        indicatorSummaryDescription TEXT,
                        unitOfMeasure TEXT,
                        originalValue TEXT
                    )
                """)

            for index, row in enumerate(csv_reader):
                if index >= 100:  # Stop reading after 100 records
                    break

                if use_database:
                    # Insert into database
                    cursor.execute("""
                        INSERT INTO records (csduid, csd, period, indicatorSummaryDescription, unitOfMeasure, originalValue) 
                        VALUES (?, ?, ?, ?, ?, ?)
                    """, (row['CSDUID'], row['CSD'], row['Period'], row['IndicatorSummaryDescription'], row['UnitOfMeasure'], row['OriginalValue']))
                else:
                    # Create Record object and store in-memory
                    record = Record(
                        csduid=row['CSDUID'],
                        csd=row['CSD'],
                        period=row['Period'],
                        indicatorSummaryDescription=row['IndicatorSummaryDescription'],
                        unitOfMeasure=row['UnitOfMeasure'],
                        originalValue=row['OriginalValue']
                    )
                    records.append(record)

            if use_database:
                connection.commit()
                connection.close()
                print(f"Loaded {index + 1} records into the database successfully.")
            else:
                print(f"Loaded {len(records)} records from {file_path} successfully.")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except KeyError as e:
        print(f"Error: Missing expected column in CSV file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return records if not use_database else None

def save_data(records=None, use_database=True):
    """
    Persist the records to a new CSV file with a unique name.

    Args:
        records (list): The list of records to be saved.
    """
    # Generate a unique filename using UUID, placed in the src directory
    unique_filename = f"src/records_{uuid.uuid4().hex}.csv"
    
    try:
        with open(unique_filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["CSDUID", "CSD", "Period", "IndicatorSummaryDescription", "UnitOfMeasure", "OriginalValue"])

            if use_database:
                connection = sqlite3.connect(DB_FILE)
                cursor = connection.cursor()

                cursor.execute("SELECT csduid, csd, period, indicatorSummaryDescription, unitOfMeasure, originalValue FROM records")
                db_records = cursor.fetchall()
                
                for record in db_records:
                    writer.writerow(record)

                connection.close()
            else:
                for record in records:
                    writer.writerow([
                        record.csduid,
                        record.csd,
                        record.period,
                        record.indicatorSummaryDescription,
                        record.unitOfMeasure,
                        record.originalValue
                    ])

        print(f"Data successfully saved to {unique_filename}")
    
    except Exception as e:
        print(f"Error saving data: {e}")

def printAllRecords(records, use_database=False):
    """
    Print all records to the console.

    Args:
        records (list): The list of records to be printed.
    """
    print("Author: Gabriel Hubert")
    print("Records:")
    print("CSDUID, CSD, Period, IndicatorSummaryDescription, UnitOfMeasure, OriginalValue")
    if use_database:
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        
        cursor.execute("SELECT csduid, csd, period, indicatorSummaryDescription, unitOfMeasure, originalValue FROM records")
        db_records = cursor.fetchall()

        if not db_records:
            print("No records found in the database.\n")
        else:
            for index, record in enumerate(db_records):
                if index > 0 and index % 10 == 0:  # Every 10 records
                    print("\nProgram by Gabriel Hubert\n") 
                print(", ".join(map(str, record)))

        connection.close()
    else:
        for index, record in enumerate(records):
            if index > 0 and index % 10 == 0:  # Every 10 records
                print("\nProgram by Gabriel Hubert\n") 
            print(f"{record.csduid}, {record.csd}, {record.period}, {record.indicatorSummaryDescription}, {record.unitOfMeasure}, {record.originalValue}")

def printSingleRecord(records, use_database=False):
    """
    Print a single record to the console based on user selection.

    Args:
        records (list): The list of records to select from.
    """
    print("Author: Gabriel Hubert")
    try:
        row = selectRow() - 1  # Convert to zero-based index

        if use_database:
            connection = sqlite3.connect(DB_FILE)
            cursor = connection.cursor()

            # Fetch a single record using OFFSET
            cursor.execute("SELECT csduid, csd, period, indicatorSummaryDescription, unitOfMeasure, originalValue FROM records LIMIT 1 OFFSET ?", (row,))
            record = cursor.fetchone()

            if record:
                print(", ".join(map(str, record)))
            else:
                print("Invalid row selection: No record found at that position.\n")

            connection.close()
        else:
            if 0 <= row < len(records):
                print(f"{records[row]}")
            else:
                print("Invalid row selection: Out of range\n")

    except ValueError:
        print("Invalid input. Please enter a valid number.\n")