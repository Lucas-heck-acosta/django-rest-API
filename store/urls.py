from django.contrib import admin
from django.urls import path
from store.views import cliente_view, produto_view, categoriaProdutos_view, vendedor_view
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', cliente_view.lista_cliente),
    path('clientes/<int:id>', cliente_view.lista_cliente_id),

    path('produtos/', produto_view.lista_produto),
    path('produtos/<int:id>', produto_view.lista_produto_id),

    path('categorias/', categoriaProdutos_view.lista_categorias),
    path('categorias/<int:id>', categoriaProdutos_view.lista_categorias_id),

    path('vendedores/', vendedor_view.lista_vendedor),
    path('vendedores/<int:id>', vendedor_view.lista_vendedor_id)
]


urlpatterns = format_suffix_patterns(urlpatterns)
