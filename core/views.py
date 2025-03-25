import requests
from django.shortcuts import render
from produits.models import Produit



# Create your views here.
def dashboard(request):
    produits = Produit.objects.all()
    return render(request, "dashboard.html", {'current_path': request.path, 'produits': produits})

def test1(request):
    return render(request, "test1.html", {'current_path': request.path})

def posts(request):
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts = response.json()

    return render(request, 'posts.html', {'posts': posts})