from rest_framework import serializers
from .models import Images

class ImagesSerealizer(serializers.ModelSerializer):
    class Meta:
        model=Images
        # fields=('__all__')
        fields = ('category','images')