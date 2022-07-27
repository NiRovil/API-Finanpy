from django.db import models

class Receitas(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.IntegerField()
    data = models.DateField(blank=False)

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
    data = models.DateField(blank=False)
    categoria = models.CharField(max_length=1, choices=DADOS, null=False, blank=False, default='O')

    def __str__(self):
        return self.descricao