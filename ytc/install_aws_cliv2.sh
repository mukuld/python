#!/bin/bash

# Directory for downloads
DOWNLOADS_DIR="$HOME/downloads"
command_name="unzip"
PIP="python3-pip"
BOTO="boto3"

# Create downloads directory if it doesn't exist
mkdir -p "$DOWNLOADS_DIR"

# Create an alias for python
alias python=python3

# Download AWS CLI installation package to the downloads directory
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "$DOWNLOADS_DIR/awscliv2.zip"

# Navigate to the downloads directory
cd "$DOWNLOADS_DIR" || exit

if ! which $command_name &>/dev/null; then
    echo "$command_name is not installed. Installing..."
    sudo apt update -y
    sudo apt install -y $command_name PIP
    sudo pip install boto3
fi

# Unzip the AWS CLI installation package
unzip awscliv2.zip

# Run the installation script
sudo ./aws/install