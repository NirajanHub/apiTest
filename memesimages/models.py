from django.db import models

# Create your models here.
class memesImages(models.Model):

    images = models.ImageField(upload_to="pics",max_length=255,null=True,blank=True)
    category = models.CharField(max_length=2)

    def _str_(self):
        return self.images

