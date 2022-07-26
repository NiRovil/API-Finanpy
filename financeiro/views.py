from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, NumberFilter
from financeiro.models import Receitas, Despesas
from financeiro.serializer import ReceitaSerializer, DespesaSerializer

class FiltroData(FilterSet):
    mes = NumberFilter(field_name='Mes', lookup_expr='exact')

    class Meta:
        model = Receitas
        fields = ['data']

class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = Receitas.objects.all()
    serializer_class = ReceitaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['descricao']
    filterset_class = FiltroData

class DespesaViewSet(viewsets.ModelViewSet):
    queryset = Despesas.objects.all()
    serializer_class = DespesaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['descricao']