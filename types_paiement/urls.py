from django.urls import path
from . import views

urlpatterns = [
    path('', views.TypePaiementListView.as_view(), name='typepaiement_list'),
    path('ajouter/', views.TypePaiementCreateView.as_view(), name='typepaiement_create'),
    path('<int:pk>/', views.TypePaiementDetailView.as_view(), name='typepaiement_detail'),
    path('<int:pk>/modifier/', views.TypePaiementUpdateView.as_view(), name='typepaiement_update'),
    path('<int:pk>/supprimer/', views.TypePaiementDeleteView.as_view(), name='typepaiement_delete'),
]
