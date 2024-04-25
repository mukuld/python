import boto3
import os

def sync_modified_files_to_s3(local_folder_path, bucket_name, s3_folder_path, s3_endpoint_url):
    # Initialize S3 client with custom endpoint URL
    s3 = boto3.client('s3', endpoint_url=s3_endpoint_url)

    # List files in the local folder
    local_files = os.listdir(local_folder_path)

    # Loop through each file in the local folder
    for file_name in local_files:
        local_file_path = os.path.join(local_folder_path, file_name)

        # Get the last modified time of the file
        last_modified_time = os.path.getmtime(local_file_path)

        # Get the object if it exists in S3
        try:
            s3_object = s3.head_object(Bucket=bucket_name, Key=s3_folder_path + file_name)
            s3_last_modified_time = s3_object['LastModified'].timestamp()

            # Compare last modified times
            if last_modified_time > s3_last_modified_time:
                print(f"Syncing {file_name} to S3")
                s3.upload_file(local_file_path, bucket_name, s3_folder_path + file_name)
        except:
            # If the object doesn't exist in S3, upload it
            print(f"Syncing {file_name} to S3")
            s3.upload_file(local_file_path, bucket_name, s3_folder_path + file_name)

if __name__ == "__main__":
    # Specify local folder path, S3 bucket name, S3 folder path, and S3 VPC endpoint URL
    local_folder_path = "/path/to/local/folder/"
    bucket_name = "your-bucket-name"
    s3_folder_path = "folder/path/in/s3/"
    s3_endpoint_url = "https://your-s3-vpc-endpoint-url"

    sync_modified_files_to_s3(local_folder_path, bucket_name, s3_folder_path, s3_endpoint_url)
