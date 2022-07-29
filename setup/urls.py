from rest_framework import routers
from financeiro.views import ReceitaViewSet, DespesaViewSet, ReceitaViewSetFiltro, DespesaViewSetFiltro 
from django.contrib import admin
from django.urls import path, include

router = routers.DefaultRouter()
router.register('receitas', ReceitaViewSet, basename='receitas')
router.register('despesas', DespesaViewSet, basename='despesas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('receitas/<int:mes>/<int:ano>', ReceitaViewSetFiltro.as_view()),
    path('despesas/<int:mes>/<int:ano>', DespesaViewSetFiltro.as_view())
]
