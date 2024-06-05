######################################
# Function: Retain last five AMIs    #
# Developed by: MUkul Dharwadkar     #
# License: MIT                       #
######################################

import boto3
from datetime import datetime

def get_creation_date_from_name_tag(name_tag):
    # Parse the creation date from the "Name" tag
    try:
        date_str = name_tag.split('_')[-1]  # Extract the date part from the tag
        creation_date = datetime.strptime(date_str, "%Y-%m-%d")  # Parse the date
        return creation_date
    except Exception as e:
        print(f"Error parsing creation date from tag: {str(e)}")
        return None

def retain_latest_images():
    ec2 = boto3.client('ec2')
    
    # Describe all the existing AMIs
    response = ec2.describe_images(Owners=['self'])
    images = response['Images']
    
    # Filter images with a valid creation date in the tag "Name" starting with "Allcareforms"
    valid_images = []
    for image in images:
        # Check if 'Tags' key exists in image metadata
        if 'Tags' in image:
            name_tag = next((tag['Value'] for tag in image['Tags'] if tag['Key'] == 'Name'), None)
            if name_tag and name_tag.startswith("Allcareforms"):
                creation_date = get_creation_date_from_name_tag(name_tag)
                if creation_date:
                    valid_images.append({'ImageId': image['ImageId'], 'CreationDate': creation_date})
        else:
            print(f"Image {image['ImageId']} does not have any tags.")
    
    # Sort the valid images by creation date (in descending order)
    valid_images = sorted(valid_images, key=lambda x: x['CreationDate'], reverse=True)
    
    # Retain only the latest five images
    images_to_retain = valid_images[:5]
    
    # Deregister any older images and delete associated snapshots
    deregistered_images = []
    for image in valid_images[5:]:
        ec2.deregister_image(ImageId=image['ImageId'])
        deregistered_images.append(image)
        
        # Find associated snapshots
        response = ec2.describe_snapshots(Filters=[{'Name': 'description', 'Values': [f"*{image['ImageId']}*"]}])
        snapshots = response['Snapshots']
        
        # Delete associated snapshots
        for snapshot in snapshots:
            ec2.delete_snapshot(SnapshotId=snapshot['SnapshotId'])
    
    if not deregistered_images:
        print("No images were deregistered.")
    else:
        print("Deregistered images:")
        for image in deregistered_images:
            print(f"- {image['ImageId']} ({image['CreationDate']})")
    
    return images_to_retain

def lambda_handler(event, context):
    retained_images = retain_latest_images()
    
    print("Retained images:")
    for image in retained_images:
        print(f"- {image['ImageId']} ({image['CreationDate']})")

    return {
        'statusCode': 200,
        'body': f"Retained {len(retained_images)} latest images"
    }
