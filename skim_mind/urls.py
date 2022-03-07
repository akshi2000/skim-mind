from django.urls import path
from django.conf.urls import include
from skim_mind import views


urlpatterns = [
    path('', views.test, name='test'),
    path('text', views.stream_for_text, name='text'),
    path('pdf', views.stream_for_pdf, name='pdf'),
    path('image', views.stream_for_image, name='image'),
    path('api-auth/', include('rest_framework.urls'))
]