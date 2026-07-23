#!/bin/bash

source venv/bin/activate

pytest test_update_visualizer.py


EXIT_CODE=$?


echo $EXIT_CODE

if [ $EXIT_CODE -eq 0 ]
then
  exit 0
else
  exit 1
fi