from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def hello(request):
    return HttpResponse("Hello World")


def job_detail(request):
    return HttpResponse("Job Detail Page")
