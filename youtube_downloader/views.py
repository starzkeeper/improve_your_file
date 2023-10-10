import os

from django.http import FileResponse
from django.shortcuts import render
from .forms import UploadUrlForm
from .utils import yt_download
from video_convertor.utils import convert_mp4_to_mp3
from video_convertor.models import UploadedFile


def yt_url(request):
    if request.method == 'POST':
        form = UploadUrlForm(request.POST)
        button_action = request.POST.get('button_action')
        if form.is_valid():
            url = form.cleaned_data.get('url')
            file_name = yt_download(url)
            if button_action == 'action1':
                video_file = open(file_name, 'rb')
                response = FileResponse(video_file)
                response['Content-Type'] = 'video/mp4'
                response['Content-Disposition'] = f'attachment; filename="{file_name}"'
                return response

            elif button_action == 'action2':
                convert_mp4_to_mp3(file_name)
                mp3_file = UploadedFile.objects.create(mp3_file='converted.mp3')
                mp3_filename = mp3_file.mp3_filename()

                mp3_path = os.path.join('media/final/', mp3_filename)
                mp3_file = open(mp3_path, 'rb')
                response = FileResponse(mp3_file)
                response['Content-Type'] = 'audio/mpeg'
                response['Content-Disposition'] = f'attachment; filename="{mp3_filename}"'

                os.remove(f'media/final/{mp3_filename}')

                return response
            os.remove(file_name)
    else:
        form = UploadUrlForm()

    return render(request, 'yt_download.html', {'form': form})
