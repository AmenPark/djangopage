from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("PS 페이지 연습장")

# Create your views here.
