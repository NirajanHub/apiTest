from rest_framework import serializers
from .models import newsFeed

class NewsfeedSerializers(serializers.ModelSerializer):
    class Meta:
        model = newsFeed
        fields = ('firstname', 'lastname', 'image')

        image_url = serializers.SerializerMethodField('get_image_url')
        def get_image_url(self, obj):
            return obj.image.url
