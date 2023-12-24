import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object # To load our pickle file 


class PredictPipeline:
    def __init__(self):
        pass

    # Mention the pkl files, triggers a util function 
    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features) # transforming the features
            preds=model.predict(data_scaled) # Preiciton collected 
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)


'''
Responsible in mapping all the inputs from the front end to the back end 
'''
class CustomData:
    def __init__( self,
        R_n_D_Spend: int,
        Administration:int,
        Marketing_Spend: int,
        State: str
    ):
        self.R_n_D_Spend = R_n_D_Spend,
        self.Administration = Administration,
        self.Marketing_Spend = Marketing_Spend,
        self.State = State


    '''
    Return all input as a dataframe 

    '''
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "R_n_D_Spend": [self.R_n_D_Spend],
                "Administration": [self.Administration],
                "Marketing_Spend": [self.Marketing_Spend],
                "State": [self.State],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)