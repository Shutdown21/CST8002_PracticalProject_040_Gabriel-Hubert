import unittest
from unittest.mock import patch
from Business.deleteRecord import deleteRecord

class TestDeleteRecord(unittest.TestCase):
    """
    Unit test case for the deleteRecord function.
    """
    @patch("Business.deleteRecord.selectRow", return_value=2)  # Mock selectRow to always return 2
    def test_delete_record(self, mock_selectRow):
        """
        Test the deleteRecord function to ensure it correctly removes a record from the list.
        """
        records = [
            {"id": 1, "name": "Record 1", "value": "Value 1"},
            {"id": 2, "name": "Record 2", "value": "Value 2"},
            {"id": 3, "name": "Record 3", "value": "Value 3"}
        ]

        deleteRecord(records)
        print("Program by Gabriel Hubert")
        self.assertEqual(len(records), 2)  # Ensure one record was removed
        self.assertNotIn({"id": 2, "name": "Record 2", "value": "Value 2"}, records)  # Ensure record with ID 2 is gone

if __name__ == '__main__':
    unittest.main()
