"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from .models import Teacher, Student, Dra, Ireadymath, Ireadyreading
from django.core import serializers


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
