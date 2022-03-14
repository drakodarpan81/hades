from django.db import models
from datetime import datetime


class Tipo(models.Model):
    name = models.CharField(verbose_name="Nombre del tipo:", max_length=50)

    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"
        db_table = 'tipo'
        ordering = ['id']

    def __str__(self):
        return self.name


"""
    def get_absolute_url(self):
        return reverse("Type_detail", kwargs={"pk": self.pk})
"""


class Categoria(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name


class Empleado(models.Model):

    names = models.CharField(max_length=150, verbose_name='Nombres')
    dni = models.CharField(max_length=10, verbose_name='DNI', unique=True)
    date_joined = models.DateField(
        verbose_name="Fecha de registro", default=datetime.now)
    date_created = models.DateTimeField(
        verbose_name="Fecha de registro", default=datetime.now)
    # auto_now => Solo cuando se registra la primera vez, tendra valor y no se movera
    date_created = models.DateTimeField(auto_now=True)
    # auto_now_add => Se va a estar modificando el valor, cada que se modifica el campo
    date_created = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0, verbose_name="Edad")
    salario = models.DecimalField(max_digits=9, decimal_places=2)
    sate = models.BooleanField(default=True)
    # sexo = models.CharField(max_length=50, verbose_name="Sexo")
    avatar = models.ImageField(upload_to='avatar', null=True, blank=True)
    cv = models.FileField(upload_to='cv', null=True, blank=True)

    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    categoria = models.ManyToManyField(Categoria)

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        db_table = 'empleado'
        ordering = ['id']

    def __str__(self):
        return self.names


"""
    def get_absolute_url(self):
        return reverse("Empleado_detail", kwargs={"pk": self.pk})
"""
