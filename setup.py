# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup


setup(
    name='PiePrompt',
    description='Python PS1',
    version='1.0.0',
    classifiers=[
        'Programming Language :: Python :: 3.5',
    ],
    entry_points={
        'console_scripts': ['pieprompt=pieprompt.main:main'],
    },
    install_requires=[
    ],
    packages=find_packages(exclude=('tests*', 'testing*')),
)
