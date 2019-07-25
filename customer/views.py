from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import account
# Create your views here.
def login(request):
    if request.method == "POST":
        name_entered=request.POST['username']
        password_entered=request.POST['password']
        if account.objects.filter(username=name_entered).exists():
            username_obj=account.objects.get(username=name_entered)
            if username_obj.password == password_entered:
                return redirect('main')
            else:
                return render(request, 'customer/login.html',{'message': 'wrong Password' })

        else:
            return render(request, 'customer/login.html',{'message': 'wrong username' })
  
    else:
        return render(request, 'customer/login.html',{})

def signup(request):
    if request.method == "POST":
        name_entered=request.POST.get('fname')
        email_entered=request.POST.get('email')
        password_entered=request.POST.get('password')
        phonenumber_entered=request.POST.get('phone')
        user_obj = account.objects.create(username=name_entered, email=email_entered, password=password_entered, phonenumber=phonenumber_entered)
        user_obj.save()
        return render(request, 'customer/login.html',{})

    else:
        return render(request, 'customer/SignUp.html',{})


def home(request):
    return render(request, 'customer/Foodie.html',{})

def main(request):
    return render(request, 'customer/Main.html')