from django.contrib import admin
from .models.cliente import Cliente
from .models.produto import Produto
from .models.categoriaProduto import CategoriaProduto
from .models.vendedor import Vendedor
from .models.venda import Venda
from .models.produtoVenda import ProdutoVenda

admin.site.register(Cliente)
admin.site.register(Produto)
admin.site.register(CategoriaProduto)
admin.site.register(Vendedor)
admin.site.register(Venda)
admin.site.register(ProdutoVenda)
