from django.db import models
from helpers.models import BaseModel 
from django.conf import settings
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    full_name = models.CharField(max_length=250, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    code = models.CharField(max_length=250, null=True, blank=True)
    code_expiration = models.DateTimeField(null=True, blank=True)
    photo = models.ImageField(upload_to='profiles/photos/', null=True, blank=True)
    background = models.ImageField(upload_to='profiles/backgrounds/', null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    subscriptions = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='subscribers',
        blank=True
    )
    wishlist = models.ManyToManyField(
        'Theme',
        related_name='wishers',
        blank=True
    )

    COMMENTATOR_CHOICES = (
        ('anyone', 'Anyone'),
        ('subscribers', 'Subscribers'),
        ('only_me', 'Only me'),
    )
    commentators = models.CharField(
        max_length=20,
        choices=COMMENTATOR_CHOICES,
        default='anyone'
    )

    def __str__(self):
        return self.username or self.full_name or f'User {self.pk}'


class Theme(BaseModel):
    title = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    username = models.CharField(max_length=250, null=True, blank=True)
    photo = models.ImageField(upload_to='themes/photos/', null=True, blank=True)
    background = models.ImageField(upload_to='themes/backgrounds/', null=True, blank=True)
    subscribers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='subscribed_themes', blank=True)

    def __str__(self):
        return self.title or f'Theme {self.pk}'


class Post(BaseModel):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250, null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField(null=True, blank=True)  
    date_posted = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title or f'Post {self.pk}'


class Comment(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    published_date = models.DateTimeField(default=timezone.now)
    text = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ('published_date',)

    def __str__(self):
        return f'Comment {self.pk} by {self.user}'


class ReactionType(BaseModel):
    title = models.CharField(max_length=250, null=True, blank=True)
    identifier = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title or str(self.identifier or self.pk)


class Reaction(BaseModel):
    reaction_type = models.ForeignKey(
        ReactionType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='reactions'
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reactions')
    TYPE_CHOICES = (
        ('like', 'Like'),
        ('dislike', 'Dislike'),
        ('love', 'Love'),
    )
    type = models.CharField(max_length=30, choices=TYPE_CHOICES, null=True, blank=True)

    class Meta:
        unique_together = ('content_type', 'object_id', 'user', 'reaction_type')

    def __str__(self):
        return f'Reaction {self.type} by {self.user}'
