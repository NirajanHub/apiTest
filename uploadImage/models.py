from django.db import models


class Images(models.Model):
    # property_id = models.ForeignKey(
    #     'properties.Address',
    #     null=False,
    #     default=1,
    #     on_delete=models.CASCADE
    #  )

    category = models.CharField(max_length=2)
    page = models.CharField(max_length=2)
    flag = models.TextField(max_length=5)
    images = models.ImageField(upload_to="pics")
    def _str_(self):
        return self.images

