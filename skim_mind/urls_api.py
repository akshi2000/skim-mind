from django.urls import path
from django.conf.urls import include
from skim_mind import views, views_api


urlpatterns = [
    path('test', views_api.test, name='test_api'),
    path('text', views_api.stream_for_text, name='text_api'),
    path('pdf', views_api.stream_for_pdf, name='pdf_api'),
    path('image', views_api.stream_for_image, name='image_api'),
    # path('api-auth/', include('rest_framework.urls'))
]