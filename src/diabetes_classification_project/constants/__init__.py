from pathlib import Path

# if I want to print this in ipynb file, I have to write from constants import CONFIG_FILE_PATH and then print(CONFIG_FILE_PATH)
CONFIG_FILE_PATH = Path("config/config.yaml")
# I have written from src.diabetes_classification_project.constants import * , now I can print CONFIG_FILE_PATH by doing print(constants.CONFIG_FILE_PATH)
PARAM_FILE_PATH = Path("param.yaml")
SCHEMA_FILE_PATH = Path("schema.yaml")
