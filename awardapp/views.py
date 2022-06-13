from email import message
from pickle import NONE
from django.shortcuts import redirect, render
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import * 
import requests
from django.db.models import Q, query
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def index(request):
    # res=requests.get('http://127.0.0.1:8000/project/').json()
    return render(request, 'index.html')


def output(request):
    res=requests.get('http://127.0.0.1:8000/project/').json()
    return render(request, 'output.html',{'res':res})





#  create endpoint for profile_list
@api_view(['GET','POST'])
def profile_list(request):
    if request.method == 'GET':
        profile = Profile.objects.all()
        serialize = ProfileSerializer(profile,many=True)
        return Response(serialize.data)

    elif request.method == 'POST':
        serialize = ProfileSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status.HTTP_201_CREATED)
        return Response(serialize.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def profile_detail(request,id):
    try:
        profile=Profile.objects.get(id=id)
    except Profile.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serialize = ProfileSerializer(profile)
        return Response(serialize.data)
    
    elif request.method == 'PUT':
        serialize = ProfileSerializer(profile, request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method =='DELETE':
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT_)

# create endpoint for project_list
@api_view(['GET',])
def project_list(request):
    if request.method == 'GET':
        profile = Project.objects.all()
        serialize = ProjectSerializer(profile,many=True)
        return Response(serialize.data)

    elif request.method == 'POST':
        serialize = ProjectSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status.HTTP_201_CREATED)
        return Response(serialize.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def project_detail(request,id):
    try:
        project=Project.objects.get(id=id)
    except Project.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serialize = ProjectSerializer(project)
        return Response(serialize.data)
    
    elif request.method == 'PUT':
        serialize = ProjectSerializer(project, request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method =='DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT_)


        


def display_profile(request):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(display_profile)
    return render(request, 'profile.html',{'form':form})






def register_user(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user=authenticate(username=username, password=password)
            login(request,user)
            # messages.success('Registration is successful')
            return redirect('register')

    else:
        form = RegisterForm()
    return render(request,'register/register.html',{'form':form})


def display_project(request):
        form =ProjectForm()
        if request.method == 'POST':
            form = ProjectForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(display_project)

        return render(request, 'project.html', {'form': form})

def dis_votes(request):
    form = VotesForm()
    if request.method == 'POST':
        form = VotesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("voted has been recorded")

    return render(request, 'votes.html',{'form':form})

def login_user(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user=authenticate(request,username=username,  password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.success(request,"there was an error loggin in lease try again")

    else:
        return render(request,'register/register.html',{'form':form})

def logout_user(request):
    logout(request)
    return redirect('login')

def search(request):
        if request.method == 'GET':
            query = request.GET.get('query')
            if query:
                projects = Project.objects.filter(title__icontains=query)
                return render(request, 'search.html',{"projects": projects})
            else:
                message = "You haven't searched for any image"
                return render(request, 'search.html',{"message":message})
        
