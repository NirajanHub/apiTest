from api_project.uploadImages.views import ImageList
from django.urls import path

app_name='api'
url_patterns=[
    path('ImageList/',ImageList.as_views()),
    path('ImageList/<int:pk>',ImageList.as_views)
]
