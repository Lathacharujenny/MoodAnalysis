from src.components.data_cleaning import DataCleaner
from src.config.configuration import ConfigurationManger


class DataCleaningPipeline:
    def __init__(self):
        pass

    def main(self):
        pipeline = DataCleaner()
        pipeline.create_pipeline()
        pipeline.save_pipeline()