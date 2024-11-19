from src.components.data_transformation import DataTransformation
from src.config.configuration import ConfigurationManger




class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManger()
        data_transformation_config = config.get_data_transformation_config()
        data_transforamtion = DataTransformation(config=data_transformation_config)
        data_transforamtion.load_pipeline()
        data_transforamtion.loading_data()
        data_transforamtion.transforming_data()
        data_transforamtion.label_encoding()
        data_transforamtion.saving_transformed_data()
