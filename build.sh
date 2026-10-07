#!/bin/bash

echo "Building Jupyter Book..."
python generate_ini_file_list.py
jupyter-book build .
typos
