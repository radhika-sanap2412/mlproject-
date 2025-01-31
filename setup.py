#for packaging and distribution
from setuptools import setup, find_packages
from typing import List 
#create a function
HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        #list comprehension for replacing \n by a blank
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

        return requirements




'''
This function will return the list of requirements
'''


setup(

name = 'mlproject',
version= '0.0.1',
author = 'Radhika',
author_email= 'radhikasanap24@gmail.com',
packages= find_packages(),
install_requires = get_requirements("requirements.txt")


)