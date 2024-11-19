from src.components.data_ingestion import DataIngestion
from src.config.configuration import ConfigurationManger


class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManger()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.loading_data()