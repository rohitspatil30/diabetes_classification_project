import logging
from pathlib import Path
import os

project_name = 'diabetes_classification_project'

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

list_of_files = [

    '.github/workflows//gitkeep',
    '.gitignore',
    'LICENSE',
    'README.md',
    'main.py',
    'app.py',
    'schema.yaml',
    'param.yaml',
    'requirements.txt',
    'setup.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/entity/config_entity.py',
    f'src/{project_name}/__init__.py',
    'research/experiment.ipynb',
    'config/config.yaml',
    'templates/index.html'
]

for filename in list_of_files:
    filepath = Path(filename)
    filedir, filename = os.path.split(filepath)

    if filedir!='':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating the folder {filedir} for file {filename}")

    # the if statement will check if the file already exists or not , and if not it will create it
    if(not os.path.exists(filepath) or (os.path.getsize(filepath)==0)):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating the file {filename} in the folder {filedir}")

    else:
        logging.info(f"The file {filename} already exists!")
