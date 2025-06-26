#!/bin/bash

# Replace these with your Pi's details
PI_USER="pi"
PI_IP="YOUR_PI_IP_ADDRESS"
PI_PATH="/home/pi/typewriter"  # Destination path on Pi
LOCAL_PATH="."  # Current directory, or specify full path to your project

# Create directory on Pi if it doesn't exist
ssh ${PI_USER}@${PI_IP} "mkdir -p ${PI_PATH}"

# Copy files, excluding unnecessary directories/files
rsync -av --progress \
    --exclude '.git' \
    --exclude '.venv' \
    --exclude '__pycache__' \
    --exclude '*.pyc' \
    --exclude '.idea' \
    ${LOCAL_PATH}/ ${PI_USER}@${PI_IP}:${PI_PATH}/