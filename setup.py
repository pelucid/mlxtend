from setuptools import setup, find_packages
import sys

requirements = [
          'matplotlib>=3.0.0',
          'joblib>=1.0.0',
          'scikit-learn==1.1.2',
          'numpy<=1.23.5', # require a version which is compatible with py3.9 and is > 1.20 due to API changes  
          'pandas~=1.5',
          'scipy~=1.10.0',
]

setup(name='mlxtend',
      version='0.1.0',
      description='Machine Learning Library Extensions',
      url='https://github.com/pelucid/mlxtend',
      packages=find_packages(),
      install_requires=requirements,
      setup_requires=["pytest-runner"],
      tests_require=['pytest~=6.2', 'pytest-cov', 'tomli==1.2.2', 'coverage==6.2']
      )
