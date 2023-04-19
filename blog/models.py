from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    author=models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, db_constraint=False, null=True, related_name="articel")
    title= models.CharField(max_length=200, blank=True)
    slug= models.SlugField (max_length=100, unique=True, null=False, blank=True, db_index=True)
    content = models.TextField()
    publish= models.DateTimeField(default=timezone.now )
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=False)
    
    def __str__(self):
        return(self.title)
