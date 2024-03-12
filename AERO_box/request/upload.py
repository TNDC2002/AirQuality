# -*- coding: utf-8 -*-
import oss2
from oss2.credentials import EnvironmentVariableCredentialsProvider

# Configure temporary access credentials by using the AccessKey pair of the RAM user obtained from environment variables. 
auth = oss2.ProviderAuth(EnvironmentVariableCredentialsProvider())
bucket = oss2.Bucket(auth, 'https://oss-ap-southeast-1.aliyuncs.com', 'vguairquality')

# with open('../data/data(3).csv', 'rb') as fileobj:
#     fileobj.seek(1000, os.SEEK_SET)
#     current = fileobj.tell()
#     bucket.put_object('test.csv', fileobj)

bucket.put_object_from_file('test.csv', '../data/data(3).csv')