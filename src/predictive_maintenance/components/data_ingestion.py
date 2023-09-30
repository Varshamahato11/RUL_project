

import os
import sys   ## to handle custom exception and logging
from src.predictive_maintenance.exception import CustomException
from src.predictive_maintenance.logger import logging
from src.predictive_maintenance.utils import read_sql_data
import pandas as pd
from src.predictive_maintenance.utils import read_sql_data
from sklearn.model_selection import train_test_split


## to giv i/p parameters we use dataclass
from dataclasses import dataclass

@dataclass     # t define parameter
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train1.csv')
    logging.info("Train file loaded")
    test_data_path:str=os.path.join('artifacts','test1.csv')
    logging.info("Test file loaded")
    #raw_data_path:str=os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()


    def initiate_data_ingestion(self):
        try:
             # reading code will come over here(how to read from sql)

            df = read_sql_data()

            logging.info("Reading from MYSQL database.")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok = True)
            os.makedirs(os.path.dirname(self.ingestion_config.test_data_path), exist_ok = True)

            df[0].to_csv(self.ingestion_config.train_data_path, index = False, header = True)
            df[1].to_csv(self.ingestion_config.test_data_path, index = False, header = True)

            #df.to_csv(self.ingestion_config.train_data_path, index = False, header = True)
            #df.to_csv(self.ingestion_config.test_data_path, index = False, header = True)

            logging.info("Data Ingestion done.")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )

        except Exception as e:
            
            raise CustomException(e,sys)





    