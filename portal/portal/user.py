from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    return HttpResponse("Hello, world. You're at the userlogin.")


def register(request):
    return HttpResponse("Hello, world. You're at the userregister.")    