from django.shortcuts import render
from .models import Funcionario
from .forms import Funcionarioform
import datetime

# Create your views here.

""" def home(request):
    data = {}
    lista = []

    for c in range(10):
        lista.append(c+1)

    data['transacoes'] = [lista]
    data['now'] = datetime.datetime.now()
    return render(request, 'gestap/home.html') """

def listagem(request):
    funcionarios = Funcionario.objects.all()

    return render(request, 'gestap/listagem.html', {'funcionarios': funcionarios})


