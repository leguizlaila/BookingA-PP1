from django.db import models


class Usuario(models.Model):
    ROL_CHOICES = [
        ('huesped', 'Huésped'),
        ('anfitrion', 'Anfitrión'),
        ('admin', 'Admin'),
    ]

    nombre = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, default='huesped')
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'{self.nombre} ({self.email})'


class Alojamiento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    anfitrion = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='alojamientos'
    )
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Alojamiento'
        verbose_name_plural = 'Alojamientos'

    def __str__(self):
        return self.titulo


class ImagenAlojamiento(models.Model):
    url_imagen = models.CharField(max_length=500)
    alojamiento = models.ForeignKey(
        Alojamiento,
        on_delete=models.CASCADE,
        related_name='imagenes'
    )

    class Meta:
        verbose_name = 'Imagen de Alojamiento'
        verbose_name_plural = 'Imágenes de Alojamiento'

    def __str__(self):
        return f'Imagen de {self.alojamiento.titulo}'


class Reserva(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
        ('completada', 'Completada'),
    ]

    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='reservas'
    )
    alojamiento = models.ForeignKey(
        Alojamiento,
        on_delete=models.CASCADE,
        related_name='reservas'
    )
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def __str__(self):
        return f'Reserva #{self.id} - {self.alojamiento.titulo}'


class Pago(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('completado', 'Completado'),
        ('fallido', 'Fallido'),
        ('reembolsado', 'Reembolsado'),
    ]

    monto = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    reserva = models.ForeignKey(
        Reserva,
        on_delete=models.CASCADE,
        related_name='pagos'
    )
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'

    def __str__(self):
        return f'Pago #{self.id} - ${self.monto}'


class Resena(models.Model):
    calificacion = models.IntegerField()  # 1 a 5
    comentario = models.TextField()
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='resenas'
    )
    alojamiento = models.ForeignKey(
        Alojamiento,
        on_delete=models.CASCADE,
        related_name='resenas'
    )
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Reseña'
        verbose_name_plural = 'Reseñas'

    def __str__(self):
        return f'Reseña de {self.usuario.nombre} - {self.calificacion}★'
