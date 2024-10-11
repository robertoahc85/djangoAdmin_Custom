from django.db import models
from django.utils.html import format_html
from django.utils.timezone import now
class Producto(models.Model):
    nombre= models.CharField(max_length=200)
    descripcion = models.TextField()
    precio= models.DecimalField(max_digits=10, decimal_places=2)
    stock =models.PositiveIntegerField()
    valoracion= models.DecimalField(max_digits=10, decimal_places=2 ,default=0)
    imagen=models.ImageField(upload_to='productos/')
    fecha_creacion= models.DateTimeField(auto_now=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    def color_precio(self):
        if self.precio < 50:
            color = 'green'
        elif self.precio <100:
            color = 'orange' 
        else:
            color = 'red'  
        return format_html('<span style="color:{};">${}</span>',color,self.precio)  
    
    def icono_valoracion(self):
        if self.valoracion >=10:
            return format_html('<span style="color:green">&#128077</span>')
        else:
            return format_html('<span style="color:green">&#128078</span>')
        
    icono_valoracion.short_description = 'Valoracion'
    color_precio.short_description = 'Precio(color)' 
          
def __str__(self):
    return self.nombre
# Create your models here.
