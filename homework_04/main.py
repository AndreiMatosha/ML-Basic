from media import AudioFile, VideoFile, PhotoFile
from storage import LocalStorage, S3Storage

# 1. Create Strategy instances
local_disk_storage = LocalStorage()
cloud_s3_storage = S3Storage(bucket_name="s3-bucket")

print("--- Working with Local Disk ---")
# 2. Create Media Photo file on Local Drive
my_photo = PhotoFile(
    name="zion_photo.jpg",
    size=2048,
    owner="Neo",
    resolution=(1920, 1080),
    extension='JPG',
    storage_strategy=local_disk_storage
)

# 3. Call method and save
my_photo.compress_image(new_resolution=(800, 600))
my_photo.save(file_content=b'1011101')

# 4. Change owner attribute
my_photo.owner = "Trinity"
print(f"The owner of {my_photo.name} is '{my_photo.owner}'.")

print("\n--- Working with S3 bucket ---")
# 5. Create Video file in S3 cloud
my_video = VideoFile(
    name="the_matrix.mp4",
    size=1048576,
    owner="Alice",
    duration=125,
    storage_strategy=cloud_s3_storage,
    codec='H.264')

# 6. Call method and save
my_video.extract_audio()
my_video.save(file_content=b'1010101110')

# 7. Delete Media file
my_video.delete()
