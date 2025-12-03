from django.db import models

# Create your models here.
class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    anoFundacion = models.PositiveIntegerField()
    propietario= models.CharField(max_length=20)
    foto = models.URLField(max_length=200, blank=True, null=True)
    
    class Meta:
        verbose_name="Editorial"
        verbose_name_plural= "Editoriales"

    def __str__(self):
        return self.nombre

class GrupoDeSuperHeroes(models.Model):
    nombre = models.CharField(max_length=100)
    Editorial = models.ForeignKey(Editorial,related_name='editorialGrupo', on_delete= models.CASCADE)
    SuperHeroe = models.ManyToManyField('SuperHeroe', related_name="superheroeGrupo")
    
    class Meta:
        verbose_name="Grupo de Superheroes"
        verbose_name_plural= "Grupos de Superheroes"

    def __str__(self):
        return self.nombre

class SuperHeroe(models.Model):
    nombre = models.CharField(max_length=100)
    poderes = models.CharField(max_length=100)
    Fnacimiento= models.PositiveIntegerField()
    foto = models.URLField(max_length=200, blank=True, null=True)

    class Meta: #Para visualizat el nombre en singular y plural del modelo en ADMIN
        verbose_name = "Superhéroe"
        verbose_name_plural = "Superhéroes"

    def __str__(self):
        return self.nombre
