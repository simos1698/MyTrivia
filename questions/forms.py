from django import forms
from . import models

class QuestionForm(forms.Form):

    CHOICES= (tuple(models.Question.categories))
    category= forms.CharField(widget=forms.Select(choices=CHOICES))
    question = forms.CharField(max_length=255)
    answer = forms.CharField(max_length=255)