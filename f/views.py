from django.shortcuts import render

# Create your views here.
def first(request):
    return render(request,'f/first.html')

def second(request):
    return render(request,'f/second.html')

def tri(request):
    return render(request,'f/tri.html')

def four(request):
    return render(request,'f/four.html')
