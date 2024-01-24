from django.http import HttpResponse

# Create your views here.
def home(request):
    """HttpResponse function"""
    return HttpResponse("Home")


def about(request):
    """HttpResponse function"""
    return HttpResponse("Sobre")


def contact(request):
    """HttpResponse function"""
    return HttpResponse("Contato")
