import os

from src.data_filtering import filter_data
from src.data_io import read_file, save_data_csv, save_data_json, save_data_xml, save_data_yaml
from src.data_processing import process_file
from src.data_statistics import calculate_stats
from src.data_statistics import identify_field_type

    
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
        data = process_file(file_path)
        stats = calculate_stats(data)
        display_stats(stats)
        loaded_menu(file_path)
    elif choice == "5":
        data = process_file(file_path)
        filter_menu(data)
        loaded_menu(file_path)
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


def display_stats(stats):
    for field, field_stats in stats.items():
        print(f"\nField: {field}")
        if "type" in field_stats and field_stats["type"] == "string":
            print("  Type: String")
        elif "min" in field_stats and "average" in field_stats:
            print(f"  Type: Numeric")
            print(f"  Minimum: {field_stats['min']}")
            print(f"  Maximum: {field_stats['max']}")
            print(f"  Average: {field_stats['average']:.2f}")
        elif "true_percentage" in field_stats:
            print(f"  Type: Boolean")
            print(f"  True: {field_stats['true_percentage']:.2f}%")
            print(f"  False: {100 - field_stats['true_percentage']:.2f}%")
        elif "min_length" in field_stats:
            print(f"  Type: List")
            print(f"  Minimum length: {field_stats['min_length']}")
            print(f"  Maximum length: {field_stats['max_length']}")
            print(f"  Average length: {field_stats['average_length']:.2f}")
            print(f"  Total length: {field_stats['total_length']}")
            print(f"  Minimum value: {field_stats['min_value']}")
            print(f"  Maximum value: {field_stats['max_value']}")
            print(f"  Average value: {field_stats['average_value']:.2f}")
            print(f"  Total items: {field_stats['total_items']}")

def get_field_choice(data):
    print("\nAvailable fields:")
    fields = list(data[0].keys())
    for i, field in enumerate(fields, 1):
        field_values = [item[field] for item in data if field in item]
        field_type = identify_field_type(field_values)
        print(f"{i}. {field} (Type: {field_type})")
    
    field_choice = input("Enter the number of the field to filter on: ")
    chosen_field = fields[int(field_choice) - 1]
    field_values = [item[chosen_field] for item in data if chosen_field in item]
    field_type = identify_field_type(field_values)
    
    return chosen_field, field_type

def get_operation_choice(operations):
    for i, op in enumerate(operations, 1):
        print(f"{i}. {op}")
    operation_choice = input("Enter the number of the comparison operation: ")
    return operations[int(operation_choice) - 1]

def string_filter_menu():
    print("\nString comparison operations:")
    operations = [
        "Equal to - Exact match",
        "Not equal to - Doesn't match exactly",
        "Lexicographically greater than - Comes after in dictionary order",
        "Lexicographically less than - Comes before in dictionary order",
        "Contains - Includes the given text (case-insensitive)",
        "Starts with - Begins with the given text (case-insensitive)",
        "Ends with - Ends with the given text (case-insensitive)",
        "Regex - Use a regular expression",
        "Compare with other string field - Compare with another string field"
    ]
    operation = get_operation_choice(operations)
    return operation.split('-')[0].strip().lower().replace(' ', '_')

def boolean_filter_menu():
    print("\nBoolean filter:")
    print("1. Show True values")
    print("2. Show False values")
    while True:
        choice = input("Enter your choice (1 or 2): ").strip().lower()
        if choice in ['1', '2']:
            return "true" if choice == "1" else "false"
        else:
            print("Invalid choice. Please enter 1 or 2.")

def numeric_filter_menu():
    print("\nNumeric comparison operations:")
    operations = [
        "Equal to - Exact match",
        "Not equal to - Doesn't match exactly",
        "Greater than - Strictly greater than the given value",
        "Less than - Strictly less than the given value",
        "Greater than or equal to - Greater than or equal to the given value",
        "Less than or equal to - Less than or equal to the given value",
        "Range - Between two values",
        "Compare with other numeric field - Compare with another numeric field"
    ]
    operation = get_operation_choice(operations)
    return operation.split('-')[0].strip().lower().replace(' ', '_')

def list_filter_menu():
    print("\nList comparison operations:")
    operations = [
        "Equal to - Exact match of list length",
        "Not equal to - Doesn't match list length exactly",
        "Length greater than - List length strictly greater than the given value",
        "Length less than - List length strictly less than the given value",
        "Length greater than or equal to - List length greater than or equal to the given value",
        "Length less than or equal to - List length less than or equal to the given value",
        "Contains - List contains a specific value",
        "All elements - All elements satisfy a condition",
        "Minimum - Minimum value in the list satisfies a condition",
        "Maximum - Maximum value in the list satisfies a condition",
        "Average - Average value of the list satisfies a condition"
    ]
    operation = get_operation_choice(operations)
    return operation.split('-')[0].strip().lower().replace(' ', '_')

def get_filter_value(field_type, operation):
    if field_type == "boolean":
        return operation  # operation contient déjà "true" ou "false"
    elif field_type == "numeric":
        if operation == "range":
            min_val = float(input("Enter the minimum value: "))
            max_val = float(input("Enter the maximum value: "))
            return (min_val, max_val)
        else:
            return float(input("Enter the numeric value to compare with: "))
    elif field_type == "list":
        if operation in ["all_elements", "minimum", "maximum", "average"]:
            print("\nChoose the condition for list elements:")
            print("1. Greater than")
            print("2. Less than")
            print("3. Equal to")
            condition_choice = input("Enter your choice (1-3): ")
            condition = ["greater_than", "less_than", "equal_to"][int(condition_choice) - 1]
            value = float(input("Enter the value to compare with: "))
            return (condition, value)
        elif operation == "contains":
            return input("Enter the value to search for in the list: ")
        else:
            return int(input("Enter the list length to compare with: "))
    else:
        return input("Enter the value to compare with: ")


def apply_multiple_filters(data):
    filters = []
    while True:
        field, field_type = get_field_choice(data)
        print(f"\nSelected field: {field} (Type: {field_type})")

        if field_type == "string":
            operation = string_filter_menu()
        elif field_type == "boolean":
            operation = boolean_filter_menu()
        elif field_type == "numeric":
            operation = numeric_filter_menu()
        elif field_type == "list":
            operation = list_filter_menu()
        else:
            print(f"Unsupported field type: {field_type}")
            continue

        value = get_filter_value(field_type, operation)
        filters.append((field, operation, value))

        filtered_data = filter_data(data, filters)
        if filtered_data == "No results...":
            print(filtered_data)
            break

        print(f"Number of items after filtering: {len(filtered_data)}")
        if input("Apply another filter? (y/n): ").lower() != 'y':
            break

    return filtered_data

def filter_menu(data):
    field, field_type = get_field_choice(data)
    print(f"\nSelected field: {field} (Type: {field_type})")

    operation, value = get_operation_and_value(data, field, field_type)
    if operation is None:
        return None

    filtered_result = apply_filter(data, field, operation, value)
    display_filtered_result(filtered_result)

    return filtered_result

def get_operation_and_value(data, field, field_type):
    if field_type == "string":
        return get_string_operation_and_value(data, field)
    elif field_type == "numeric":
        return get_numeric_operation_and_value(data, field)
    elif field_type == "boolean":
        return get_boolean_operation_and_value()
    elif field_type == "list":
        return get_list_operation_and_value()
    else:
        print(f"Unsupported field type: {field_type}")
        return None, None

def get_string_operation_and_value(data, field):
    operation = string_filter_menu()
    if operation == "compare_with_other_string_field":
        return handle_field_comparison(data, field, "string")
    else:
        value = input("Enter the value to compare with: ")
        return operation, value

def get_numeric_operation_and_value(data, field):
    operation = numeric_filter_menu()
    if operation == "compare_with_other_numeric_field":
        return handle_field_comparison(data, field, "numeric")
    else:
        value = get_filter_value("numeric", operation)
        return operation, value

def get_boolean_operation_and_value():
    operation = boolean_filter_menu()
    return operation, operation

def get_list_operation_and_value():
    operation = list_filter_menu()
    value = get_filter_value("list", operation)
    return operation, value

def handle_field_comparison(data, field, field_type):
    compare_field = select_field_to_compare(data, field, field_type)
    if compare_field:
        compare_operation = get_comparison_menu(field_type)
        value = (compare_field, compare_operation)
        return f"compare_with_other_{field_type}_field", value
    else:
        print(f"No other {field_type} fields available for comparison.")
        return None, None

def select_field_to_compare(data, field, field_type):
    if field_type == "string":
        return select_string_field_to_compare(data, field)
    elif field_type == "numeric":
        return select_numeric_field_to_compare(data, field)

def get_comparison_menu(field_type):
    if field_type == "string":
        return string_comparison_menu()
    elif field_type == "numeric":
        return numeric_comparison_menu()

def apply_filter(data, field, operation, value):
    return filter_data(data, [(field, operation, value)])

def display_filtered_result(filtered_result):
    if isinstance(filtered_result, str):
        print(filtered_result)
    else:
        print("Filtered data:")
        for item in filtered_result:
            print(item)

def save_filtered_results(filtered_data, test_format=None, test_filename=None):
    if filtered_data == "No results...":
        print("No data to save.")
        return

    print("\nSave options:")
    print("1. Save as JSON")
    print("2. Save as CSV")
    print("3. Save as XML")
    print("4. Save as YAML")
    
    save_choice = test_format or input("Enter your choice: ")
    filename = test_filename or input("Enter the filename to save: ")
    
    if save_choice == "1":
        if not filename.lower().endswith('.json'):
            filename += '.json'
        save_data_json(filtered_data, filename)
    elif save_choice == "2":
        if not filename.lower().endswith('.csv'):
            filename += '.csv'
        save_data_csv(filtered_data, filename)
    elif save_choice == "3":
        if not filename.lower().endswith('.xml'):
            filename += '.xml'
        save_data_xml(filtered_data, filename)
    elif save_choice == "4":
        if not filename.lower().endswith('.yaml'):
            filename += '.yaml'
        save_data_yaml(filtered_data, filename)
    else:
        print("Invalid choice. File not saved.")


def save_filtered_results(filtered_data, test_format=None, test_filename=None):
    if filtered_data == "No results...":
        print("No data to save.")
        return

    print("\nSave options:")
    print("1. Save as JSON")
    print("2. Save as CSV")
    print("3. Save as XML")
    print("4. Save as YAML")
    
    save_choice = test_format or input("Enter your choice: ")
    filename = test_filename or input("Enter the filename to save: ")
    
    if save_choice == "1":
        if not filename.lower().endswith('.json'):
            filename += '.json'
        save_data_json(filtered_data, filename)
    elif save_choice == "2":
        if not filename.lower().endswith('.csv'):
            filename += '.csv'
        save_data_csv(filtered_data, filename)
    elif save_choice == "3":
        if not filename.lower().endswith('.xml'):
            filename += '.xml'
        save_data_xml(filtered_data, filename)
    elif save_choice == "4":
        if not filename.lower().endswith('.yaml'):
            filename += '.yaml'
        save_data_yaml(filtered_data, filename)
    else:
        print("Invalid choice. File not saved.")

def select_string_field_to_compare(data, current_field):
    string_fields = [field for field in data[0].keys() if isinstance(data[0][field], str) and field != current_field]
    if not string_fields:
        print("No other string fields available for comparison.")
        return None
    print("\nSelect a string field to compare with:")
    for i, field in enumerate(string_fields, 1):
        print(f"{i}. {field}")
    choice = int(input("Enter your choice: ")) - 1
    return string_fields[choice]


def string_comparison_menu():
    print("\nHow do you want to compare the two string fields?")
    operations = [
        "Equal to - Exact match",
        "Not equal to - Doesn't match exactly",
        "Contains - First field contains the second",
        "Starts with - First field starts with the second",
        "Ends with - First field ends with the second"
    ]
    operation = get_operation_choice(operations)
    return operation.split('-')[0].strip().lower().replace(' ', '_')

def select_numeric_field_to_compare(data, current_field):
    numeric_fields = [field for field in data[0].keys() if isinstance(data[0][field], (int, float)) and field != current_field]
    if not numeric_fields:
        print("No other numeric fields available for comparison.")
        return None
    print("\nSelect a numeric field to compare with:")
    for i, field in enumerate(numeric_fields, 1):
        print(f"{i}. {field}")
    choice = int(input("Enter your choice: ")) - 1
    return numeric_fields[choice]

def numeric_comparison_menu():
    print("\nHow do you want to compare the two numeric fields?")
    operations = [
        "Equal to - Exact match",
        "Not equal to - Doesn't match exactly",
        "Greater than - First field greater than the second",
        "Less than - First field less than the second",
        "Greater than or equal to - First field greater than or equal to the second",
        "Less than or equal to - First field less than or equal to the second"
    ]
    operation = get_operation_choice(operations)
    return operation.split('-')[0].strip().lower().replace(' ', '_')