from django.db import models

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_content = models.TextField()
    published_date = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.post_title