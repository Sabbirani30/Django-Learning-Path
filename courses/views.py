from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Sabbir (request):
    return HttpResponse("Sabbir is a one of the noob student in the class")
def course  (request):
    course1="Math"
    course2="physics"
    course3="Chemistry"
    free_courses={'c1':course1, 'c2':course2, 'c3':course3}

    return render(request, 'courses/freecourses.html',free_courses)
def Mahdi_Sir (request):
    return render(request, 'courses/freecourses.html')

def Data_Analysis (request):
    return render(request, 'courses/Data_Analysis.html')

def Artificial_Intelligence (request):
    return render(request, 'courses/AI.html')
    