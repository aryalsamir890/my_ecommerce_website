from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('this is the accounts app haha bitch')

def myapp(request):
    return HttpResponse('this is the text which supposed to get debugged!!')