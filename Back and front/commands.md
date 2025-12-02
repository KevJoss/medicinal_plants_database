#### Borrar el contenedor con el volumen

docker-compose down -v

#### Volver a crear el docker limpio
docker-compose up -d

##### A. Cuando te sientas a trabajar (Encender)
docker-compose up -d

(Esto levanta la base de datos con los datos que tenías guardados la última vez).

##### B. Cuando terminas por hoy (Apagar SIN borrar)
docker-compose stop

##### C. Cuando quieres "Resetear" (BORRAR LA BD)
docker-compose down -v


Acción,	Comando
1. Encender todo,	docker-compose up -d
2. Ver estado,	docker ps
3. Ejecutar App (Crear tablas),	python app.py
4. Entrar a mirar (SQL),	docker exec -it medicinal_plants_mysql mysql -u root -p1234
5. BORRAR TODO (Reset),	docker-compose down -v