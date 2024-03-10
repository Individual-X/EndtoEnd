import pandas as pd
import numpy as np
import sys
import os
from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from src.exception import CustomException
from src.logger import logging

@dataclass
class datatransformationconfig:
    preprocessor_obj_file_path: str = os.path.join('E:\\Python\\AI\\Project\\EndtoEnd\\artifacts',"preprocessor.pkl")

class datatransformation:
    def __init__(self):
        self.data_transformation = datatransformationconfig()
    def get_data_transformer_object(self):
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]
            num_pipeline = Pipeline(
                steps = [
                    ("Imputer", SimpleImputer(strategy="median")),
                    ("Scaler", StandardScaler())
                ]
            )
            logging.info("Numerical transformer Executed")
            categorical_pipeline = Pipeline(
                steps=[
                    ("Imputer", SimpleImputer(strategy="most_frequent")),
                    ("Onehot Encoder", OneHotEncoder()),
                    ("Scaler", StandardScaler())
                    
                ]
            )
            logging.info("Categorical transformaer executed")
            prepocessor = ColumnTransformer(
                [
                    ("Numerical pipeline", num_pipeline, numerical_columns),
                    ("Categorical pipeline", categorical_pipeline, categorical_columns)
                ]
            )
            return prepocessor
        
        except Exception as e:
            raise CustomException(e,sys)
    
    def initiate_datatransformation(self,train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df= pd.read_csv(test_path)
            logging.info("Train Test Data From data ingestion")
            preprocessing_obj = self.get_data_transformer_object()
            targey
            
        
        
        except Exception as e:
            raise CustomException(e,sys)