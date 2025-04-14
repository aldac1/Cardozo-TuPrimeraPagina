# Proyecto Django - Tienda de Ropa (Alda Cardozo)

## Descripción
Aplicación web que permite gestionar clientes y prendas de ropa.

## Requisitos
- Python >=3.9
- Django >=4

## Inicialización
Obtener e ingresar al proyecto:
```bash
git clone repositorio
cd tienda_ropa
```

Aplicar migraciones para generar una base de datos local:
```bash
python manage.py makemigrations
python manage.py migrate
```

Ejecutar el servidor localmente y acceder a `http://localhost:8000`
```bash
python manage.py runserver
```

## Funcionalidades
1. Alta, Baja, Modificación:
   1. CLientes
   2. Ropa
2. Vista de listado de ropa.
3. Vista de listado de clientes.

## Orden para probar
1. Ir a la sección clientes.
   1. Crear nuevo cliente
      1. (opcional) Editar cliente
      2. (opcional) Borrar cliente
2. Ir a la sección Ropa
   1. Crear nueva ropa
      1. (opcional) Editar ropa
      2. (opcional) Borrar ropa
3. Volver al inicio por medio del navbar.
