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
        paginator = Paginator(memesImages1, 10)
        self.count+=1
        serealizer2 = ImagesSerealizer(paginator.page(self.count), many=True)
        return Response(serealizer2.data)


def post(self):
    pass
