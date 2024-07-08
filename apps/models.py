from django.db import models

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=200)
    text= models.TextField(max_length=100, )
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='image')
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name