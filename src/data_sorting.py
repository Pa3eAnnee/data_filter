def sort_data(data):
    if not data:
        return "No data to sort"
    
    fields = list(data[0].keys())
    print("Available fields for sorting:")
    for i, field in enumerate(fields, 1):
        print(f"{i}. {field}")
    
    field_choice = int(input("Enter the number of the field to sort by: ")) - 1
    if field_choice < 0 or field_choice >= len(fields):
        return "Invalid field choice"
    
    sort_field = fields[field_choice]
    
    order_choice = input("Sort in ascending (a) or descending (d) order? ").lower()
    reverse = order_choice == 'd'
    
    sorted_data = sorted(data, key=lambda x: x.get(sort_field, ''), reverse=reverse)
    return sorted_data

def display_sorted_data(sorted_data):
    if isinstance(sorted_data, str):
        print(sorted_data)
    else:
        for item in sorted_data:
            print(item)