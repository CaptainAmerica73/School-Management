from datetime import time
from django.shortcuts import redirect, render
from .models import User,Teacher
from .forms import LoginForm,SignupForm

def home(request):
    # print(f"Available between {time(9,0).strftime('%I:%M %p')} and {time(18,0).strftime('%I:%M %p')}.")
    return render(request,'home.html')

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User(username=username,email=email,password=password)
            user.save()
            return redirect('home')
    else:
        form = LoginForm()
    return render(request,'login.html',{'form' : form})

def signup(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password']
            password2 = form.cleaned_data['confirmPassword']
            if(password1 != password2):
                form.add_error('confirmPassword', 'Passwords do not match')
            else:
                user = User(username=username,email=email,password=password1)
                user.save()
                return redirect('home')
    else:
        form = SignupForm()
    return render(request,'signup.html',{'form' : form})    

def teachers(request):
    teachers = Teacher.objects.all()
    return render(request,'teachers.html',{'teachers': teachers})

def teacher(request,name):
    teacher = Teacher.objects.filter(name = name).first()
    if teacher:
        related = Teacher.objects.filter(specialization = teacher.specialization).exclude(name = name)
    else:
        related = []
    return render(request,'teacher.html',{ 'teacher': teacher, 'related_teachers': related })