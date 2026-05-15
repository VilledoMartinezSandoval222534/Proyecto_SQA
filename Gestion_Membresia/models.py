from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.

class membresia(models.Model):
    """ Modelo que registra un tipo de membresía """
    Tipo_Membresia = models.CharField(max_length=150) 
    """ Campo que representa el nombre del tipo de membresía se un cliente """
    Precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.0)]  
    )
    """ Campo que representa el precio del tipo de membresía  """
    Duracion_dias = models.PositiveIntegerField()
    """ Campo que representa la duración en días del tipo de membresía  """
    def __str__(self): 
        return self.Tipo_Membresia
    """ Define cómo se muestra una instancia de 'membresia' """
