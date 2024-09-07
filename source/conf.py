# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Bucees API'
copyright = '2024, Jordan Samaniego'
author = 'Jordan Samaniego'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_extra_path = ['docs/doxygen/html']

# Add breathe to your Sphinx extensions
extensions = ['breathe']

# Specify where the Doxygen XML output is located
breathe_projects = {
    "MyProject": "./docs/doxygen/xml"  # Adjust path if necessary
}

breathe_default_project = "MyProject"

# Run doxygen for the readthedocs build
import subprocess, os

read_the_docs_build = os.environ.get('READTHEDOCS', None) == 'True'

if read_the_docs_build:
     subprocess.call('cd ../doxygen; doxygen', shell=True)
