# DataSaver.py

class DataSaver:

    # Method to write data in the file
    def save_data_to_file(self, data, file_path):
        try:
            with open(file_path, 'w') as file:
                file.write(str(data))
            print(f"Data saved to file: {file_path}")
        except Exception as e:
            print(f"Error saving data to file: {e}")

    def save_data_to_database(self, data):
        # Implement the logic to save data to the database
        pass
