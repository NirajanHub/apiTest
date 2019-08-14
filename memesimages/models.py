from django.db import models

# Create your models here.
class memesImages(models.Model):

    images=models.ImageField(upload_to='pics')

    def _str_(self):
        return self.images