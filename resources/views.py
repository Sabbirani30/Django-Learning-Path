from django.shortcuts import render
from django.http import HttpResponse
from .forms import CustomUserCreationForm  #Usercreation form signup er kaj kore thake 
# Create your views here.
def Math(request):
    return HttpResponse("Welcome to the Math Course!")
def Physics(request):
    return HttpResponse("Welcome to the Physics Course!")
def Chemistry(request):
    return render(request, 'resources/freeresources.html', {'chem': 2})
def Biology(request):
   return render(request, 'resources/blog.html',{'fcrs':5, 'Anik':"Future Big Thing"})
def Big_Data(request):
    Available_Courses = {'fcourses': ["Math", "Physics", "Chemistry", "Biology"]}
    return render(request, 'resources/Big_Data.html',  Available_Courses)


def User_Signup(request):
    if request.method == 'POST':
        frm= CustomUserCreationForm(request.POST)
        if frm.is_valid():
            frm.save()
            
    else:
        frm= CustomUserCreationForm()
    return render(request, 'resources/signup.html', {'form': frm})
