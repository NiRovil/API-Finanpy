from financeiro.models import Receitas, Despesas

def receita_existe(descricao, valor, data_transacao):
    existe = Receitas.objects.filter(descricao=descricao, valor=valor, data__month=data_transacao.month, data__year=data_transacao.year).exists()
    return existe

def despesa_existe(descricao, valor, data_transacao):
    existe = Despesas.objects.filter(descricao=descricao, valor=valor, data__month=data_transacao.month, data__year=data_transacao.year).exists()
    return existe