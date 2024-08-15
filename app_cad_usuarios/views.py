import requests
from django.shortcuts import render
from .models import  Usuario
from django.http import HttpResponse, JsonResponse
from django.core.management import call_command
from django.views.decorators.csrf import csrf_exempt

def run_migrations(request):
    call_command('run_migrations')
    return HttpResponse('Migrations complete.')


# Create your views here.
def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    #Salvando os dados no DB
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    #Trazer dados contidos no DB
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    #carregar pg com os dados
    return render(request, 'usuarios/usuarios.html', usuarios)


#whatsapp
@csrf_exempt
def send_whatsapp_message(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')

        # Substitua 'YOUR_ACCESS_TOKEN' pelo token que você recebeu na configuração da API
        token = 'EAAPPqOxns5EBO8fBzCaZCtkTtrOM9aemA1v5xgnoWVKwSszvVZBH34WkXEE6ztVaZClalmSerRyxjHqPemS4w5LoRMtTCRzwWlKyQlQfSNZCwn50GCD6ZBE2rZBgJ8QTuJIMZAArZAHJcVea621H4rnxDAsFjoclC3onKiBiwxfmRnilHHOTvgP9daONQZCKZBCmiFFZBaN6FBK8yJIIanKl4K8T9ChUfUZD'
        url = 'https://graph.facebook.com/v20.0/422114017645657/messages'

        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }

        data = { "messaging_product": "whatsapp", "to": phone_number, "type": "template", "template": { "name": "saudacao", "language": { "code": "pt_BR" } } }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            return JsonResponse({"status": "Mensagem enviada com sucesso!"})
        else:
            return JsonResponse({"status": f"Falha ao enviar mensagem: {response.status_code}, {response.text}"})

    return HttpResponse(status=405)

def chat_view(request):
    user_name = ""
    if request.method == 'POST':
        user_name = request.POST.get('name')

    return render(request, 'usuarios/chat.html', {'user_name': user_name})