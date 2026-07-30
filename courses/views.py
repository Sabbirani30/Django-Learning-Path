import email

from django.forms import forms
from django.shortcuts import render
from django.http import HttpResponse
from . models import Student
from . forms import StudentRegistration
from django.http import HttpResponseRedirect
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
            print('first_name : ', form.cleaned_data['name'])
            print('email : ', form.cleaned_data['email'])
            print('age : ', form.cleaned_data['age'])
            print('course : ', form.cleaned_data['course'])
            print('batch : ', form.cleaned_data['batch'])
            print('department : ', form.cleaned_data['department'])
            print('password : ', form.cleaned_data['password'])
            print('re_password : ', form.cleaned_data['re_password'])
            print('textarea : ', form.cleaned_data['textarea'])
            print('payment : ', form.cleaned_data['payment'])
            print("Valid form")
            return HttpResponseRedirect('/success/')
        
    else:
        form = StudentRegistration()
        form.order = form.order_fields(field_order=['name', 'email', 'age', 'course', 'batch', 'department', 'password', 'textarea', 'payment'])
        print("Execute Get")

    return render(request, 'courses/forms.html', {'form': form})

def success(request):
    return render(request, 'courses/success.html')