from django.db import models
from django.conf import settings
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=225, unique=True)
    slug = models.SlugField(unique=True, max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Category, self).save(*args, **kwargs)        

    class Meta:
        verbose_name_plural = 'Categories'

class Author(models.Model):
    name = models.CharField(max_length=225, unique=True)
    bio = models.CharField(max_length=225, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title = models.CharField(max_length=225)
    description = models.CharField(max_length=512, blank=True, null=True,)
    content = RichTextUploadingField()
    image = models.ImageField(upload_to='blog/', default='thumbnail.png', blank=True, null=True,)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE,)
    author = models.ForeignKey(Author, blank=True, null=True, on_delete=models.CASCADE,)
    slug = models.SlugField(unique=True, max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    published_at = models.DateTimeField(auto_now=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Blog, self).save(*args, **kwargs)        

    class Meta:
        ordering = ['-published_at']
        verbose_name_plural = 'Blogs'
