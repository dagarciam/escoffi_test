# Diagnostico Pyspark

## Instrucciones

1. Realizar un fork de este repositorio a tu cuenta de github.
2. Crear una rama que por nombre lleve tus iniciales a partir de la rama master.
3. Realizar los ejercicios solicitados abajo.
4. Enviar por correo electronico tus comentarios respecto a la solución y el link a tu repositorio.

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
1. El cliente ha solicitado realizar el cruce la tabla sunedu_people_education y la tabla risk_parameter, para ello nos
indica que la llaves son: `education_level_desc` y `parameter_value_desc`. Para cada registro en la tabla sunedu debemos
agregar la columna `parameter_id` con el nombre `education_level_type`. Un ejemplo de la salida deseada es el siguiente:

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

## Prueba necesaria

* De acuerdo a la regla anterior se espera la siguiente tabla de cifras de control:
   
````python
df.\
  groupBy("education_level_type").\
  agg(count("*").alias("count"))
````

| education_level_type | count |
| -------------------- | ----- |
|||


¡Buena suerte!
