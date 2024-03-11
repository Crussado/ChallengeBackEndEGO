# ChallengeBackEndEGO
Repositorio prueba técnica para el puesto de Backend Python/Django de EGO.
# Uso e Instalacion
Pasos:
- Clonar el repositorio
- (Opcional pero recomendado):
*`virtualenv -p=python3.7 ENV`
*`source ENV/bin/activate`
- `cd ChallengeBackEndEGO`
- Instalar los requerimientos: `pip install -r requirements.txt`
- Habilitar el servidor `python back/manage.py runserver`

Desde `localhost:8000/admin` obtenemos el admin para administrar la base de datos. Es posible loguearse utilizando `admin` como usuario y contraseña.

Desde `localhost:8000/swagger/` o `localhost:8000/redoc/` se obtiene una documentacion sobre las apis habilitadas.

Ejecutando `python back/manage.py test` se corren los unit tests.
# EER
Diagrama entidad relacion echo con MySQL Workbench.

![image](https://github.com/Crussado/ChallengeBackEndEGO/assets/64971042/61724ddb-b33a-4043-9ac2-515024769092)

Dadas las pantallas del FrontEnd asi fue como plantie el diseño de la base de datos.

Con mas informacion es posible realizar un diagrama muy distinto, por ejemplo:
- Manejar las ventas, y reviews de usuarios.
- Los productos y servicios esten asociados a partes o modelos.
- Hacer familia de partes con cada una sus caracteristicas (Motor, Suspension, Transmicion, etc).
