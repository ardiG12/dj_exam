from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)

    def has_group(self, group_name):
        return self.groups.filter(name=group_name).exists()

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_img/', null=True, blank=True, default='img/default.jpg')

    def __str__(self):
        return f"{self.user.username}"



class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    publish_year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.title
