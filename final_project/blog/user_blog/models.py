from django.db import models
from django.contrib.auth.models import User

# class category(models.Model):
    
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content_blog = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-created_date']
    # category
    
    def __str__(self):
        return self.title
    
# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL,null= True)
#     created_date = models.DateTimeField(auto_now_add=True)
#     body = models.TextField()    
#     blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.body