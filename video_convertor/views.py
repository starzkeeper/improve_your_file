import os
from django.shortcuts import render
from .forms import UploadFileForm
from .utils import convert_mp4_to_mp3, delete_files_from_uploads
from django.http import FileResponse, HttpResponse
from .models import UploadedFile
from .tasks import process_uploaded_file


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        file_data = request.FILES.get('file')
        filename = file_data.name
        if form.is_valid():
            upload_dir = 'media/uploads/'
            file_path = os.path.join(upload_dir, filename)

            # Сохраните файл на диск
            with open(file_path, 'wb') as destination:
                for chunk in file_data.chunks():
                    destination.write(chunk)

            # Запуск фоновой обработки
            result = process_uploaded_file.delay(file_path)
            mp3_file, mp3_path = result.get()

            response = FileResponse(mp3_file)
            response['Content-Type'] = 'audio/mpeg'
            response['Content-Disposition'] = f'attachment; filename="{mp3_path}"'

            return response
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
