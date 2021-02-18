from django.contrib import admin

# Register your models here.

from gestionPedidos.models import Cliente, articulos, pedidos

class ClienteAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion","telefono")
    search_fields=("nombre","telefono")
class ArticulosAdmin(admin.ModelAdmin):
    list_display=('nombre','seccion','precio')

class PedidosAdmin(admin.ModelAdmin):
    list_display=('numero','fecha')
    list_filter=('fecha',)
    date_hierarchy='fecha'


admin.site.register(Cliente,ClienteAdmin)
admin.site.register(articulos, ArticulosAdmin)
admin.site.register(pedidos, PedidosAdmin)
