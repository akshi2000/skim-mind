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

mostUsedWords = []

def loadWords():
    if(len(mostUsedWords) > 0):
        return
    try:
        print(os.getcwd())
        with open('mostUsedWords.txt', 'r') as text_file:
            data = list(text_file.read().replace('\n', ' ').split())
            for word in data:
                mostUsedWords.append(word)
    except:
        print("Couldn't Load Words")

@api_view(('GET',))
def test(request):
    print(request)
    return Response(data="Request Successfull")

@api_view(('POST',))
def stream_for_text(request):
    loadWords()
    req_body = request.data
    text = req_body['text']
    data = list(text.replace('\n', ' ').split())
    resp = []
    for word in data:
        if word in mostUsedWords:    
            resp.append({'word': word, 'factor' : 0.4}) 
        else:
            extra = 0
            if(word[-1] == '.'):
                extra = 0.2
            if(word[-1] == ','):
                    extra = 0.1
            resp.append({'word': word, 'factor' : 0.5 + extra}) 
    return Response(resp)

@api_view(('POST',))
def stream_for_pdf(request):
    loadWords()
    file = request.FILES['pdf']
    file_name = default_storage.save(file.name, ContentFile(file.read()))
    file_url = default_storage.url(file_name)
    try:
        convertapi.convert('txt', {'File': os.getcwd() + file_url}, from_format = 'pdf').save_files('temp.txt')
        with open('temp.txt', 'r') as text_file:
            data = list(text_file.read().replace('\n', ' ').split())
        default_storage.delete(file_name)
        resp = []
        for word in data:
            if word in mostUsedWords:    
                resp.append({'word': word, 'factor' : 0.4}) 
            else:
                extra = 0
                if(word[-1] == '.'):
                    extra = 0.2
                if(word[-1] == ','):
                    extra = 0.1
                resp.append({'word': word, 'factor' : 0.5 + extra})
        return Response(resp)
    except:
        default_storage.delete(file_name)
        return Response(data="File wasn't uploaded correctly!", status=500)
    

@api_view(('POST',))
def stream_for_image(request):
    loadWords()
    file = request.FILES['image']
    file_name = default_storage.save(file.name, ContentFile(file.read()))
    file_url = default_storage.url(file_name)
    try:
        img = Image.open(os.getcwd() + file_url) # the second one 
        img = img.filter(ImageFilter.MedianFilter())
        # enhancer = ImageEnhance.Contrast(img)
        # img = enhancer.enhance(2)
        # img = img.convert('1')
        img.save('temp2.jpg')
        data = pytesseract.image_to_string(Image.open('temp2.jpg'), lang='eng').split()
        resp = []
        for word in data:
            if word in mostUsedWords:    
                resp.append({'word': word, 'factor' : 0.4}) 
            else:
                extra = 0
                if(word[-1] == '.'):
                    extra = 0.2
                if(word[-1] == ','):
                    extra = 0.1
                resp.append({'word': word, 'factor' : 0.5 + extra})
        default_storage.delete(file_name)
        return Response(resp)
    except:
        default_storage.delete(file_name)
        return Response(data="File wasn't uploaded correctly!" ,status=500)

