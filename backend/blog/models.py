from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=250)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    
    