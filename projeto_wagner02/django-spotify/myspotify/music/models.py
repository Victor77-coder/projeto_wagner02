from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='artist_pics/', null=True)

    def __str__(self):
        return f"{self.user.username} - Artist Profile"

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    description = models.TextField()
    duration = models.DurationField()
    file = models.FileField(upload_to='songs/')
    uploaded_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
