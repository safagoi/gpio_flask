# Raspberry Pi GPIO's pins (LED) controlled by web Flask application

En este proyecto, controlaremos un LED de 5mm conectado a los GPIO pins de una [Raspberry Pi 4 model B](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/). Esto lo conseguiremos a través de una aplicación web simple creada con [Flask](https://flask.palletsprojects.com/en/2.2.x/) y un poco de HTML, CSS y Javascript.

En nuestra Raspberry Pi, serviremos una aplicación de Python que hará uso de la librería de control de GPIO pins [*gpiozero*](https://gpiozero.readthedocs.io/en/stable/), que nos facilitará el control de los pins con escasas líneas de código y que permite manejar distintos dispositivos electrónicos, en nuestro caso un LED.


### Circuito empleado

Se tratará de un circuito básico con LED de 5mm y una resistencia conectadas en serie a tierra y el GPIO 17 respectivamente, como se aprecia en la ilustración. Para más información https://gpiozero.readthedocs.io/en/stable/recipes.html#led .

![Imagen del circuito](https://gpiozero.readthedocs.io/en/stable/_images/led_bb.svg)



### Preparación del entorno de desarrollo

En primer lugar, es importante que cambiemos a una contraseña segura en nuestra Raspberry Pi, pues expondremos ciertos puertos para conectarnos a través de SSH desde otro ordenador para [no necesitar una pantalla externa](https://www.raspberrypi.com/documentation/computers/remote-access.html).
Una vez habilitada la conexión SSH y obtenida la dirección IP de la Raspberry Pi, podremos acceder a ella (modo consola) desde un plugin ([Remote - SSH, Microsoft](https://code.visualstudio.com/docs/remote/ssh)) en VSCode que nos permitirá editar código cómodamente desde nuestro ordenador principal.


### Instalación y puesta en marcha del proyecto (modo desarrollo)

Al descargar el repositorio crear un entorno virtual [venv](https://docs.python.org/3/library/venv.html) y activarlo, instalar dependencias
y lanzar la aplicación Flask. Si tenemos conectado nuestro circuito correctamente, podremos acceder al servidor de desarrollo que lanza Flask y mediante los dos botones activar y desactivar nuestro LED.
