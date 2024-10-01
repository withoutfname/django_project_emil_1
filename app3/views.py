from django.http import HttpResponse


# Create your views here.
def filter(request):
    return HttpResponse('Фильтр')

def favorites(request):
    return HttpResponse('Избранное')

def cart(request):
    return HttpResponse('Корзина')

