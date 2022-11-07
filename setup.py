from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'SimCLR pretrained'

setup(
    name="Sim CLR",
    version=VERSION,
    author="Link An Jarad",
    description=DESCRIPTION,
    url="https://github.com/LinkAnJarad/SimCLRv2-Pytorch/",
    packages=find_packages(),
    install_requires=['torch']
)
