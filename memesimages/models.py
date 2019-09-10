from django.db import models

# Create your models here.
class memesImages(models.Model):
    images = models.ImageField(upload_to='pics')
    category = models.CharField(max_length=2)

    def _str_(self):
        return self.images
