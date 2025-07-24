#!/bin/bash

echo "Running formatter..."
./format.sh

echo "Building Jupyter Book..."
jupyter-book build .
