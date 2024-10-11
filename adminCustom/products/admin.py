from django.contrib import admin
from django.http import HttpRequest
from django.http.response import HttpResponse
from .models import Producto




class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    ordering = ('fecha_creacion',)
    list_filter = ('valoracion', 'fecha_modificacion')
    list_display = ('nombre', 'color_precio', 'stock', 'valoracion','icono_valoracion', 'fecha_creacion')
    
    fieldsets = (
        ('Información Básica', {'fields': ('nombre', 'descripcion', 'precio', 'stock', 'valoracion')}),
        ('Multimedia', {'fields': ('imagen',)}),
        ('Fechas', {'fields': ('fecha_creacion', 'fecha_modificacion')}),
    )

    # Personalizar los títulos y menú
    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': 'Inventario de Productos 2024'}
        return super().changelist_view(request, extra_context=extra_context)
    
    def change_view(self, request, object_id, form_url='', extra_context=None):
        producto = Producto.objects.get(id=object_id)
        extra_context = {'title': f'Aqui puedes Editar Producto: {producto.nombre}'}
        return super().change_view(request, object_id, form_url, extra_context=extra_context)
    
    def add_view(self, request, form_url='', extra_context=None):
        extra_context = {'title': 'Aqui puede Añadir un nuevo producto'}
        return super().add_view(request, form_url, extra_context=extra_context)

class CustomAdminSite(admin.AdminSite):
    site_header = 'Gestión de Inventario'
    site_title = 'Administrador de Inventarios'
    index_title = 'Panel de Control de Inventario'

admin.site = CustomAdminSite(name='custom_admin')
admin.site.register(Producto, ProductoAdmin)
