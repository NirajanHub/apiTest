from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Images
from .serializer import ImagesSerealizer
from uploadImage.helpers import modify_input_for_multiple_files

from .serializer import ImagesSerealizer


class Image(APIView):
    count = 0
    totalPages = 0

    # parser_classes = (MultiPartParser,FormParser)
    # def get(self,request):
    #     all_images=Image.objects.all()
    #     serializer=ImagesSerealizer(all_images,many=True)
    #     return JsonResponse(serializer.data,safe=False)
    #

    def get(self, request):
        memesImages1 = Images.objects.all()
        paginator = Paginator(memesImages1, 3)
        self.count += 1
        serealizer2 = ImagesSerealizer(paginator.page(self.count), many=True)
        return Response(serealizer2.data)

    def post(self, request, *args, **kwargs):
        page = request.data['page']
        flags = request.data['flag']
        if flags == "true":
            category = request.data['category']
            images = dict(request.data.lists())['images']
            flag = 1
            arr = []
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
                return Response("success", status=status.HTTP_201_CREATED)
            else:
                return Response("something went wrong", status=status.HTTP_400_BAD_REQUEST)
        else:
            memesImages1 = Images.objects.get_queryset().order_by('id')
            paginator = Paginator(memesImages1, 5)
            numberOfItems = paginator.count
            numberOfPages = paginator.num_pages + 1
            if (numberOfPages - page < 1):
                return Response("There are more updates coming soon")
            serealizer2 = ImagesSerealizer(paginator.page(numberOfPages - page), many=True)
            return Response(serealizer2.data)
