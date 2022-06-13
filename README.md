
Documentacion de endpoint en la carpeta app/server/yaml

Test unitarios en carpeta app/server/unit_test
  
  para ejecutar las pruebas unitarias ejecutar dentro de la carpeta app el comendo pytest

Descripcion de la actividad Modulo Joke:

  se crearon los distintos servicios para las peticiones CRUD

    - Search: busca un chiste segun el parametro indicado o uno al azar si no se le indica parametro
    - Find: Busca en la base de datos un chiste ya almacenado en la base de datos
    - Save: almacena un chiste en la base de datos
    - Update: modifica un chiste almacenado en la base de datos
    - Delete: borra un chiste en la base de datos
    - List: devuelve todos los chistes almacenados en la base de datos

Descripcion de la actividad Modulo Math:


  se crearon los distintos servicios para las peticiones minimo comun multiplo y sumar valores

    - numbers: dado una lista de n numeros naturales se descomponen cada numero para expresarlos en potencias, luego se unen y eliminan las potencias y solo se toma la de mayor valor, luego se multiplica el valor resultante

    - number: se suma 1 al numero indicado


Que repositorio utilizarias?

  utilizaria mariadb

  - Es una base de datos libre y se maneja tal cual como mysql
  - La cantidad y estuctura de datos utilizada en la app no requiere de una arquitectura compleja ni se maneja gran volumenes de datos

  -- creacion de base de datos sql
  
  el password creado para el servidor de la base de datos es: Jvdf76sFWGYZHWUD

  si se utiliza la implementacion por docker no se necesita ningun cambio, si es requerido cambiar el password del servidor:

  modifique el valor passqord en la definicion de variables de entorno en el archivo app/server/server.py

  ejemplo:
    
    os.environ["mariadb"] = json.dumps({'host': 'mysqldb','port': 3306,'user': 'root','password': 'Jvdf76sFWGYZHWUD','database': 'squadmarker'})

  -- Sentencias de creacion

  CREATE DATABASE squadmarker;

    use squadmarker;

    CREATE TABLE `jokes` (
    `uid` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8_spanish2_ci NOT NULL,
    `joke_new` varchar(500) CHARACTER SET utf8mb3 COLLATE utf8_spanish2_ci NOT NULL,
    `joke_old` varchar(500) CHARACTER SET utf8mb3 COLLATE utf8_spanish2_ci DEFAULT NULL,
    `created_at` datetime NOT NULL,
    `updated_at` datetime DEFAULT NULL,
    `deleted_at` datetime DEFAULT NULL
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish2_ci;

  ALTER TABLE `jokes`
    ADD PRIMARY KEY (`uid`);

  -- creacion de base de datos noSql

  use squadmarker;

  db.squadmarker.save(
    {
      uid:'0c0a70d6-ea8d-11ec-bfa7-0242ac130004',
      joke_new: 'init row',
      joke_old: null,
      created_at: '2022-06-12 19:00:00',
      updated_at: null,
      deleted_at: null,
    }
  );