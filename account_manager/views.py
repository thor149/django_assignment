from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *


@login_required
def doctor_dashboard(request):
    # Add logic for doctor dashboard
    doctor_profile = request.user
    name = doctor_profile.first_name
    print(name)
    context = {'doctor_profile': doctor_profile}

    return render(request, 'doctor_dashboard.html', context)


@login_required
def patient_dashboard(request):
    patient_profile = request.user
    name = patient_profile.first_name
    print(name)
    context = {'patient_profile': patient_profile}

    return render(request, 'patient_dashboard.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(1)
        if user is not None:
            print(2)
            login(request, user)
            print(user.user_type)
            if user.user_type == 'doctor':
                print(3)
                return redirect('doctor_dashboard')
            elif user.user_type == 'patient':
                return redirect('patient_dashboard')
        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(form.errors)  # Add this line to print form errors to the console
        if form.is_valid():
            print(3)
            print(form)
            form.save()
            return redirect('login')  # Redirect to the login page after successful signup
    else:
        print(2)
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def doctor_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.user_type != 'doctor':
            messages.error(request, 'You do not have permission to access this page.')
            return redirect('login')  # Redirect to login page or another page as needed
        return view_func(request, *args, **kwargs)

    return _wrapped_view


@login_required
@doctor_required
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('blog_posts_list')
    else:
        form = BlogPostForm()

    return render(request, 'create_blog_post.html', {'form': form})


def blog_posts_list(request):
    if request.user.is_authenticated and request.user.user_type == 'patient':
        blog_posts = BlogPost.objects.filter(draft=False)
        print(blog_posts, 1)
    else:
        blog_posts = BlogPost.objects.filter(author=request.user)

    return render(request, 'blog_posts_list.html', {'blog_posts': blog_posts, 'user': request.user})


def user_profile(request):
    if request.user.is_authenticated:
        if request.user.user_type == 'doctor':
            print(3)
            return redirect('doctor_dashboard')
        elif request.user.user_type == 'patient':
            return redirect('patient_dashboard')
    else:
        return HttpResponseRedirect('/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
