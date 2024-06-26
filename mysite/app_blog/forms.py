# -*- coding: utf-8 -*-
from django import forms
from .models import ArticleImage

class ArticleImageForm(forms.ModelForm):
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = ArticleImage
        fields = '__all__'

class MultipleFileUploadForm(forms.Form):
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

