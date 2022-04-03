from urllib import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
import PyPDF2 
import pytesseract
from PIL import Image

from .modules import getReturnResponse

def index(request):
    return render(request, 'index.html')

def stream_for_text(request):
    try:
        req_body = request.POST
        text = req_body['text']
        resp =  getReturnResponse(text)
        return render(request, 'player.html', context={"data": resp}) 
    except:
        return render(request, 'index.html')

def stream_for_pdf(request):
    try:
        
        file = request.FILES['pdf']
        pdfReader = PyPDF2.PdfFileReader(file) 
        text = ""
        for i in range(pdfReader.numPages):
            text += pdfReader.getPage(i).extractText();
        resp = getReturnResponse(text)
        return render(request, 'player.html', context={"data": resp}) 
    except:
        return render(request, 'index.html')

def stream_for_image(request):
    # try:
    file = request.FILES['image']
    text = pytesseract.image_to_string(Image.open(file), lang='eng')
    resp = getReturnResponse(text)
    return render(request, 'player.html', context={"data": resp}) 
    # except:
    #     return render(request, 'index.html')

        