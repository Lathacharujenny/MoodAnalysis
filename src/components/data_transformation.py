from src.logger import logging
from src.exception import CustomException
import sys
from src.entity.config_entity import DataTransformationConfig
import pickle
import os
from src.utilis.common import load_csv_data, save_csv_data
from sklearn.preprocessing import LabelEncoder
import json



class DataTransformation:
    def __init__(self, config:DataTransformationConfig):
        self.config = config

    def load_pipeline(self):
        try:
            logging.info('Loading the pipeline')
            with open(self.config.pipeline_path, 'rb') as f:
                self.pipeline = pickle.load(f)
            logging.info('Successfully Loaded pipeline')
            return self.pipeline
        except Exception as e:
            logging.error(f'Error Occured: {e}')
            raise CustomException(e,sys)
        
    def loading_data(self):
        try:
            self.data = load_csv_data(self.config.data_path)
            
            return self.data
        except Exception as e:
            logging.error(f'Error Occured: {e}')
            raise CustomException(e,sys)
               
    def label_encoding(self):
        try:
            logging.info('Encoding the labels')
            data = self.loading_data()
            encoder = LabelEncoder()
            data['label'] = encoder.fit_transform(data['label'])
            label_encoding = dict(zip(encoder.classes_, encoder.transform(encoder.classes_)))
            label_dict = {str(key):int(value) for key, value in label_encoding.items()}
            label_path = os.path.join(self.config.labels_path,'labels.json')
            with open(label_path, 'w') as file_obj:
                json.dump(label_dict, file_obj, indent=4)
            logging.info(f'Successfully dumped the labels dict into {label_path}')
            return data['label']
        except Exception as e:
            logging.error(f'Error Occurred : {e}')
            raise CustomException(e,sys)
        
    def transforming_data(self):
        try:
            logging.info('Cleaning the data started.......')
            pipeline = self.load_pipeline()
            data = self.loading_data()
            data['text'] = pipeline.fit_transform(data)
            return data['text']
    
        except Exception as e:
            logging.error(f'Error Occured: {e}')
            raise CustomException(e,sys)
        
    def saving_transformed_data(self):
        try:
            file_path = os.path.join(self.config.root_dir,'cleaned_data.csv')
            data = self.loading_data()
            data['label'] = self.label_encoding()
            data['text'] = self.transforming_data()
            data.dropna(inplace=True)
            save_csv_data(data, file_path)
            logging.info('Finished the cleaning data ...............')
        except Exception as e:
            logging.error(f'Error Occured: {e}')
            raise CustomException(e,sys)
        
 




