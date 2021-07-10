from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#response를 되돌려준다.
def hello_world(request):
    return HttpResponse('Hi!!!!!')