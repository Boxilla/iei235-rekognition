Creado por Alejandro Quintana Saravia - alejandro.quintana@sansano.usm.cl

# [IEI235] Tarea aws-rekognition

Tarea de la asignatura IEI235-Pruebas de Software, donde se debe ocupar rekognition de aws para verificar si un rostro aparece en una imagen.

## Descripcion

El proposito de este programa es  utilizar rekognition para comparar rostros y generar casos de prueba para esto, además crea un archivo llamado "log_tarea_rekognition.txt" donde se agrega una linea con la fecha de ejecucion, el nombre de las imagenes y el resultado de la comparación cada vez que el programa es ejecutado con exito.

## Requisitos

* Windows 10
* Python 3.9.x
* libreria boto3 para python
* Cuenta en aws con acceso a rekognition

## Ejecucion

Para ejecutar el programa y que cumpla totalmente su funcionaldiad se debe tener instalada la versión 3.9.5 de python en Windows 10.

Se deben poner las credenciales de la cuenta de aws aws_acces_key_id, aws_secret_acces_key y aws_sesion_token en las lineas 8,9 y 10 respectivamente.

Como el programa genera un documento se deben tener permisos suficientes para esto al ejecutar el programa.

El codigo fue escrito en python version 3.9.5

En la linea de comandos de windows se ejecutaria de la siguiente forma estando en el directorio donde se encuentra el archivo "tarea_aws.py"

```bash
python .\tarea_aws.py
```

## Uso
Luego de ejecutar el programa este mostrará el nombre de las imagenes disponibles para comparar, luego se debe ingresar el numero de la opcion que queramos comparar. (Si se desea ver la imagen se puede acceder a la carpeta "images").

Luego esta imagen seleccionada se comparará con la de luke skywalker proporcionada en el enunciado de la tarea y nos dirá si el rostro aparece o no en la opcion seleccionada.

Se debe ingresar un número de los proporcionados.

Para finalizar el programa se debe escribir "x", como lo indica por pantalla el mismo programa.

```bash
Imagenes disponibles:  
Opción 0 : Han_solo.jpg
Opción 1 : luke_skywalker1.jpg
Opción 2 : luke_skywalkerAdulto1.jpg
Opción 3 : luke_skywalkerAdulto2.jpg
Opción 4 : luke_skywalkerAdulto3.jpg
Opción 5 : luke_skywalkerCaricatura.jpg
Opción 6 : luke_skywalkerEdadViejo.jpg
Opción 7 : luke_skywalkerFormatoDistinto.bmp
Opción 8 : luke_skywalkerFormatoPng.png
Opción 9 : luke_skywalkerMismaEdad.jpg
Opción 10 : luke_skywalkerVideoJuegoRealista.jpg
Opción 11 : luke_junto_a_actor_diferente.jpg
Opción 12 : ValorMinimoResolucion1.jpg
Opción 13 : ValorMinimoResolucion2.jpg
Opción 14 : ValorMaximoResolucion1.jpg
Ingrese opcion: 6
Luke no aparece en la imagen
ENTER para repetir, o escriba X para salir.

```

* Se suprimio el uso de tildes en este readme
