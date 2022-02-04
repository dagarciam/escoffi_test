# Diagnostico Pyspark

## Instrucciones

1. Realizar un clone de este proyecto.
2. Crear una rama que por nombre lleve tus iniciales a partir de la rama solution.
3. Realizar los ejercicios solicitados abajo.
4. Crear un repositorio vácio en tu cuenta que debe ser privado.
5. Cambiar la url remote origin en tu clone local para apuntar a tu repositorio vacío.
6. Sube los cambios a tu repositorio.
7. Enviar por correo electronico la notificación de finalización y el link al repositorio de solución.

_**Haz que tu repositorio sea privdo** y brinda acceso de lectrua a tu repositorio al usuario **dagarciam**_

_**Toda PR a este repositorio será declinada y ocasionará la anulación del examen.**_

## ¿Qué evaluaremos?

* Resuelva con el API de SparkSQL el ejercicio planteado.
* El uso de sentencias SQL queda estrictamente prohibido.
* El uso de cadenas en las clases que implementan la lógica de solución están muy mal vistos por nuestra area de QA, sea
  cuidadoso.
* Amamos las pruebas de calidad, la implementación de pruebas unitarias a alguno de los métodos implementados nos hará
  muy felices.
* Modularice sú código lo suficiente de tal forma que cada método haga una sola cosa.
* Hemos soñado con poder leer las rutas de entrada y salida desde un archivo de configuración, sería increible tener
  uno!
* Documente cada método que se implemente para tener contexto claro de su uso.

## Ejercicio

Uno de nuestros Jrs necesita ayuda, le han dado la siguiente regla de negocio:
* El cliente ha solicitado realizar el cruce la tabla sunedu y la tabla risk, para ello nos
indica que la llaves son: `education_level_desc` y `parameter_value_desc`. Para cada registro en la tabla sunedu debemos
agregar la columna `parameter_id` con el nombre `education_level_type`. 

* Un ejemplo de la salida deseada es el siguiente:

| education_level_desc | education_level_type |
| -------------------- | -------------------- |
|MAESTRO EN CIENCIAS: MEDICINA|MASTER|
|MAESTRO EN CONTABILIDAD CON MENCIÓN EN AUDITORIA|MASTER|
|MEDICO CIRUJANO|LICENCIADO|
|MEDICO CIRUJANO REVALIDA - UNIVERSIDAD MAYOR, REAL Y PONTIFICIA DE SAN FRANCISCO XAVIER DE CHUQUISACA TIPO: REVALIDA|LICENCIADO|
|TITULO DE ESPECIALISTA EN GESTION ESCOLAR CON LIDERAZGO PEDAGOGICO|ESPECIALIDAD|
|INGENIERO MECANICO ELECTRICISTA|LICENCIADO|
|INGENIERO METALURGISTA|LICENCIADO|
|INGENIERO METALURGICO Y SIDERURGICO|LICENCIADO|


Nuestro chico ha intentado realizar un join para obtener el cruce pero se ha encontrado con un escenario complicado, sólo cruza el valor `SIN INFORMACION`.

### Validación

El DataFrame resultante al ser agrupado por `educatuion_level_type` y realizar un conteo debería entregar una matriz como la siguiente:

| education_level_type | count|
|----------------------|------|
|BACHILLER             |   885|
|null                  |     1|
|MASTER                |    21|
|SIN INFO              | 51871|
|ESPECIALIDAD          |    31|
|LICENCIADO            |   256|
|DOCTORADO             |     2|

De tal forma que sólo hay un registro que no tiene correspondencia.

¡Buena suerte!
