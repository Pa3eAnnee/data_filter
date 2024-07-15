import csv
import json
import xml.etree.ElementTree as ET
import xml.dom.minidom


def read_file(file_path):
    with open(file_path, "r") as f:
        return f.read()


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
def save_data_xml(data, filename):
    try:
        root = ET.Element("root")
        for item in data:
            item_elem = ET.SubElement(root, "item")
            for key, value in item.items():
                child = ET.SubElement(item_elem, key)
                child.text = str(value)
        
        # Convert the ElementTree to a string
        xml_string = ET.tostring(root, encoding='unicode')
        
        # Use minidom to pretty-print the XML
        dom = xml.dom.minidom.parseString(xml_string)
        pretty_xml = dom.toprettyxml(indent="  ")
        
        # Write the formatted XML to the file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(pretty_xml)
        
        print(f"Data successfully saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")


