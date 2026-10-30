
from setuptools import setup, find_packages


def get_requirements(file_path):
    with open(file_path, "r") as f:
        requirements = [line.strip() for line in f if line.strip()]

    return [r for r in requirements if r != "-e ."]


setup(
    name="mlproject",
    version="0.0.1",
    author="Guru",
    author_email="gururajab@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
