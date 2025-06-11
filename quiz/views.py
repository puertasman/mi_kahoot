from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Preguntas de prueba
QUESTIONS = [
    {"question": "¿Cuál es la capital de Francia?", "options": ["Madrid", "París", "Roma", "Berlín"], "answer": 1},
    {"question": "¿Cuánto es 5x6?", "options": ["11", "30", "56", "25"], "answer": 1},
    {"question": "¿Quién escribió 'Don Quijote'?", "options": ["Cervantes", "Lorca", "Quevedo", "Góngora"], "answer": 0}
]

def index(request):
    return render(request, 'index.html')

def host_game(request):
    return render(request, 'host.html')

def join_game(request):
    return render(request, 'player.html')

@csrf_exempt
def get_question(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        q_index = data.get('index', 0)
        if q_index < len(QUESTIONS):
            question = QUESTIONS[q_index]
            return JsonResponse({"question": question["question"], "options": question["options"]})
        else:
            return JsonResponse({"end": True})

@csrf_exempt
def check_answer(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        q_index = data.get('index')
        selected = data.get('selected')
        correct = QUESTIONS[q_index]['answer']
        return JsonResponse({"correct": selected == correct})
