from celery import shared_task
import os
from .utils import convert_mp4_to_mp3,delete_files_from_uploads
from django.http import FileResponse
from .models import UploadedFile

@shared_task()
def upload_file_task(file_data):
    notdb_mp4_file = file_data  # Получение загруженного MP4 файла
    mp4_file = UploadedFile.objects.create(mp4_file=notdb_mp4_file)
    convert_mp4_to_mp3(mp4_file)  # Конвертация в MP3
    mp3_file = UploadedFile.objects.create(mp3_file='converted.mp3')
    mp3_filename = mp3_file.mp3_filename()

    mp3_path = os.path.join('media/final/', mp3_filename)
    mp3_file = open(mp3_path, 'rb')
    response = FileResponse(mp3_file)
    response['Content-Type'] = 'audio/mpeg'
    response['Content-Disposition'] = f'attachment; filename="{mp3_filename}"'

    os.remove(f'media/final/{mp3_filename}')
    delete_files_from_uploads()
    return response
