from django.db import models


class Images(models.Model):
    # property_id = models.ForeignKey(
    #     'properties.Address',
    #     null=False,
    #     default=1,
    #     on_delete=models.CASCADE
    #  )
    images = models.ImageField(upload_to="pics")
    category = models.CharField(max_length=2)
    page=models.TextField()
    flag=models.BooleanField()

    def _str_(self):
        return self.images

