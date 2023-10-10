from moviepy.editor import VideoFileClip
import os


def convert_mp4_to_mp3(input_file):
    if isinstance(input_file, str):
        video = VideoFileClip(input_file)
    else:
        video = VideoFileClip(f'media/uploads/{input_file.mp4_filename()}')
    mp3_file = video.audio.write_audiofile(f'media/final/converted.mp3')
    print('ЗАКОНЧЕНО ЗАКОНЧЕНО ЗАКОНЧЕНО ЗАКОНЧЕНО ЗАКОНЧЕНО ЗАКОНЧЕНО ЗАКОНЧЕНО ЗАКОНЧЕНО ЗАКОНЧЕНО ЗАКОНЧЕНО ЗАКОНЧЕНО')
    return mp3_file


def delete_files_from_uploads():  # Удаление файлов из папки uploads
    files = os.listdir('media/uploads/')
    if files:
        files = [os.path.join('media/uploads', file) for file in files]
        for file in files:
            os.remove(file)


