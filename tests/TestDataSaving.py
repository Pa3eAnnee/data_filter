import unittest
import os
import json
import csv
from src.data_processing import process_file
from src.data_io import save_data_json, save_data_csv

class TestDataSaving(unittest.TestCase):
    def setUp(self):
        self.test_data_path = "tests/data/test_data.csv"
        self.output_json = "tests/data/output_test.json"
        self.output_csv = "tests/data/output_test.csv"

    def tearDown(self):
        for file in [self.output_json, self.output_csv]:
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

if __name__ == "__main__":
    unittest.main()