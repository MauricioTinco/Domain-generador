from django.db import models

class Entidad(models.Model):
    id_entidad = models.CharField(max_length=7, primary_key=True)
    nombre = models.CharField(max_length=50)
    sigla = models.CharField(max_length=9)

    def __str__(self):
        return self.nombre

class Proyecto(models.Model):
    id_proyecto = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=50)
    fecha = models.DateField()
    id_entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Usuenti(models.Model):
    id_usuenti = models.CharField(max_length=7, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.DecimalField(max_digits=9, decimal_places=0)
    correo = models.CharField(max_length=30)
    area = models.CharField(max_length=30)
    cargo = models.CharField(max_length=30)
    id_entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    id_proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class UsuDomain(models.Model):
    id_usudomain = models.CharField(max_length=7, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.DecimalField(max_digits=9, decimal_places=0)
    cargo = models.CharField(max_length=30)
    area = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Seguimiento(models.Model):
    id_seguimiento = models.CharField(max_length=7, primary_key=True)
    id_proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    id_usudomain = models.ForeignKey(UsuDomain, on_delete=models.CASCADE)
    tipo_seguimiento = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.tipo_seguimiento} - {self.id_proyecto}'













