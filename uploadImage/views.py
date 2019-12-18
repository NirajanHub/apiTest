from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
<<<<<<< HEAD

=======
from .models import Images
from .serializer import ImagesSerealizer
>>>>>>> 958c6f1fae6b20c7b762874e5af83e4d5dc4925a
from uploadImage.helpers import modify_input_for_multiple_files

from .serializer import ImagesSerealizer


class Image(APIView):
<<<<<<< HEAD
    # parser_classes = (MultiPartParser,FormParser)

    def get(self, request):
        all_images = Images.objects.all()
        serializer = ImagesSerealizer(all_images, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        category = request.data['category']
        images = dict((request.data).lists())['images']
        flag = 1
        arr = []
=======
    count = 0

    # parser_classes = (MultiPartParser,FormParser)
    # def get(self,request):
    #     all_images=Image.objects.all()
    #     serializer=ImagesSerealizer(all_images,many=True)
    #     return JsonResponse(serializer.data,safe=False)
    #

    def get(self, request):
        memesImages1 = Images.objects.all()
        paginator =  Paginator(memesImages1, 3)
        self.count += 1
        serealizer2 = ImagesSerealizer(paginator.page(self.count), many=True)
        return Response(serealizer2.data)

    def post(self,request,*args,**kwargs):
        category=request.data['category']
        images=dict((request.data).lists())['images']
        flag=1
        arr=[]
>>>>>>> 958c6f1fae6b20c7b762874e5af83e4d5dc4925a
        for img_name in images:

            modified_data = modify_input_for_multiple_files(category, img_name)
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
