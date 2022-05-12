# SarquizWallet
Bitcoin Wallet


billetera digital para bitcoin, diseño de su interfaz con un usuario.
la Arquitectura de datos acopla las variables fundamentales en las fases de funciones, red, seguridad(...)

Ubuntu: 20.04,
Backend: Python 3.8.10,
Frontend: HTML, CSS, Javascript
Django: 3.2.9,
BDD: sqlite3,
bitcoin: 1.1.42

Para iniciar debes crear un Entorno Virtual:


activar el Entorno Virtual:

source myvenv/bin/activate
 
Descargar las Dependencias para el projecto:
pip3 install -r requirements.txt

Hacer Migraciones:
 1. python3 manage.py makemigrations
 2. python3 manage.py migrate
 3. python3 manage.py createsuperuser

Go...
python3 manage.py runserver


CHECK IN __OK__: Descargar las dependecias, migrar, interfaz
