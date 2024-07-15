import re

def filter_data(data, filters):
    filtered_data = data
    for field, operation, value in filters:
        filtered_data = [item for item in filtered_data if field in item and compare_values(item[field], operation, value)]
    return filtered_data if filtered_data else "No results..."

def regex_filter(item_value, pattern):
    try:
        return re.search(pattern, str(item_value), re.IGNORECASE) is not None
    except re.error:
        print("Expression régulière invalide.")
        return False
    
def range_filter(value, min_val, max_val):
    return min_val <= value <= max_val

def list_contains_filter(item_list, value):
    return str(value) in [str(item) for item in item_list]

def compare_values(item_value, operation, compare_value):
    if isinstance(item_value, bool):
        return compare_boolean(item_value, operation, compare_value)
    elif isinstance(item_value, (int, float)):
        return compare_numeric(item_value, operation, compare_value)
    elif isinstance(item_value, str):
        return compare_string(item_value, operation, compare_value)
    elif isinstance(item_value, list):
        return compare_list(item_value, operation, compare_value)
    else:
        raise ValueError(f"Unsupported data type: {type(item_value)}")

def compare_string(item_value, operation, compare_value):
    item_value = str(item_value)
    compare_value = str(compare_value)
    
    if operation == "equal_to":
        return item_value.lower() == compare_value.lower()
    elif operation == "not_equal_to":
        return item_value.lower() != compare_value.lower()
    elif operation == "contains":
        return compare_value.lower() in item_value.lower()
    elif operation == "starts_with":
        return item_value.lower().startswith(compare_value.lower())
    elif operation == "ends_with":
        return item_value.lower().endswith(compare_value.lower())
    elif operation == "lexicographically_greater_than":
        return item_value.lower() > compare_value.lower()
    elif operation == "lexicographically_less_than":
        return item_value.lower() < compare_value.lower()
    elif operation == "regex":
        try:
            return re.search(compare_value, item_value, re.IGNORECASE) is not None
        except re.error:
            print(f"Invalid regex pattern: {compare_value}")
            return False
    else:
        return False

def compare_numeric(item_value, operation, compare_value):
    if operation == "equal_to":
        return item_value == float(compare_value)
    elif operation == "not_equal_to":
        return item_value != float(compare_value)
    elif operation == "greater_than":
        return item_value > float(compare_value)
    elif operation == "less_than":
        return item_value < float(compare_value)
    elif operation == "greater_than_or_equal_to":
        return item_value >= float(compare_value)
    elif operation == "less_than_or_equal_to":
        return item_value <= float(compare_value)
    elif operation == "range":
        min_val, max_val = compare_value
        return float(min_val) <= item_value <= float(max_val)

def compare_boolean(item_value, operation, compare_value):
    return item_value == (compare_value.lower() == "true")

def compare_list(item_value, operation, compare_value):
    if operation == "length_equal_to":
        return len(item_value) == int(compare_value)
    elif operation == "length_greater_than":
        return len(item_value) > int(compare_value)
    elif operation == "length_less_than":
        return len(item_value) < int(compare_value)
    elif operation == "contains":
        return str(compare_value) in [str(x) for x in item_value]
    else:
        return False