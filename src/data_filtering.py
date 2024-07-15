def filter_data(data, field, operation, value):
    filtered_data = []
    for item in data:
        if field not in item:
            continue
        if compare_values(item[field], operation, value):
            filtered_data.append(item)
    
    if not filtered_data:
        return "No results..."
    return filtered_data

def compare_values(item_value, operation, compare_value):
    if isinstance(item_value, str):
        return compare_string(item_value, operation, compare_value)
    elif isinstance(item_value, (int, float)):
        return compare_numeric(item_value, operation, float(compare_value))
    elif isinstance(item_value, bool):
        return compare_boolean(item_value, operation, compare_value.lower() == 'true')
    elif isinstance(item_value, list):
        return compare_list(item_value, operation, int(compare_value))
    else:
        raise ValueError(f"Unsupported data type: {type(item_value)}")

def compare_string(item_value, operation, compare_value):
    if operation == "==":
        return item_value == compare_value
    elif operation == "!=":
        return item_value != compare_value
    elif operation == ">":
        return item_value > compare_value
    elif operation == "<":
        return item_value < compare_value
    elif operation == ">=":
        return item_value >= compare_value
    elif operation == "<=":
        return item_value <= compare_value
    elif operation == "contains":
        return compare_value in item_value
    elif operation == "startswith":
        return item_value.startswith(compare_value)
    elif operation == "endswith":
        return item_value.endswith(compare_value)

def compare_numeric(item_value, operation, compare_value):
    if operation == "==":
        return item_value == compare_value
    elif operation == "!=":
        return item_value != compare_value
    elif operation == ">":
        return item_value > compare_value
    elif operation == "<":
        return item_value < compare_value
    elif operation == ">=":
        return item_value >= compare_value
    elif operation == "<=":
        return item_value <= compare_value

def compare_boolean(item_value, operation, compare_value):
    if operation == "==":
        return item_value == compare_value
    elif operation == "!=":
        return item_value != compare_value

def compare_list(item_value, operation, compare_value):
    if operation == "==":
        return len(item_value) == compare_value
    elif operation == "!=":
        return len(item_value) != compare_value
    elif operation == ">":
        return len(item_value) > compare_value
    elif operation == "<":
        return len(item_value) < compare_value
    elif operation == ">=":
        return len(item_value) >= compare_value
    elif operation == "<=":
        return len(item_value) <= compare_value