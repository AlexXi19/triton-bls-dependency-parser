import boto3
import random 
import os

s3 = boto3.client('s3')
bucket = os.environ['S3_BUCKET']

isExist = os.path.exists('models/')
if not isExist:

   # Create a new directory because it does not exist
   os.makedirs('models/')


# Replace 'my-bucket' and 'my-directory/' with your S3 bucket name and directory path
operation_parameters = {'Bucket': bucket, 'Prefix': 'models/'}
paginator = s3.get_paginator('list_objects_v2')

python_files = []
for page in paginator.paginate(**operation_parameters):
    if "Contents" in page:
        for obj in page["Contents"]:
            if obj["Key"].endswith(".py"):
                python_files.append(obj["Key"])
    if "CommonPrefixes" in page:
        for subdir in page["CommonPrefixes"]:
            operation_parameters["Prefix"] = subdir["Prefix"]
            for file in s3.list_objects_v2(**operation_parameters)["Contents"]:
                if file["Key"].endswith(".py"):
                    python_files.append(file["Key"])

sampled_model_files = random.sample(python_files, 100)
for i, file in enumerate(sampled_model_files):
    model_name = file.split('/')[1]
    s3.download_file(bucket, file, 'models/'+model_name+'.py')
    if i % 5 == 0:
        print("Downloaded " + str(i) + " files") 




