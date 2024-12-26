from django import forms
from .models import Article, Profile

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'summary', 'pdf']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'picture', 'summary', 'resume']