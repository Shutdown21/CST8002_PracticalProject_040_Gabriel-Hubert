from Presentation.ui import userInterface
from Persistence.csv_reader import printAllRecords, loadRecords, save_data, printSingleRecord

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
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
