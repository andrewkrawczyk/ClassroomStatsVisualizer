from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def home(request):
    """Renders home page for parents"""
    return render(
        request, 
        'Parent/home.html', 
        {
            'title':'Parent Home Page',
            'message':'View your child\'s stats here',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders contact page for parents"""
    return render(
        request, 
        'Parent/contact.html', 
        {
            'title':'Parent Contact Page',
            'year':datetime.now().year,
        }
    )


def about(request):
    """Renders about page for parents"""
    return render(
        request, 
        'Parent/about.html', 
        {
            'title':'Parent About Page',
            'year':datetime.now().year,
        }
    )