import sqlite3
import csv

# Create table matching dataset structure
import sqlite3

def create_database():
    """Creates an SQLite database and the records table if it does not exist."""
    connection = sqlite3.connect("database.db")  # Create or connect to the database
    cursor = connection.cursor()

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

    connection.commit()
    connection.close()
    print("Database and table successfully created.")

# Run the function
create_database()


def load_csv_to_db(csv_file):
    """Reads CSV file and inserts data into the SQLite database."""
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    with open(csv_file, "r", encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row

        for row in csv_reader:
            cursor.execute("""
                INSERT INTO records (csduid, csd, period, indicatorSummaryDescription, unitOfMeasure, originalValue)
                VALUES (?, ?, ?, ?, ?, ?)""", row)

    connection.commit()
    connection.close()
    print("CSV data successfully loaded into database.")

# Run the function with your CSV file
load_csv_to_db("data/records.csv")