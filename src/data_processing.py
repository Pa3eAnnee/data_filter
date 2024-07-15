# Manipuler les données (charger, sauvegarder, filtrer, trier et afficher des données)
import json
import csv

from src.data_io import read_file


def check_extension(filepath):
    return filepath.split(".")[-1]

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
        values = row.split(";")
        dic = dict(zip(headers, values))
        data.append(dic)

    return data


def process_file(filepath):
    ext = check_extension(filepath)
    if ext == "csv":
        return process_csv(filepath)
    if ext == "json":
        return process_json(filepath)
    else:
        raise ValueError("Invalid file format")

def save_data_json(data, filename):
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Data successfully saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")

def save_data_csv(data, filename):
    try:
        # Assuming data is a list of dictionaries
        if not data:
            print("No data to save.")
            return

        # Get the fieldnames from the first dictionary in the list
        fieldnames = list(data[0].keys())

        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        print(f"Data successfully saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")

