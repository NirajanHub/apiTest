from rest_framework import serializers
from .models import Image

class ImagesSerealizer(serializers.ModelSerializer):
    class Meta:
        model=Image
        fields=('__all__')