from rest_framework import serializers
from .models import memesImages

class ImagesSerealizer(serializers.ModelSerializer):
    class Meta:
        model=memesImages
        fields=('__all__')

