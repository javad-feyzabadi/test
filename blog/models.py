from django.db import models
from django.utils import timezone
from accounts.models import User
from django.utils.html import format_html
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation

from accounts.models import User

from comment.models import Comment



class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField()


#My Manager
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='P')

class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)


class Category(models.Model):
    parent = models.ForeignKey("self",related_name='childern',blank=True,null=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100,unique=True)
    status = models.BooleanField(default=True)
    position = models.IntegerField()

    class Meta:
        ordering = ['parent__id','position']

    def __str__(self):
        return self.title

    objects = CategoryManager()


class Article (models.Model):
    STATUS_CHOICES=(
    ("D","Draft"),
    ("P","Published"),
    ("I","Investigation"),
    ("B","Back"),

    )
    author = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,related_name='articles')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100,unique=True)
    descriptions = models.TextField()
    thumbnail = models.ImageField(upload_to='images')
    category = models.ManyToManyField(Category,related_name='articles')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES)
    is_special = models.BooleanField(default=False)
    comments = GenericRelation(Comment)
    hits = models.ManyToManyField(IPAddress,through='ArticleHit' ,blank=True,related_name="hits")

    class Meta:
        ordering = ['-publish']

    def __str__(self):
        return self.title


    def thumbnail_tag(self):
        return format_html("<img width=100 height=70 style='border-radius:10px;' src='{}'>".format(self.thumbnail.url))

    def get_category(self):
        return ", ".join([category.title for category in self.category.active()])

    def get_absolute_url(self):
        return reverse('accounts:homee')

    objects = ArticleManager()


class ArticleHit(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    ip_address = models.ForeignKey(IPAddress,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
