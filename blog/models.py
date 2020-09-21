from datetime import datetime

from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now, blank=True)
    text = models.TextField()
    image = models.ImageField(upload_to='post_images/')

    def get_summary(self):
        return self.text[:70]
