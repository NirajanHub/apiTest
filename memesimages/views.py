from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import memesImages
from .serializer import ImagesSerealizer


class ImageList(APIView):

    def get(self, request):
        memesImages1 = memesImages.objects.all()
        serealizer2 = ImagesSerealizer(memesImages1, many=True)
        return Response(serealizer2.data)

    def post(self, request):
        postRequest = request.data.get()
        serealizer = ImagesSerealizer(data=postRequest)
        if serealizer.is_valid(raise_exception=True):
            article_saved = serealizer.save()
        return Response(serealizer.data)
