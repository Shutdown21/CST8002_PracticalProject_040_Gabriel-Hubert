from Presentation.ui import userInterface, newRecord
from Persistence.csv_reader import printAllRecords, loadRecords, save_data, printSingleRecord, searchRecords
from Business.updateRecord import updateRecord
from Business.deleteRecord import deleteRecord
from Persistence.database import create_database

def main():
    """
    Main function to run the program. It provides a user interface to interact with records.
    The user can load, save, print, add, update, delete records, or exit the program.
    """
    create_database()
    while True:
        choice = userInterface()
        if choice == "1":
            loadRecords()
        elif choice == "2":
            save_data()
        elif choice == "3":
            printAllRecords()
        elif choice == "4":
            printSingleRecord()
        elif choice == "5":
            newRecord()
        elif choice == "6":
            updateRecord()
        elif choice == "7":
            deleteRecord()
        elif choice == "8":
            searchRecords()
        elif choice == "9":
            break
        else:
            print("Invalid choice, please try again.\n")


if __name__ == "__main__":
    main()
