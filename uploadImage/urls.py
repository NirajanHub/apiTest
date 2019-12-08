from uploadImage.views import Images
from django.urls import path

app_name='api'
url_patterns=[
    path('Images/',Images.as_views()),
    path('Images/<int:pk>',Images.as_views)
]
