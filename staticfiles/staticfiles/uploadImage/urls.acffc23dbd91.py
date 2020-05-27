from api_project.uploadImages.views import Image
from django.urls import path

app_name = 'api'
url_patterns = [

    path('Image/', Image.as_views()),
    path('Image/<int:pk>', Image.as_views)
]
