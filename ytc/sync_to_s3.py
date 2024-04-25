import boto3
import os

def upload_directory_to_s3(local_path, bucket_name, s3_folder_path, endpoint_url):
    # Create an S3 client with the specified endpoint URL
    s3 = boto3.client('s3', endpoint_url=endpoint_url)

    # Walk through the local directory
    for root, dirs, files in os.walk(local_path):
        for file in files:
            # Get local file path
            local_file_path = os.path.join(root, file)

            # Get S3 object key
            s3_object_key = os.path.relpath(local_file_path, local_path)

            # Upload file to S3 bucket
            try:
                s3.upload_file(local_file_path, bucket_name, os.path.join(s3_folder_path, s3_object_key))
                print(f"Uploaded {local_file_path} to S3")
            except Exception as e:
                print(f"Error uploading {local_file_path} to S3: {e}")

if __name__ == "__main__":
    # Specify local directory path, S3 bucket name, S3 folder path, and S3 VPC endpoint URL
    local_folder_path = "/path/to/local/folder/"
    bucket_name = "your-bucket-name"
    s3_folder_path = "folder/path/in/s3/"
    s3_endpoint_url = "https://your-s3-vpc-endpoint-url"

    upload_directory_to_s3(local_path, bucket_name, s3_folder_path, endpoint_url)