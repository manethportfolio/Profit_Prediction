# READING DATA FROM SOME KIND OF A SOURCE 

import os
import sys 
from src.exception import CustomException
from src.logger import logging 
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.Stages.data_transformation import DataTransConfig
from src.Stages.data_transformation import DataTransformation

from src.Stages.model_trainer import ModelTrainerConfig
from src.Stages.model_trainer import ModelTrainer

@dataclass
class DataIngestionConfig:
#The trained data will be saved in the artficats folder as the following files
    train_data_path : str=os.path.join("artifacts","train.csv") 
    test_data_path : str=os.path.join("artifacts","test.csv")
    raw_data_path : str=os.path.join("artifacts","data.csv")

class DataIngestion:
    def __init__(self):
        # The three files above will be saved under that variable 
        self.ingestion_config= DataIngestionConfig()
    
    ''' 
    Data ingestion from the source, DB from utils file etc 
    '''
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv("notebook/data/1000_Companies.csv")
            logging.info("Read the dataset as a dataframe")

            # Make the directories above in the config file 
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            # Write some data to the csv file
            df.to_csv(self.ingestion_config.raw_data_path, index = False, header = True)

            logging.info("Train and split initiated")

            # Splitting
            train_set, test_set = train_test_split(df, test_size=0.2, random_state= 42)
            
            # Write the test data set to the train file
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header = True)

            # Write the test data set to the test file
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header = True)

            logging.info("Ingestion is completed")

            # Return the files 
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys) 


if __name__ == "__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))

