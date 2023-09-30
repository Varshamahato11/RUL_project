from pathlib import Path
import logging
import os

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "predictive_maintenance"

list_of_files = [
    "github/workflow/.gitkeep",
    
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    #f"src/{project_name}/exception.py",
    f"src/{project_name}/utils.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitoring.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/pipeline/prediction_pipeline.py",

    
    "setup.py",
    "varsha.py",
    "Dockerfile",
    "requirements.txt"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)  ## we will get 2 info ie; file path and filedir

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  ## if not we will make dir
        logging.info(f"Creating directory:{filedir} for the file {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")
