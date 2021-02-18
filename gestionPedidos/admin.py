from django.contrib import admin

# Register your models here.

from gestionPedidos.models import Cliente, articulos, pedidos

class ClienteAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion","telefono")
    search_fields=("nombre","telefono")


admin.site.register(Cliente,ClienteAdmin)
admin.site.register(articulos)
admin.site.register(pedidos)
