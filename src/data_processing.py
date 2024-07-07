# Manipuler les données (charger, sauvegarder, filtrer, trier et afficher des données)

def process_file(csv_text):
    rows = csv_text.split('\n')
    headers = rows[0].split(';')

    data = []

    for row in rows[1:]:
        values = row.split(';')
        dic = dict(zip(headers, values))
        data.append(dic)

    return data
