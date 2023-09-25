import os
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .utils import convert_mp4_to_mp3
from django.http import FileResponse
from .models import UploadedFile
from django.conf import settings


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            notdb_mp4_file = request.FILES['file']  # Получение загруженного MP4 файла
            mp4_file = UploadedFile.objects.create(mp4_file=notdb_mp4_file)
            notdb_mp3_file = convert_mp4_to_mp3(mp4_file)  # Конвертация в MP3
            mp3_file = UploadedFile.objects.create(mp3_file=f'converted.mp3')
            return redirect('download_mp3', mp3_filename=mp3_file.mp3_filename())
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def download_mp3(request, mp3_filename):
    mp3_path = os.path.join('media/final/', mp3_filename)
    mp3_file = open(mp3_path, 'rb')
    response = FileResponse(mp3_file)
    response['Content-Type'] = 'audio/mpeg'
    response['Content-Disposition'] = f'attachment; filename="{mp3_filename}"'

    os.remove(f'media/final/{mp3_filename}')
    files = os.listdir('media/uploads/')
    if files:
        files = [os.path.join('media/uploads', file) for file in files]
    for file in files:
        os.remove(file) # Удаление файлов из папки uploads
    return response
