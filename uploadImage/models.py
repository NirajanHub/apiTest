from django.db import models


class Image(models.Model):
    property_id=models.ForeignKey(
        'properties.Address',
        null=False,
        default=1,
        on_delete=models.CASCADE

    )
    image=models.ImageField(upload_to="pics")