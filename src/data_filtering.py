import re
import json

def filter_data(data, filters):
    filtered_data = data
    for field, operation, value in filters:
        if operation in ["compare_with_other_string_field", "compare_with_other_numeric_field"]:
            compare_field, compare_operation = value
            filtered_data = [
                item for item in filtered_data 
                if field in item and compare_field in item and 
                compare_fields(item[field], compare_operation, item[compare_field])
            ]
        else:
            filtered_data = [
                item for item in filtered_data 
                if field in item and compare_values(item[field], operation, value)
            ]
    return filtered_data if filtered_data else "No results..."

def compare_fields(field1_value, operation, field2_value):
    if isinstance(field1_value, (int, float)) and isinstance(field2_value, (int, float)):
        return compare_numeric(field1_value, operation, field2_value)
    elif isinstance(field1_value, str) and isinstance(field2_value, str):
        return compare_string(field1_value, operation, field2_value)
    else:
        return False


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
    item_value = str(item_value).lower()
    compare_value = str(compare_value).lower()
    
    if operation == "equal_to":
        return item_value == compare_value
    elif operation == "not_equal_to":
        return item_value != compare_value
    elif operation == "contains":
        return compare_value in item_value
    elif operation == "starts_with":
        return item_value.startswith(compare_value)
    elif operation == "ends_with":
        return item_value.endswith(compare_value)
    elif operation == "lexicographically_greater_than":
        return item_value > compare_value
    elif operation == "lexicographically_less_than":
        return item_value < compare_value
    elif operation == "regex":
        try:
            return re.search(compare_value, item_value, re.IGNORECASE) is not None
        except re.error:
            print(f"Invalid regex pattern: {compare_value}")
            return False
    else:
        return False

def compare_numeric(item_value, operation, compare_value):
    try:
        item_value = float(item_value)
        if operation != "range" and not isinstance(compare_value, (int, float)):
            compare_value = float(compare_value)
    except ValueError:
        return False

    if operation == "equal_to":
        return item_value == compare_value
    elif operation == "not_equal_to":
        return item_value != compare_value
    elif operation == "greater_than":
        return item_value > compare_value
    elif operation == "less_than":
        return item_value < compare_value
    elif operation == "greater_than_or_equal_to":
        return item_value >= compare_value
    elif operation == "less_than_or_equal_to":
        return item_value <= compare_value
    elif operation == "range":
        min_val, max_val = compare_value
        return float(min_val) <= item_value <= float(max_val)
    else:
        return False

def compare_boolean(item_value, operation, compare_value):
    return item_value == (compare_value.lower() == "true")

def compare_list(item_value, operation, compare_value):
    if not item_value:
        return False
    if operation == "length_equal_to":
        return len(item_value) == compare_value
    elif operation == "length_not_equal_to":
        return len(item_value) != compare_value
    elif operation == "length_greater_than":
        return len(item_value) > compare_value
    elif operation == "length_less_than":
        return len(item_value) < compare_value
    elif operation == "length_greater_than_or_equal_to":
        return len(item_value) >= compare_value
    elif operation == "length_less_than_or_equal_to":
        return len(item_value) <= compare_value
    elif operation == "contains":
        return str(compare_value) in [str(x) for x in item_value]
    elif operation == "all_elements":
        condition, value = compare_value
        return all(compare_numeric(x, condition, value) for x in item_value)
    elif operation == "minimum":
        condition, value = compare_value
        return compare_numeric(min(item_value), condition, value)
    elif operation == "maximum":
        condition, value = compare_value
        return compare_numeric(max(item_value), condition, value)
    elif operation == "average":
        condition, value = compare_value
        try:
            avg = sum(float(x) for x in item_value if isinstance(x, (int, float))) / len(item_value)
            return compare_numeric(avg, condition, value)
        except (ValueError, ZeroDivisionError):
            return False
    else:
        return False
    

def save_filtered_data(filtered_data, filename):
    if isinstance(filtered_data, str):
        print("No data to save.")
        return

    try:
        with open(filename, 'w') as f:
            json.dump(filtered_data, f, indent=4)
        print(f"Filtered data saved to {filename}")
    except IOError as e:
        print(f"An error occurred while saving the file: {e}")