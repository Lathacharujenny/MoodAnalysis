from src.config.configuration import ConfigurationManger
from src.components.model_training import ModelTraining


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManger()
        model_training_config = config.get_model_training_config()
        model_training = ModelTraining(config=model_training_config)
        model_training.loading_data()
        model_training.training_model()