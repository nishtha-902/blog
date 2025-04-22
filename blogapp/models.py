# blog/models.py
from django.db import models
from django.contrib.auth.models import User,AbstractUser
import datetime
from django.utils.timezone import timezone 

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class datauser(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    qualification = models.CharField(max_length=50, null=False, blank=False, default="12")
    age =  models.IntegerField(null=False, blank=False)
    created = models.DateTimeField(default=datetime.datetime.now())
    profile_image = models.ImageField(upload_to='images/', null=True, blank=True)


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,default='1')
    image = models.ImageField(upload_to='images/',default='default.jpg')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    

    def __str__(self):
        return self.title

class Question(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Answer by {self.author} to '{self.question.title}'"