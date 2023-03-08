from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='blog')
    description = models.TextField()


    author = models.CharField(max_length=20)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}:: {self.author}'
