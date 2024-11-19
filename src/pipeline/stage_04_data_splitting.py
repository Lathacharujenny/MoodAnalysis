from src.components.data_splitting import DataSplitting
from src.config.configuration import ConfigurationManger



class DataSplittingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManger()
        data_splitting_config = config.get_data_splitting_config()
        data_splitting = DataSplitting(config=data_splitting_config)
        data_splitting.load_data()
        data_splitting.splitting_data()

