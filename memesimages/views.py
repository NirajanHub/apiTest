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
        serealizer2 = ImagesSerealizer(memesImages1, many=True)
        return Response(serealizer2.data)

    def post(self, request):
        postRequest = request.data.get('page')
        serealizer = ImagesSerealizer(data=postRequest)
        if (serealizer.is_valid(raise_exception=True)):
            # paginator=Paginator(serealizer.data)
            # page=request.GET.get('page')
            # imageJson=paginator.get_page(page)
            # if serealizer.is_valid(raise_exception=True):
            article_saved = serealizer.save()


        return Response({"success": "Article '{}' created sucessfully".format(article_saved.title)})
