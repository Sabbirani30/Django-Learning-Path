from django.forms import forms
from django.shortcuts import render
from django.http import HttpResponse
from . models import Student
from . forms import StudentRegistration
# Create your views here.

def Sabbir(request):
    return HttpResponse("Sabbir is a one of the noob student in the class")


def course(request):
    course1 = "Math"
    course2 = "physics"
    course3 = "Chemistry"
    free_courses = {'c1': course1, 'c2': course2, 'c3': course3}

    return render(request, 'courses/freecourses.html', free_courses)


def Mahdi_Sir(request):
    return render(request, 'courses/freecourses.html')


def Data_Analysis(request):
    return render(request, 'courses/Data_Analysis.html')


def Artificial_Intelligence(request):
    return render(request, 'courses/AI.html')


def Student_Info(request):
    studentdetails = Student.objects.all()
    return render(request, 'courses/student.html', {'students': studentdetails})


def Show_Form(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            print("form.changed_data")
            print("Valid form")
        else:
            form = StudentRegistration(auto_id='true')
            form.order_fields(['name', 'age', 'batch', 'age', 'course', 'department', 'password'])
    else:
        form = StudentRegistration()
        print("Execute Get")

    return render(request, 'courses/forms.html', {'form': form})