from minio import Minio
from minio.error import ResponseError
import os

minioClient = Minio('play.minio.io:9000',
                    access_key='Q3AM3UQ867SPQQA43P2F',
                    secret_key='zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG',
                    secure=True)


def createBucket(bucketName):
    minioClient.make_bucket(bucketName, location="us-east-1")
    
def addObjectTobucket(filePath, bucketName):
    try:
        file_stat = os.stat(filePath)
        file_data = open(filePath, 'rb')
        etag=minioClient.put_object(bucketName, filePath, file_data, file_stat.st_size, content_type='video/mp4')
    except ResponseError as err:
        etag = err
    return etag


def getObjectList(filePath, bucketName):
    data = minioClient.presigned_get_object(bucketName, filePath)
    
        
    return data