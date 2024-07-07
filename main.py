def main_menu():
    print("Welcome to the Data Filtering Application")
    print("Please select an option:")
    print("1 ... Select a file")
    print("2 ... Filter data")
    print("3 ... Sort data")
    print("4 ... Export data")
    print("5 ... Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Selecting file feature WIP")
    elif choice == "2":
        print("Filtering data feature WIP")
    elif choice == "3":
        print("Sorting data feature WIP")
    elif choice == "4":
        print("Exporting data feature WIP")
    elif choice == "5":
        print("Quitting the application")
        return
    else:
        print("Invalid choice. Please try again.")


def main():
    main_menu()


if __name__ == "__main__":
    main()
