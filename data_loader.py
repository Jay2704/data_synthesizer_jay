# data_loader.py
import json


# Class to load data form the user
class DataLoader:

    # read the data from the input
    def read_data(self):
        file_path = input("Enter the file path: ")
        return self.read_from_file(file_path)

    def read_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                data = file.read()
            return data
        except FileNotFoundError:
            print(f"File not found at path: {file_path}")
            return None


    # parsing the attributes of the data
    def parse_data(self, json_data):
        try:
            parsed_data = json.loads(json_data)
            return parsed_data
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON data: {e}")
            return None
