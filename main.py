import os
from src.data_io import read_csv, write_csv, read_json, write_json


class MenuOption:
    def __init__(self, name, action=None, child_options=None):
        self.name = name
        self.action = action
        self.child_options = child_options or []


def display_menu(options):
    for i, option in enumerate(options):
        print(f"{i + 1}. {option.name}")


def main_menu(data):
    return [
        MenuOption("Load data", child_options=load_data_menu(data)),
        MenuOption("Save data", child_options=save_data_menu(data)),
        MenuOption("Exit"),
    ]


def load_data_menu(data):
    return [
        MenuOption("Load CSV", child_options=load_choice_menu(read_csv, data)),
        MenuOption("Load JSON", child_options=load_choice_menu(read_json, data)),
        MenuOption("Back to Main Menu"),
    ]


def save_data_menu(data):
    return [
        MenuOption("Save CSV", action=lambda: save_csv(data)),
        MenuOption("Save JSON", action=lambda: save_json(data)),
        MenuOption("Back to Main Menu"),
    ]


def load_choice_menu(load_func, data):
    return [
        MenuOption(
            "Enter file path",
            action=lambda: load_func(input("Enter the file path: "), data),
        ),
        MenuOption(
            "Select a file", action=lambda: select_file_from_folder(load_func, data)
        ),
        MenuOption("Back to Load Data Menu"),
    ]


def list_json_files(folder_path):
    json_files = [f for f in os.listdir(folder_path) if f.endswith(".json")]
    return json_files


def select_file_from_folder(load_func, data):
    data_folder_path = "data"
    json_files = list_json_files(data_folder_path)
    if json_files:
        print("Available JSON files:")
        for i, file_name in enumerate(json_files):
            print(f"{i + 1}. {file_name}")
        file_index = int(input("Enter the number of the JSON file to load: "))
        if 1 <= file_index <= len(json_files):
            file_path = os.path.join(data_folder_path, json_files[file_index - 1])
            load_func(file_path, data)
            print("Data loaded successfully.")
        else:
            print("Invalid choice. Please try again.")
    else:
        print("No files available in the folder.")
        file_path = input("Enter the file path: ")
        load_func(file_path, data)
        print("Data loaded successfully.")


def save_csv(data):
    file_path = input("Enter the CSV file path: ")
    write_csv(file_path, data)
    print("Data saved successfully.")


def save_json(data):
    file_path = input("Enter the JSON file path: ")
    write_json(file_path, data)
    print("Data saved successfully.")


def navigate_menu(options, data):
    while True:
        display_menu(options)
        choice = int(input("Enter your choice: "))

        if 1 <= choice <= len(options):
            option = options[choice - 1]

            if option.action:
                option.action()

            elif option.child_options:
                navigate_menu(option.child_options, data)

            elif option.name == "Back to Main Menu":
                break

            else:
                print("Exit program...")
                return

        else:
            print("Invalid choice. Please try again.")


def main():
    data = None
    navigate_menu(main_menu(data), data)


if __name__ == "__main__":
    main()
