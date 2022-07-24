from rest_framework import serializers
from financeiro.models import Receitas, Despesas

class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receitas
        fields = ['descricao', 'valor', 'data']

class DespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesas
        fields = ['descricao', 'valor', 'data']