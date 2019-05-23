# -*- coding: UTF-8 -*-
#  __author__ = 'hxx'

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']


