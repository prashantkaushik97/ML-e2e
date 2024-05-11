#Will help in building this ml appliication as a package and also to install it.
#This is a setup file for the package

#Importing the required libraries

from setuptools import setup, find_packages
from typing import List

def get_requirements(filepath) -> List[str]:
    with open("requirements.txt", "r") as file:
        requirements = file.readlines()
        [req.replace("\n", "") for req in requirements]
        #
        if "-e ." in requirements:
            requirements.remove("-e .")
    
setup(name="mlops",version="0.0.1", author="Prashant", description="MLOps package with DVC",packages=find_packages(), install_requires=get_requirements("requirements.txt"))
