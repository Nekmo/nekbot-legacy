# coding=utf-8
__author__ = 'nekmo'

from . import global_settings

class Settings(object):
    def __init__(self, defaults=global_settings):
        self.write_conf(global_settings) # Primero guardo la configuración global

    def configure(self, module):
        """Módulo (archivo de configuración) donde se encuentran los parámetros con
        la configuración del usuario. Esta sobrescribirá la global
        """
        self.write_conf(module)

    def write_conf(self, settings_mod, prevent_override=False):
        for setting in dir(settings_mod):
            if prevent_override and hasattr(self, setting): continue
            if setting.isupper():
                setattr(self, setting, getattr(settings_mod, setting))

settings = Settings()