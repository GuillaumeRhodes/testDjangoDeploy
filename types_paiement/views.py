from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import TypePaiement

# Create your views here.

class TypePaiementListView(ListView):
    model = TypePaiement
    template_name = 'types_paiement/list.html'
    context_object_name = 'object_list'

class TypePaiementDetailView(DetailView):
    model = TypePaiement
    template_name = 'types_paiement/detail.html'

class TypePaiementCreateView(CreateView):
    model = TypePaiement
    fields = ['nom', 'actif', 'environnement']
    template_name = 'types_paiement/form.html'
    success_url = reverse_lazy('typepaiement_list')

class TypePaiementUpdateView(UpdateView):
    model = TypePaiement
    fields = ['nom', 'actif', 'environnement']
    template_name = 'types_paiement/form.html'
    success_url = reverse_lazy('typepaiement_list')

class TypePaiementDeleteView(DeleteView):
    model = TypePaiement
    template_name = 'types_paiement/confirm_delete.html'
    success_url = reverse_lazy('typepaiement_list')
