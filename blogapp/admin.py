from django.contrib import admin
from .models import Post, Question, Answer,Category

admin.site.register(Post)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Category)

