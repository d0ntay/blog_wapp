from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    date = models.CharField(default='march 13,2002', max_length=255) 
    slug = models.SlugField()
    date_added = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(default='default.png', blank=True) #THIS IS FOR ADDING COVER PHOTO TO BLOG POST

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title
