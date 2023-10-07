from yt_dlp import YoutubeDL


def yt_download(url):
    ydl_ops = {
        'outtmpl': 'media/youtube_downloader/%(title)s.%(ext)s'
    }
    with YoutubeDL(ydl_ops) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        file_name = ydl.prepare_filename(info_dict)
        ydl.download(url)
        print(file_name[:-4] + 'mp4')
        print(file_name)
        print(file_name)
        print(file_name)
        print(file_name)
        print(file_name)
        print('FINISHED FINISHED FINISHED FINISHED FINISHED FINISHED FINISHED FINISHED FINISHED FINISHED')
    return file_name[:-4] + 'mp4'
#
# yt_download("https://www.youtube.com/watch?v=gph_4Decsj8")
