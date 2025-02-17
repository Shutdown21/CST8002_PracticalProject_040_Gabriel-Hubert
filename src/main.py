from Presentation.ui import userInterface
from Persistence.csv_reader import printRecords, loadRecords, save_data

def main():
    records = []
    while True:
        choice = userInterface()
        if choice == "1":
            records = loadRecords()
            printRecords(records)
        if choice == "2":
            save_data(records)
        if choice == "3":
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
