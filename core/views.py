from django.shortcuts import render
from clients.models import Client

def dashboard(request):
    clients_env_ifs = Client.objects.filter(environnement='IFS')
    clients_env_cfg = Client.objects.filter(environnement='CFG')
    return render(request, 'dashboard.html', {
        'clients_env_ifs': clients_env_ifs,
        'clients_env_cfg': clients_env_cfg,
    })


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from clients.models import Client
import json

@csrf_exempt
@require_POST
def dashboard_save_changes(request):
    try:
        data = json.loads(request.body)
        ids_ifs = data.get('env_ifs', [])
        ids_cfg = data.get('env_cfg', [])

        Client.objects.filter(id__in=ids_ifs).update(environnement='IFS')
        Client.objects.filter(id__in=ids_cfg).update(environnement='CFG')

        return JsonResponse({'status': 'ok'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
