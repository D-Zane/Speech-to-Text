from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='Speech-to-Text',
    version='0.1',
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.6.13',
)