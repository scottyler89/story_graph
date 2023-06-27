
from setuptools import setup, find_packages

setup(
    name='story_graph',
    version='0.1.0',
    description='Narrative graph classes for story representation',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)

