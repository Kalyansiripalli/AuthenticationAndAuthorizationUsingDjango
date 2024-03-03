from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def receipes(request):
    if request.method =="POST":
        data=request.POST
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')
        receipe_image=request.FILES.get('receipe_image')
        print(receipe_name)
        print(receipe_description)
        print(receipe_image)
        Receipe.objects.create(receipe_name=receipe_name, receipe_description=receipe_description, receipe_image=receipe_image)
        return redirect('/receipe')
    queryset=Receipe.objects.all()

    if request.GET.get('search'):
        queryset=queryset.filter(receipe_name__icontains = request.GET.get('search'))
    context={'receipes':queryset}

    return render(request, "receipes.html", context)

@login_required(login_url="/login/")
def update_receipe(request,id):
    queryset=Receipe.objects.get(id=id)
    if request.method=='POST':
        data=request.POST
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')
        receipe_image=request.FILES.get('receipe_image')
        queryset.receipe_name=receipe_name
        queryset.receipe_description=receipe_description
        if receipe_image:
            queryset.receipe_image=receipe_image
        queryset.save()
        return redirect('/receipe/')
    context={'receipe':queryset}
    return render(request, 'update_receipe.html', context)

@login_required(login_url="/login/")
def delete_receipe(request, id):
    queryset=Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipe/')



def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(username=username, password=password)
        
        if user is not None:
            # Login the user
            login(request, user)
            return redirect('/receipe/')  # Redirect to the desired page after successful login
        else:
            # If authentication fails, display an error message
            messages.error(request, 'Invalid username or password')
            return redirect('/login/')  # Redirect back to the login page

    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login')

 
def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('Username')
        password = request.POST.get('password')

        # Check if a user with the same username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username not available. Please choose a different username.')
            return redirect('/register/')
        
        # Create a new user
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password)
        messages.success(request, 'Account created successfully. You can now log in.')
        return redirect('/register/')

    # If request method is not POST, render the registration form
    return render(request, 'register.html')
