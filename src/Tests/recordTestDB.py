import unittest
from unittest.mock import patch
import sqlite3
from Business.deleteRecord import deleteRecord
from Persistence.database import create_database

class TestDeleteRecord(unittest.TestCase):
    """
    Unit test case for the deleteRecord function.
    """
    @patch("Business.deleteRecord.selectRow", return_value=2)  # Mock selectRow to always return 2
    def test_delete_record(self, mock_selectRow):
        """
        Test the deleteRecord function to ensure it correctly removes a record from the mock database.
        """
        # Connect to the persistent database file
        connection = sqlite3.connect("database.db")  # Use the actual database file
        cursor = connection.cursor()

        # Create the records table in the mock database (if it doesn't exist)
        create_database()

        # Insert mock data into the database
        cursor.executemany("""
            INSERT INTO records (csduid, csd, period, indicatorSummaryDescription, unitOfMeasure, originalValue)
            VALUES (?, ?, ?, ?, ?, ?)
        """, [
            ("CSD001", "CSD Name 1", "2023", "Indicator 1", "Units", "1000"),
            ("CSD002", "CSD Name 2", "2023", "Indicator 2", "Units", "2000"),
            ("CSD003", "CSD Name 3", "2023", "Indicator 3", "Units", "3000")
        ])
        connection.commit()

        # Perform the delete operation (pass the connection explicitly)
        print("Before delete:")
        cursor.execute("SELECT * FROM records")
        print(cursor.fetchall())  # Print all records before delete

        deleteRecord(use_database=True)  # Pass connection here

        print("After delete:")
        cursor.execute("SELECT * FROM records")
        print(cursor.fetchall())  # Print all records after delete

        # Verify that the record with id = 2 is deleted
        cursor.execute("SELECT * FROM records WHERE id = 2")
        result = cursor.fetchone()

        # Assert that the record with id = 2 no longer exists
        self.assertIsNone(result)  # Should be None since the record was deleted

        # Clean up: close the connection to the mock database
        connection.close()

if __name__ == '__main__':
    unittest.main()
