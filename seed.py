"""
Script de datos semilla (seed) para poblar la base de datos con registros de prueba.
Ejecutar con: python manage.py shell < seed.py
  o con:      python seed.py  (si se configura Django previamente)
"""

import os
import django
from decimal import Decimal
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from tickets.models import Usuario, Alojamiento, ImagenAlojamiento, Reserva, Pago, Resena

print("Iniciando carga de datos semilla...")

# ---------- Usuarios ----------
usuarios_data = [
    {'nombre': 'Ana García',     'email': 'ana@example.com',     'password': 'hashed_pw_1', 'rol': 'anfitrion'},
    {'nombre': 'Luis Martínez',  'email': 'luis@example.com',    'password': 'hashed_pw_2', 'rol': 'anfitrion'},
    {'nombre': 'María López',    'email': 'maria@example.com',   'password': 'hashed_pw_3', 'rol': 'huesped'},
    {'nombre': 'Carlos Pérez',   'email': 'carlos@example.com',  'password': 'hashed_pw_4', 'rol': 'huesped'},
    {'nombre': 'Sofía Rodríguez','email': 'sofia@example.com',   'password': 'hashed_pw_5', 'rol': 'huesped'},
    {'nombre': 'Admin Sistema',  'email': 'admin@example.com',   'password': 'hashed_pw_6', 'rol': 'admin'},
]

usuarios = []
for data in usuarios_data:
    obj, created = Usuario.objects.get_or_create(email=data['email'], defaults=data)
    usuarios.append(obj)
    print(f"  {' Creado' if created else '  Ya existe'}: Usuario {obj.nombre}")

anfitrion1, anfitrion2 = usuarios[0], usuarios[1]
huesped1, huesped2, huesped3 = usuarios[2], usuarios[3], usuarios[4]

# ---------- Alojamientos ----------
alojamientos_data = [
    {'titulo': 'Cabaña en el bosque', 'descripcion': 'Hermosa cabaña rodeada de naturaleza, ideal para descansar.', 'ubicacion': 'San Bernardino, Paraguay', 'precio': Decimal('150000.00'), 'anfitrion': anfitrion1},
    {'titulo': 'Apartamento céntrico', 'descripcion': 'Moderno apartamento en el centro de Asunción con todas las comodidades.', 'ubicacion': 'Asunción, Paraguay', 'precio': Decimal('200000.00'), 'anfitrion': anfitrion1},
    {'titulo': 'Casa de playa', 'descripcion': 'Casa frente al río con acceso directo a la playa privada.', 'ubicacion': 'Encarnación, Paraguay', 'precio': Decimal('250000.00'), 'anfitrion': anfitrion2},
    {'titulo': 'Loft moderno', 'descripcion': 'Loft de diseño con vista panorámica a la ciudad.', 'ubicacion': 'Lambaré, Paraguay', 'precio': Decimal('180000.00'), 'anfitrion': anfitrion2},
    {'titulo': 'Estancia rural', 'descripcion': 'Amplia estancia con pileta, canchas y actividades rurales.', 'ubicacion': 'Villarrica, Paraguay', 'precio': Decimal('300000.00'), 'anfitrion': anfitrion1},
]

alojamientos = []
for data in alojamientos_data:
    obj, created = Alojamiento.objects.get_or_create(titulo=data['titulo'], defaults=data)
    alojamientos.append(obj)
    print(f"  {'Creado' if created else ' Ya existe'}: Alojamiento {obj.titulo}")

# ---------- Imágenes de Alojamiento ----------
imagenes_data = [
    {'url_imagen': 'https://example.com/img/cabana1.jpg',     'alojamiento': alojamientos[0]},
    {'url_imagen': 'https://example.com/img/cabana2.jpg',     'alojamiento': alojamientos[0]},
    {'url_imagen': 'https://example.com/img/apto1.jpg',       'alojamiento': alojamientos[1]},
    {'url_imagen': 'https://example.com/img/playa1.jpg',      'alojamiento': alojamientos[2]},
    {'url_imagen': 'https://example.com/img/loft1.jpg',       'alojamiento': alojamientos[3]},
    {'url_imagen': 'https://example.com/img/estancia1.jpg',   'alojamiento': alojamientos[4]},
]

for data in imagenes_data:
    obj, created = ImagenAlojamiento.objects.get_or_create(url_imagen=data['url_imagen'], defaults=data)
    print(f"  {' Creado' if created else ' Ya existe'}: Imagen {obj.url_imagen}")

# ---------- Reservas ----------
reservas_data = [
    {'fecha_inicio': date(2026, 6, 1),  'fecha_fin': date(2026, 6, 5),  'precio_total': Decimal('600000.00'), 'estado': 'confirmada',  'usuario': huesped1, 'alojamiento': alojamientos[0]},
    {'fecha_inicio': date(2026, 6, 10), 'fecha_fin': date(2026, 6, 12), 'precio_total': Decimal('400000.00'), 'estado': 'pendiente',   'usuario': huesped2, 'alojamiento': alojamientos[1]},
    {'fecha_inicio': date(2026, 7, 1),  'fecha_fin': date(2026, 7, 7),  'precio_total': Decimal('1750000.00'),'estado': 'confirmada',  'usuario': huesped3, 'alojamiento': alojamientos[2]},
    {'fecha_inicio': date(2026, 7, 15), 'fecha_fin': date(2026, 7, 18), 'precio_total': Decimal('540000.00'), 'estado': 'cancelada',   'usuario': huesped1, 'alojamiento': alojamientos[3]},
    {'fecha_inicio': date(2026, 8, 5),  'fecha_fin': date(2026, 8, 10), 'precio_total': Decimal('1500000.00'),'estado': 'completada',  'usuario': huesped2, 'alojamiento': alojamientos[4]},
]

reservas = []
for data in reservas_data:
    obj, created = Reserva.objects.get_or_create(
        usuario=data['usuario'],
        alojamiento=data['alojamiento'],
        fecha_inicio=data['fecha_inicio'],
        defaults=data
    )
    reservas.append(obj)
    print(f"  {' Creado' if created else ' Ya existe'}: Reserva #{obj.id}")

# ---------- Pagos ----------
pagos_data = [
    {'monto': Decimal('600000.00'),  'estado': 'completado', 'reserva': reservas[0]},
    {'monto': Decimal('400000.00'),  'estado': 'pendiente',  'reserva': reservas[1]},
    {'monto': Decimal('1750000.00'), 'estado': 'completado', 'reserva': reservas[2]},
    {'monto': Decimal('540000.00'),  'estado': 'reembolsado','reserva': reservas[3]},
    {'monto': Decimal('1500000.00'), 'estado': 'completado', 'reserva': reservas[4]},
]

for data in pagos_data:
    obj, created = Pago.objects.get_or_create(reserva=data['reserva'], defaults=data)
    print(f"  {' Creado' if created else' Ya existe'}: Pago #{obj.id} - ${obj.monto}")

# ---------- Reseñas ----------
resenas_data = [
    {'calificacion': 5, 'comentario': 'Excelente lugar, muy tranquilo y limpio. Volvería sin dudarlo.', 'usuario': huesped1, 'alojamiento': alojamientos[0]},
    {'calificacion': 4, 'comentario': 'Muy buena ubicación, el apartamento estaba bien equipado.', 'usuario': huesped2, 'alojamiento': alojamientos[1]},
    {'calificacion': 5, 'comentario': 'La casa de playa es increíble. El anfitrión muy amable.', 'usuario': huesped3, 'alojamiento': alojamientos[2]},
    {'calificacion': 3, 'comentario': 'Bien en general, pero el loft necesita mejor mantenimiento.', 'usuario': huesped1, 'alojamiento': alojamientos[3]},
    {'calificacion': 5, 'comentario': 'La estancia superó todas nuestras expectativas. 100% recomendado.', 'usuario': huesped2, 'alojamiento': alojamientos[4]},
]

for data in resenas_data:
    obj, created = Resena.objects.get_or_create(
        usuario=data['usuario'],
        alojamiento=data['alojamiento'],
        defaults=data
    )
    print(f"  {' Creado' if created else ' Ya existe'}: Reseña de {obj.usuario.nombre} - {obj.calificacion}★")

print("\n Seed completado exitosamente.")
