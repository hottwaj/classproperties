from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name='classproperties',

    version='0.1',
    
    python_requires='>3.0',

    description='Decorators for classproperty and cached_classproperty',
    long_description=long_description,

    url='https://github.com/hottwaj/classproperties',

    author='Jonathan Clarke',
    author_email='jonathan.a.clarke@gmail.com',

    license='MIT, Copyright 2021',

    classifiers=[
    ],

    keywords='',

    packages=["classproperties"],
    
    install_requires=[],
)
