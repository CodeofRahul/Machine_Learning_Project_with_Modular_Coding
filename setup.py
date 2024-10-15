# If we want to release our project as a package or library in future. in this case 
# setup file would be important for us

# In python, setup.py is  a file that contains metadata about a project, including 
# its name, version, author, and dependencies, as well as instructions for building
# ans installing the package.



from setuptools import setup, find_packages
from typing import List


PROJECT_NAME = "Machine Learning Project"
VERSION = "0.0.1"
DESCRIPTION = "This is my machine learning project using modular coding"
AUTHOR_NAME = "Rahul"
AUTHOR_EMAIL = "dummy@successanalytics.ai"


REQUIREMENTS_FILE_NAME = "requirements.txt"

HYPHEN_E_DOT = "-e ."
# Requirements.txt file open
# read
# \n -> ""

def get_requirements_list()->List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]

        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)

        return requirement_list



setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR_NAME,
      author_email=AUTHOR_EMAIL,
      packages=find_packages(),
      install_requires = get_requirements_list()
     )