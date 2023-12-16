import re
from yt_dlp import YoutubeDL


def yt_download(url):  # Функция для скачивания видео с YouTube
    ydl_opts = {
        'outtmpl': 'media/youtube_downloader/%(title)s.%(ext)s'
    }

    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        file_name = ydl.prepare_filename(info_dict)

        try:
            ydl.download([url])
        except Exception as e:
            print(f"Error during download: {e}")
            return None

    last_dot_index = file_name.rfind('.')
    file_name = file_name[:last_dot_index]

    return file_name + '.mp4'


def delete_quotes(file_name):  # Функция приводит название файла в безопасный вид
    last_slash_index = file_name.rfind('/')
    file_name = file_name[last_slash_index + 1:]

    safe_file_name = re.sub(r'[^\w\s_]', '', file_name)  # Удаление всех несуществующих символов

    return safe_file_name[:-3]
