import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
import os

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig

    def get_data_transformer_object(selfs):
        """
        This Function is responsible for data transformation
        :return:
        """
        try:
            numerical_columns=["writing_score","reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parenta;_level_of_education",
                "test_prepration_course"
            ]

            num_pipeline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="medium")), #handling missing value
                    ("scaler",StandardScaler())
                ]
            )

            cat_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder",OneHotEncoder()),
                    ("scaler",StandardScaler())
                ]
            )

            logging.info("Categorical columns encoding completed")
            logging.info("Categorical columns encoding completed")

            preprocessor=ColumnTransformer([
                ("num_pipeline",num_pipeline,numerical_columns),
                ("cat_pipeline",cat_pipeline,categorical_columns)
                 ]

            )

            return preprocessor


        except Exception as e:
            raise CustomException(e,sys)
            pass

    def initiate_data_transformation(self,train_path,test_path):

        try:
            train_df=pd.read_csv(train_path)
            test_df =pd.read_csv(test_path)

            logging.info("Read train and test data completed")
            logging.info("Obtaining preprocessing object")

            preprocessing_obj=self.get_data_transformer_object()

            target_column_name="math_score"
            numerical_columns = ['writing_score',"reading_score"]

            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
        except:
            pass
