import os
import sys   ## to handle custom exception and logging
from src.predictive_maintenance.exception import CustomException
from src.predictive_maintenance.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score
from dataclasses import dataclass
import pickle



load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv('db')

#Function for reading data from MYSQL workbench
def read_sql_data():
    logging.info("Reading SQL Database")
    
    try:
        logging.info("Trying to connect with MySQL workbench")
        mydb = pymysql.connect(
            host = host,
            user = user,
            password = password,
            db = db
        )
        logging.info("Connection establish",mydb)
        
        df_train = pd.read_sql_query("select * from train1", mydb)
        logging.info("Train file readed")
        df_test = pd.read_sql_query("select * from test1", mydb)
        logging.info("Test file readed")
        
        return df_train, df_test
    
    except Exception as e:
        logging.info("Error occured in reading data from MYSQL database")
        raise CustomException(e,sys)

    #Function for saving a object in pickle file format

def save_object(file_path,obj):
    try:
        logging.info(f"Saving object for {file_path} in pickle format started")
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok = True)

        #os.makedirs=(dir_path, exist_ok = True)

        with open(file_path,'wb') as file_obj:
            pickle.dump(obj, file_obj)
        logging.info(f"{file_obj} saved in pickle format with it's define path")






    except Exception as e:
        logging.info(f"Error occur in saving pickle object for {file_obj}")
        raise CustomException(e,sys)


        #Below one is Function for evaluating different model, for the accuracy

def evaluate_model(X_train, y_train, X_test, y_test, models,param):
    try:
        logging.info("Model Training Started")
        report= {}
        logging.info("Creating model report")

        for i in range(len(models)):
            model=list(models.values())[i]
            logging.info("Model Listed in Dictionary")
            para=param[list(models.keys())[i]]

            gs=GridSearchCV(model,para,cv=3)
            logging.info("Model getting trained using hyperparameter")
            gs.fit(X_train,y_train)


            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            logging.info(f"{model} trained")

            y_test_pred=model.predict(X_test)
            logging.info(f"{model} predicted")

            test_model_score= r2_score(y_test, y_test_pred)
            logging.info("Report generated")
            report[list(models.keys())[i]] = test_model_score
        logging.info("All models report generated")
        return report

    except Exception as e:
        logging.info("Error occur at Model Training Step")
        raise CustomException(e,sys)


        #Defining Function for loading the object

def load_object(file_path):
    try:
        logging.info("load object started")
        with open(file_path, "rb") as file_obj:
            logging.info("Pickle file loaded.")
            return pickle.load(file_obj)

    except Exception as e:
        logging.info()
        raise CustomException(e,sys)




     
