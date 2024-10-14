import os, sys
from pathlib import Path
import logging

# define the list of files and folders

while True:
    project_name = input("Enter your project name :")
    if project_name != "":
        break

# src/__init__.py
# src/components/__init__.py
list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"config/config.yaml",
    "schema.yaml",
    "app.py",
    "main.py",
    "logs.py",
    "exception.py",
    "setup.py"        
]



# create directories and files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # create directory if it doesn't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    # open folder and generate the list_of_files
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass

    else:
        logging.info(f"file is already present at : {filepath}")