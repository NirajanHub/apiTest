from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import memesImages
from .serializer import ImagesSerealizer
from django.core.paginator import Paginator


class ImageList(APIView):
    count = 0

    def get(self, request):
        memesImages1 = memesImages.objects.all()
        paginator = Paginator(memesImages1, 20)
        self.count += 1
        serealizer2 = ImagesSerealizer(paginator.page(self.count), many=True)
        return Response(serealizer2.data)

    def post(self, request):
        images = memesImages.objects.all()
        paginator = Paginator(images, 10)
        serealizer = ImagesSerealizer(paginator.page(request.data.get('page')), many=True)
        # if (serealizer.is_valid(raise_exception=True)):
        print(serealizer.data)
        return Response(serealizer.data)
