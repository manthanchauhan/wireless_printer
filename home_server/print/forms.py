from django import forms


class PrintForm(forms.Form):
    file2print = forms.FileField(label='Upload file to print',
                                 widget=forms.FileInput(attrs={}))
