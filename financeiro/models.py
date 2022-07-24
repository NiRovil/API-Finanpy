from django.db import models
from datetime import date

class Receitas(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.IntegerField()
    data = models.DateField(default=date.today())

    def __str__(self):
        return self.descricao

class Despesas(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.IntegerField()
    data = models.DateField(default=date.today())

    def __str__(self):
        return self.descricao