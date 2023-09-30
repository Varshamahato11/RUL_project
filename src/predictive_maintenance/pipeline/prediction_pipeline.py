import os,sys
from src.predictive_maintenance.exception import CustomException
from src.predictive_maintenance.logger import logging
from src.predictive_maintenance.utils import load_object
import pandas as pd


# class for predition pipeline

class PredictPipeline:

        def __init__(self):
                pass

        def predict(self, features):
                try:
                        logging.info("prediction pipeline path started")
                        preprocessor_path=os.path.join("artifacts", "preprocessor.pkl")
                        model_path=os.path.join("artifacts", "model.pkl") 
                        logging.info("Preprocessor & Model path joined")

                        preprocessor=load_object(preprocessor_path) 
                        model= load_object(model_path)
                        logging.info("Preprocessor object loaded")

                        data_scaled=preprocessor.transform(features) 
                        logging.info("Features transform through Preprocessor")

                        pred= model.predict(data_scaled)
                        logging.info("Output predicted through model")

                        return pred

                except Exception as e:
                        logging.info("Error occured in prediction step.")
                        raise CustomException(e,sys)


        #Defining the custom class to input data through form

class CustomData:
        logging.info("Initializing custom data")
        def __init__(self,

                Engine_no:int,
                Cycle_no:int,
                LPC_outlet_temperature:float,
                HPC_outlet_temperature:float,
                LPT_outlet_temperature:float,
                HPC_outlet_pressure:float,
                Physical_fan_speed:float,
                Physical_core_speed:float,
                HPC_outlet_static_pressure:float,
                Fuel_flow_ratio:float,
                Fan_speed:float,
                Bypass_ratio:float,
                Bleed_enthalpy:float,
                High_pressure_cool_air_flow:float,
                Low_pressure_cool_air_flow:float):

        #self.engine_no=Engine_no
                self.Engine_no = Engine_no
                self.Cycle_no= Cycle_no
                self.LPC_outlet_temperature = LPC_outlet_temperature
                self.HPC_outlet_temperature = HPC_outlet_temperature
                self.LPT_outlet_temperature = LPT_outlet_temperature
                self.HPC_outlet_pressure = HPC_outlet_pressure
                self.Physical_fan_speed= Physical_fan_speed
                self.Physical_core_speed = Physical_core_speed
                self.HPC_outlet_static_pressure = HPC_outlet_static_pressure
                self.Fuel_flow_ratio = Fuel_flow_ratio
                self.Fan_speed= Fan_speed
                self.Bypass_ratio = Bypass_ratio
                self.Bleed_enthalpy = Bleed_enthalpy
                self.High_pressure_cool_air_flow= High_pressure_cool_air_flow
                self.Low_pressure_cool_air_flow = Low_pressure_cool_air_flow

                logging.info("All features self initialized")

                 #defining function to store obtain data in the form of the dataframe
                
                
        def get_data_as_dataframe(self):
                try:
                        logging.info("get_data_as_dataframe")
                        custom_data_input_dict={
                                "Engine_no":[self.Engine_no],
                                "Cycle_no":[self.Cycle_no],
                                "LPC_outlet_temperature":[self.LPT_outlet_temperature],
                                "HPC_outlet_temperature":[self.HPC_outlet_temperature],
                                "LPT_outlet_temperature":[self.LPT_outlet_temperature],
                                "HPC_outlet_pressure":[self.HPC_outlet_pressure],
                                "Physical_fan_speed":[self.Physical_fan_speed],
                                "Physical_core_speed":[self.Physical_core_speed],
                                "HPC_outlet_static_pressure":[self.HPC_outlet_static_pressure],
                                "Fuel_flow_ratio":[self.Fuel_flow_ratio],
                                "Fan_speed":[self.Fan_speed],
                                "Bypass_ratio":[self.Bypass_ratio],
                                "Bleed_enthalpy":[self.Bleed_enthalpy],
                                "High_pressure_cool_air_flow":[self.High_pressure_cool_air_flow],
                                "Low_pressure_cool_air_flow":[self.Low_pressure_cool_air_flow]
                        }

                        logging.info("Data inputed inputed inform of Dictonary to input features")
                        df=pd.DataFrame(custom_data_input_dict)
                        logging.info("Dataframe is gathered as dataframe")

                        return df

                

                except Exception as e:
                        logging.info("Exception occured in prediction pipeline")
                        raise CustomException(e,sys)



        





        
      