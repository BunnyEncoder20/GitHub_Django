from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, world. You're at the DjangoProject01 home page.")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("Hello, world. You're at the DjangoProject01 about page.")

def contact(request):
    return HttpResponse("Hello, world. You're at the DjangoProject01 contact page.")