import os
from minio import Minio
from app.config import settings

class StorageService:
    def __init__(self):
        self.client = Minio(
            settings.minio_endpoint,
            access_key=settings.minio_access_key,
            secret_key=settings.minio_secret_key,
            secure=False,
        )

    def ensure_bucket(self):
        if not self.client.bucket_exists(settings.minio_bucket):
            self.client.make_bucket(settings.minio_bucket)

    def upload_file(self, local_path: str, object_name: str):
        self.ensure_bucket()
        self.client.fput_object(settings.minio_bucket, object_name, local_path)
        return f"{settings.minio_endpoint}/{settings.minio_bucket}/{object_name}"