from setuptools import find_packages,setup
from typing import List

# Function to return the list of requirements 
HYPEN_E = '-e .'
def get_requiremts(filePath:str)->List[str]:
    requirements=[]
    with open(filePath) as fileObj:
        requirements=fileObj.readlines()
        requirements=[req .replace("\n","") for req in requirements]

        if HYPEN_E in requirements:
            requirements.remove(HYPEN_E)
    
    return requirements


setup(
    name='Profit Predicion',
    version='0.0.1',
    author='Maneth',
    author_email='manethbcodes11@gmail.com',
    packages=find_packages(),
    intall_requires=get_requiremts('requirements.txt')
)