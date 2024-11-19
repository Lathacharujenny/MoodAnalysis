from src.logger import logging
from src.exception import CustomException
import sys
import os
from src.entity.config_entity import DataSplittingConfig
from src.utilis.common import load_csv_data, save_csv_data
from sklearn.model_selection import train_test_split


class DataSplitting:
    def __init__(self, config:DataSplittingConfig):
        self.config = config

    def load_data(self):
        try:
            logging.info('Loading cleaned data for data splitting')
            data = load_csv_data(self.config.data_path)
            return data
        except Exception as e:
            logging.error(f'Error Occured {e}')
            raise CustomException(e,sys)
        
    def splitting_data(self):
        try:
            data = self.load_data()
            logging.info(f'Splitting the trian and test data')
            train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

            logging.info(f'Saving the train and test data')
            save_csv_data(train_data, os.path.join(self.config.root_dir, 'train.csv'))
            save_csv_data(test_data,os.path.join(self.config.root_dir, 'test.csv'))

        except Exception as e:
            logging.error(f'Error Occured : {e}')
            raise CustomException(e,sys)

