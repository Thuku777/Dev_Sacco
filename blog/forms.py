from django import forms
from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'status', 'restrict_comment',]
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'post-create',
                    'label': 'Title'
                }
            ),
            'body': forms.TextInput(
                attrs={
                    'class': 'post-create',
                    'label': 'Message'
                } 
            ),
            'status': forms.CheckboxSelectMultiple(
                attrs={
                    'class': 'post-create',
                    'label': 'Status'
                }
            ),
            'restrict_comment': forms.CheckboxInput(
                attrs={
                    'class': 'post-create',
                    'label': 'Restrict Comments'
                }
            ),
        }


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'status', 'restrict_comment',]
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'post-create',
                    'label': 'Title'
                }
            ),
            'body': forms.TextInput(
                attrs={
                    'class': 'post-create',
                    'label': 'Message'
                }
            ),
            'status': forms.CheckboxSelectMultiple(
                attrs={
                    'class': 'post-create',
                    'label': 'Status'
                }
            ),
            'restrict_comment': forms.CheckboxInput(
                attrs={
                    'class': 'post-create',
                    'label': 'Restrict Comments'
                }
            ),
        }

class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Text goes here!!!', 'rows':'4', 'cols': '50'}))
    class Meta:
        model = Comment
        fields = ('content',)