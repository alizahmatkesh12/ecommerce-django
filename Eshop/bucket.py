from django.conf import settings  
import boto3
import os




class Bucket:
    def __init__(self):
        session = boto3.Session(
            aws_access_key_id=os.getenv('LIARA_ACCESS_KEY'),
            aws_secret_access_key=os.getenv('LIARA_SECRET_KEY'),
            region_name=os.getenv('AWS_S3_REGION_NAME')
        )
        self.conn = session.client(
            's3',
            endpoint_url=os.getenv('LIARA_ENDPOINT')
        )
    def get_objects(self):
        result = self.conn.list_objects_v2(Bucket=settings.AWS_STORAGE_BUCKET_NAME)
        if result['KeyCount']:
            return result['Contents']
        else:
            return None
        
    def delete_object(self, key):
        self.conn.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=key)
        return True
    
    def download_object(self, key):
        file_path = settings.AWS_LOCAL_STORAGE + key

        try:

            os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Create the directory if it doesn't exist

            with open(file_path, 'wb') as f:
                self.conn.download_fileobj(settings.AWS_STORAGE_BUCKET_NAME, key, f)

        except FileNotFoundError:

            print(f"Error: File {file_path} does not exist")

bucket = Bucket()


# bucket.py

# from django.conf import settings  
# import boto3
# import os

# class Bucket:
#     # def __init__(self):
#     #     session = boto3.Session(
#     #         aws_access_key_id=os.getenv('LIARA_ACCESS_KEY'),
#     #         aws_secret_access_key=os.getenv('LIARA_SECRET_KEY'),
#     #         region_name=os.getenv('AWS_S3_REGION_NAME')
#     #     )
#     #     self.conn = session.client(
#     #         's3',
#     #         endpoint_url=os.getenv('LIARA_ENDPOINT')
#     #     )
        
        
#     def __init__(self):
#         session = boto3.session.Session()
#         self.conn = session.client(
#             service_name=settings.AWS_SERVICE_NAME,
#             aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
#             aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
#             endpoint_url=settings.AWS_S3_ENDPOINT_URL,
#         )

#     def get_objects(self):
#         try:
#             result = self.conn.list_objects_v2(Bucket=settings.AWS_STORAGE_BUCKET_NAME)
#             if result['KeyCount']:
#                 return result['Contents']
#             else:
#                 return None
#         except Exception as e:
#             print(f"Error getting objects: {e}")
#             return None

#     def delete_object(self, key):
#         try:
#             self.conn.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=key)
#             return True
#         except Exception as e:
#             print(f"Error deleting object: {e}")
#             return False
    
#     def download_object(self, key):
#         try:
#             with open(os.path.join(settings.AWS_LOCAL_STORAGE, key), 'wb') as f:
#                 self.conn.download_fileobj(settings.AWS_STORAGE_BUCKET_NAME, key, f)
#             return True
#         except Exception as e:
#             print(f"Error downloading object: {e}")
#             return False

# bucket = Bucket()
