import sys
import os
from src.logger import logging
from src.exception import CustomException
from src.entity.config_entity import DataIngestionConfig
import requests
import pandas as pd
import os
from src.utilis.common import load_url_data, save_csv_data, load_csv_data


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        logging.info(f'COnfig: {self.config}')

    def loading_data(self):
        try:
          logging.info('Entered the Data Ingestion')
          data = load_url_data(self.config.data_url)
          data_path = os.path.join(self.config.root_dir,'emotions.csv')
          print('Shape of the data: ', data.shape)
          save_csv_data(data, data_path)
          logging.info(f'Successfully saved the data')
        except Exception as e:
            logging.error(f'Error Occured: {e}')
            raise CustomException(e,sys)
        