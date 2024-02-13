from moviepy.editor import VideoFileClip
import os


def convert_mp4_to_mp3(input_file):
    video = VideoFileClip(input_file)
    mp3_path = 'media/final/converted.mp3'
    video.audio.write_audiofile(mp3_path)
    print('ЗАКОНЧЕНО ЗАКОНЧЕНО ЗАКОНЧЕНО ЗАКОНЧЕНО ЗАКОНЧЕНО ЗАКОНЧЕНО ЗАКОНЧЕНО ЗАКОНЧЕНО ЗАКОНЧЕНО ЗАКОНЧЕНО ЗАКОНЧЕНО')
    return video, mp3_path


def delete_files_from_uploads():  # Удаление файлов из папки uploads
    files = os.listdir('media/uploads/')
    if files:
        files = [os.path.join('media/uploads', file) for file in files]
        for file in files:
            os.remove(file)




