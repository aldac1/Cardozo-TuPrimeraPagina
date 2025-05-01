# Proyecto Django - Tienda de Ropa (Alda Cardozo)

## Descripción
Aplicación web que permite gestionar prendas de ropa.

## Requisitos
- Python >=3.9
- Django >=4

## Inicialización
Obtener e ingresar al proyecto:
```bash
git clone `https://github.com/aldac1/Cardozo-TuPrimeraPagina.git`
cd tienda_ropa
```

Instalar dependencias a través del requirements.txt
```bash
pip install -r requirements.txt
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
   1. Prenda de ropa.
2. Vista de listado de ropa.
3. Gestión de clientes a través de:
   1. Registro de nuevo usuario.
   2. Detalle de perfil del usuario.
   3. Edición del perfil del usuario.
4. Acceso al administrador de Django. Vista de:
   1. Ropa
   2. Cliente


## Orden para probar
1. Registrarse a través del boton "Registrarse"
2. Iniciar sesión con los datos registrados.
1. Ir a la sección del perfil.
   1. Completar datos.
   2. (opcional) Modificar los datos.
2. Ir a la sección "listado de productos" en la barra de navegacion
   1. Agregar nueva prenda
   2. Listar las prendas disponibles.
      1. (opcional) Editar prenda.
      2. (opcional) Borrar prenda.
3. Volver al inicio/home por medio de la barra de navegación.
4. Cerrar sesion.
