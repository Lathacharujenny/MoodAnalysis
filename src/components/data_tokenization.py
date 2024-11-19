from src.logger import logging
from src.exception import CustomException
import sys
import os
from src.entity.config_entity import DataTokenizationConfig
import nltk
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from src.utilis.common import load_csv_data, save_csv_data
import pickle
import numpy as np


class DataTokenization:
    def __init__(self, config: DataTokenizationConfig):
        self.config = config

    def loading_data(self):
        try:
            logging.info('Loading Training data for tokenization')
            self.train_data = load_csv_data(self.config.train_data_path)
            self.train_data.dropna(inplace=True)
            logging.info(f'Null values of train_data: {self.train_data.isnull().sum()}')
            self.X_train = self.train_data['text']
            self.y_train = self.train_data['label']
            
            logging.info('Loading Test data for tokenization')
            self.test_data = load_csv_data(self.config.test_data_path)
            self.test_data.dropna(inplace=True)
            logging.info(f'Null values of test_data: {self.test_data.isnull().sum()}')
            self.X_test = self.test_data['text']
            self.y_test = self.test_data['label']
            
            return self.X_train, self.y_train, self.X_test, self.y_test
        
        except Exception as e:
            logging.error(f'Error Occured: {e}')
            raise CustomException(e,sys)
        
    def data_tokenizing(self):
        try:
            X_train, y_train, X_test, y_test = self.loading_data()

            logging.info('Tokenizing the data')

            tokenizer = Tokenizer(num_words=50000)
            tokenizer.fit_on_texts(X_train)

            X_train_sequence = tokenizer.texts_to_sequences(X_train)
            X_test_sequence = tokenizer.texts_to_sequences(X_test)

            maxlen = max((len(token)) for token in X_train_sequence)
            logging.info(f'Maxlength of sequence is {maxlen}')

            X_train_paddded = pad_sequences(X_train_sequence, maxlen=maxlen, padding='post')
            X_test_padded = pad_sequences(X_test_sequence, maxlen=maxlen, padding='post')

            tokenizer_path = os.path.join(self.config.pickle_path, 'tokenizer.pkl')
            maxlen_path = os.path.join(self.config.pickle_path, 'maxlen.pkl')

            logging.info(f'Dumping the tokenizer into {tokenizer_path}')
            with open(tokenizer_path, 'wb') as file:
                pickle.dump(tokenizer, file)

            logging.info(f'Dumping the maxlen into {maxlen_path}')
            with open(maxlen_path, 'wb') as file:
                pickle.dump(maxlen, file)

            logging.info(f'Saving the tokenized data into :{self.config.tokenizer_data_path}')
            np.save(os.path.join(self.config.tokenizer_data_path, 'X_train.npy'), X_train_paddded)
            np.save(os.path.join(self.config.tokenizer_data_path, 'X_test.npy'), X_test_padded)
            save_csv_data(y_train, os.path.join(self.config.tokenizer_data_path, 'y_train.csv'))
            save_csv_data(y_test, os.path.join(self.config.tokenizer_data_path, 'y_test.csv'))            


        except Exception as e:
            logging.error(f'Error Occured: {e}')
            raise CustomException(e,sys)
        
    

    