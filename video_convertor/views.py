import os
from django.shortcuts import render
from .forms import UploadFileForm
from .utils import convert_mp4_to_mp3, delete_files_from_uploads
from django.http import FileResponse
from .models import UploadedFile


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        file_data = request.FILES['file']
        filename = file_data.name
        if form.is_valid():
            mp3_file, mp3_path = convert_mp4_to_mp3(file_data)  # Конвертация в MP3

            mp3_file = open(mp3_path, 'rb')
            response = FileResponse(mp3_file)
            response['Content-Type'] = 'audio/mpeg'
            response['Content-Disposition'] = f'attachment; filename="{mp3_path}"'

            os.remove(mp3_path)
            delete_files_from_uploads()
            return response
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
