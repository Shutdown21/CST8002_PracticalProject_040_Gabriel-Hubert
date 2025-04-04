import csv
import uuid
from Presentation.ui import selectRow
import sqlite3

DB_FILE = "database.db"
file_path = "src/dailyvehiclesdownload.csv"  # CSV file location

def loadRecords():
    """
    Load records from a CSV file.

    Returns: A list of Record objects loaded from the CSV file.
    """
    try:
        # Connect to the database
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()

        # Open the CSV file
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)

            for index, row in enumerate(csv_reader):
                if index >= 100:  # Stop after 100 records
                    break

                # Insert each row into the database
                cursor.execute("""
                    INSERT INTO records (csduid, csd, period, indicatorSummaryDescription, unitOfMeasure, originalValue) 
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (row['CSDUID'], row['CSD'], row['Period'], row['IndicatorSummaryDescription'], row['UnitOfMeasure'], row['OriginalValue']))

        # Commit and close the connection
        connection.commit()
        connection.close()

        print(f"Successfully loaded records from {file_path} into the database.")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def save_data():
    """
    Persist the records to a new CSV file with a unique name.

    Args:
        records (list): The list of records to be saved.
    """
    # Generate a unique filename using UUID, placed in the src directory
    unique_filename = f"src/records_{uuid.uuid4().hex}.csv"
    
    try:
        # Connect to the database
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()

        # Retrieve all records from the database
        cursor.execute("SELECT csduid, csd, period, indicatorSummaryDescription, unitOfMeasure, originalValue FROM records")
        db_records = cursor.fetchall()

        # Check if there are records
        if not db_records:
            print("No records found in the database to save.")
            connection.close()
            return

        # Open the CSV file for writing
        with open(unique_filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # Write the header row
            writer.writerow(["CSDUID", "CSD", "Period", "IndicatorSummaryDescription", "UnitOfMeasure", "OriginalValue"])

            # Write all records to the CSV
            for record in db_records:
                writer.writerow(record)

        # Close the database connection
        connection.close()

        print(f"Data successfully saved to {unique_filename}")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def printAllRecords():
    """
    Print all records to the console.

    Args:
        records (list): The list of records to be printed.
    """
    print("Author: Gabriel Hubert")
    print("Records:")
    print("CSDUID, CSD, Period, IndicatorSummaryDescription, UnitOfMeasure, OriginalValue")
    try:
        # Connect to the database
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()

        # Retrieve all records from the database
        cursor.execute("SELECT csduid, csd, period, indicatorSummaryDescription, unitOfMeasure, originalValue FROM records")
        db_records = cursor.fetchall()

        # Check if there are any records
        if not db_records:
            print("No records found in the database.\n")
            connection.close()
            return

        # Print the records
        print("Author: Gabriel Hubert")
        print("Records:")
        print("CSDUID, CSD, Period, IndicatorSummaryDescription, UnitOfMeasure, OriginalValue")

        for index, record in enumerate(db_records):
            # Every 10 records, print the message
            if index > 0 and index % 10 == 0:
                print("\nProgram by Gabriel Hubert\n")

            print(", ".join(map(str, record)))

        # Close the database connection
        connection.close()

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def printSingleRecord():
    """
    Print a single record to the console based on user selection.

    Args:
        records (list): The list of records to select from.
    """
    print("Author: Gabriel Hubert")
    try:
        # Get the user input for the row (1-based index from selectRow)
        row = selectRow() - 1  # Convert to zero-based index for SQLite

        # Connect to the database
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()

        # Fetch the record from the database based on the row selected
        cursor.execute("""
            SELECT csduid, csd, period, indicatorSummaryDescription, unitOfMeasure, originalValue
            FROM records
            LIMIT 1 OFFSET ?
        """, (row,))

        record = cursor.fetchone()

        # If record exists, print it, otherwise print an error message
        if record:
            print(f"Author: Gabriel Hubert\n")
            print(", ".join(map(str, record)))
        else:
            print("Invalid row selection: No record found at that position.\n")

        # Close the database connection
        connection.close()

    except ValueError:
        print("Invalid input. Please enter a valid number.\n")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def searchRecords():
    """
    Search or filter records in the SQLite database based on multiple columns.

    Returns:
        None
    """
    print("Enter search criteria for each field. Leave blank to skip a field.")
    csduid = input("CSDUID: ").strip()
    csd = input("CSD: ").strip()
    period = input("Period: ").strip()
    indicatorSummaryDescription = input("Indicator Summary Description: ").strip()
    unitOfMeasure = input("Unit of Measure: ").strip()
    originalValue_min = input("Original Value (Min): ").strip()
    originalValue_max = input("Original Value (Max): ").strip()

    # Build the SQL query dynamically based on user input
    query = "SELECT csduid, csd, period, indicatorSummaryDescription, unitOfMeasure, originalValue FROM records WHERE 1=1"
    params = []

    if csduid:
        query += " AND csduid = ?"
        params.append(csduid)
    if csd:
        query += " AND csd = ?"
        params.append(csd)
    if period:
        query += " AND period = ?"
        params.append(period)
    if indicatorSummaryDescription:
        query += " AND indicatorSummaryDescription = ?"
        params.append(indicatorSummaryDescription)
    if unitOfMeasure:
        query += " AND unitOfMeasure = ?"
        params.append(unitOfMeasure)
    if originalValue_min:
        query += " AND originalValue >= ?"
        params.append(originalValue_min)
    if originalValue_max:
        query += " AND originalValue <= ?"
        params.append(originalValue_max)

    try:
        # Connect to the database
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()

        # Execute the query with the parameters
        cursor.execute(query, params)
        results = cursor.fetchall()

        # Display the results
        if results:
            print("\nMatching Records:")
            print("CSDUID, CSD, Period, Indicator Summary Description, Unit of Measure, Original Value")
            for record in results:
                print(", ".join(map(str, record)))
        else:
            print("\nNo matching records found.")

        # Close the database connection
        connection.close()

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")