import os

from src.data_io import *
from src.data_processing import *


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
            print("Loaded file:", file_path)
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
    print("\nOptions:")
    print("1. Display raw file")
    print("2. Display structured file")
    print("3. Save file")
    print("4. Stats")
    print("5. Filter")
    print("6. Sort")
    print("0. Quit")
    

    choice = input("\nEnter your choice: ")

    if choice == "1":
        print(read_file(file_path))
        loaded_menu(file_path)
    elif choice == "2":
        print(process_file(file_path))
        loaded_menu(file_path)
    elif choice == "3":
        data = process_file(file_path)
        save_file(file_path, data)
        loaded_menu(file_path)
    elif choice == "4":
        print("stats(data)")
    elif choice == "5":
        print("filter_data(data)")
    elif choice == "6":
        print("sort_data(data)")
    elif choice == "0":
        print("Quitting the application")
        return
    else:
        print("Invalid choice")


def save_file(file_path, data):
    print("\nSave options:")
    print(data)
    print("1. Save as JSON")
    print("2. Save as CSV")
    print("3. Save as XML")
    print("4. Save as YAML")
    
    save_choice = input("Enter your choice: ")
    
    if save_choice == "1":
        filename = input("Enter the filename to save (including .json extension): ")
        if not filename.lower().endswith('.json'):
            filename += '.json'
        save_path = os.path.join(os.path.dirname(file_path), filename)
        save_data_json(data, save_path)
    elif save_choice == "2":
        filename = input("Enter the filename to save (including .csv extension): ")
        if not filename.lower().endswith('.csv'):
            filename += '.csv'
        save_path = os.path.join(os.path.dirname(file_path), filename)
        save_data_csv(data, save_path)
    elif save_choice == "3":
        filename = input("Enter the filename to save (including .xml extension): ")
        if not filename.lower().endswith('.xml'):
            filename += '.xml'
        save_path = os.path.join(os.path.dirname(file_path), filename)
        save_data_xml(data, save_path)
    elif save_choice == "4":
        filename = input("Enter the filename to save (including .yaml extension): ")
        if not filename.lower().endswith('.yaml'):
            filename += '.yaml'
        save_path = os.path.join(os.path.dirname(file_path), filename)
        save_data_yaml(data, save_path)
    else:
        print("Invalid choice. File not saved.")