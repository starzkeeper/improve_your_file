import os
from django.shortcuts import render
from .forms import UploadFileForm
from .utils import convert_mp4_to_mp3, delete_files_from_uploads
from django.http import FileResponse
from .models import UploadedFile
from .tasks import upload_file_task


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        file_data = request.FILES['file'].read()
        if form.is_valid():
            upload_file_task.delay(file_data)
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
