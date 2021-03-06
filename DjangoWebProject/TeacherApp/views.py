"""
Definition of views.
"""

from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import F, Max
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from .forms import *
from .models import *


# @login_required(login_url='login')
def home(request):
    """Renders the home page."""
    if request.user.is_authenticated:
        teacher = Teacher.objects.get(pk=request.user.id)
        email = request.user.email
        students = Student.objects.filter(teacher=request.user.id).all().order_by('student_id')
        math = Ireadymath.objects.annotate(max_date=Max('student__ireadymath__entry_date')) \
            .filter(entry_date=F('max_date')).filter(student__teacher__teacher_id=request.user.id).order_by('student')
        reading = Ireadyreading.objects.annotate(max_date=Max('student__ireadyreading__entry_date')) \
            .filter(entry_date=F('max_date')).filter(student__teacher__teacher_id=request.user.id).order_by('student')

        # assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/index.html',
            {
                'title': 'Home',
                'teacher_name': teacher.first_name + " " + teacher.last_name,
                'teacher_email': email,
                'message': 'Student List for the School Term',
                'year': datetime.now().year,
                'students': students,
                'math': math,
                'reading': reading,
            }
        )
    else:
        # assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/index.html',
            {
                'title': 'Home',
                'problem_statement': 'Problem Statement',
                'problem_message': 'K-12 educators need to be able to analyze large set of data gather from their '
                                   'classroom for determining the correct learning path for the class. Since the '
                                   'educators are currently looking at data from a table perspective, '
                                   'they are spending more time deciphering the data instead of planning the next '
                                   'learning activity. This is also a problem for the students, since educators are '
                                   'less focus on catering to their learning.',
                'solution_statement': 'Solution Statement',
                'solution_message': 'The goal of Classroom Stats Visualizer is to analyze and determine a performance '
                                    'metric for each student given the student???s grades. This performance metric will '
                                    'allow for teachers to quickly determine which students are in needed of '
                                    'assistance. Also, Classroom Stats Visualizer will provide teachers with the '
                                    'ability to dive deeper into each individual student. This deep dive will display '
                                    'the student???s performance metric along with generate visual aids based on '
                                    'student grades over the semester. ',
                'account_creation': 'Try Classroom Stats Visualizer Now',
                'year': datetime.now().year,
                # 'students': students,
            }
        )


def contact(request):
    """Renders the contact page."""
    # assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title': 'CEN 3031: Group 6',
            'students': [['Andrew Krawczyk', 'Product Manager', 'placeholder'],
                         ['Bayron Najera', 'Scrum Master', 'placeholder'],
                         ['Michael Deaver', 'Dev Team Member', 'placeholder'],
                         ['Abdoul-Karim Konate', 'Dev team Member', 'placeholder']],
            'year': datetime.now().year,
        }
    )


def about(request):
    """Renders the about page."""
    # assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title': 'About Us',
            'message': 'A group of University of Florida students taking CEN 3031 looking to develop an application '
                       'to ease teachers??? workload. Teachers saw a shift from in person learning to online learning '
                       'due to the pandemic; therefore, there is a strain on the educational system due to lack of '
                       'tools for facilitating online learning. Our goal is to provide teachers with a resource to '
                       'decipher their class data for them and provide a detail report on their student progress.',
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

    context = {'form': form, 'title': 'Register'}
    return render(request, 'app/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('about')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR Password is incorrect')

        context = {'title': 'Login'}
        return render(request, 'app/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def deleteStudent(request, student_id=None):
    student = Student.objects.get(pk=student_id)
    student.delete()
    return redirect('home')


def createStudent(request):
    data = dict()

    if request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False

    else:
        form = CreateStudentForm(initial={'teacher': request.user.id, 'composite_score': 0})

    context = {'form': form}
    data['html_form'] = render_to_string('app/student_create.html', context, request=request)
    return JsonResponse(data)
