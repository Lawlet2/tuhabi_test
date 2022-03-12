![tuhabiAPI](docs/images/header.gif)
# tuhabiAPI

Prueba técnica tuhabi.mx

## Introducción

Habi desea tener una herramienta en la que sus usuarios puedan consultar los 
inmuebles disponibles para la venta. 

En esta herramienta los usuarios deben ser capaces de ver tanto los inmuebles 
vendidos como los disponibles. Con el objetivo de hacer más fácil la búsqueda, 
se espera que los usuarios puedan aplicar diferentes filtros a la búsqueda.
Adicionalmente, se espera que los usuarios puedan darle “me gusta” a los 
inmuebles con el fin de tener un ranking interno de los inmuebles más 
llamativos.

## Historias de usuario

### Servicio de consulta

- Los usuarios pueden consultar los inmuebles con los estados: “pre_venta”, 
  “en_venta” y “vendido” (los inmuebles con estados distintos nunca deben 
  ser visibles por el usuario).
  
- Los usuarios pueden filtrar estos inmuebles por: Año de construcción,
  Ciudad, Estado.
  
- Los usuarios pueden aplicar varios filtros en la misma consulta.
  
- Los usuarios pueden ver la siguiente información del inmueble: Dirección, 
  Ciudad, Estado, Precio de venta y Descripción.

### Servicio "Me gusta"

- Los usuarios pueden darle me gusta a un inmueble en específico y esto 
  debe quedar registrado en la base de datos.
  
- Los “Me gusta” son de usuarios registrados, y debe quedar registrado en 
  la base de datos el histórico de “me gusta” de cada usuario y a cuáles 
  inmuebles.
  
## Metodología de desarrollo

### Servicio de consulta

Para implementar el servicio de consulta emplearé
el framework FastAPI que me permitirá exponer el endpoint para que 
los usuarios consulten los inmuebles de acuerdo a los filtros aplicados.

La base de datos proporcionada para la prueba es MySQL y por ello 
emplearé el conector MySQL Connector/Python (el cual cumple con la 
especificación [Python Database API Specification v2.0 PEP 249](
https://peps.python.org/pep-0249/))
y que permite que los programas en Python accedan a bases de datos 
MySQL.

La metodología de diseño propuesta es TDD (Test Driven Development) que 
consiste en el siguiente flujo:
  
* Escribir la prueba, se ejecuta y falla.
* Se escribe el código suficiente para que la 
    prueba pase el test.
* Se refactoriza el código para mejorarlo.
  
  ![TDD](docs/images/tdd.png)

### Servicio de "Me gusta"

Este requerimiento es conceptual debido a que no existe el modelo en la 
base de datos para implementarlo. La propuesta es crear un diagrama 
entidad - relación empleando la herramienta de Google 
Drawings y el código SQL para extender el modelo se codificará en archivos
.sql relacionados a este servicio.

## Stack tecnológico y herramientas

- Python 3.8.9
- FastAPI 0.75.0
- MySQL 5.7.12 (MySQL Community Server (GPL))
- MySQL Connector/Python  8.0.28
- Google Drawings

## Configuración del proyecto

## Documentación










