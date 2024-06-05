import boto3
import os

def share_ami(image_id, account_id):
    ec2 = boto3.client('ec2')
    
    try:
        response = ec2.modify_image_attribute(
            ImageId=image_id,
            LaunchPermission={
                'Add': [{'UserId': account_id}]
            }
        )
        return True
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

def lambda_handler(event, context):
    # Extract image_id from the input event
    # payload = json.loads(event)
    print(f'{event}')
    try:
        image_id = event
    except KeyError:
        print("Image ID is missing in the input.")
        return {
            'statusCode': 400,
            'body': "Image ID is missing in the input."
        }

    # Extract account_id from environment variable
    account_id = os.environ.get('ACCOUNT_ID')
    
    if not account_id:
        print("Account ID is missing in the environment variables.")
        return {
            'statusCode': 400,
            'body': "Account ID is missing in the environment variables."
        }
    
    # Share the AMI
    if share_ami(image_id, account_id):
        print(f"AMI {image_id} shared with account {account_id} successfully")
        return {
            'statusCode': 200,
            'body': f"AMI {image_id} shared with account {account_id} successfully"
        }
    else:
        print("Failed to share AMI")
        return {
            'statusCode': 500,
            'body': "Failed to share AMI"
        }
