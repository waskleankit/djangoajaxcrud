from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def home(request):
    form = StudentRegistration()
    return render(request,'enroll/home.html',{'form':form})