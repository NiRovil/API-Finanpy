from rest_framework import serializers
from financeiro.models import Receitas, Despesas
from financeiro.validator import *

class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receitas
        fields = ['descricao', 'valor', 'data']

    def validate(self, data):
        if receita_existe(data['descricao'], data['valor'], data['data']):
            raise serializers.ValidationError('Movimentação já lançada!')
        return data

class DespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesas
        fields = ['descricao', 'valor', 'data', 'categoria']

    def validate(self, data):
        if despesa_existe(data['descricao'], data['valor'], data['data']):
            raise serializers.ValidationError('Movimentação já lançada!')
        return data