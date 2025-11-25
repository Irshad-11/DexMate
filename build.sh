#!/usr/bin/env bash
set -e
python -m pip install --upgrade pip
pip install -r requirements.txt
# create artifact
zip -r build.zip src -x "*.pyc" "__pycache__/*"
echo "Built build.zip"
