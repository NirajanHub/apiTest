from django.http import JsonResponse
from django.http.multipartparser import MultiPartParser
from rest_framework import status
from rest_framework.parsers import FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from api_project.uploadImage.helpers import modify_input_for_multiple_files

from .serializer import ImagesSerealizer

class ImageList(APIView):
    parser_classes = (MultiPartParser,FormParser)

    # def get(self,request):
    #     all_images=Image.objects.all()
    #     serializer=ImagesSerealizer(all_images,many=True)
    #     return JsonResponse(serializer.data,safe=False)
    #

    def post(self,request,*args,**kwargs):
        category=request.data['category']
        images=dict((request.data).lists())['images']
        flag=1
        arr=[]
        for img_name in images:
            modified_data = modify_input_for_multiple_files
            repr((category, img_name))
            file_serializer = ImagesSerealizer(data=modified_data)
            if file_serializer.is_valid():
                file_serializer.save()
                arr.append(file_serializer.data)
            else:
                flag = 0
            if flag == 1:
                return Response(arr, status=status.HTTP_201_CREATED)
            else:
                return Response(arr, status=status.HTTP_400_BAD_REQUEST)
