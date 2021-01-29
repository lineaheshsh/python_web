from django.urls import path
from main.views import *

## 이미지 업로드 관련
from django.conf.urls.static import static
from django.conf import settings

app_name='main'

urlpatterns=[
    path('', index),
    path('blog/', blog),
    path('blog/<int:pk>', posting, name="posting"),
    path('blog/new_post/', new_post),
    path('blog/<int:pk>/remove/', remove_post),
    path('covid/', covid),
    path('covid/covidAdd/', covidAdd),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)