def get_available_fields(data):
    if not data:
        return []
    return list(data[0].keys())

def display_available_fields(fields):
    print("Available fields for sorting:")
    for i, field in enumerate(fields, 1):
        print(f"{i}. {field}")

def get_sort_field(fields):
    field_choice = input("Enter the number of the field to sort by: ")
    try:
        field_choice = int(field_choice) - 1
        if 0 <= field_choice < len(fields):
            return fields[field_choice]
        else:
            print("Invalid field choice.")
            return None
    except ValueError:
        print("Please enter a valid number.")
        return None

def get_sort_order():
    order_choice = input("Sort in ascending (a) or descending (d) order? ").lower()
    if order_choice == 'a':
        return False
    elif order_choice == 'd':
        return True
    else:
        print("Invalid choice. Please enter 'a' for ascending or 'd' for descending.")
        return None 

def sort_data(data):
    if not data:
        return "No data to sort"
    
    fields = get_available_fields(data)
    display_available_fields(fields)
    
    sort_field = get_sort_field(fields)
    if sort_field is None:
        return data  # Return unsorted data if no valid field is selected
    
    reverse = get_sort_order()
    if reverse is None:
        return data  # Return unsorted data if no valid order is selected
    
    return sorted(data, key=lambda x: x.get(sort_field, ''), reverse=reverse)

def display_sorted_data(sorted_data):
    if isinstance(sorted_data, str):
        print(sorted_data)
    else:
        for item in sorted_data:
            print(item)

