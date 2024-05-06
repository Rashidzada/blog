from django.shortcuts import render

# Create your views here.
def index(requset):
    return render(requset,'index.html')


def contact(requset):
    return render(requset,'contact.html')


def about(request):
    return render(request,'about.html')


def blog(request):
    return render(request,'blog.html')