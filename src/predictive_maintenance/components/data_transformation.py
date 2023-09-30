import pandas as pd 
import numpy as np
import sys
import pickle
from dataclasses import dataclass
from src.predictive_maintenance.exception import CustomException
from src.predictive_maintenance.logger import logging
from sklearn.pipeline import Pipeline
from src.predictive_maintenance.utils import save_object
from sklearn.preprocessing import RobustScaler
from sklearn.decomposition import PCA
import os
from  sklearn.compose import ColumnTransformer

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts", "preprocessor.pkl") # pickle file is going to be save int this path

#Creating DataTransformation Class
class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig() # creating var to store path
        logging.info("Data Transformation Config Class initiated")

    # this is function which is going to do feature engineering and data transformation
    def get_data_transformer_object(self):
        try:
            logging.info("Data Transformation object selection class started")
            num_cols=['Engine_no', 'Cycle_no',
            'LPC_outlet_temperature',
            'HPC_outlet_temperature','LPT_outlet_temperature',
            'HPC_outlet_pressure',
            'Physical_fan_speed','Physical_core_speed',
            'HPC_outlet_static_pressure','Fuel_flow_ratio','Fan_speed',
            'Bypass_ratio','Bleed_enthalpy',
            'High_pressure_cool_air_flow','Low_pressure_cool_air_flow'
           
       
       
      
      
      
       
            ]
            logging.info("Numericals Columns Added.")
            logging.info("Pipeline steps initiated for scaling & applying the PCA.")
            num_pipeline=Pipeline(

                steps=[
                    ("scaler",RobustScaler()),
                    ("PCA",PCA(n_components=8))
                ]
                
            )
            logging.info("Pipeline created.")
            logging.info("Preprocessor object creation started.")
            preprocessor=ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline,num_cols)
                ]
            )
            logging.info("Preprocessor object created.")
            return preprocessor


        except Exception as e:
            logging.info("Error occur at getting tranformation object.")
            raise CustomException(e,sys)


    def initiate_data_transformation(self,train_path,test_path): #  Function for initializing the data transformation 

        try:
            
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            

            train_df["RUL"][train_df["RUL"]>103]=103
            test_df["RUL"][test_df["RUL"]>103]=103
            

            # logging.info("Preprocessor object initiated for the train & test data")
            # preprocessor_obj=self.get_data_transformer_object()

            target_column_name="RUL"

            drop_cols=[
                'Setting_1', 'Setting_2', 'Setting_3', 'Fan_inlet_temperature', 'Fan_inlet_pressure', 
                'Bypass_duct_pressure', 'Engine_pressure_ratio', 'Core_speed', 'Burner_fuel_air_ratio', 
                'Required_fan_speed', 'Required_fan_conversion_speed'
            ]

            #logging.info("Feature selection and target feature initiated for train and test data.")
            input_feature_train_df=train_df.drop(columns=[target_column_name] + drop_cols)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name] + drop_cols)
            target_feature_test_df=test_df[target_column_name]
            #logging.info("Input & Target features defined for train & test data")
            
            preprocessor_obj = self.get_data_transformer_object()
            logging.info("Applying preprocessing obj on train & test dataframe")
            
            
            
              #Transforming into Preprocessor object to data
            #logging.info("Applying preprocessing obj on train & test dataframe")
            input_feature_train_arr=preprocessor_obj.fit_transform(input_feature_train_df) 
            input_feature_test_arr= preprocessor_obj.transform(input_feature_test_df)
            logging.info("Preprocessor applied to data frame")
            
             #Converting into numpy array for train & test data

            logging.info("Converting Preprocessor array into numpy array")
            train_arr= np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr= np.c_[input_feature_test_arr, np.array(target_feature_test_df)]
            logging.info("Data transform to numpy array.")


            #function from save the preprocessor file
            logging.info("Saving the Preprocessor object initialized")
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessor_obj
            )
            logging.info("Preprocessor file saved as Pickle file")
            logging.info("Data Transformation step completed")

            return(
                train_arr,test_arr
            )


        except Exception as e:
            logging.info("Error occur at initializing the data Transformation step")
            raise CustomException(e,sys)














        
            


            

            

        except Exception as e:
            logging.info("")
            raise CustomException(e,sys)
           

             
            
             

                

           

          

    


  

        
          

       

            




             


              
        
            

            
            

     


                                                




