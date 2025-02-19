from Presentation.ui import userInterface, newRecord
from Persistence.csv_reader import printAllRecords, loadRecords, save_data, printSingleRecord
from Business.updateRecord import updateRecord

def main():
    records = []
    while True:
        choice = userInterface()
        if choice == "1":
            records = loadRecords()
        elif choice == "2":
            save_data(records)
        elif choice == "3":
            printAllRecords(records)
        elif choice == "4":
            printSingleRecord(records)
        elif choice == "5":
            newRecord(records)
        elif choice == "6":
            updateRecord(records)
        elif choice == "7":
            break
        else:
            print("Invalid choice, please try again.\n")


if __name__ == "__main__":
    main()
