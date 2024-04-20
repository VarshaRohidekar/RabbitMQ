#!/bin/bash

# Run your Python script
python healthcheck.py

# Check the exit status of the Python script
if [ $? -ne 0 ]; then
    # If the script exits with a non-zero status, trigger a keyboard interrupt
    echo "Python script exited with a non-zero status. Triggering keyboard interrupt..."
    kill -2 $$
fi
