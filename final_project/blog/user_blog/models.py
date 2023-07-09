from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content_blog = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    images = models.ImageField(upload_to= 'images/', blank=True, null=True)
    
    class Meta:
        ordering = ['-created_date']
            
    def __str__(self):
        return self.title
    
    # @property
    # def truncated_content(self):
    #     return Truncator(self.content_blog).chars(100)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    created= models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    body = models.TextField()
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE, null=True)
    
    
    def __str__(self):
        return self.body
    
    class Meta:
        ordering = ['-created']
    
# class Profile(models.Model):
#     profile = models.ForeignKey(User, on_delete=models.CASCADE