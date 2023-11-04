from django.shortcuts import render

def index (request):
    return render(request, 'main/index.html')

def authorization (request):
    return render(request, 'main/authorization.html')
