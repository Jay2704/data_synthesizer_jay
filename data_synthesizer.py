# DataSynthesizer.py
from data_loader import DataLoader
from data_analyzer import DataAnalyzer
from model_generator import ModelGenerator
from data_saver import DataSaver

class DataSynthesizer:
    def __init__(self):
        self.data_loader = DataLoader()
        self.data_analyzer = DataAnalyzer()
        self.model_generator = ModelGenerator()
        self.data_saver = DataSaver()

    def load_data(self):
        raw_data = self.data_loader.read_data()
        return self.data_loader.parse_data(raw_data)

    def analyze_data(self, data):
        self.data_analyzer.analyze_distributions(data)
        self.data_analyzer.identify_relationships(data)
        self.data_analyzer.detect_sensitive_attributes(data)

    def generate_model(self, data):
        model_type = self.model_generator.select_model_type()
        self.model_generator.train_model(data, model_type)

    def generate_synthetic_data(self, model_type):
        synthetic_data = self.model_generator.generate_samples(model_type)
        return synthetic_data

    def save_data(self, data):
        file_path = self.data_saver.save_data_to_file(data)
        self.data_saver.save_data_to_database(data)
        return file_path
