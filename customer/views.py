from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def login(request):
    return render(request, 'customer/login.html')


def signup(request):
    return render(request, 'customer/SignUp.html')


def home(request):
    return render(request, 'customer/Foodie.html')

def main(request):
    return render(request, 'customer/Main.html')
