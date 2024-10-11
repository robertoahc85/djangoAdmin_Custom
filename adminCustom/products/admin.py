from django.contrib import admin
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields= ('fecha_creacion','fecha_modificacion',)
    ordering =('fecha_creacion',)
    list_filter = ('valoracion','fecha_modificacion')
    list_display = ('nombre','color_precio', 'stock','valoracion','fecha_creacion')
    
    fieldsets = (
       ('Información Básica',{'fields':('nombre','descripcion','precio','stock', 'valoracion')}) ,
       ('Multimedia',{ 'fields' : ('imagen',)}),
       ('Fechas', {'fields': ('fecha_creacion','fecha_modificacion') }), 
    )

# Register your models here.
admin.site.register(Producto,ProductoAdmin)

# menor 10 rojo
# mayor que 5 , verde