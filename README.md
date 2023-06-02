
<img src="https://github.com/juanmacaaz/Jetsy/blob/main/Resources/jetsy.png" align="right" width="300" alt="header pic"/>

# Robotender

Dispensador de bebidas automatico a través del reconocimiento facial de los usuarios.

# Tabla de Contenidos
   * [Descripción del proyecto](#descripción-del-proyecto)
   * [Demo](#demo)
   * [Requerimientos](#requirements)
   * [Funcionalidad Principal](#funcionalidad-principal)
   * [Guía de uso](#guía-de-uso)
      * [Caso 1: El usuario usa el robot por primera vez](#guía-de-uso)
      * [Caso 2: El usuario ha usado el robot previamente](#guía-de-uso)
   * [Componentes](#componentes)
   * [Hardware Scheme](#hardware-scheme)
   * [Arquitectura de Software](#software-architecture)
   * [Software Modules](#software-modules)
   * [Additional Implementations](#additional-implementations)
   * [Built With](#built-with)
   * [License](#license)
   * [Use-case](#use-case)
   * [Amazing Contribution](#amazing-contribution)
   * [How to contribute](#How-to-contribute)
   * [Citing](#citing)
   * [Support](#support)
   * [Authors](#authors)
   * [Bibliography](#bibliography)

# Descripción del proyecto

Este proyecto tiene como objetivo cumplir con los requisitos del curso de Robótica. Consiste en el desarrollo de un robot completo, incluyendo tanto sus componentes de hardware como software.

En particular, nuestro enfoque se centra en la implementación de un robot capaz de dispensar diferentes bebidas al usuario utilizando el reconocimiento facial.

# Demo

[![Demo](https://img.youtube.com/vi/N_IYzQ1feL4/0.jpg)](https://www.youtube.com/watch?v=N_IYzQ1feL4)

# Funcionalidad Principal

El robot tiene la capacidad de servir bebidas a los usuarios basándose en el reconocimiento facial. Utilizando un modelo de visión por computador, el robot detecta las caras de las personas y, si el usuario ha seleccionado previamente su bebida preferida, el robot la dispensará automáticamente. 

En caso de que sea la primera vez que el usuario utilice el robot, este le solicitará que elija entre las tres opciones de bebidas disponibles, para que en futuras ocasiones el robot pueda servirle directamente su bebida favorita según su reconocimiento facial.

# Requirements

For running each sample code:

- [Python 3.9.x](https://www.python.org/)

- [pytorch](https://pytorch.org/)
- [opencv](https://opencv.org/)
- [pipwin](https://pypi.org/project/pipwin/)
- [pyaudio](https://pypi.org/project/PyAudio/)
- [pygame](https://www.pygame.org/)
- [torchaudio](https://pytorch.org/audio/)
- [omegaconf](https://omegaconf.readthedocs.io/)
- [sox](https://pypi.org/project/sox/)
- [noisereduce](https://pypi.org/project/noisereduce/)
- [Levenshtein](https://en.wikipedia.org/wiki/Levenshtein_distance)
- [fuzzywuzzy](https://pypi.org/project/fuzzywuzzy/)

# Guía de uso

Para utilizar el robot, el usuario simplemente necesita colocarse frente a la cámara del robot, que cuenta con un sensor infrarrojo para detectar la presencia de personas.

Cuando se detecta la presencia de una persona, se activa el módulo de reconocimiento facial, que identifica si hay una cara frente a la cámara.

## Caso 1: El usuario usa el robot por primera vez

Si es la primera vez que el usuario es detectado por el modelo, se le solicitará que elija su bebida preferida de entre las tres opciones disponibles, utilizando los botones correspondientes.

El usuario seleccionará su bebida preferida presionando uno de los tres botones, y a partir de esa elección, el robot comenzará a dispensar la bebida seleccionada.

### Caso 2: El usuario ha usado el robot previamente

En caso de que el usuario ya haya utilizado previamente el robot, este ya tendrá una bebida asociada y, por lo tanto, el robot dispensará automáticamente esa bebida sin que el usuario tenga que hacer ninguna selección adicional.

# Componentes Elctrónicos

<table align="center" border="0">
        <td align="center">




<tr>

<td align="center">

[Two Trees Stepping Motor Model 17HS4401](https://www.amazon.es/Twotrees-Nema-17-impresora-HS4401S/dp/B07SQNZ66Q/ref=asc_df_B07SQNZ66Q/?tag=googshopes-21&linkCode=df0&hvadid=513590746798&hvpos=&hvnetw=g&hvrand=12539990065257522260&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=20270&hvtargid=pla-853487347177&psc=1)
</td><td align="center">

[Valvula con Solenoide 12V - 1/2"](https://tienda.bricogeek.com/otros-sensores/937-valvula-con-solenoide-12v.html)
</td>><td align="center">

[3 Push Buttons](https://www.digikey.es/es/products/detail/cui-devices/TS02-66-60-BK-100-SCR-D/15634358?utm_adgroup=Tactile%20Switches&utm_source=google&utm_medium=cpc&utm_campaign=Shopping_Product_Switches&utm_term=&productid=15634358&gclid=Cj0KCQjw4NujBhC5ARIsAF4Iv6f_8dzIUEkD_Q8xm6bYCE63TOHERH17kFTZA9TtDuOEQVtOX9fEyV0aAn0mEALw_wcB)
</td></tr>

<tr>
    <td align="center">
        <a href="https://www.amazon.es/Twotrees-Nema-17-impresora-HS4401S/dp/B07SQNZ66Q/ref=asc_df_B07SQNZ66Q/?tag=googshopes-21&linkCode=df0&hvadid=513590746798&hvpos=&hvnetw=g&hvrand=12539990065257522260&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=20270&hvtargid=pla-853487347177&psc=1" target="_blank"><img border="0" src="https://m.media-amazon.com/images/I/614657YGFaL._SL1500_.jpg" ></a>
        <img src="https://www.amazon.es/Twotrees-Nema-17-impresora-HS4401S/dp/B07SQNZ66Q/ref=asc_df_B07SQNZ66Q/?tag=googshopes-21&linkCode=df0&hvadid=513590746798&hvpos=&hvnetw=g&hvrand=12539990065257522260&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=20270&hvtargid=pla-853487347177&psc=1" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
    </td>
    <td align="center">
        <a href="https://tienda.bricogeek.com/otros-sensores/937-valvula-con-solenoide-12v.html" target="_blank"><img border="0" src="https://tienda.bricogeek.com/3872-thickbox_default/valvula-con-solenoide-12v.jpg" ></a>
        <img src="https://tienda.bricogeek.com/otros-sensores/937-valvula-con-solenoide-12v.html" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
    </td>
         <td align="center">
        <a href="https://www.digikey.es/es/products/detail/cui-devices/TS02-66-60-BK-100-SCR-D/15634358?utm_adgroup=Tactile%20Switches&utm_source=google&utm_medium=cpc&utm_campaign=Shopping_Product_Switches&utm_term=&productid=15634358&gclid=Cj0KCQjw4NujBhC5ARIsAF4Iv6f_8dzIUEkD_Q8xm6bYCE63TOHERH17kFTZA9TtDuOEQVtOX9fEyV0aAn0mEALw_wcB" target="_blank"><img border="0" src="https://media.digikey.com/Photos/CUI%20Photos/MFG_TS02-Sm-BK-SCR.jpg" ></a>
        <img src="https://www.digikey.es/es/products/detail/cui-devices/TS02-66-60-BK-100-SCR-D/15634358?utm_adgroup=Tactile%20Switches&utm_source=google&utm_medium=cpc&utm_campaign=Shopping_Product_Switches&utm_term=&productid=15634358&gclid=Cj0KCQjw4NujBhC5ARIsAF4Iv6f_8dzIUEkD_Q8xm6bYCE63TOHERH17kFTZA9TtDuOEQVtOX9fEyV0aAn0mEALw_wcB" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
    </td>

</tr>
<td align="center">

[A4988 Controlador para motor paso a paso](https://www.hta3d.com/es/a4988-controlador-motor-paso-a-paso-pololu-driver?gclid=CjwKCAjwpuajBhBpEiwA_Ztfhbq1hR--vj-H2azsVW6Nx2s-FVPZ3zZIGuDwAl1MMluSK8seG8oXqhoC9DoQAvD_BwE)
</td><td align="center">

[DRV8825 Controlador paramotor paso a paso](https://www.e-ika.com/m%C3%B3dulo-paso-a-paso-drv8825)
</td>
</tr>

<tr>
    <td align="center">
        <a href="https://www.hta3d.com/es/a4988-controlador-motor-paso-a-paso-pololu-driver?gclid=CjwKCAjwpuajBhBpEiwA_Ztfhbq1hR--vj-H2azsVW6Nx2s-FVPZ3zZIGuDwAl1MMluSK8seG8oXqhoC9DoQAvD_BwE" target="_blank"><img border="0" src="https://www.hta3d.com/image/cache/cache/1-1000/244/additional/5e45-a4988-02-0-4-1000x1000.jpg.webp" ></a>
        <img src="https://www.hta3d.com/es/a4988-controlador-motor-paso-a-paso-pololu-driver?gclid=CjwKCAjwpuajBhBpEiwA_Ztfhbq1hR--vj-H2azsVW6Nx2s-FVPZ3zZIGuDwAl1MMluSK8seG8oXqhoC9DoQAvD_BwE" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
    </td>
    <td align="center">
        <a href="https://www.e-ika.com/m%C3%B3dulo-paso-a-paso-drv8825" target="_blank"><img border="0" src="https://www.e-ika.com/images/thumbs/0003414_controlador-para-motores-paso-a-paso-drv8825_600.jpeg" ></a>
        <img src="https://www.e-ika.com/m%C3%B3dulo-paso-a-paso-drv8825" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
    </td>

</tr>


<tr>







<tr><td colspan="3">
</table>


# Componentes Caja


# Hardware Scheme
<img src="https://github.com/juanmacaaz/Jetsy/blob/main/Resources/Scheme/hardware.png" width="640" alt="hardware pic">


# Software Modules
<img src="./assets/sw_scheme.png" width="640" alt="software modules pic">

# Eyes
## Affirmation
<img src="https://github.com/juanmacaaz/Jetsy/blob/main/Resources/Eyes/affirmation.gif" width="640" alt="affirmation pic">

## Loved
<img src="https://github.com/juanmacaaz/Jetsy/blob/main/Resources/Eyes/loved.gif" width="640" alt="loves pic">

## Suspicious
<img src="https://github.com/juanmacaaz/Jetsy/blob/main/Resources/Eyes/suspicious.gif" width="640" alt="suspicius pic">

## Angry
<img src="https://github.com/juanmacaaz/Jetsy/blob/main/Resources/Eyes/angry.gif" width="640" alt="angry pic">

## Happy
<img src="https://github.com/juanmacaaz/Jetsy/blob/main/Resources/Eyes/happy.gif" width="640" alt="happy pic">

## Normal
<img src="https://github.com/juanmacaaz/Jetsy/blob/main/Resources/Eyes/normal.gif" width="640" alt="normal pic">

## Sad
<img src="https://github.com/juanmacaaz/Jetsy/blob/main/Resources/Eyes/sad.gif" width="640" alt="sad pic">

# Arms
<img src="https://github.com/juanmacaaz/Jetsy/blob/main/Resources/Arms/move.gif" width="640" alt="arm move pic">

# Movements
## Front
<img src="https://github.com/juanmacaaz/Jetsy/blob/main/Resources/Moviments/front.gif" width="640" alt="go pic">

## Left
<img src="https://github.com/juanmacaaz/Jetsy/blob/main/Resources/Moviments/left.gif" width="640" alt="left pic">

## Right
<img src="https://github.com/juanmacaaz/Jetsy/blob/main/Resources/Moviments/right.gif" width="640" alt="right pic">

## Back
<img src="https://github.com/juanmacaaz/Jetsy/blob/main/Resources/Moviments/back.gif" width="640" alt="back pic">

# Proximity Sensors
## Frontal
<img src="https://github.com/juanmacaaz/Jetsy/blob/main/Resources/Proximity_Sensors/sensor.gif" width="640" alt="sensor pic">

# Command Voice
## Voice Controller
[![Voice Controller](https://img.youtube.com/vi/iem644UcZ8E/0.jpg)](https://www.youtube.com/watch?v=iem644UcZ8E)

## Dance
[![Dance](https://img.youtube.com/vi/3rkEBKqAFxo/0.jpg)](https://www.youtube.com/watch?v=3rkEBKqAFxo)

## Tell me a joke
[![tell me a joke](https://img.youtube.com/vi/mcBkq9uVq2E/0.jpg)](https://youtu.be/mcBkq9uVq2E)

## Object Classification
[![object classification](https://img.youtube.com/vi/gnggCI5NF00/0.jpg)](https://www.youtube.com/watch?v=gnggCI5NF00)

# Additional Implementations
- Where I am
- Emotion Detection
# Built With
- [TinkerCard](https://www.tinkercad.com/) - Model Design Program.
- [Arduino](https://www.arduino.cc/) - IDE used for the development of the servos.
- [VSCode](https://code.visualstudio.com/) - Code editor to program hardware components.
- [Python](https://www.python.org/) - Language used for programming.
- [Adoble Suit](https://www.adobe.com/) - For visual content creation.
# License
This project is under the MIT License - see the [LICENSE](https://github.com/juanmacaaz/Jetsy/blob/main/LICENSE.md) file for details

# Use-Case
If this project helps your robotics project, please let us know with creating an issue.

# Amazing Contribution
- An emotional human-robot interaction never seen before.
- Table assistant 2.0 equipped with artificial intelligence.
- An assistant with next-level computer vision. Leaving current trade assistants behind.
- An easy-to-program framework to add new functionality to the robot.
- All the code is open-source and does not require the internet to work.

  
# Support 
- [Escola d'Enginyeria - UAB Barcelona](https://www.uab.cat/enginyeria/)
- [UAB Open Labs](https://www.uab.cat/open-labs/)

# Authors
* **Daniel Alcover** (https://github.com/danialcover)
* **Alexandre Galvany** (https://github.com/AlexGalPar14)
* **Jordi González** (https://github.com/Jordigg2000)
* **Fco Javier Honrubia** (https://github.com/javihonrubia)

# Bibliography
- [Controlar un servo con arduino, Luis Llamas, 2016](https://www.luisllamas.es/controlar-un-servo-con-arduino/)
- [Modulo sensor de llama, Andrés Cortés, 2021](https://acortes.co/proyecto-14-modulo-sensor-de-llama/)
- [Tutorial de uso del modulo l298n, Naylamp Mechatronics, 2017](https://naylampmechatronics.com/blog/11_tutorial-de-uso-del-modulo-l298n.html)
- [CSI Camera, Jetson Hacks Nano, 2019](https://github.com/JetsonHacksNano/CSI-Camera)
