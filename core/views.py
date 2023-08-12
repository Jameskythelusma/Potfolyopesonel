from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def apwopo(request):
    return render(request,'apwopo.html')

def potfolyo(request):
    return render(request,'potfolyo.html')

def konpetans(request):
    return render(request,'konpetans.html')

def kontak(request):
    return render(request,'kontak.html')
