"""
Generates environment files separately for python 2 and python 3. (rep_py2, rep_py3)
Simply substitutes fields in the template. Usage:

python environments_generate.py
"""
from __future__ import division, print_function, absolute_import
import os

__author__ = 'Alex Rogozhnikov'

here = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(here, 'environment-rep-template.yaml'), 'r') as template_file:
    content = template_file.read()

for python_version in ["2.7", "3.4"]:
    python_major_version = python_version[:1]
    new_content = content.replace('{PYTHON_MAJOR_VERSION}', python_major_version)\
                         .replace('{PYTHON_VERSION}', python_version)
    new_content = "# This file is AUTOMATICALLY GENERATED BY SCRIPT, don't modify it! \n" + new_content
    with open(os.path.join(here, 'environment-rep' + python_major_version + '.yaml'), 'w') as new_file:
        new_file.write(new_content)