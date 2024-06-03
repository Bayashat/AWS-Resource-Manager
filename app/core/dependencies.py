import boto3

# s3 client

def get_s3_client():
    return boto3.client("s3")
