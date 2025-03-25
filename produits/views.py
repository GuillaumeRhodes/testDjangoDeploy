from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from produits.models import Produit
# Create your views here.
class ProduitListView(ListView):
    model = Produit
    template_name = 'produits/list.html'

class ProduitDetailView(DetailView):
    model = Produit
    template_name = 'produits/detail.html'

class ProduitCreateView(CreateView):
    model = Produit
    fields = ['nom', 'description']
    template_name = 'produits/form.html'
    success_url = reverse_lazy('produit_list')

class ProduitUpdateView(UpdateView):
    model = Produit
    fields = ['nom', 'description']
    template_name = 'produits/form.html'
    success_url = reverse_lazy('produit_list')

class ProduitDeleteView(DeleteView):
    model = Produit
    template_name = 'produits/confirm_delete.html'
    success_url = reverse_lazy('produit_list')
