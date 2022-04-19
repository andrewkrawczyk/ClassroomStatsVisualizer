"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseRedirect
from .models import Teacher, Student, Dra, Ireadymath, Ireadyreading
from django.core import serializers
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

#Create user view here
from .models import *
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title': 'Home Page',
            'message': 'Your one-stop shop for entering and retrieving student data',
            'year': datetime.now().year,
        }
    )


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


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title': 'About',
            'message': 'All about CSV app',
            'year': datetime.now().year,
        }
    )

def register(request):
    """Renders the teacher registration page."""
    form = CreateUserForm()

    if request.method == 'POST':
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
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'app/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')


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
