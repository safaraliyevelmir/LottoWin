from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=127)
    slug = models.SlugField('Slug',max_length=150)  
    image = models.ImageField('Image', upload_to='blog_image')

    short_description = models.TextField(max_length=127)
    text = RichTextField()
    
    date = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    view = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('blog:blog_inner',args=[self.slug])

    def __str__(self):
        return self.title
    


class BlogTitle(models.Model):

    title = models.CharField(max_length=255)
    desc = models.TextField()


    def __str__(self):
        return self.title