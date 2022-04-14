from .boto3_fun import boto_module

s3 = boto_module()
file_val = s3.latest_file_url(prefix='test/')

s3.latest_file_read(path = file_val)




