from rest_framework import viewsets, filters, generics
from django_filters.rest_framework import DjangoFilterBackend, CharFilter, FilterSet
from financeiro.models import Receitas, Despesas
from financeiro.serializer import ReceitaSerializer, DespesaSerializer


# Filtro para usuários que acessarem a API de forma visual, por meio do site, etc...
class FilterDataReceita(FilterSet):
    mes = CharFilter(label='Mes', field_name='data__month', lookup_expr='exact')
    ano = CharFilter(label='Ano', field_name='data__year', lookup_expr='exact')
    class Meta:
        model = Receitas
        fields = ['mes', 'ano']

class FilterDataDespesa(FilterSet):
    mes = CharFilter(label='Mes', field_name='data__month', lookup_expr='exact')
    ano = CharFilter(label='Ano', field_name='data__year', lookup_expr='exact')
    class Meta:
        model = Despesas
        fields = ['mes', 'ano']

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

# Filtro para requisições em URL -> /receitas/'mes'/'ano'/
class ReceitaViewSetFiltro(generics.ListAPIView):
    def get_queryset(self):
        queryset = Receitas.objects.filter(data__month=self.kwargs['mes'], data__year=self.kwargs['ano'])
        return queryset
    serializer_class = ReceitaSerializer

class DespesaViewSetFiltro(generics.ListAPIView):
    def get_queryset(self):
        queryset = Despesas.objects.filter(data__month=self.kwargs['mes'], data__year=self.kwargs['ano'])
        return queryset
    serializer_class = DespesaSerializer