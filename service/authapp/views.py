import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from .models import User


def authentication(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        user = User.objects.filter(login=data['login'], password=data['password'])
        if user:
            return JsonResponse({'status': 'Аутентификация пройдена'}, status=200)
        else:
            return JsonResponse({'status': 'Аутентификация провалена'}, status=400)


def authorization(request):
    if request.method == 'POST':
        return JsonResponse({'status': 'Авторизация'})
