from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Math(request):
    return HttpResponse("Welcome to the Math Course!")
def Physics(request):
    return HttpResponse("Welcome to the Physics Course!")
def Chemistry(request):
    return render(request, 'resources/freeresources.html', {'chem': 2})
def Biology(request):
   return render(request, 'resources/blog.html')