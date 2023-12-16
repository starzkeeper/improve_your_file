import os
from wsgiref.util import FileWrapper
from django.http import FileResponse, HttpResponse
from django.shortcuts import render
from .forms import UploadUrlForm
from .utils import yt_download, delete_quotes
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
                if os.path.exists(file_name):
                    file = FileWrapper(open(f'{file_name}', 'rb'))
                    response = HttpResponse(file, content_type='video/mp4')
                    response['Content-Disposition'] = f'attachment; filename={delete_quotes(file_name)}'

                    os.remove(file_name)

                    return response
                else:
                    return HttpResponse("File not found", status=404)

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
    else:
        form = UploadUrlForm()

    return render(request, 'yt_download.html', {'form': form})