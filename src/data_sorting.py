def get_available_fields(data):
    if not data:
        return []
    return list(data[0].keys())

def display_available_fields(fields):
    print("Available fields for sorting:")
    for i, field in enumerate(fields, 1):
        print(f"{i}. {field}")

def get_sort_fields(fields):
    sort_fields = []
    while True:
        field_choice = input("Enter the number of the field to sort by (or 0 to finish): ")
        if field_choice == '0':
            break
        try:
            field_choice = int(field_choice) - 1
            if 0 <= field_choice < len(fields):
                sort_fields.append(fields[field_choice])
                print(f"Current sort order: {', '.join(sort_fields)}")
            else:
                print("Invalid field choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
    return sort_fields

def get_sort_orders(sort_fields):
    order_choices = []
    for field in sort_fields:
        while True:
            order_choice = input(f"Sort {field} in ascending (a) or descending (d) order? ").lower()
            if order_choice in ['a', 'd']:
                order_choices.append(order_choice == 'd')
                break
            print("Invalid choice. Please enter 'a' for ascending or 'd' for descending.")
    return order_choices


def sort_data(data):
    if not data:
        return "No data to sort"
    
    fields = get_available_fields(data)
    display_available_fields(fields)
    
    sort_fields = get_sort_fields(fields)
    if not sort_fields:
        return data  # Return unsorted data if no fields are selected
    
    order_choices = get_sort_orders(sort_fields)
    
    def sort_key(item):
        return tuple((item.get(field, ''), reverse) for field, reverse in zip(sort_fields, order_choices))
    
    return sorted(data, key=sort_key)

def display_sorted_data(sorted_data):
    if isinstance(sorted_data, str):
        print(sorted_data)
    else:
        for item in sorted_data:
            print(item)

