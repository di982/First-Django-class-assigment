from django.shortcuts import render

# Create your views here.
def home1(request):
    return render(request,'home1.html')

def contact(request):
    return render(request,'contact.html')

def classes(request):
    return render(request, 'classes.html')

def teachers(request):
    return render(request, 'teachers.html')