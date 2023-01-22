from django.db import models
from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100,unique=True)
    status = models.BooleanField(default=True)
    position = models.IntegerField()

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.title


class Article (models.Model):
    STATUS_CHOICES=(
    ("D","Draft"),
    ("P","Published")
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100,unique=True)
    descriptions = models.TextField()
    thumbnail = models.ImageField(upload_to='images')
    category = models.ManyToManyField(Category,related_name='articles')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES)

    class Meta:
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def categoruy_published(self):
        return self.category.filter(status = True)