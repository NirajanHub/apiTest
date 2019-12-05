from django.db import models


# Create your models here.
class memesImages(models.Model):

    images = models.TextField()
    category = models.CharField(max_length=2)


    def _str_(self):
        return self.images
