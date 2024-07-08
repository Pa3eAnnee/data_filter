import os

from src.data_io import read_file


def select_file():
    data_folder = "data"
    files = os.listdir(data_folder)
    print("Files in the data folder:")
    for i, file in enumerate(files, start=1):
        print(f"{i} ... {file}")

    choice = input("Enter your choice: ")

    if int(choice) < 1 or int(choice) > len(files):
        print("Invalid choice. Please try again.")
        return select_file()
    else:
        selected_file = files[int(choice) - 1]
        return os.path.join(data_folder, selected_file)


def main_menu():
    print("Please select an option:")
    print("1 ... Select a file")
    print("2 ... Filter data WIP")
    print("3 ... Sort data WIP")
    print("4 ... Export data WIP")
    print("0 ... Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        file_path = select_file()
        if file_path:
            print(f"Loaded : {file_path}")
            loaded_menu(file_path)
    elif choice == "2":
        print("Filtering data feature WIP")
    elif choice == "3":
        print("Sorting data feature WIP")
    elif choice == "4":
        print("Exporting data feature WIP")
    elif choice == "0":
        print("Quitting the application")
        return
    else:
        print("Invalid choice. Please try again.")
        main_menu()

def loaded_menu(file_path):
    # Print the loaded file path
    print("Loaded file:", file_path)

    # Print the menu options
    print("\nOptions:")
    print("1. Display raw file")
    print("2. Display structured file")
    print("3. Save file")
    print("4. Stats")
    print("5. Filter")
    print("6. Sort")

    # Get the user's choice
    choice = input("\nEnter your choice: ")

    # Perform the corresponding action based on the user's choice
    if choice == "1":
        print("display_raw_file(file_path)")
    elif choice == "2":
        print("display_structured_file(data)")
    elif choice == "3":
        print("save_file(file_path, data)")
    elif choice == "4":
        print("stats(data)")
    elif choice == "5":
        print("filter_data(data)")
    elif choice == "6":
        print("sort_data(data)")
    else:
        print("Invalid choice")