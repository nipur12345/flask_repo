import boto3
from io import StringIO
import pandas as pd

class boto_module:
    def __init__(self):
        self.__s3 = boto3.client('s3',)
    def save_df(self,df):
        csv_buf = StringIO()
        df.to_csv(csv_buf, header=True, index=False)
        csv_buf.seek(0)
        value = self.__s3.put_object(Bucket='nipur-input-bucket', Body=csv_buf.getvalue(), Key='test/test.csv')
        return value
    def latest_file_url(self,prefix = None):
        response = self.__s3.list_objects_v2(Bucket='nipur-input-bucket', Prefix=prefix)
        all = response['Contents']
        latest = max(all, key=lambda x: x['LastModified'])
        print(latest,"<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>")
        path_value = latest['Key']
        return path_value

    def latest_file_read(self,path):
        response = self.__s3.get_object(Bucket='nipur-input-bucket', Key=path)
        # books_df = pd.read_csv(response.get("Body"))
        body = response.get()['Body'].read()
        print(body,"<<<< Hello we are geting the read file accordingly!>>")
        return 'value'