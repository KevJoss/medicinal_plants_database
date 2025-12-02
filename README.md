# Sistema de base de datos para plantas medicinales de la provincia de Imbabura

Este proyecto es una Base de datos de plantas medicinales de la provincia de Imbabura. Contiene por momento una API diseñada para crear, gestionar y administrar las tablas de una base de datos relacional SQL. Ademas,hace uso de  un archivo .ipynb para limpiar e insertar los datos obtenidos del .xlsx  para ser insertados en el modelo  SQL.

---

## Características

- **Creacion de tablas**:   La API tiene la capacidad de crear instantaneamente las tablas de la estrucctura relacional.
- **Insertar datos del .xlsx**: El archivo Data_cleaning insertar la informacíon del archivo excel a la estrucctura de la base de datos.
- **Insertar nuevos registros**: Los usuarios pueden insertar a travez de la API nuevos registros de las plantas y asi mismo informacion relacionada a ellas como entrevistas.
- **Modificacion de datos**: Los usuarios pueden modificar y actualizar los datos  de un registro en especifico usando la API.
- **Joins entre tablas**: Los usuarios pueden realizar consultas del tipo join entre dos tablas, ademas de un join entre 3 tablas usando la API.
- **Modelo grafico del modelo**: El desarrollador podrá ver el modelo implementado a travez del archivo LOGICAL_DESIGN_PLANTS.architect

---

## Estructura de la Base de Datos

El sistema utiliza una base de datos relacional con las siguientes tablas principales:

- **PLANTS**: Detalla el nombre común y nombre científico.
- **LOCATIONS**: Registra el nombre del canton y provincia. 
- **PLANTS_LOCATIONS**: Registra el id unico de la tabla PLANTS y LOCATIONS (Es una tabla intermedia).
- **Images**: Contiene los registros de las imagenes asociadas a las plantas y al lugar de investigación, ademas de su fecha, lugar donde se tomó la foto y el link de la foto.
- **Previous_researches**: Refiere a las investigaciones previas realizadas a una planta específica en un lugar específico, ademas incluye la información sobre el título de la investigación (En el caso de que tuviere) y el link asociado.
- **Uses**: Describe el uso que se le da a una planta en un lugar de investigación específico, asi como el tipo de uso que es.
- **Toponimos**: Relaciona una planta y un lugar de investigación a travez del lugar de origen, distribucion y distribucion comercial. 
- **Interview_customers**: Refiere a las entrevistas a consumidores relacionadas a donde se realizó la investigacion, contiene un link a la entrevista digital y las pregunas asociadas.
- **Interview_vendors**: Refiere a las entrevistas a vendedores relacionadas a donde se realizó la investigacion, contiene un link a la entrevista digital y las pregunas asociadas.
---

## Esquema de la base de datos

### Tabla: plants

| **Field**       | **Type**     |**Null** | **Key** | **Default** | **Extra**      |
|-----------------|--------------|---------|---------|-------------|----------------|
| id_plant_pk     | int          | NO      | PRI     | NULL        | auto_increment |
| current_name    | varchar(100) | NO      |         | NULL        |                |
| scientific_name | varchar(100) | NO      |         | NULL        |                |



---

### Tabla: locations


| **Field**      | **Type**     | **Null** | **Key** | **Default** | **Extra**      |
|----------------|--------------|----------|---------|-------------|----------------|
| id_location_pk | int          | NO       | PRI     | NULL        | auto_increment |
| city_name      | varchar(100) | NO       |         | NULL        |                |
| province_name  | varchar(100) | NO       |         | NULL        |                |

---

### Tabla: plants_locations

| **Field**      | **Type**     | **Null** | **Key** | **Default** | **Extra**       |
|----------------|--------------|----------|---------|-------------|-----------------|
| id_plant_pk    | int          | NO       | PRI     | NULL        |                 |
| id_location_pk | int          | NO       | PRI     | NULL        |                 |


---

### Tabla: images

| **Field**      | **Type**     | **Null** | **Key** | **Default** | **Extra**       |
|----------------|--------------|----------|---------|-------------|-----------------|
| id_image_pk    | int          | NO       | PRI     | NULL        |                 |
| id_plant_pk    | int          | NO       | PRI     | NULL        |                 |
| id_location_pk | int          | NO       | PRI     | NULL        |                 |
| link           | text         | NO       |         | NULL        |                 |
| date           | date         | NO       |         | NULL        |                 |
| place          | varchar(100) | NO       |         | NULL        |                 |

---

### Tabla: uses

| **Field**      | **Type**     | **Null** | **Key** | **Default** | **Extra**      |
|----------------|--------------|----------|---------|-------------|----------------|
| id_use_pk      | int          | NO       | PRI     | NULL        |                |
| id_plant_pk    | int          | NO       | PRI     | NULL        |                |
| id_location_pk | int          | NO       | PRI     | NULL        |                |
| description    | text         | NO       |         | NULL        |                |
| type_use       | varchar(200) | NO       |         | NULL        |                |



---

### Tabla: previous_researchs

| **Field**      | **Type**     |**Null** | **Key** | **Default** | **Extra**      |
|----------------|--------------|---------|---------|-------------|----------------|
| id_research_pk | int          | NO      | PRI     | NULL        |                |
| id_plant_pk    | int          | NO      | PRI     | NULL        |                |
| id_location_pk | int          | NO      | PRI     | NULL        |                |
| title          | varchar(255) | NO      |         | NULL        |                |
| link           | text         | YES     |         | NULL        |                |




### Tabla: toponimos

| **Field**               | **Type**     | **Null** | **Key** | **Default** | **Extra**      |
|-------------------------|--------------|----------|---------|-------------|----------------|
| id_toponimo_pk          | int          | NO       | PRI     | NULL        |                |
| id_plant_pk             | int          | NO       | PRI     | NULL        |                |
| id_location_pk          | int          | NO       | PRI     | NULL        |                |
| origin                  | text         | YES      |         | NULL        |                |
| commercial_distribution | varchar(400) | YES      |         | NULL        |                |
| distribution            | varchar(400) | YES      |         | NULL        |                |


---

### Tabla: interview_customers

| **Field**                  |  **Type**    | **Null**     | **Key** | **Default** | **Extra**      |
|----------------------------|--------------|--------------|---------|-------------|----------------|
| id_interviews_customer_pk  | int          | NO           | PRI     | NULL        |                |
| id_location_pk             | int          | NO           | PRI     | NULL        |                |
| link                       | varchar(500) | NO           |         | NULL        |                |
| q1                         | varchar(255) | YES          |         | NULL        |                |
| q2                         | varchar(255) | YES          |         | NUL         |                |
| q3                         | varchar(255) | YES          |         | NULL        |                |
| q4                         | varchar(255) | YES          |         | NULL        |                |
| q5                         | varchar(255) | YES          |         | NULL        |                |
| q6                         | varchar(255) | YES          |         | NULL        |                |
| q7                         | varchar(255) | YES          |         | NULL        |                |
| q8                         | varchar(255) | YES          |         | NULL        |                |
| q9                         | varchar(255) | YES          |         | NULL        |                |
| q10                        | varchar(255) | YES          |         | NULL        |                |
| q11                        | varchar(255) | YES          |         | NULL        |                |
| q12                        | varchar(255) | YES          |         | NULL        |                |
| q13                        | varchar(255) | YES          |         | NULL        |                |
| q14                        | varchar(255) | YES          |         | NULL        |                |
| q15                        | varchar(255) | YES          |         | NULL        |                |
| q16                        | varchar(255) | YES          |         | NULL        |                |
| q17                        | varchar(255) | YES          |         | NULL        |                |
| q18                        | varchar(255) | YES          |         | NULL        |                |
| q19                        | varchar(255) | YES          |         | NULL        |                |
| q20                        | varchar(255) | YES          |         | NULL        |                |
| q21                        | varchar(255) | YES          |         | NULL        |                |
| q22                        | varchar(255) | YES          |         | NULL        |                |
| q23                        | varchar(255) | YES          |         | NULL        |                |
| q24                        | varchar(255) | YES          |         | NULL        |                |

---
### Tabla: Interview_vendors

| **Field**               | **Type**     | **Null** | **Key** | **Default** | **Extra**      |
|-------------------------|--------------|----------|---------|-------------|----------------|
| id_interviews_vendor_pk | int          | NO       | PRI     | NULL        |                |
| id_location_pk          | int          | NO       | PRI     | NULL        |                |
| link                    | varchar(500) | NO       |         | NULL        |                |
| q1                      | varchar(255) | YES      |         | NULL        |                |
| q2                      | varchar(255) | YES      |         | NULL        |                |
| q3                      | varchar(255) | YES      |         | NULL        |                |
| q4                      | varchar(255) | YES      |         | NULL        |                |
| q5                      | varchar(255) | YES      |         | NULL        |                |
| q6                      | varchar(255) | YES      |         | NULL        |                |
| q7                      | varchar(255) | YES      |         | NULL        |                |
| q8                      | varchar(255) | YES      |         | NULL        |                |
| q9                      | varchar(255) | YES      |         | NULL        |                |
| q10                     | varchar(255) | YES      |         | NULL        |                |
| q11                     | varchar(255) | YES      |         | NULL        |                |
| q12                     | varchar(255) | YES      |         | NULL        |                |
| q13                     | varchar(255) | YES      |         | NULL        |                |
| q14                     | varchar(255) | YES      |         | NULL        |                |
| q15                     | varchar(255) | YES      |         | NULL        |                |
| q16                     | varchar(255) | YES      |         | NULL        |                |
| q17                     | varchar(255) | YES      |         | NULL        |                |
| q18                     | varchar(255) | YES      |         | NULL        |                |
| q19                     | varchar(255) | YES      |         | NULL        |                |
| q20                     | varchar(255) | YES      |         | NULL        |                |
| q21                     | varchar(255) | YES      |         | NULL        |                |
| q22                     | varchar(255) | YES      |         | NULL        |                |
| q23                     | varchar(255) | YES      |         | NULL        |                |


---

## Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/aldrinchp/Medicinal-plants-proyect.git
   ```

2. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar la base de datos en docker**:
Este proyecto utiliza un contenedor Docker para MySQL con persistencia de datos mediante volúmenes.
-Crear y levantar el contenedor
```bash
docker run -d \
  --name mysql \
  -e MYSQL_ROOT_PASSWORD=123456789 \
  -p 3306:3306 \
  -v mysql_data:/var/lib/mysql \
  mysql:latest
```
- Iniciar el contenedor si no está instanciado.
```bash
docker start mysql
```
-Ejecutar el contenedor
```bash
docker exec -it mysql mysql -u root -p
```
-Crear la base de datos en el contenedor
```bash
CREATE DATABASE Medicinal_plants_proyect;
```
Notas:
-Asegúrate de tener creado un tabla llamada Medicinal_plants_proyect en una instancia de MySQL.
- Actualiza la configuración de la base de datos en el archivo `config.py` con tus credenciales de MySQL (En caso de cambiar las contraseña propuesta).

8. **Ejecutar la aplicación**:
   ```bash
   tu_directorio/app.py
   ```

---

## Uso

Una vez que la aplicación esté en funcionamiento, puedes interactuar con la API utilizando herramientas como [Postman](https://www.postman.com/) o [cURL](https://curl.se/).

### Endpoints Principales (En correción debido a cambios)

#### Plants

- `POST /plants`: Crea una nuevo registro de una planta.
- `DELETE /plants/<id>`: Elimina un registro de una planta.
- `GET /plants/all_plants`: Obtiene la lista de todos las plantas registradas.
- `GET /plants/<id>`: Obtiene información de una planta específica.
- `PUT /plants/<id>`: Actualiza información de una planta.


#### Locations

- `POST /locations`: Crea un nuevo registro de un sitio.
- `DELETE /locations/<id>`: Elimina un registro de un sitio.
- `GET /locations/all_locations`: Obtiene la lista de todos los sitios.
- `GET /locations/<id>`: Obtiene información de un sitio específico.
- `PUT /locations/<id>`: Actualiza información de un sitio.

#### Images

- `POST /images`: Crea un nuevo registro de imagen.
- `DELETE /images/<id>`: Elimina un registro de imagen.
- `GET /images/all_images`: Obtiene la lista de todos los sitios.
- `GET /images/<id>`: Obtiene información de un sitio específico.
- `PUT /images/<id>`: Actualiza información de un sitio.
---
Los queries para las demas tablas pueden ser inferidos a partir de las inferencias anteriores.

## Contacto

Cualquier duda, puedes contactarme:

- **Nombre**: [Aldrin](https://github.com/aldrinchp)

- **Correo**: aldrinchp@gmail.com
