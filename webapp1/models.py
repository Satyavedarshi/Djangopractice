from django.db import models
from Djangopractice.util import unique_slug_generator

# Create your models here.
class testmodel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title + ' --> ' + self.description + ' '


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, null=True, blank=True)
    text = models.TextField(max_length=500)
    published_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=(('draft','DRAFT'),('published','PUBLISHED')), default='draft')

    class Meta:
        ordering = ('-published_at', )

    def __str__(self):
        return self.title

def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)