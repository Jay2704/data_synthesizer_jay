classDiagram
    DataSynthesizer --> DataLoader : Loads
    DataSynthesizer --> DataAnalyzer : Analyzes
    DataSynthesizer --> ModelGenerator : Generates
    DataSynthesizer --> DataSaver : Saves

    class DataSynthesizer {
        +load_data()
        +analyze_data()
        +generate_model()
        +generate_synthetic_data()
        +save_data()
    }

    class DataLoader {
        +read_data(file_path)
        +parse_data()
    }

    class DataAnalyzer {
        +analyze_distributions()
        +identify_relationships()
        +detect_sensitive_attributes()
    }

    class ModelGenerator {
        +select_model_type()
        +train_model()
        +generate_samples()
    }

    class DataSaver {
        +save_data_to_file(file_path)
        +save_data_to_database()
    }
