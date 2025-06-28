from django import forms
from .models import Song


class SongUploadForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist', 'audio_file']



class SongEditForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'artist': forms.TextInput(attrs={'class': 'form-control'}),
        }
