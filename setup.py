# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md','r', encoding='utf-8') as f:
    readme = f.read()

with open('LICENSE', 'r', encoding='utf-8') as f:
    license = f.read()

setup(
    name='gemini',
    version='1.0.6',
    description='Backtesting for sleepless cryptocurrency markets',
    long_description=readme,
    url='https://github.com/liamhartley/Gemini',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
