.. first_steps:

.. highlight:: python

Mi primer plugin
################
¡Crear un plugin es fácil, rápido, y para toda la familia! En serio, es tan fácil que te sentirás insultado. Procura
no ofenderte mucho.

.. WARNING::
    En un estado posterior del proyecto, habrá un sistema de creación de proyectos, estando el código fuente de
    NekBot y el entorno de trabajo del usuario separados. Este manual está escrito con ello en cuenta.

1. Primero, crea un archivo de plugin en el directorio "plugins" de tu proyecto. Por ejemplo, "hello.py".
2. Pon lo siguiente en el archivo::

    from nekbot.core.commands import command

    @command
    def hello(message):
        return 'Hello world! Your message: %s' % message

3. Pon el nombre del archivo (sin el .py) en el PLUGINS del archivo settings.py de tu proyecto y... ¡Listo! Ahora
puedes ejecutar el comando "!hello" en una sala o conversación donde esté tu bot, y devolverá el texto del return.

Si quisieses poner un nombre no permitido por Python (guiones, palabras reservas, etc.), puedes emplear en el
decorador::

    @command('my-command')
    def my_command(message):
        pass


Argumentos posicionales
=======================
NekBot permite añadir argumentos de una forma fácil a tus comandos. ¡Y es tan fácil como usar los propios argumentos
de tus funciones!

Argumentos posicionales

Por ejemplo, el siguiente comando exigirá un argumento (obligatorio)::

    @command
    def greet(message, person):
        return '¡Hola %s!' % person

Lo cual se ejecutará con::

    !greet Pepe

Por supuesto, también podemos usar `*args`::

    @command
    def greet(message, *args):
        return '¡Hola %s!' % ', '.join(args)

Lo cual se usará con::

    !greet Pepe "José Pérez" Fernando

Validación
==========
Por supuesto, de nada sirve obtener valores, si estos no nos sirve. NekBot tiene un sistema que se encarga de
comprobar la validez de dichos datos, transformarlos, y mostrar un error en caso de no ser correctos. Por ejemplo, la
 siguiente función solo funcionará si los valores son números::

    from random import randint

    @command('random', int, int)
    def random(message, start, end):
        return randint(start, end)

En caso de no devolverse un valor correcto, obtendremos algo como lo siguiente::

    In: !random 3 spam
    Out:El argumento en la posición 2 con valor "spam", no es válido. El valor debe ser un número.

