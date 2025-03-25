from django.shortcuts import render
from clients.models import Client

from types_paiement.models import TypePaiement

def dashboard(request):
    model = request.GET.get('model', 'clients')
    context = {'selected_model': model}

    if model == 'clients':
        context['env_ifs'] = Client.objects.filter(environnement='IFS')
        context['env_cfg'] = Client.objects.filter(environnement='CFG')
    elif model == 'types_paiement':
        context['env_ifs'] = TypePaiement.objects.filter(environnement='IFS')
        context['env_cfg'] = TypePaiement.objects.filter(environnement='CFG')
    else:
        context['env_ifs'] = []
        context['env_cfg'] = []

    return render(request, 'dashboard.html', context)


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from clients.models import Client
from types_paiement.models import TypePaiement

@csrf_exempt
def dashboard_save_changes(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        env_ifs = data.get('env_ifs', [])
        env_cfg = data.get('env_cfg', [])
        model = data.get('model')

        if model == 'clients':
            Model = Client
        elif model == 'types_paiement':
            Model = TypePaiement
        else:
            return JsonResponse({'error': 'Modèle inconnu'}, status=400)

        Model.objects.filter(id__in=env_ifs).update(environnement='IFS')
        Model.objects.filter(id__in=env_cfg).update(environnement='CFG')

        return JsonResponse({'status': 'success'})

    return JsonResponse({'error': 'Méthode non autorisée'}, status=405)
