from setuptools import find_packages,setup
from typing import List

trigger = '-e .'
def requirements(file_path:str)->List[str]:
    '''
    This method to get the requirements from the requirements file
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if trigger in requirements:
            requirements.remove(trigger)
    return requirements

setup(
    name = 'EndToEnd_ML',
    author= 'Sajib_Hossain',
    version = '0.0.1',
    author_email='sajib.hossain.limon@gmail.com',
    maintainer='Sajib_Hossain',
    packages = find_packages(),
    install_requires = requirements('requirements.txt')  
)
