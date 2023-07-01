from django.db import models

# Create your models here.

class Funcionario(models.Model):
   nome = models.CharField(max_length=100)
   cargo = models.CharField(max_length=20)
   email = models.CharField(max_length=100)
   departamento = models.CharField(max_length=20)
   data_nascimento = models.DateField()
   data_admissao = models.DateField()
   salario = models.DecimalField(max_digits=10, decimal_places=2)
   competencias = models.TextField()
   supervisor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
   foto = models.ImageField(upload_to='funcionarios/', null=True, blank=True)   
   def __str__(self):
        return self.nome 

