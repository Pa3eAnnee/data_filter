import statistics

def identify_field_type(values):
    if all(isinstance(v, bool) or (isinstance(v, str) and str(v).lower() in ['true', 'false']) or v in [True, False] for v in values):
        print(f"{values} is bool")
        return "boolean"
    elif all(isinstance(v, (int, float)) or (isinstance(v, str) and v.replace('.', '').isdigit()) for v in values):
        print(f"{values} is numeric")
        return "numeric"
    elif all(isinstance(v, list) or (isinstance(v, str) and v.startswith('[') and v.endswith(']')) for v in values):
        print(f"{values} is list")
        return "list"
    else:
        print(f"{values} is string")
        return "string"
    

def calculate_numeric_stats(values):
    numeric_values = [float(v) if isinstance(v, str) else v for v in values]
    return {
        "min": min(numeric_values),
        "max": max(numeric_values),
        "average": statistics.mean(numeric_values)
    }


def calculate_boolean_stats(values):
    bool_values = [v if isinstance(v, bool) else str(v).lower() == 'true' for v in values]
    true_count = sum(bool_values)
    total = len(bool_values)
    return {
        "true_percentage": (true_count / total) * 100
    }


import statistics

def calculate_list_stats(values):
    lists = [eval(v) if isinstance(v, str) else v for v in values]
    
    lengths = [len(lst) for lst in lists]
    
    all_values = [item for lst in lists for item in lst]
    
    return {
        "min_length": min(lengths),
        "max_length": max(lengths),
        "average_length": statistics.mean(lengths),
        "total_length": sum(lengths),
        "min_value": min(all_values),
        "max_value": max(all_values),
        "average_value": statistics.mean(all_values),
        "total_items": len(all_values)
    }



def calculate_stats(data):
    if not data:
        return {}

    stats = {}
    for field in data[0].keys():
        values = [row[field] for row in data]
        field_type = identify_field_type(values)
        
        if field_type == "numeric":
            stats[field] = calculate_numeric_stats(values)
        elif field_type == "boolean":
            stats[field] = calculate_boolean_stats(values)
        elif field_type == "list":
            stats[field] = calculate_list_stats(values)
        else:
            stats[field] = {"type": "string"}

    return stats
