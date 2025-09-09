from abc import ABC, abstractmethod
from datetime import datetime
from storage import StorageStrategy


class MediaFile(ABC):
    """
    Absract base class for all media files. Defines the common interface and common data.
    """

    def __init__(self, name: str, size: int, owner: str, storage_strategy: StorageStrategy):
        self.name = name
        self.size = size
        self.creation_date = datetime.now()
        self.owner = owner
        self._storage = storage_strategy

    def get_info(self):
        """Returns dictionary containing all file information"""
        return {'name': self.name, 'size': self.size, 'creation_date': self.creation_date.strftime('%Y-%m-%d %H:%M'),
                'owner': self.owner, 'storage': self._storage.get_info()}

    @abstractmethod
    def get_metadata(self):
        pass

    def save(self, file_content):
        """Save instructions"""
        self._storage.save(file_name=self.name, content=file_content)

    def delete(self):
        """Delete instructions"""
        self._storage.delete(self.name)
        print(f"Media file '{self.name}' has been removed")


class AudioFile(MediaFile):

    def __init__(self, name: str, size: int, owner: str, duration: int, bit_rate: int,
                 storage_strategy: StorageStrategy):
        super().__init__(name=name, size=size, owner=owner, storage_strategy=storage_strategy)
        self.duration = duration
        self.bit_rate = bit_rate
        print(f"Audio file {self.name} created on {storage_strategy.get_info()}")

    def get_metadata(self):
        """Provide all metadata"""
        print(f"Duration {self.duration}, Bit rate {self.bit_rate}")

    def convert_to_mp3(self):
        """Converts audio file to mp3 format"""
        pass


class VideoFile(MediaFile):

    def __init__(self, name: str, size: int, owner: str, duration: int, codec: str, storage_strategy: StorageStrategy):
        super().__init__(name=name, size=size, owner=owner, storage_strategy=storage_strategy)
        self.duration = duration
        self.codec = codec
        print(f"Video file {self.name} created on {storage_strategy.get_info()}")

    def get_metadata(self):
        """Provide all meta data"""
        print(f"Duration {self.duration}, Codec {self.codec}")

    def extract_audio(self):
        """Extract audio track"""
        pass

    def extract_subtitles(self):
        """Extract subtitles"""
        pass


class PhotoFile(MediaFile):

    def __init__(self, name: str, size: int, owner: str, resolution: (int, int), extension: str,
                 storage_strategy: StorageStrategy):
        super().__init__(name=name, size=size, owner=owner, storage_strategy=storage_strategy)
        self.resolution = resolution
        self.extension = extension
        print(f"Photo file {self.name} created on {storage_strategy.get_info()}")

    def compress_image(self, new_resolution):
        """Compresses the photo by decreasing the resolution"""
        pass

    def get_metadata(self):
        """Provide all meta data"""
        print(f"Resolution {self.resolution}, Extension {self.extension}")
