"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Teacher, Student, Dra, Ireadymath, Ireadyreading
from django.core import serializers
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


#Create user view here
from .models import *
from .models import Student
from .models import Ireadymath
from .models import Ireadyreading
from .forms import CreateUserForm



@login_required(login_url='login')
def home(request):
    students = Student.objects.all().order_by('student_id')
    # math = Ireadymath.objects.all().order_by('student')
    # reading = Ireadyreading.objects.all().order_by('student')
    
    
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title': 'Welcome Teacher',
            'message': 'Student List for the School Term',
            'year': datetime.now().year,
            'students':students, 
        }
    )
    


@login_required(login_url='login')
def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title': 'MR. CSV',
            'message': '3rd Grade Math',
            'year': datetime.now().year,
        }
    )

@login_required(login_url='login')
def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title': 'About',
            'message': 'Our primary objective is to provide a convenient and comprehensive place for teachers to more easily manage a variety of student metrics that may normally be accessed among several different websites or programs.',
            'year': datetime.now().year,
        }
    )

def register(request):
    """Renders the teacher registration page."""
    form = CreateUserForm()

    if request.method == 'POST':
        if request.user.is_authenticated:
            return redirect('home')
        else:
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

    context = {'form' :form}
    return render(request, 'app/register.html', context)
    
    # return render(
    #     request,        
    #     'app/register.html',
    #      {
    #          'form': form,
    #          'title': 'Register Today',
    #          'year': datetime.now().year,
    #      }
    # )
def loginPage(request):
	if request.user.is_authenticated:
		return redirect('about')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR Password is incorrect')

		context = {}
		return render(request, 'app/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def Profile(request):
    return render(
        request,
        'app/profile.html',
        {
            
        }
    )
    
    
    
   

@login_required(login_url='login')
def searchtest(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    if request.method == "POST":
        searched = request.POST['searched']

        if searched:
            querydata = (Student.objects.filter(teacher=int(searched))).values('student_id', 'first_name',
                                                                               'last_name', 'truancy',
                                                                               'composite_score')
        else:
            querydata = Teacher.objects.all()

        return render(
            request,
            'app/test.html',
            {
                'title': 'Home Page',
                'message': 'Your one-stop shop for entering and retrieving student data',
                'year': datetime.now().year,
                'searched': searched,
                'querydata': querydata,
            }
        )
    else:
        querydata = Teacher.objects.all()

        return render(
            request,
            'app/test.html',
            {
                'title': 'Home Page',
                'message': 'Your one-stop shop for entering and retrieving student data',
                'year': datetime.now().year,
                'querydata': querydata,
            }
        )
