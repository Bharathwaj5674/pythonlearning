import boto3
import datetime

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = 'bpythontest'
    prefix = 'sample_dups/' + datetime.datetime.now().strftime('%Y-%m-%d') + '/'
    print("Checking prefix:", prefix)

    result = s3.list_objects_v2(Bucket=bucket, Prefix=prefix)

    if 'Contents' in result:
        return {"proceed": True, "prefix": prefix}
    else:
        return {"proceed": False, "message": "No file found for today's date"}
