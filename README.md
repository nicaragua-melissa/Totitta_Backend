# Tōtitta Backend

Es el proyecto backend que gestiona la lógica del servidor, la base de datos y exposición de Apis, del sistema web Tōtitta.
Permite a los usuarios explorar reservas naturales, guías certificados, actividades accesibles, catálogos de aves 
y realizar reservas seguras desde cualquier dispositivo, promoviendo el turismo sostenible en Nicaragua.

---
### Instalación y ejecución

1. **Clona el repositorio**
   git clone https://github.com/nicaragua-melissa/Totitta_Backend.git

2. **Crea un entorno virtual**
   python -m venv totitta
   
3. **Activa el entorno virtual**  
   .\totitta\Scripts\activate (en la consola de Windows)

4. **Instala dependencias**  
   pip install -r requirements.txt

5. **Aplica migraciones**  
   python manage.py migrate

6. **Ejecuta el servidor**  
   python manage.py runserver

Nota: Puedes revisar el /redoc para obtener todas las direcciones de las apis y poderlas consumir desde un software como Postman.
