# Sistema de Base de Datos de Plantas Medicinales (Imbabura)

Este repositorio contiene un sistema integral para la gestión, administración y consulta de una base de datos de plantas medicinales de la provincia de Imbabura, Ecuador. El proyecto incluye una API RESTful construida con Flask, una interfaz web básica, scripts de limpieza de datos y una base de datos relacional contenerizada en Docker.

## 📋 Características

  - **API RESTful**: Endpoints para crear, leer, actualizar y eliminar (CRUD) registros de plantas, ubicaciones, usos, imágenes e investigaciones.
  - **Interfaz Web**: Vistas HTML (`create_plant.html`, `plant_list.html`, etc.) para interactuar visualmente con el sistema.
  - **Gestión de Base de Datos**:
      - Creación automática de tablas relacionales.
      - Soporte para consultas complejas (Joins) entre tablas.
  - **Procesamiento de Datos**: Scripts en Jupyter Notebook (`Data_cleaning`) para limpiar e importar datos masivos desde archivos Excel (`.xlsx`) y CSV.
  - **Entorno Dockerizado**: Configuración lista para usar con Docker Compose para la base de datos MySQL.

## 🛠️ Tecnologías Utilizadas

  - **Lenguaje**: Python 3.x
  - **Backend**: Flask, Flask-SQLAlchemy
  - **Base de Datos**: MySQL 8.0
  - **Contenedores**: Docker & Docker Compose
  - **Ciencia de Datos**: Pandas, Jupyter Notebooks (para limpieza de datos)
  - **Frontend**: HTML5, CSS3

## 📂 Estructura del Proyecto

  - `Back and front/`: Contiene el código fuente de la aplicación Flask, modelos, rutas y plantillas HTML.
  - `Data_cleaning/`: Contiene los notebooks (`.ipynb`) y archivos CSV para la limpieza y transformación de los datos crudos recolectados.
  - `.vscode/`: Configuraciones del editor.

## 🚀 Instalación y Configuración

Sigue estos pasos para configurar el entorno de desarrollo localmente.

### 1\. Clonar el repositorio

```bash
git clone <URL_DE_TU_REPOSITORIO>
cd <NOMBRE_DE_LA_CARPETA>
```

### 2\. Crear un entorno virtual (Opcional pero recomendado)

```bash
python -m venv venv
# En Windows
venv\Scripts\activate
# En Linux/Mac
source venv/bin/activate
```

### 3\. Instalar dependencias

Instala las librerías necesarias listadas en `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4\. Configurar la Base de Datos con Docker

El proyecto utiliza Docker Compose para levantar una instancia de MySQL con persistencia de datos.

**Levantar la base de datos:**
Asegúrate de estar en el directorio donde se encuentra el archivo `docker-compose.yml` (o ejecuta apuntando al archivo):

```bash
cd "Back and front"
docker-compose up -d
```

> **Nota:** Esto levantará un contenedor llamado `medicinal_plants_mysql` en el puerto `3306` con la base de datos `Medicinal_plants_project` y contraseña `1234` (según tu `docker-compose.yml`).

### 5\. Ejecutar la Aplicación

Una vez que la base de datos esté activa, puedes iniciar la aplicación Flask. Esto también creará las tablas automáticamente si no existen.

```bash
# Estando en la carpeta "Back and front"
python app.py
```

La aplicación estará disponible en `http://127.0.0.1:5000`.

## 📖 Uso de la API

Puedes interactuar con la API utilizando herramientas como Postman o cURL. A continuación, los endpoints principales:

### Plantas (`/plants`)

  - `GET /plants/all_plants`: Obtener todas las plantas.
  - `POST /plants`: Crear un nuevo registro de planta.
  - `GET /plants/<id>`: Obtener detalles de una planta específica.
  - `PUT /plants/<id>`: Actualizar una planta.
  - `DELETE /plants/<id>`: Eliminar una planta.

### Ubicaciones (`/locations`)

  - `GET /locations/all_locations`: Listar todos los sitios de investigación.
  - `POST /locations`: Registrar una nueva ubicación.

*También existen endpoints para `/images`, `/uses` y las rutas del frontend.*

## 🐳 Comandos útiles de Docker

Guía rápida para gestionar el contenedor de la base de datos (basado en `commands.md`):

| Acción | Comando |
|Opcion| Descripción |
|---|---|
| **Encender** | `docker-compose up -d` (Levanta la BD y mantiene los datos guardados) |
| **Ver estado** | `docker ps` |
| **Apagar** | `docker-compose stop` (Detiene sin borrar datos) |
| **Resetear (Borrar todo)** | `docker-compose down -v` (Borra el contenedor y los volúmenes/datos) |
| **Entrar a SQL** | `docker exec -it medicinal_plants_mysql mysql -u root -p1234` |

## 🗂️ Esquema de Base de Datos

El sistema relacional consta de las siguientes tablas principales:

  - **PLANTS**: Información taxonómica (nombre común, científico).
  - **LOCATIONS**: Datos geográficos (cantón, provincia).
  - **PLANTS\_LOCATIONS**: Tabla intermedia para la relación N:M.
  - **IMAGES**: Metadatos y enlaces a fotografías de las muestras.
  - **USES**: Descripción y categorización de usos medicinales.
  - **PREVIOUS\_RESEARCHES**: Bibliografía y estudios previos relacionados.
  - **TOPONIMOS**: Origen y distribución.
  - **INTERVIEWS**: Tablas separadas para entrevistas a consumidores y vendedores.

## 👤 Autors

**Aldrin**

  - GitHub: [aldrinchp](https://github.com/aldrinchp)
  - Correo: aldrinchp@gmail.com

**Kevin**

  - GitHub: [KevJoss](https://github.com/KevJoss/)
  - Correo: kevin.sanchez@yachaytech.edu.ec

**Jhony**

  - GitHub: [ShonyALV](https://github.com/ShonyALV)
  - Correo: ljhonyalfonso@gmail.com

