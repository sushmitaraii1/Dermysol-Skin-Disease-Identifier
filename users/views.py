from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, AppontmentForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import mail_admins
from .models import Disease


# Create your views here.
def registeruser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = UserRegisterForm()
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            try:
                if form.is_valid:
                    form.save()
                    username = form.cleaned_data.get('username')
                    messages.success(request, f'Account created for {username}!')
                    return redirect('login')
            except ValueError:
                messages.info(request, '')
        return render(request, 'users/register.html', {'form': form})


def loginuser(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request, 'users/login.html', context)


def logoutuser(request):
    logout(request)
    return redirect('home')


def homepage(request):
    return render(request, 'users/home.html')


def dashboard(request):
    return render(request, 'users/dashboard.html')


def doctor(request):
    return render(request, 'users/doctor.html')


def appointment(request):
    if request.method == 'POST':
        f = AppontmentForm(request.POST)
        if f.is_valid():
            name = f.cleaned_data['name']
            sender = f.cleaned_data['email']
            service = f.cleaned_data['service']
            time = f.cleaned_data['time']
            print(f.cleaned_data['subject'],f.cleaned_data['note'])
            subject = "You have a new Appointment from {}:{} for {} at {}".format(name, sender,service, time)
            message = "Subject: {}\n\nMessage: {}".format(f.cleaned_data['subject'], f.cleaned_data['note'])
            mail_admins(subject, message)
            f.save()
            messages.add_message(request, messages.INFO, 'Appointment mail sent')
            return redirect('appointment')

    else:
        f = AppontmentForm()
        print("GET request")
    return render(request, 'users/appointment.html', {'form': f})


def diseaseinfo(request):
    diseases= Disease.objects.all()
    return render(request,'users/diseaseinfo.html',{'diseases':diseases})
