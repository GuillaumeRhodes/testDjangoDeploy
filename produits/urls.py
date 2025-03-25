from django.urls import path
from .views import (
    ProduitListView,
    ProduitDetailView,
    ProduitCreateView,
    ProduitUpdateView,
    ProduitDeleteView,
)

urlpatterns = [
    path('', ProduitListView.as_view(), name='produit_list'),                     
    path('<int:pk>/', ProduitDetailView.as_view(), name='produit_detail'),        
    path('create/', ProduitCreateView.as_view(), name='produit_create'),          
    path('<int:pk>/update/', ProduitUpdateView.as_view(), name='produit_update'),
    path('<int:pk>/delete/', ProduitDeleteView.as_view(), name='produit_delete'),
]
