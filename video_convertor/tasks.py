from celery import shared_task
import os
from .utils import convert_mp4_to_mp3, delete_files_from_uploads
from django.http import FileResponse


@shared_task
def process_uploaded_file(file_data):
    dir = "/Users/starzkeeper/PycharmProjects/improve_your_file/improve_your_file/"
    full_path = file_data
    print(full_path)
    mp3_file, mp3_path = convert_mp4_to_mp3(full_path) # Конвертация в MP3

    mp3_file = open(mp3_path, 'rb')
    print(mp3_file, mp3_file.name, mp3_path)
    response = FileResponse(mp3_file)
    response['Content-Type'] = 'audio/mpeg'
    response['Content-Disposition'] = f'attachment; filename="{mp3_path}"'

    # os.remove(mp3_path)
    # delete_files_from_uploads()

    return mp3_file,mp3_path
