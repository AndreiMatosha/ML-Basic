"""
This module implements Strategy pattern for storing Media files to different locations
"""

from abc import ABC, abstractmethod


class StorageStrategy(ABC):
    """
    Abstract class for storing files strategies
    Defines the interface for all specific strategies
    """

    @abstractmethod
    def save(self, file_name: str, content: bytes):
        pass

    @abstractmethod
    def delete(self, file_name: str):
        pass

    @abstractmethod
    def get_info(self) -> str:
        pass


class LocalStorage(StorageStrategy):
    """Strategy for storing file on local drive"""

    def save(self, file_name: str, content: bytes):
        print(f"File '{file_name}' has been saved on LOCAL DRIVE")

    def delete(self, file_name: str):
        print(f"File '{file_name}' has been removed from LOCAL DRIVE")

    def get_info(self) -> str:
        return "LOCAL DRIVE"


class S3Storage(StorageStrategy):
    """Strategy for storing file to S3-cloud"""

    def __init__(self, bucket_name: str):
        self.bucket = bucket_name

    def save(self, file_name: str, content: bytes):
        print(f"File '{file_name}' has been uploaded to S3 bucket '{self.bucket}'.")

    def delete(self, file_name: str):
        print(f"File '{file_name}' has been removed from S3 bucket '{self.bucket}'.")

    def get_info(self) -> str:
        return f"S3 storage (bucket: {self.bucket})"
