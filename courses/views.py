import email

from django.forms import forms
from django.shortcuts import render
from django.http import HttpResponse
from . models import Student,Info
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
            First_Name=form.cleaned_data['name']
            Email=form.cleaned_data['email']
            Age=form.cleaned_data['age']
            Course=form.cleaned_data['course']
            Batch=form.cleaned_data['batch']
            Department=form.cleaned_data['department']
            Password=form.cleaned_data['password']
            Re_password=form.cleaned_data['re_password']
            Textarea=form.cleaned_data['textarea']
            Payment=form.cleaned_data['payment']

            django_fourteen = Info(name=First_Name, Email=Email, Age=Age, course=Course, batch=Batch, department=Department, password=Password, re_password=Re_password, textarea=Textarea, payment=Payment)
            django_fourteen.save()

            print("Valid form")
            return HttpResponseRedirect('/success/')
        
    else:
        form = StudentRegistration()
        form.order = form.order_fields(field_order=['name', 'email', 'age', 'course', 'batch', 'department', 'password', 're_password', 'textarea', 'payment'])
        print("Execute Get")

    return render(request, 'courses/forms.html', {'form': form})

def success(request):
    return render(request, 'courses/success.html')