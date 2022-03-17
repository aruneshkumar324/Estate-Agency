from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from contacts.models import Inquiry


def register(request):
    messages = {
        "success" : 'Account Created Successfully',
        'failed': 'fail',
    }
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                return render(request, 'accounts/register.html', {"message": "Username not available."})
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, 'accounts/register.html', {"message": "Email not available."})
                else:
                    # CREATE USER
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                    login(request,user)
                    user.save()
                    return redirect('home')
        else:
            # return redirect('register', message="Password didn't match with confirm_password.")
            return render(request, 'accounts/register.html', {"message": "Password didn't match with confirm_password."})

    else:
        return render(request, 'accounts/register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {"message": "User not available."})

    else:
        return render(request, 'accounts/login.html')


def user_logout(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def dashboard(request):
    user_inquiry = Inquiry.objects.order_by('-created_date').filter(user_id=request.user.id)
    
    return render(request, 'accounts/dashboard.html', {"user_inquiry": user_inquiry})

