from django.contrib import admin
from .models import Usuario, Alojamiento, ImagenAlojamiento, Reserva, Pago, Resena


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'rol', 'creado_en')
    list_filter = ('rol',)
    search_fields = ('nombre', 'email')


@admin.register(Alojamiento)
class AlojamientoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ubicacion', 'precio', 'anfitrion', 'creado_en')
    list_filter = ('ubicacion',)
    search_fields = ('titulo', 'ubicacion')


@admin.register(ImagenAlojamiento)
class ImagenAlojamientoAdmin(admin.ModelAdmin):
    list_display = ('alojamiento', 'url_imagen')
    search_fields = ('alojamiento__titulo',)


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('id', 'alojamiento', 'usuario', 'fecha_inicio', 'fecha_fin', 'estado', 'precio_total')
    list_filter = ('estado',)
    search_fields = ('alojamiento__titulo', 'usuario__nombre')


@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('id', 'reserva', 'monto', 'estado', 'creado_en')
    list_filter = ('estado',)
    search_fields = ('reserva__id',)


@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'alojamiento', 'calificacion', 'creado_en')
    list_filter = ('calificacion',)
    search_fields = ('usuario__nombre', 'alojamiento__titulo')
