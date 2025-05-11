# blog/forms.py
from django import forms
from .models import Post,Question,Answer,Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content','image','category']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter category name'})
        }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Write your answer...'})
        }

