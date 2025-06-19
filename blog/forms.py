from django import forms
from .models import Blog, User, Comment
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields = ['title','body']

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields = ('username', 'password1')

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['content']
    
