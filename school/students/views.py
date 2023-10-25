from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,"Home.html")

def Contact(request):
    return render(request, "Contact.html")

def Classes(request):
    return render(request, "Classes.html")

def Students(request):
    return render(request, "Students.html")
