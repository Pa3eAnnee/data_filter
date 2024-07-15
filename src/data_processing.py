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

