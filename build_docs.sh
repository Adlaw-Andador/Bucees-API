#!/bin/bash

# Generate Doxygen documentation
doxygen Doxyfile

# Build Sphinx documentation
make html
