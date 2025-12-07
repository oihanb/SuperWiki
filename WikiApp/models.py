from django.db import models

# Create your models here.
class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    anoFundacion = models.PositiveIntegerField()
    propietario= models.CharField(max_length=50)
    imagenEditorial = models.URLField(max_length=600, blank=True, null=True)
    

    def __str__(self):
        return self.nombre

class GrupoDeSuperHeroes(models.Model):
    nombre = models.CharField(max_length=100)
    Editorial = models.ForeignKey(Editorial,related_name='editorialGrupo', on_delete= models.CASCADE)
    SuperHeroe = models.ManyToManyField('SuperHeroe', related_name="superheroeGrupo")
    
   

    def __str__(self):
        return self.nombre

class SuperHeroe(models.Model):
    nombre = models.CharField(max_length=50)
    poderes = models.CharField(max_length=100)
    Fnacimiento= models.PositiveIntegerField()
    imagenSuperHeroe = models.URLField(max_length=200, blank=True, null=True)

 

    def __str__(self):
        return self.nombre
