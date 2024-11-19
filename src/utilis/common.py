from src.logger import logging
from src.exception import CustomException
from pathlib import Path
import sys
import os
import yaml
import requests
import pandas as pd



def read_yaml(filepath):
    # Loading the yaml file
    try:
        with open(filepath) as file_obj:
            content = yaml.safe_load(file_obj)
            logging.info(f'Loaded yaml {file_obj} successfully')
            return content
    except Exception as e:
        logging.error(f'Error Occured: {e}')
        raise CustomException(e,sys)


def create_directories(filepath):
    # Creating the directories
    try:
        if not os.path.exists(filepath):
            os.makedirs(filepath, exist_ok=True)
        else:
            logging.info(f'{filepath} already exists')
    except Exception as e:
        logging.error(f'Error occured: {e}')
        raise CustomException(e,sys)


def load_url_data(data_url):
    # Loading the data from url
    try:
        logging.info(f'Loading the data from url {data_url}.........')
        response = requests.get(data_url)
        json_data = response.json()
        data = pd.DataFrame(json_data)
        logging.info('Successfully loaded the data from the url')
        return data
    except Exception as e:
        logging.error(f'Error Occured: {e}')
        raise CustomException(e,sys)
        

def load_csv_data(filepath):
    # Load csv data
    try:
        logging.info(f'Loading data from {filepath}')
        if not os.path.exists(filepath):
            logging.info(f'File path {filepath} does not exist')
        data = pd.read_csv(filepath)
        logging.info(f'Successfully loaded data from {filepath}')
        return data
    except Exception as e:
        logging.error(f'Error Occured: {e}')
        raise CustomException(e,sys)

def save_csv_data(data, filepath):
    # Saving the data 
    try:
        data.to_csv(filepath, index=False)
        logging.info(f'Saved the data into {filepath}')
    except Exception as e:
        logging.error(f'Error Occured: {e}')
        raise CustomException(e,sys)
    

    