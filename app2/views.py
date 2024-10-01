from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def profile(request):
    return HttpResponse('Профиль')


def registration(request):
    return HttpResponse('Регистрация')

def authorization(request):
    return HttpResponse('Авторизация')
