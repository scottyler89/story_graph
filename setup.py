
from setuptools import setup, find_packages

# Read the requirements from requirements.txt file
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='story_graph',
    version='0.1.0',
    description='Narrative graph classes for story representation',
    author='Scott Tyler',
    author_email='scottyler89@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=requirements
)

