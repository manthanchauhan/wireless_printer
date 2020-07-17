from django import forms
from .models import SavedText

class TextShare(forms.ModelForm):
    class Meta:
        model = SavedText
        fields = ['content', ]
        labels = {'content': 'Shared Text', }