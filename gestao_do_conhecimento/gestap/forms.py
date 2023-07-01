from django.forms import ModelForm 
from .models import Funcionario

class Funcionarioform (ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'departamento', 'foto', 'competencias' ]
        