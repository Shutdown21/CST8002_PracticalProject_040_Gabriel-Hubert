"""
Author: Gabriel Hubert
Date: 2025-01-26
Due Date: 2025-01-26
Course: CST8002 Section 040 - Programming Research Project
Professor: Tyler DeLay
Assignment: Practical Project 1
Description: This program reads the first few records from a CSV file and displays them in a tabular format.
"""
import csv
import uuid
from Model.record import Record # Import the Record class from record.py
from Presentation.ui import selectRow


# Function to load records from a CSV file
def loadRecords():
    file_path = "src/dailyvehiclesdownload.csv"  # CSV file location
    records = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            # Loop through the rows and parse the first 100 records or fewer if the dataset is smaller
            for index, row in enumerate(csv_reader):
                # Stop reading if we've reached 100 records
                if index >= 100:
                    break
                # Create a Record object for each row in the CSV file
                record = Record(
                    csduid=row['CSDUID'],
                    csd=row['CSD'],
                    period=row['Period'],
                    indicatorSummaryDescription=row['IndicatorSummaryDescription'],
                    unitOfMeasure=row['UnitOfMeasure'],
                    originalValue=row['OriginalValue']
                )
                # Append the record to the list
                records.append(record)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except KeyError as e:
        print(f"Error: Missing expected column in CSV file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    print(f"Loaded {len(records)} records from {file_path} successfully.")
    return records

def save_data(records):
    """Persists the records to a new CSV file with a unique name."""
    # Generate a unique filename using UUID, placed in the src directory
    unique_filename = f"src/records_{uuid.uuid4().hex}.csv"
    
    try:
        with open(unique_filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["CSDUID", "CSD", "Period", "IndicatorSummaryDescription", "UnitOfMeasure", "OriginalValue"])
            
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

def printAllRecords(records):
    print("Author: Gabriel Hubert")
    print("Records:")
    print("CSDUID, CSD, Period, IndicatorSummaryDescription, UnitOfMeasure, OriginalValue")
    for index, record in enumerate(records):
        if index > 0 and index % 10 == 0:  # Every 10 records
            print("\nProgram by Gabriel Hubert\n") 
        print(f"{record.csduid}, {record.csd}, {record.period}, {record.indicatorSummaryDescription}, {record.unitOfMeasure}, {record.originalValue}")

def printSingleRecord(records):
    print("Author: Gabriel Hubert")
    try:
        row = selectRow()-1
        print(f"{records[row]}")
    except KeyError:
        print("Invalid row selection\n")
    except IndexError:
        print("Invalid row selection\n")
    