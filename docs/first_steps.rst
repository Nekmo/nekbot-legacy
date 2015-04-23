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

