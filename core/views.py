import requests
from django.shortcuts import render


# Create your views here.
def dashboard(request):
    return render(request, "dashboard.html", {'current_path': request.path})

def test1(request):
    return render(request, "test1.html", {'current_path': request.path})

def posts(request):
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts = response.json()

    return render(request, 'posts.html', {'posts': posts})