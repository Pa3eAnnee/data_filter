import statistics

def identify_field_type(values):
    non_none_values = [v for v in values if v is not None]
    if not non_none_values:
        return "unknown"
    if all(isinstance(v, bool) or (isinstance(v, str) and str(v).lower() in ['true', 'false']) or v in [0, 1] for v in non_none_values):
        return "boolean"
    elif all(isinstance(v, (int, float)) or (isinstance(v, str) and v.replace('.', '').isdigit()) for v in non_none_values):
        return "numeric"
    elif all(isinstance(v, list) or (isinstance(v, str) and v.startswith('[') and v.endswith(']')) for v in non_none_values):
        return "list"
    else:
        return "string"
    

def calculate_numeric_stats(values):
    numeric_values = [float(v) if isinstance(v, str) else v for v in values if v is not None]
    if not numeric_values:
        return {"min": None, "max": None, "average": None}
    return {
        "min": min(numeric_values),
        "max": max(numeric_values),
        "average": statistics.mean(numeric_values)
    }


def calculate_boolean_stats(values):
    bool_values = [v if isinstance(v, bool) else 
                   (v == 1 or str(v).lower() == 'true') for v in values if v is not None]
    true_count = sum(bool_values)
    total = len(bool_values)
    return {
        "true_percentage": (true_count / total) * 100 if total > 0 else 0
    }


def calculate_list_stats(values):
    lists = [eval(v) if isinstance(v, str) else v for v in values if v is not None]
    if not lists:
        return {"min_length": None, "max_length": None, "average_length": None, 
                "total_length": 0, "min_value": None, "max_value": None, 
                "average_value": None, "total_items": 0}
    
    lengths = [len(lst) for lst in lists]
    all_values = [item for lst in lists for item in lst]
    
    return {
        "min_length": min(lengths),
        "max_length": max(lengths),
        "average_length": statistics.mean(lengths),
        "total_length": sum(lengths),
        "min_value": min(all_values) if all_values else None,
        "max_value": max(all_values) if all_values else None,
        "average_value": statistics.mean(all_values) if all_values else None,
        "total_items": len(all_values)
    }


def calculate_stats(data):
    if not data:
        return {}

    stats = {}
    for field in set().union(*data):  # This will get all unique keys from all dictionaries
        values = [row.get(field) for row in data]
        field_type = identify_field_type(values)
        
        if field_type == "numeric":
            stats[field] = calculate_numeric_stats(values)
        elif field_type == "boolean":
            stats[field] = calculate_boolean_stats(values)
        elif field_type == "list":
            stats[field] = calculate_list_stats(values)
        elif field_type == "unknown":
            stats[field] = {"type": "unknown"}
        else:
            stats[field] = {"type": "string"}
        
        stats[field]["type"] = field_type

    return stats
