#!/bin/bash

# Set the virtual environment directory
VENV_DIR="venv"

# Check if the virtual environment exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Virtual environment not found! Please create one first."
    exit 1
fi

# Check if the script is being sourced, not executed
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    echo "Please source this script to activate the virtual environment."
    exit 1
else
    # Activate the virtual environment
    source "$VENV_DIR/bin/activate"
fi