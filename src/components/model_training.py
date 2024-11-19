from src.logger import logging
from src.exception import CustomException
import sys
import os
from src.entity.config_entity import ModelTrainingConfig
from src.utilis.common import load_csv_data
import numpy as np
import pickle
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.layers import *
from sklearn.utils.class_weight import compute_class_weight


class ModelTraining:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config

    def loading_data(self):
        try:
            logging.info(f'Loading Training data for model training')
            self.X_train = np.load(self.config.x_train_data_path)
            self.y_train = load_csv_data(self.config.y_train_data_path)
            
            logging.info(f'Loading Test data for model training')
            self.X_test = np.load(self.config.x_test_data_path)
            self.y_test = load_csv_data(self.config.y_test_data_path)

            return self.X_train, self.X_test, self.y_train, self.y_test
        
        except Exception as e:
            logging.error(f'Error Occured: {e}')
            raise CustomException(e,sys)
    
    def training_model(self):
        try:
            X_train, X_test, y_train, y_test = self.loading_data()

            logging.info('Loading maxlen pickle')
            with open(self.config.maxlen_path, 'rb') as file:
                maxlen = pickle.load(file)

            input_size = np.max(X_train)+1

            weights = compute_class_weight(
                class_weight='balanced', 
                classes=np.unique(y_train), 
                y=y_train
            )
            class_weights = dict(enumerate(weights))

            model = Sequential()
            
            model.add(Embedding(input_dim=input_size, output_dim=100, input_length=maxlen))
            model.add(Bidirectional(GRU(128, return_sequences=True)))
            model.add(Bidirectional(GRU(64, return_sequences=True)))
            model.add(BatchNormalization())
            model.add(Dropout(0.5))
            model.add(Bidirectional(GRU(64)))
            model.add(Dense(64, activation='relu'))
            model.add(Dropout(0.5))
            model.add(Dense(6, activation='softmax'))

            model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

            history = model.fit(X_train, y_train, validation_data=(X_test, y_test), class_weight=class_weights, batch_size=50, epochs=10, callbacks=[EarlyStopping(patience=3)])
            
            history_path = os.path.join(self.config.root_dir, 'history.pkl')
            logging.info(f'Dumping the history after training the model into: {history_path}')
            with open(history_path, 'wb') as file:
                pickle.dump(history.history, file)

            model_path = os.path.join(self.config.root_dir,'model.pkl')
            logging.info('Dumping the model into :{model_path}')
            with open(model_path, 'wb') as file:
                pickle.dump(model, file)

        except Exception as e:
            logging.error({e})
            raise CustomException(e,sys)


