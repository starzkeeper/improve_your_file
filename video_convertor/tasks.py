from celery import shared_task
from .utils import convert_mp4_to_mp3, delete_files_from_uploads
from .models import UploadedFile
import os


@shared_task
def process_uploaded_file(file_data):
    notdb_mp4_file = file_data  # Получение загруженного MP4 файла
    mp4_file = UploadedFile.objects.create(mp4_file=notdb_mp4_file)
    convert_mp4_to_mp3(mp4_file)  # Конвертация в MP3
    mp3_file = UploadedFile.objects.create(mp3_file='converted.mp3')
    mp3_filename = mp3_file.mp3_filename()

    mp3_path = os.path.join('media/final/', mp3_filename)
    mp3_file = open(mp3_path, 'rb')
    mp3_content = mp3_file.read()
    os.remove(f'media/final/{mp3_filename}')
    delete_files_from_uploads()

    return mp3_content, mp3_filename
