import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    #Create train and test data folder
    train_data_path: str = os.path.join('artifacts', 'train_data.csv')
    test_data_path: str = os.path.join('artifacts', 'test_data.csv')
    raw_data_path: str=os.path.join('artifacts', 'raw_data.csv')

class DataIngestion:
    def __init__(self):
        self.Ingestion_config = DataIngestionConfig()
    
    def Initiate_data_ingestion(self):
        logging.info('Starting data ingestion from source')
        try:
            df = pd.read_csv('AI\Project\EndtoEnd\Notebook\Data\stud.csv')
            logging.info('data has been read from source')
            #making directory for the train and test data files
            os.makedirs(os.path.dirname(self.Ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.Ingestion_config.raw_data_path, Index=False, header = True)
        except:
            pass