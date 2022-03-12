from rest_framework.response import Response
from rest_framework.decorators import api_view
import PyPDF2 
import pytesseract
from PIL import Image

from .modules import getReturnResponse

@api_view(('GET',))
def test(request):
    print(request)
    return Response(data="Request Successfull")

@api_view(('POST',))
def stream_for_text(request):
    try:
        req_body = request.data
        text = req_body['text']
        resp = getReturnResponse(text)
        return Response(data=resp)
    except:
        return Response(data="Text could not be loaded. Invalid Request", status=400)

@api_view(('POST',))
def stream_for_pdf(request):
    try:
        file = request.FILES['pdf']
        pdfReader = PyPDF2.PdfFileReader(file) 
        text = ""
        for i in range(pdfReader.numPages):
            text += pdfReader.getPage(i).extractText();
        resp = getReturnResponse(text)
        return Response(data=resp)
    except:
        return Response(data="Unable to extract text from the pdf!!", status=400)

@api_view(('POST',))
def stream_for_image(request):
    try:
        file = request.FILES['image']
        text = pytesseract.image_to_string(Image.open(file), lang='eng')
        resp = getReturnResponse(text)
        return Response(data=resp)
    except:
        return Response(data="Unable to extract text from the image!!" ,status=400)
