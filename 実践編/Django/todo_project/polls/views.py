# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    		return HttpResponse("Hello, world!")
def home(request):
    		return render(request, 'polls/home.html')
