from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone


class Cuenta(models.Model):
    usuario = models.CharField(max_length=80, unique=True)
    correo = models.CharField(max_length=120)                        

    class Meta:
        db_table = "cuenta"
        verbose_name = "cuenta"
        verbose_name_plural = "cuentas"

    def __str__(self):
        return self.usuario


class Personaje(models.Model):
    raza = models.CharField(max_length=20)                                  
    descripcion = models.CharField(max_length=200, null=True, blank=True)   
    nivel = models.PositiveIntegerField(validators=[MinValueValidator(0)])   
    ban = models.BooleanField(default=False)                                 
    creado = models.DateTimeField(default=timezone.now)                      

    class Meta:
        db_table = "personaje"
        verbose_name = "personaje"
        verbose_name_plural = "personajes"

    def __str__(self):
        return f"Personaje {self.id} - {self.raza} (nivel {self.nivel})"


class CuentaPersonaje(models.Model):
    cuenta = models.ForeignKey(
        Cuenta, on_delete=models.CASCADE, related_name="cuenta_personajes"
    )
    personaje = models.ForeignKey(
        Personaje, on_delete=models.CASCADE, related_name="cuenta_personajes"
    )

    class Meta:
        db_table = "cuenta_personaje"
        verbose_name = "cuenta-personaje"
        verbose_name_plural = "cuentas-personajes"

    def __str__(self):
        return f"{self.cuenta} -> {self.personaje}"


class Categoria(models.Model):
    nombre = models.CharField(max_length=120)                 
    tipo = models.CharField(max_length=100, unique=True)     

    class Meta:
        db_table = "categoria"
        verbose_name = "categoría"
        verbose_name_plural = "categorías"

    def __str__(self):
        return self.nombre


class Item(models.Model):
    # adquiere: personaje 1 --- N item (CASCADE)
    personaje = models.ForeignKey(
        Personaje, on_delete=models.CASCADE, related_name="items"
    )
    # clasifica: categoria 1 --- N item (CASCADE)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name="items"
    )
    nombre = models.CharField(max_length=100)                                
    descripcion = models.TextField()                                         
    nivel = models.PositiveIntegerField(validators=[MinValueValidator(0)])  
    cantidad = models.IntegerField(default=1)                          

    class Meta:
        db_table = "item"
        verbose_name = "ítem"
        verbose_name_plural = "ítems"

    def __str__(self):
        return f"{self.nombre} ({self.categoria}) x{self.cantidad}"