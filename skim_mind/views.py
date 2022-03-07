from urllib import request, response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from .config import *
import convertapi
import os
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
tesseract_cmd = '/usr/bin/tesseract'

convertapi.api_secret = API_SECRET


from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


@api_view(('GET',))
def test(request):
    print(request)
    return Response(data="Request Successfull")

@api_view(('POST',))
def stream_for_text(request):
    req_body = request.data
    text = req_body['text']
    data = list(text.replace('\n', ' ').split())
    resp = []
    for word in data:
        resp.append({'word': word, 'factor' : 1}) 
    return Response(resp)

@api_view(('POST',))
def stream_for_pdf(request):
    file = request.FILES['pdf']
    file_name = default_storage.save(file.name, ContentFile(file.read()))
    file_url = default_storage.url(file_name)
    try:
        convertapi.convert('txt', {'File': os.getcwd() + file_url}, from_format = 'pdf').save_files('temp.txt')
        with open('temp.txt', 'r') as text_file:
            data = list(text_file.read().replace('\n', ' ').split())
        print(data)
        default_storage.delete(file_name)
        resp = []
        for word in data:
            resp.append({'word': word, 'factor' : 1}) 
        return Response(resp)
    except:
        default_storage.delete(file_name)
        return Response(status=500)
    

@api_view(('POST',))
def stream_for_image(request):
    file = request.FILES['image']
    file_name = default_storage.save(file.name, ContentFile(file.read()))
    file_url = default_storage.url(file_name)
    try:
        print(file_name)
        img = Image.open(os.getcwd() + file_url) # the second one 
        img = img.filter(ImageFilter.MedianFilter())
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(2)
        img = img.convert('1')
        img.save('temp2.jpg')
        data = pytesseract.image_to_string(Image.open('temp2.jpg'), lang='eng').split()
        resp = []
        for word in data:
            resp.append({'word': word, 'factor' : 1}) 
        default_storage.delete(file_name)
        return Response(resp)
    except:
        default_storage.delete(file_name)
        return Response(status=500)

