
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
import re
import os
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import pickle
from src.logger import logging
import sys
from src.exception import CustomException
from pathlib import Path

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

stop_words = stopwords.words('english')
lemmatizer = WordNetLemmatizer()

contraction_dict = {
    "ive": "I have",
    "dont": "don't",
    "cant": "can't",
    "wont": "won't",
    "isnt": "isn't",
    "wasnt": "wasn't",
    "hasnt": "hasn't",
    "havent": "haven't",
    "im": "I am",
    "youre": "you are",
    "hes": "he is",
    "shes": "she is",
    "its": "it is",
    "were": "we are",
    "theyre": "they are",
    "ive": "I have",
    "id": "I would",
    "ive": "I have",
    "wouldve": "would have",
    "couldve": "could have",
    "shouldve": "should have"
}

class DataCleaner(BaseEstimator, TransformerMixin):
    def __init__(self, contraction_dict=contraction_dict):
        self.contraction_dict = contraction_dict


    def fit(self, X, y=None):
        return self
    
    def transform(self, X):

        # Check if the input is a Pandas Series or Dataframe
        if isinstance (X, pd.DataFrame):
            if 'text' not in X.columns:
                raise ValueError('DataFrame must contain text column')
            X = X.dropna()
            X = X.drop_duplicates()
            X = X['text']

        if not isinstance(X, pd.Series):
            raise ValueError('Data must be DataFrame or Series')
        
        X = X.str.lower()
        X = X.apply(lambda text: ' '.join(contraction_dict.get(word, word) for word in word_tokenize(text)))
        X = X.apply(lambda text: ' '.join([lemmatizer.lemmatize(word) for word in word_tokenize(text)]))
        X = X.apply(lambda text: re.sub(r'http?S+', '', text))
        X = X.apply(lambda text: re.sub(r'[^a-zA-Z\s]', '', text))
        X = X.apply(lambda text: re.sub(r'\d+', '', text))
        X = X.apply(lambda text: re.sub(r'\s+', ' ', text))
        X = X.apply(lambda text: ' '.join([word for word in word_tokenize(text) if word not in stop_words]))
        X = X.str.replace(r'\bn\b', '', regex=True)

        return X
    
    def create_pipeline(self):
        self.pipeline = Pipeline(steps=[
            ('data_cleaner', self)
        ])

    def save_pipeline(self):
        try:
           file_path = Path('artifacts/cleaning_pipeline')
           os.makedirs(file_path, exist_ok=True)
           with open(file_path/'cleaning_pipeline.pkl', 'wb') as f:
              pickle.dump(self.pipeline, f)
           logging.info('Pipeline Successfully dumped')
        except Exception as e:
            logging.error(f'Error Occured: {e}')
            raise CustomException(e,sys)


if __name__=='__main__':
     obj = DataCleaner()
     obj.create_pipeline()
     obj.save_pipeline()




