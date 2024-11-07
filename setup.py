from setuptools import setup, find_packages

setup(
    name='monotone_color_filters',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'Pillow'
    ],
    description='A Python library to apply random monotone color transformations to images.',
    author='Alexander Lobashev',
    author_email='lobashevalexander@gmail.com',
    url='https://github.com/alobashev/monotone_color_filters', 
)
