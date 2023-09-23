import os.path

from django.db import models


class UploadedFile(models.Model):
    mp4_file = models.FileField(upload_to='uploads/', default=None)
    mp3_file = models.FileField(upload_to='uploads/', default=None)

    def mp4_filename(self):
        return os.path.basename(self.mp4_file.name)

    def mp3_filename(self):
        return os.path.basename(self.mp3_file.name)