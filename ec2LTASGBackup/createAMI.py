######################################
# Function: Create AMI               #
# Developed by: MUkul Dharwadkar     #
# License: MIT                       #
######################################

import boto3
import os
from datetime import datetime

def create_ami(instance_id, ami_description, ami_name_prefix):
    ec2 = boto3.client('ec2')
    
    # Generate AMI name dynamically using a static prefix and timestamp
    #ami_name_prefix = "MyAMI-"  # Static prefix
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    timestamp_name_tag = datetime.now().strftime("%Y-%m-%d")
    ami_name = f"{ami_name_prefix}{timestamp}"

    try:
        response = ec2.create_image(
            InstanceId=instance_id,
            Name=ami_name,
            Description=ami_description,
            NoReboot=True,  # To prevent instance reboot during AMI creation
            TagSpecifications=[
                {
                    'ResourceType': 'image',
                    'Tags': [
                        {'Key': 'Name', 'Value': f"{ami_name_prefix}{timestamp_name_tag}"},
                        {'Key': 'Description', 'Value': ami_description}
                    ]
                }
            ]
        )
        return response['ImageId']
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def lambda_handler(event, context):
    # Extract parameters from environment variables
    instance_id = os.environ.get('INSTANCE_ID')
    ami_description = os.environ.get('AMI_DESCRIPTION')
    ami_name_prefix = os.environ.get('AMI_NAME_PREFIX')

    # Create the AMI
    ami_id = create_ami(instance_id, ami_description, ami_name_prefix)

    if ami_id:
        print(f"AMI {ami_id} created successfully")
        return {
        #    'statusCode': 200,
        #    'body': f"AMI {ami_id} created successfully"
            'image_id': f'{ami_id}'
        }
    else:
        print("Failed to create AMI")
        return {
            'statusCode': 500,
            'body': "Failed to create AMI"
        }
