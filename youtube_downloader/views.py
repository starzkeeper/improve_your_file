import os

from django.http import FileResponse
from django.shortcuts import render
from .forms import UploadUrlForm
from .utils import yt_download


def yt_url(request):
    if request.method == 'POST':
        form = UploadUrlForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get('url')
            file_name = yt_download(url)
            video_path = os.path.join(file_name)
            video_file = open(video_path, 'rb')
            response = FileResponse(video_file)
            response['Content-Type'] = 'video/mp4'
            response['Content-Disposition'] = f'attachment; filename="{file_name}"'

            return response
    else:
        form = UploadUrlForm()
    return render(request, 'yt_download.html', {'form': form})
