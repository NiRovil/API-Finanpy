from email.policy import default
from django.db import models
from datetime import date

class Receitas(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.IntegerField()
    data = models.DateField(default=date.today())

    def __str__(self):
        return self.descricao

class Despesas(models.Model):

    DADOS = (
        ('O','Outros'),
        ('A','Alimentação'),
        ('S','Saúde'),
        ('M','Moradia'),
        ('T','Transporte'),
        ('E','Educação'),
        ('L','Lazer'),
        ('I','Imprevistos'),
    )


    descricao = models.CharField(max_length=100)
    valor = models.IntegerField()
    data = models.DateField(default=date.today())
    categoria = models.CharField(max_length=1, choices=DADOS, null=False, blank=False, default='O')

    def __str__(self):
        return self.descricao