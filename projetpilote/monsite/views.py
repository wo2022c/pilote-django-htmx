from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

# Create your views here.
from django.shortcuts import render, redirect

def hello(request):
    return render(request, 'monsite/hello.html')