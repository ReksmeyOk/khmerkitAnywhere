from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from embed_video.fields import EmbedVideoField
from ckeditor.fields import RichTextField

class Category(models.Model):
    title = models.CharField(max_length=200, unique= True)
    description = models.CharField(max_length=250, default=True)

    class Meta:
        ordering = ('title', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    #
    # def get_absolute_url(self):
    #     return reverse('post:category-list-page', args=[self.slug])

    def __str__(self):
        return self.title + " | " +'id: ' + str(self.id)
    #
    # def get_absolute_url(self):
    #     return reverse('news-page')


class Post(models.Model):
    title = models.CharField(max_length = 250)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    # content = models.TextField()
    # article1 = models.TextField(default='articleone', blank=True)

    content = RichTextField(blank=True, null=True)
    article1 = RichTextField(blank=True, null=True)
    thumbnailIndex = models.ImageField(default='default.png', blank=True, unique=False)
    photo_credit_thumbnailIndex = models.CharField(max_length=50, default='?')

    video = EmbedVideoField(default='default.mp3', blank=True)
    youtube_link = RichTextField(blank=True, null=True)

    thumbnail1 = models.ImageField( default='default.png', blank=True, unique= False)
    photo_credit_thumbnail1 = models.CharField(max_length=50, default='?')

    article2 = RichTextField(blank=True, null=True)
    thumbnail2 = models.ImageField( default='default.png', blank=True)
    photo_credit_thumbnail2 = models.CharField(max_length=50, default='?')

    article3 = RichTextField(blank=True, null=True)
    thumbnail3 = models.ImageField(default='default.png', blank=True)
    photo_credit_thumbnail3 = models.CharField(max_length=50, default='?')


    author = models.ForeignKey(User, on_delete= models.CASCADE)

    # timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    # Do not use this odering of title, or it wont work the accumulating the number of posts in each category in the widget category
    # class Meta:
    #     ordering = ('-title',)

    # def get_absolute_url(self):
    #     return reverse('post:news-details', args=[self.id,])

    def __str__(self):
        return self.title + ' | ' + 'Author: ' + str(self.author)

    # def get_absolute_url(self):
    #     return reverse('news-page')


# class Comment(models.Model):
#     post = models.ForeignKey(Post, related_name= "comments", on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     body = models.TextField()
#     date_added = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return '%s - %s' % (self.post.title, self.name)
