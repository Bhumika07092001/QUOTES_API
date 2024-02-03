from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Quotes(models.Model):
    quote_text = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.author
    
# class Users(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     email = models.TextField(blank=True)