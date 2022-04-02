"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .models import Student, Dra, Ireadymath, Ireadyreading
from django.core import serializers


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    test_list = serializers.serialize('json', Student.objects.filter(teacher=8861, pk=94526222))

    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'message':'Your one-stop shop for entering and retreiving student data',
            'year':datetime.now().year,
            'tlist':test_list,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'MR. CSV',
            'message':'3rd Grade Math',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'All about CSV app',
            'year':datetime.now().year,
        }
    )
