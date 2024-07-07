# Manipuler les données (charger, sauvegarder, filtrer, trier et afficher des données)

def process_file(raw_data):
    print(raw_data)
    rows = raw_data.split("\n")
    headers = rows[0].split(";")
    data = rows[1].split(";")

    return dict(zip(headers, data))
