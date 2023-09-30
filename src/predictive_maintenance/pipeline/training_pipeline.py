from src.predictive_maintenance.components.data_ingestion import DataIngestion
from src.predictive_maintenance.components.data_transformation import DataTransformation
from src.predictive_maintenance.components.model_trainer import ModelTrainer
import sys
from src.predictive_maintenance.exception import CustomException

#from src.exception import CustomException
#from src.logger import logging
from src.predictive_maintenance.exception import CustomException
from src.predictive_maintenance.logger import logging

# Training Pipleine
try:
        if __name__=="__main__":
                logging.info("Training pipeline initiated")
                data_ingestion=DataIngestion()
                train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()
                logging.info("Data Ingestion path completed.")

                logging.info("Data Transformation Step initated")
                data_transformation=DataTransformation()
                train_arr,test_arr=data_transformation.initiate_data_transformation(train_data_path, test_data_path)
                logging.info("Data Transformation step completed")

                logging.info("Model Trainer step initiated")
                model_trainer=ModelTrainer()
                model_trainer.initiate_model_training(train_arr,test_arr)
                logging.info("Model Trainer step completed")

                logging.info("Training Pipeline completed sucessfully")




except Exception as e:
        
        logging.info("Error occured in Training Pipeline")
        raise CustomException(e,sys)
