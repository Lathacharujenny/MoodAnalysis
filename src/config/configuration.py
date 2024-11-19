from src.entity.config_entity import DataIngestionConfig, DataTransformationConfig, DataSplittingConfig, ModelTrainingConfig, DataTokenizationConfig, ModelEvaluationConfig
from src.constants import *
from src.utilis.common import read_yaml, create_directories

class ConfigurationManger:
    def __init__(self, config_filepath = CONFIG_FILE_PATH):
        self.config = read_yaml(config_filepath)
        create_directories(self.config['artifacts_root'])


    def get_data_ingestion_config(self):
        config = self.config['data_ingestion']
        create_directories(config['root_dir'])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config['root_dir'],
            data_url=config['data_url']
        )

        return data_ingestion_config
    
    def get_data_transformation_config(self):
        config = self.config['data_transformation']
        create_directories(config['root_dir'])
        create_directories(config['labels_path'])

        data_transformation_config = DataTransformationConfig(
            root_dir=config['root_dir'],
            data_path = config['data_path'],
            pipeline_path=config['pipeline_path'],
            labels_path=config['labels_path']
        )
        
        return data_transformation_config
    
    def get_data_splitting_config(self):
        config = self.config['data_splitting']
        create_directories(config['root_dir'])

        data_splitting_config = DataSplittingConfig(
            root_dir=config['root_dir'],
            data_path=config['data_path']
        )

        return data_splitting_config
    
    def get_data_tokenization_config(self):
        config = self.config['data_tokenization']
        create_directories(config['root_dir'])
        create_directories(config['pickle_path'])
        create_directories(config['tokenizer_data_path'])

        data_tokenization_config = DataTokenizationConfig(
            root_dir=config['root_dir'],
            train_data_path=config['train_data_path'],
            test_data_path=config['test_data_path'],
            pickle_path=config['pickle_path'],
            tokenizer_data_path=config['tokenizer_data_path']
        )
        
        return data_tokenization_config
    
    def get_model_training_config(self):
        config = self.config['model_training']
        create_directories(config['root_dir'])

        model_training_config = ModelTrainingConfig(
            root_dir=config['root_dir'],
            x_train_data_path=config['x_train_data_path'],
            x_test_data_path=config['x_test_data_path'],
            y_train_data_path=config['y_train_data_path'],
            y_test_data_path=config['y_test_data_path'],
            maxlen_path=config['maxlen_path']
        )

        return model_training_config
    
    def get_model_evaluation_config(self):
        config = self.config['model_evaluation']
        create_directories(config['root_dir'])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config['root_dir'],
            model_path=config['model_path'],
            model_history_path=config['model_history_path'],
            x_test_data_path=config['x_test_data_path'],
            y_test_data_path=config['y_test_data_path']
        )

        return model_evaluation_config


if __name__=='__main__':
    obj = ConfigurationManger()
    obj.get_data_ingestion_config()