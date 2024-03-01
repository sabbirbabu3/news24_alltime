from django import forms
from .models import Article,ArticleRating

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"

class RatingForm(forms.ModelForm):
    class Meta:
        model = ArticleRating
        fields = ['rating']