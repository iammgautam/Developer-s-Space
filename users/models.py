from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True,null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    short_intro = models.CharField(max_length=500)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(null=True, blank= True, upload_to = 'profile/', default='profile/user-default.png')
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_youtube = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add= True)
    id = models.UUIDField(default= uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)

class Skill(models.Model):
    onwer = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add= True)
    id = models.UUIDField(default= uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)
