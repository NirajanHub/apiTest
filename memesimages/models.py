from django.db import models


# Create your models here.
class memesImages(models.Model):
    images = models.TextField()
    category = models.CharField(max_length=2)
   # page = models.IntegerField()

    def _str_(self):
        return self.images
