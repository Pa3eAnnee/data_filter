import unittest
import os
import json
import csv
import xml.etree.ElementTree as ET
import yaml
from src.data_processing import process_file
from src.data_io import save_data_json, save_data_csv, save_data_xml, save_data_yaml

class TestDataSaving(unittest.TestCase):
    def setUp(self):
        self.test_data_path = "tests/data/test_data.csv"
        self.output_json = "tests/data/output_test.json"
        self.output_csv = "tests/data/output_test.csv"
        self.output_xml = "tests/data/output_test.xml"
        self.output_yaml = "tests/data/output_test.yaml"

    def tearDown(self):
        for file in [self.output_json, self.output_csv, self.output_xml, self.output_yaml]:
            if os.path.exists(file):
                os.remove(file)

    def test_save_to_json(self):
        data = process_file(self.test_data_path)
        
        save_data_json(data, self.output_json)
        
        self.assertTrue(os.path.exists(self.output_json))
        
        with open(self.output_json, 'r') as f:
            saved_data = json.load(f)
        
        self.assertEqual(len(saved_data), len(data))

    def test_save_to_csv(self):
        data = process_file(self.test_data_path)
        
        save_data_csv(data, self.output_csv)
        
        self.assertTrue(os.path.exists(self.output_csv))
        
        with open(self.output_csv, 'r') as f:
            csv_reader = csv.DictReader(f)
            saved_data = list(csv_reader)
        
        self.assertEqual(len(saved_data), len(data))

    def test_save_to_xml(self):
        data = process_file(self.test_data_path)
        
        save_data_xml(data, self.output_xml)
        
        self.assertTrue(os.path.exists(self.output_xml))
        
        tree = ET.parse(self.output_xml)
        root = tree.getroot()
        
        self.assertEqual(len(root), len(data))
        
        with open(self.output_xml, 'r') as f:
            xml_content = f.read()
        self.assertIn('\n', xml_content)
    
    def test_save_to_yaml(self):
        data = process_file(self.test_data_path)
        
        save_data_yaml(data, self.output_yaml)
        
        self.assertTrue(os.path.exists(self.output_yaml))
        
        with open(self.output_yaml, 'r') as f:
            saved_data = yaml.safe_load(f)
        
        self.assertEqual(len(saved_data), len(data))

if __name__ == "__main__":
    unittest.main()