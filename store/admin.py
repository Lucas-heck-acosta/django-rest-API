from django.contrib import admin
from .models.cliente import Cliente
from .models.produto import Produto
from .models.categoriaProduto import CategoriaProduto

admin.site.register(Cliente)
admin.site.register(Produto)
admin.site.register(CategoriaProduto)
