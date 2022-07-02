from dataclasses import field
from django import forms
from .models import Blog

class BlogForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)

class BolgModelFro(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'