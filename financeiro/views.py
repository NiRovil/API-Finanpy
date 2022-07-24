from rest_framework import viewsets
from financeiro.models import Receitas, Despesas
from financeiro.serializer import ReceitaSerializer, DespesaSerializer

class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = Receitas.objects.all()
    serializer_class = ReceitaSerializer

class DespesaViewSet(viewsets.ModelViewSet):
    queryset = Despesas.objects.all()
    serializer_class = DespesaSerializer
