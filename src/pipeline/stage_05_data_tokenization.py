from src.config.configuration import ConfigurationManger
from src.components.data_tokenization import DataTokenization


class DataTokenizationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManger()
        data_tokenization_config = config.get_data_tokenization_config()
        data_tokenization = DataTokenization(config=data_tokenization_config)
        data_tokenization.loading_data()
        data_tokenization.data_tokenizing()