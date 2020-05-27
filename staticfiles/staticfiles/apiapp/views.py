from rest_framework.views import APIView
from rest_framework.response import Response
from .models import newsFeed
from .serializer import NewsfeedSerializers

class newsList(APIView):

    def get(self,request):
        newsFeed1 = newsFeed.objects.all()
        serealizer = NewsfeedSerializers(newsFeed1, many=True)
        return Response(serealizer.data)

    def post(self):
        pass
