from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from clients.models import Client

class ClientListView(ListView):
    model = Client
    template_name = 'clients/list.html'

class ClientDetailView(DetailView):
    model = Client
    template_name = 'clients/detail.html'

class ClientCreateView(CreateView):
    model = Client
    fields = ['nom', 'email']
    template_name = 'clients/form.html'
    success_url = reverse_lazy('client_list')

class ClientUpdateView(UpdateView):
    model = Client
    fields = ['nom', 'email']
    template_name = 'clients/form.html'
    success_url = reverse_lazy('client_list')

class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'clients/confirm_delete.html'
    success_url = reverse_lazy('client_list')
