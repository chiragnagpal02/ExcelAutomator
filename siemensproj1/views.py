from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response 
# request handler

def say_hello(request):
    return HttpResponse('Hello World')
    
def upload_file(request):
    return render(request, 'upload.html')
