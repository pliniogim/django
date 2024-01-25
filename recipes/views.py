from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    """HttpResponse function"""
    print(request)
    # return HttpResponse("Home")
    return render(request, 'recipes/home.html', context={
        'name': 'Plínio Gimenez',
    })
    # return render(request, 'global/home.html')

def about(request):
    """HttpResponse function"""
    print(request)
    return HttpResponse("Sobre")


def contact(request):
    """HttpResponse function"""
    print(request)
    return HttpResponse("Contato")
