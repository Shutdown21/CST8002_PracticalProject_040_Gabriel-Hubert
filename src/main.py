from Presentation.ui import userInterface
from Persistence.csv_reader import printRecords, loadRecords

def main():
    records = []
    while True:
        choice = userInterface()
        if choice == "1":
            records = loadRecords()
            printRecords(records)
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
