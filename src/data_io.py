import csv
import json


def read_csv(file_path):
    data = []
    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data


def write_csv(file_path, data):
    with open(file_path, "w", newline="") as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def read_json(file_path):
    with open(file_path) as json_file:
        data = json.load(json_file)
    return data


def write_json(file_path, data):
    with open(file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)
