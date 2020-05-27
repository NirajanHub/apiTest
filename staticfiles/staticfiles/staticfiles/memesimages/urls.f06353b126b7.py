from django.urls import path

from api_project.memesimages.views import ImageList

app_name = 'api'
urlpatterns = [
    path('ImageList/', ImageList.as_view()),
    path('ImageList/<int:pk>', ImageList.as_view()),
]