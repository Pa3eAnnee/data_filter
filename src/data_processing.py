# Manipuler les données (charger, sauvegarder, filtrer, trier et afficher des données)
import json
import yaml
import xml.etree.ElementTree as ET

from src.data_io import read_file


def check_extension(filepath):
    return filepath.split(".")[-1]

def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
    
def is_boolean(s):
    return s.lower() in ('true', 'false', '1', '0')


def process_json(filepath):
    with open(filepath, "r") as file:
        data = json.load(file)

    return data

def process_csv(filepath):
    raw_data = read_file(filepath)
    rows = raw_data.split("\n")
    headers = rows[0].split(";")

    data = []

    for row in rows[1:]:
        if row.strip():
            values = row.split(";")
            dic = {}
            for header, value in zip(headers, values):
                value = value.strip().strip('"')
                if is_integer(value):
                    dic[header] = int(value)
                elif is_boolean(value):
                    dic[header] = value.lower() in ('true', '1')
                else:
                    dic[header] = value
            data.append(dic)

    return data



def process_xml(filepath):
    tree = ET.parse(filepath)
    root = tree.getroot()
    
    data = []
    
    for item in root:
        dic = {}
        for child in item:
            value = child.text.strip() if child.text else ""
            if is_integer(value):
                dic[child.tag] = int(value)
            elif is_boolean(value):
                dic[child.tag] = value.lower() in ('true', '1')
            else:
                dic[child.tag] = value
        data.append(dic)
    
    return data


def process_yaml(filepath):
    with open(filepath, 'r') as file:
        data = yaml.safe_load(file)
    
    # If the YAML file contains a list at the root level, process each item
    if isinstance(data, list):
        for item in data:
            for key, value in item.items():
                if isinstance(value, str):
                    if is_integer(value):
                        item[key] = int(value)
                    elif is_boolean(value):
                        item[key] = value.lower() in ('true', '1')
    
    return data

def process_file(filepath):
    ext = check_extension(filepath)
    if ext == "csv":
        return process_csv(filepath)
    if ext == "json":
        return process_json(filepath)
    if ext == "xml":
        return process_xml(filepath)
    if ext == "yaml":
        return process_yaml(filepath)
    else:
        raise ValueError("Invalid file format")

