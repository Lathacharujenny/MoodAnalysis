from src.logger import logging
from src.exception import CustomException
import sys
import os
from src.entity.config_entity import ModelEvaluationConfig
import pickle
import numpy as np
from src.utilis.common import load_csv_data, save_csv_data
from sklearn.metrics import confusion_matrix, accuracy_score
import pandas as pd


class ModelEvaluation:
    def __init__(self, config:ModelEvaluationConfig):
        self.config = config

    def load_data(self):
        try:
            logging.info('Loading test data for evaluation')
            self.X_test = np.load(self.config.x_test_data_path)
            self.y_test = load_csv_data(self.config.y_test_data_path)
            return self.X_test, self.y_test
        except Exception as e:
            logging.error(f'Error Occured: {e}')
            raise CustomException(e,sys)

    def model_evaluation(self):
        try:
            X_test, y_test = self.load_data()

            logging.info(f'Loading model of the history : {self.config.model_history_path}')
            with open(self.config.model_history_path, 'rb') as file:
                history = pickle.load(file)
            print(history)

            logging.info(f'Loading the model: {self.config.model_path}')
            with open(self.config.model_path, 'rb') as file:
                model = pickle.load(file)

            logging.info(f'Saving the history into {self.config.root_dir}')
            
            history_df = pd.DataFrame(history)

            save_csv_data(history_df, os.path.join(self.config.root_dir, 'history.csv'))
            
            y_pred = model.predict(X_test)
            y_pred = np.argmax(y_pred, axis=1)
            accuracy = accuracy_score(y_test, y_pred)
            conf_matrix = confusion_matrix(y_test, y_pred)
            conf_matrix_df = pd.DataFrame(conf_matrix)
            save_csv_data(conf_matrix_df, os.path.join(self.config.root_dir, 'confusion_matrix.csv'))

            logging.info(f'Accuracy: {accuracy}')
            logging.info(f'Confusion Matric: {conf_matrix}')

        except Exception as e:
            logging.error(f'Error Occured: {e}')
            raise CustomException(e,sys)