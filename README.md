# django_Orm_Mysql

Proyecto Django con una aplicación para listar, registrar, actualizar y eliminar
cuentas almacenadas en una base de datos MySQL.

## Requisitos

- Python 3.12
- Mysql
- Git 

## Instalación

Desde la carpeta raíz del repositorio, crea y activa un entorno virtual:

```
py -3.12 -m env .venv
.\.venv\Scripts\Activate.ps1
```

Instala las dependencias:

```
python -m pip install -r requirements.txt
```

## Configuración de MySQL

Inicia MySQL y crea una base de datos llamada `adso_django_Orm` (por ejemplo,
desde DBeaver). La aplicación lee la conexión desde estas variables de
entorno; ajusta sus valores a tu instalación.



## Ejecutar

Con el entorno virtual activo y las variables configuradas, desde la raíz del
repositorio ejecuta:

```
cd .\proyecto
python manage.py migrate
python manage.py runserver
```

Abre <http://127.0.0.1:8000/cuentas/> para ver las cuentas. El servidor de
desarrollo se detiene con `Ctrl+C`.

## Estructura principal

```text
proyecto/
  Banco/       Aplicación, modelo, vistas, rutas y plantillas
  proyecto/    Configuración y rutas principales de Django
  static/      Archivos CSS
  manage.py
requirements.txt
```
