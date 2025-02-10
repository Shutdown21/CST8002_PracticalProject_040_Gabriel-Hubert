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
from record import Record # Import the Record class from record.py


#Function to load records from a CSV file
def loadRecords(file_path):
    records = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                record = Record(
                    csduid=row['CSDUID'],
                    csd=row['CSD'],
                    period=row['Period'],
                    indicatorSummaryDescription=row['IndicatorSummaryDescription'],
                    unitOfMeasure=row['UnitOfMeasure'],
                    originalValue=row['OriginalValue']
                )
                records.append(record)
                if len(records) >= 20:  #Limit the amount of record rows read
                    break
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except KeyError as e:
        print(f"Error: Missing expected column in CSV file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return records

#Main function
if __name__ == "__main__":
    file_path = "src\dailyvehiclesdownload.csv"  #CSV file location
    records = loadRecords(file_path)
    print("Author: Gabriel Hubert")
    print("Records:")
    print("CSDUID, CSD, Period, IndicatorSummaryDescription, UnitOfMeasure, OriginalValue")
    for record in records:
        print(f"{record.csduid}, {record.csd}, {record.period}, {record.indicatorSummaryDescription}, {record.unitOfMeasure}, {record.originalValue}")