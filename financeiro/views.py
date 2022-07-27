from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend, CharFilter, FilterSet
from financeiro.models import Receitas, Despesas
from financeiro.serializer import ReceitaSerializer, DespesaSerializer

class FilterDataReceita(FilterSet):
    mes = CharFilter(label='Mes', field_name='data__month', lookup_expr='exact')
    class Meta:
        model = Receitas
        fields = ['mes']

class FilterDataDespesa(FilterSet):
    mes = CharFilter(label='Mes', field_name='data__month', lookup_expr='exact')
    class Meta:
        model = Despesas
        fields = ['mes']

class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = Receitas.objects.all()
    serializer_class = ReceitaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['descricao']
    filterset_class = FilterDataReceita

class DespesaViewSet(viewsets.ModelViewSet):
    queryset = Despesas.objects.all()
    serializer_class = DespesaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['descricao']
    filterset_class = FilterDataDespesa