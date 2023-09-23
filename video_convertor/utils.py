from moviepy.editor import VideoFileClip


def convert_mp4_to_mp3(mp4_file):
    video = VideoFileClip(f'media/uploads/{mp4_file.mp4_filename()}')
    mp3_file = video.audio.write_audiofile('media/final/converted.mp3')
    return mp3_file

