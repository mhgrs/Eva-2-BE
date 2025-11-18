from django.db import models
from django.utils import timezone

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    descripcion = models.TextField(null=True, blank=True, verbose_name="Descripción")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    stock = models.IntegerField(verbose_name="Stock")
    categoria = models.CharField(max_length=50, verbose_name="Categoría")
    estado = models.CharField(max_length=20, default='Activo', verbose_name="Estado")
    observaciones = models.TextField(null=True, blank=True, verbose_name="Observaciones")
    proveedor = models.CharField(max_length=100, null=True, blank=True, verbose_name="Proveedor")
    sku = models.CharField(max_length=50,unique=True, null=True, blank=True, verbose_name="SKU")
    urlImagen = models.URLField(max_length=255, null=True, blank=True, verbose_name="URL Imagen" ) 
    marca = models.CharField(max_length=50, null=True, blank= True, verbose_name="Marca")
    destacado = models.BooleanField(default=False, verbose_name="Es destacado?")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

class Cliente(models.Model):
    TIPO_CLIENTE_CHOICES = [
        ('minorista', 'Minorista'),
        ('mayorista', 'Mayorista'),
        ('corporativo', 'Corporativo'),
    ]
    
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]

    idCliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre Completo")
    correo = models.EmailField(unique=True, max_length=100, verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=20, null=True, blank=True, verbose_name="Teléfono")
    direccion = models.CharField(max_length=255, null=True, blank=True, verbose_name="Dirección")
    ciudad = models.CharField(max_length=50, null=True, blank=True, verbose_name="Ciudad")
    pais = models.CharField(max_length=50, null=True, blank=True, verbose_name="País")
    fechaRegistro = models.DateField(default=timezone.now, verbose_name="Fecha de Registro")
    tipoCliente = models.CharField(max_length=20, choices=TIPO_CLIENTE_CHOICES, default='minorista', verbose_name="Tipo de Cliente")
    preferencias = models.TextField(null=True, blank=True, verbose_name="Preferencias")
    fechaNacimiento = models.DateField(null=True, blank=True, verbose_name="Fecha de Nacimiento")
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES, null=True, blank=True, verbose_name="Género")
    rut =  models.CharField(max_length=20, unique=True, blank= True, null=True, verbose_name= "RUT")
    activo = models.BooleanField(default=False, verbose_name="Esta activo?")
    razonSocial = models.CharField(max_length=50, null=True, blank=True, verbose_name="Razon social")
    ultimaCompra = models.DateField(null=True, blank=True, verbose_name="Fecha Última Compra")

    def __str__(self):
        return f"{self.nombre} ({self.correo})"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"