from setuptools import setup, find_packages

setup(
    name="latexgen",
    version="0.3",
    packages=find_packages(),
    install_requires=[
        'joblib == 1.3.2',
        'pip == 24.0',
        'setuptools == 69.2.0',
        'wheel == 0.42.0'
    ],
    # Дополнительная информация
    author="Arsenii Pimenov",
    author_email="aepimenov@edu.hse.ru",
    description="Package for Advances Python course homework 2. This package has two functions, \
                that generate latex code. generate_table creates a latex table from 2D array. \
                generate_png create a picture in latex syntacsis.",
    url="https://github.com/parseny/Advanced-Python/tree/main/hw2",
)
