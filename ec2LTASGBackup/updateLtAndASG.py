##############################################
# Function: Update Launch Template and ASG   #
# Developed by: MUkul Dharwadkar             #
# License: MIT                               #
##############################################

import os
import boto3
from botocore.exceptions import ClientError

def create_launch_template_version(ec2_client, launch_template_id, ami_id, instance_type, security_group_ids):
    try:
        response = ec2_client.create_launch_template_version(
            LaunchTemplateId=launch_template_id,
            SourceVersion='$Latest',
            LaunchTemplateData={
                'ImageId': ami_id,
                'InstanceType': instance_type,
                'SecurityGroupIds': security_group_ids.split(',') if security_group_ids else []
            }
        )
        new_version_number = response['LaunchTemplateVersion']['VersionNumber']
        return new_version_number
    except ClientError as e:
        print(f"An error occurred while creating launch template version: {e}")
        raise e

def update_auto_scaling_group(asg_client, asg_name, launch_template_id, new_version_number):
    try:
        asg_client.update_auto_scaling_group(
            AutoScalingGroupName=asg_name,
            LaunchTemplate={
                'LaunchTemplateId': launch_template_id,
                'Version': str(new_version_number)
            }
        )
    except ClientError as e:
        print(f"An error occurred while updating the Auto Scaling Group: {e}")
        raise e

def lambda_handler(event, context):
    launch_template_id = os.environ.get('LAUNCH_TEMPLATE_ID')
    instance_type = os.environ.get('INSTANCE_TYPE')
    security_group_ids = os.environ.get('SECURITY_GROUP_IDS')
    asg_name = os.environ.get('ASG_NAME')

    ami_id = event.get('image_id') 

    if not launch_template_id or not instance_type or not asg_name or not ami_id:
        return {
            'statusCode': 400,
            'body': 'Missing required environment variables or AMI ID'
        }

    ec2_client = boto3.client('ec2')
    asg_client = boto3.client('autoscaling')

    try:
        new_version_number = create_launch_template_version(ec2_client, launch_template_id, ami_id, instance_type, security_group_ids)
        update_auto_scaling_group(asg_client, asg_name, launch_template_id, new_version_number)

        print(f"ASG {asg_name} updated to use Launch Template Version: {new_version_number}")

        return {
            'statusCode': 200,
            'body': f"Launch Template Version {new_version_number} created and ASG updated successfully."
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': f"An error occurred: {e}"
        }
