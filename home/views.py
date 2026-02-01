from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "Login.html")


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'About.html')


def contact(request):
    return render(request, 'Contact.html')


def form_view(request):
    return render(request, 'form.html')


def register(request):
    return render(request, 'Register.html')


def home_page(request):
    return render(request, 'Home.html')
