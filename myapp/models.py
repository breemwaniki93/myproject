
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    image = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
