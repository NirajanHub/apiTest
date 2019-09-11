from rest_framework import serializers
from .models import memesImages

class ImagesSerealizer(serializers.ModelSerializer):
    # class Meta:
    #     model=memesImages
    #     fields=('__all__')
    #
    #
    page=serializers.CharFiled(max_length=2)

    def create(self, validated_data):
        return memesImages.object.create(**validated_data)
