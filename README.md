# RoboTender

## Descripción del proyecto

Este proyecto tiene como objetivo cumplir con los requisitos del curso de Robótica. Consiste en el desarrollo de un robot completo, incluyendo tanto sus componentes de hardware como software.

En particular, nuestro enfoque se centra en la implementación de un robot capaz de dispensar diferentes bebidas al usuario utilizando el reconocimiento facial.

### Fucnionalidad principal

El robot tiene la capacidad de servir bebidas a los usuarios basándose en el reconocimiento facial. Utilizando un modelo de visión por computador, el robot detecta las caras de las personas y, si el usuario ha seleccionado previamente su bebida preferida, el robot la dispensará automáticamente. En caso de que sea la primera vez que el usuario utilice el robot, este le solicitará que elija entre las tres opciones de bebidas disponibles, para que en futuras ocasiones el robot pueda servirle directamente su bebida favorita según su reconocimiento facial.

## Guía de uso

Para utilizar el robot, el usuario simplemente necesita colocarse frente a la cámara del robot, que cuenta con un sensor infrarrojo para detectar la presencia de personas.

Cuando se detecta la presencia de una persona, se activa el módulo de reconocimiento facial, que identifica si hay una cara frente a la cámara.

### Caso 1: El usuario usa el robot por primera vez

Si es la primera vez que el usuario es detectado por el modelo, se le solicitará que elija su bebida preferida de entre las tres opciones disponibles, utilizando los botones correspondientes.

El usuario seleccionará su bebida preferida presionando uno de los tres botones, y a partir de esa elección, el robot comenzará a dispensar la bebida seleccionada.

### Caso 2: El usuario ha usado el robot previamente

En caso de que el usuario ya haya utilizado previamente el robot, este ya tendrá una bebida asociada y, por lo tanto, el robot dispensará automáticamente esa bebida sin que el usuario tenga que hacer ninguna selección adicional.

## Componentes

Raspberry Pi 4 4GB RAM - Modelo B

- Precio: 66,90€

Raspberry Pi Camara Rev 1.3

- Precio:  

Valvulas

- Precio:  

Pulsadores

- Precio:  

Sensor infrarrojo sharp 2y0a21

- Precio:  

Set de cables:

- Precio:  
