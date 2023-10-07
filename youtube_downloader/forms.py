from django import forms


class UploadUrlForm(forms.Form):
    url = forms.URLField()