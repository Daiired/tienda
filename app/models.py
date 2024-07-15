from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    nuevo = models.BooleanField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    fecha_fabricacion = models.DateField()
    imagen = models.ImageField(upload_to="productos", null=True)
    def __str__(self):
        return self.nombre
    

opciones_consultas = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"]
]


class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta= models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre
    




#tablas tienda proyecto






class CategoriaAlimento(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Alimento(models.Model):
    nombre_alimento = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=1000)
    precio = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='alimentos/')
    cantidad = models.PositiveIntegerField()
    proteinas = models.FloatField(max_length=3, null =True)
    carbohidratos = models.FloatField(max_length=3, null =True)
    grasas = models.FloatField(max_length=3, null =True)
    energia = models.FloatField(max_length=3, null =True)
    id_categoria = models.ForeignKey(CategoriaAlimento, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre_alimento
    



class LibreDeAlimento(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Dieta(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class AlimentoLibreDe(models.Model):
    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE)
    id_libre = models.ForeignKey(LibreDeAlimento, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('alimento', 'id_libre')

    def __str__(self):
        return f'{self.alimento} - {self.id_libre}'

class AlimentoDieta(models.Model):
    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE)
    id_dieta = models.ForeignKey(Dieta, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('alimento', 'id_dieta')

    def __str__(self):
        return f'{self.alimento} - {self.id_dieta}'