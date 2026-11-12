# django_Orm_Mysql

Proyecto Django con una aplicación para listar, registrar, actualizar y eliminar
cuentas almacenadas en una base de datos MySQL.

## Requisitos

- Python 3.12
- MySQL Server
- Git 

## Instalación

Desde la carpeta raíz del repositorio, crea y activa un entorno virtual:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instala las dependencias:

```powershell
python -m pip install -r requirements.txt
```

## Configuración de MySQL

Inicia MySQL y crea una base de datos llamada `adso_django_Orm` (por ejemplo,
desde MySQL Workbench). La aplicación lee la conexión desde estas variables de
entorno; ajusta sus valores a tu instalación.

En PowerShell, antes de iniciar Django:

```powershell
$env:MYSQL_DATABASE = "adso_django_Orm"
$env:MYSQL_USER = "root"
$env:MYSQL_PASSWORD = "tu_contraseña_de_mysql"
$env:MYSQL_HOST = "localhost"
$env:MYSQL_PORT = "3306"
$env:DJANGO_SECRET_KEY = "una-clave-local-para-desarrollo"
```

Estas variables solo se conservan en la ventana actual de PowerShell. No pongas
contraseñas ni claves reales en archivos que vayas a subir al repositorio.
Si `MYSQL_PASSWORD` queda vacío, la configuración intentará conectarse sin
contraseña.

## Ejecutar

Con el entorno virtual activo y las variables configuradas, desde la raíz del
repositorio ejecuta:

```powershell
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
