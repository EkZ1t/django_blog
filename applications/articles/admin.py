from django.contrib import admin
from .models import Article, Tag, Comment 

# Register your models here.
admin.site.register([Article, Tag, Comment])
