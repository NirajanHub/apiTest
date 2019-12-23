from rest_framework import serializers
from .models import Images

class ImagesSerealizer(serializers.ModelSerializer):
    category=serializers.CharField()
    images=serializers.ImageField()
    class Meta:
        model=Images
        # fields=('__all__')
        fields = ('category','images')