import sqlite3
import csv

# Create table matching dataset structure
import sqlite3

def create_database():
    """Creates an SQLite database and the records table if it does not exist."""
    connection = sqlite3.connect("database.db")  # Create or connect to the database
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS records")

    cursor.execute("""
        CREATE TABLE records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            csduid TEXT NOT NULL,
            csd TEXT NOT NULL,
            period TEXT NOT NULL,
            indicatorSummaryDescription TEXT NOT NULL,
            unitOfMeasure TEXT NOT NULL,
            originalValue TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()
    print("Database and table successfully created.")