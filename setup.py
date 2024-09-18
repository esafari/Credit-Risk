from setuptools import setup, find_packages
from typing import List
E_='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file:
        requirements=file.readlines()
        requirements=[library.replace('\n','') for library in requirements]
        if E_ in requirements:
            requirements.remove(E_)
    return requirements
setup(
nqme='Credit Risk',
version='0.0.1',
author='Ehram Safari',
author_email='Ehram.safari@gmail.com',
packages=find_packages(),
#install_requiers=['pandas','numpy','seaborn'],
install_requiers=get_requirements('requirements.txt')
)